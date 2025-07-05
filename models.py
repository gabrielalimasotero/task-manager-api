# ORM = Object Relational Mapping
from flask_sqlalchemy import SQLAlchemy  # Python <-> SQL translator
from datetime import datetime  # For timestamps

db = SQLAlchemy()  # Global db instance to access database

class Task(db.Model):  # Class representing 'task' table in SQLite (SQLAlchemy translates)
    # Table columns definition
    id = db.Column(db.Integer, primary_key=True)  # Integer column, primary key
    title = db.Column(db.String(100), nullable=False)  # Text up to 100 chars, required field
    description = db.Column(db.String(500), nullable=True)  # Text up to 500 chars, optional
    status = db.Column(db.String(20), nullable=False)  # String up to 20 chars, required
    due_date = db.Column(db.Date, nullable=True)  # Date only (no time)
    
    # Valid status options
    VALID_STATUSES = ['backlog', 'doing', 'done']
    
    def __repr__(self):  # For debugging - shows object info when printed
        return f'<Task {self.id}: {self.title}>'
    
    def to_dict(self):  # Object to dictionary for JSON API response (auto conversion)
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'status': self.status,
            'due_date': self.due_date.isoformat() if self.due_date else None,
        }
    
    def is_valid_status(self, status):  # Validates status values
        return status in self.VALID_STATUSES