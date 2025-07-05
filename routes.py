# API endpoints and request handling
from flask import Blueprint, request, jsonify
from models import db, Task
from datetime import datetime

# Create blueprint for task routes
tasks_bp = Blueprint('tasks', __name__)  # Groups related routes together

@tasks_bp.route('/tasks', methods=['POST'])  # POST endpoint for creating tasks
def create_task():  # Function to handle task creation
    try:
        data = request.get_json()  # Get JSON data from request body
        
        # Validate required fields
        if not data or 'title' not in data or 'status' not in data:  # Check required fields
            return jsonify({'error': 'Title and Status are required'}), 400  # Bad request
            
        # Validate status value
        if data['status'] not in Task.VALID_STATUSES:  # Check if status is valid
            return jsonify({'error': f'Status must be: {Task.VALID_STATUSES}'}), 400

        # Handle optional due_date
        due_date = None
        if 'due_date' in data and data['due_date']:  # If due date provided
            try:
                due_date = datetime.strptime(data['due_date'], '%Y-%m-%d').date()  # Convert string to date
            except ValueError:  # If date format is wrong
                return jsonify({'error': 'Due date must be in YYYY-MM-DD format'}), 400
        
        # Create new task object
        new_task = Task(  # Creates Task instance
            title=data['title'],  # Required field
            description=data.get('description'),  # Optional field (None if not provided)
            status=data['status'],  # Required field
            due_date=due_date  # Optional converted date
        )
        
        # Save to database
        print(f"Adding task to database: {new_task.title}")
        db.session.add(new_task)  # Adds task to session (staging area)
        db.session.commit()  # Commits changes to database (actually saves)
        print(f"Task saved with ID: {new_task.id}")
        
        return jsonify(new_task.to_dict()), 201  # Returns created task with 201 status
        
    except Exception as e:  # Catch any unexpected errors
        print(f"Error creating task: {e}")
        db.session.rollback()  # Undo changes if something went wrong
        return jsonify({'error': 'Internal server error'}), 500  # Internal server error

@tasks_bp.route('/tasks', methods=['GET'])  # GET endpoint for listing tasks
def get_tasks():  # Function to handle task listing
    try:
        status_filter = request.args.get('status')  # Get status parameter from URL (?status=pendente)
        
        if status_filter:  # If status filter is provided
            if status_filter not in Task.VALID_STATUSES:  # Validate status
                return jsonify({'error': f'Status must be: {Task.VALID_STATUSES}'}), 400
            tasks = Task.query.filter_by(status=status_filter).all()  # Filter by status
        else:
            tasks = Task.query.all()  # Get all tasks
        
        return jsonify([task.to_dict() for task in tasks])  # Convert all tasks to dict list
        
    except Exception as e:
        return jsonify({'error': 'Internal server error'}), 500

@tasks_bp.route('/tasks/<int:task_id>', methods=['GET'])  # GET single task by ID
def get_task(task_id):  # Function to get specific task
    try:
        task = Task.query.get_or_404(task_id)  # Get task or return 404 if not found
        return jsonify(task.to_dict())  # Return task as JSON
        
    except Exception as e:
        return jsonify({'error': 'Internal server error'}), 500

@tasks_bp.route('/tasks/<int:task_id>', methods=['PUT'])  # PUT endpoint for updating tasks
def update_task(task_id):  # Function to handle task updates
    try:
        task = Task.query.get_or_404(task_id)  # Get existing task or 404
        data = request.get_json()  # Get update data from request
        
        if not data:  # If no data provided
            return jsonify({'error': 'No data provided'}), 400
        
        # Update fields if provided
        if 'title' in data:  # Update title if provided
            task.title = data['title']
            
        if 'description' in data:  # Update description if provided
            task.description = data['description']
            
        if 'status' in data:  # Update status if provided
            if data['status'] not in Task.VALID_STATUSES:  # Validate status
                return jsonify({'error': f'Status must be: {Task.VALID_STATUSES}'}), 400
            task.status = data['status']
            
        if 'due_date' in data:  # Update due date if provided
            if data['due_date']:  # If due_date is not null
                try:
                    task.due_date = datetime.strptime(data['due_date'], '%Y-%m-%d').date()
                except ValueError:
                    return jsonify({'error': 'Due date must be in YYYY-MM-DD format'}), 400
            else:
                task.due_date = None  # Set to null if empty string or null provided
        
        # Save changes
        db.session.commit()  # Commit updates to database
        return jsonify(task.to_dict())  # Return updated task
        
    except Exception as e:
        db.session.rollback()  # Rollback if error occurs
        return jsonify({'error': 'Internal server error'}), 500

@tasks_bp.route('/tasks/<int:task_id>', methods=['DELETE'])  # DELETE endpoint
def delete_task(task_id):  # Function to handle task deletion
    try:
        task = Task.query.get_or_404(task_id)  # Get task or 404
        
        db.session.delete(task)  # Mark task for deletion
        db.session.commit()  # Commit deletion
        
        return jsonify({'message': 'Task deleted successfully'}), 200  # Success message
        
    except Exception as e:
        db.session.rollback()  # Rollback if error
        return jsonify({'error': 'Internal server error'}), 500