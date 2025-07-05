# Task Manager API

RESTful API for task management with CRUD operations, status filtering, and data validation. Built with Flask and SQLite.

## 🚀 Features

- ✅ **Complete CRUD Operations** - Create, Read, Update, Delete tasks
- ✅ **Status Filtering** - Filter tasks by status (backlog, doing, done)
- ✅ **Data Validation** - Required fields and format validation
- ✅ **RESTful Design** - Proper HTTP methods and status codes
- ✅ **SQLite Database** - Persistent data storage
- ✅ **Modular Architecture** - Separated concerns (models, routes, app)

## 🛠️ Technologies

- **Backend**: Python 3.x, Flask 2.3.3
- **Database**: SQLite with SQLAlchemy ORM
- **API Testing**: Postman Collection included

## 📦 Installation

1. **Clone the repository**
```bash
git clone https://github.com/gabrielalimasotero/task-manager-api.git
cd task-manager-api
```

2. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run the application**
```bash
python app.py
```

The API will be available at `http://localhost:5001`

## 📚 API Endpoints

### Base URL: `http://localhost:5001/api`

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/tasks` | List all tasks |
| GET | `/tasks?status={status}` | Filter tasks by status |
| GET | `/tasks/{id}` | Get task by ID |
| POST | `/tasks` | Create new task |
| PUT | `/tasks/{id}` | Update task |
| DELETE | `/tasks/{id}` | Delete task |

### Status Values
- `backlog` - Task to be done
- `doing` - Task in progress  
- `done` - Completed task

## 🔧 Usage Examples

### Create Task
```bash
curl -X POST http://localhost:5001/api/tasks \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Study Flask API",
    "description": "Learn REST API development",
    "status": "backlog",
    "due_date": "2025-07-15"
  }'
```

### List All Tasks
```bash
curl http://localhost:5001/api/tasks
```

### Filter by Status
```bash
curl http://localhost:5001/api/tasks?status=backlog
```

### Update Task
```bash
curl -X PUT http://localhost:5001/api/tasks/1 \
  -H "Content-Type: application/json" \
  -d '{"status": "doing"}'
```

### Delete Task
```bash
curl -X DELETE http://localhost:5001/api/tasks/1
```

## 📋 Task Schema

### Request Body (POST/PUT)
```json
{
  "title": "string (required)",
  "description": "string (optional)",
  "status": "string (required) - backlog|doing|done",
  "due_date": "string (optional) - YYYY-MM-DD format"
}
```

### Response Format
```json
{
  "id": 1,
  "title": "Study Flask API",
  "description": "Learn REST API development",
  "status": "backlog",
  "due_date": "2025-07-15",
  "created_at": "2025-07-05T03:50:21.530814"
}
```

## 🧪 Testing with Postman

Import the Postman collection from `postman_collection.json`:

1. Open Postman
2. Click "Import" 
3. Select `postman_collection.json`
4. Test all endpoints with pre-configured requests

## 📁 Project Structure

```
task-manager-api/
├── app.py                 # Main application file
├── models.py              # Database models
├── routes.py              # API endpoints
├── requirements.txt       # Dependencies
├── postman_collection.json # Postman collection
├── .gitignore            # Git ignore rules
└── tasks.db              # SQLite database (auto-generated)
```

## ✅ HTTP Status Codes

- `200 OK` - Successful operations
- `201 Created` - Resource created successfully
- `400 Bad Request` - Validation errors
- `404 Not Found` - Resource not found
- `500 Internal Server Error` - Server errors

## 🔍 Validation Rules

- **Title**: Required, max 100 characters
- **Status**: Required, must be one of: `backlog`, `doing`, `done`
- **Description**: Optional, max 500 characters
- **Due Date**: Optional, must be valid date in YYYY-MM-DD format

## 🏗️ Development

The application follows modular architecture:

- **models.py** - Database schema and ORM models
- **routes.py** - API endpoints and business logic  
- **app.py** - Application configuration and initialization

## 📝 Requirements Compliance

✅ **Complete CRUD Implementation** - All operations working  
✅ **Data Validation** - Required fields and format validation  
✅ **Proper HTTP Responses** - Correct status codes (200, 201, 400, 404, 500)  
✅ **Modular Code Organization** - Separated into logical modules  
✅ **Database Integration** - Persistent SQLite storage  
✅ **API Testing** - Postman collection included

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'feat: add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is part of a Software Engineering course assignment.

---

**Author:** Gabriela Lima Sotero  
**Course:** Computer Science - CIn UFPE  
**Project:** Backend Challenge - Task Management REST API
