# Main application file - Flask app initialization and configuration
from flask import Flask
from models import db
from routes import tasks_bp

def create_app():  # Factory pattern - creates and configures Flask app
    app = Flask(__name__)  # Create Flask application instance
    
    # Database configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'  # SQLite file path
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable event system (saves memory)
    
    # Initialize database with app
    db.init_app(app)  # Connect SQLAlchemy to Flask app
    
    # Register blueprints (route groups)
    app.register_blueprint(tasks_bp, url_prefix='/api')  # All routes will have /api prefix
    
    # Create tables if they don't exist
    with app.app_context():  # Required context for database operations
        print("Creating database tables...")
        db.create_all()  # Create all tables defined in models.py
        print("Database tables created successfully!")
    
    # Root endpoint for API info
    @app.route('/')  # Base route
    def api_info():  # Function to show API information
        return {
            'message': 'Task Manager API',
            'version': '1.0',
            'endpoints': {
                'GET /api/tasks': 'List all tasks or filter by status (?status=backlog)',
                'POST /api/tasks': 'Create new task',
                'GET /api/tasks/{id}': 'Get specific task',
                'PUT /api/tasks/{id}': 'Update task',
                'DELETE /api/tasks/{id}': 'Delete task'
            }
        }
    
    return app  # Return configured Flask app

# Create app instance
app = create_app()

# Run application if this file is executed directly
if __name__ == '__main__':  # Only runs when file is executed directly (not imported)
    app.run(debug=True, host='0.0.0.0', port=5001)  # Start development server
    # debug=True: Auto-reload on code changes + detailed error messages
    # host='0.0.0.0': Accept connections from any IP (not just localhost)
    # port=5001: Run on port 5001 (changed from 5000 due to macOS AirPlay conflict)