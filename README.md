# Task Tracker

Task Tracker is a simple task management server—helping you manage your tasks efficiently by allowing you to create, view, update, and delete—built with FastAPI using SQLAlchemy.

## Start FastAPI
Run this command in the src directory:
```bash
make all
```
## Main Features
Make sure the FastAPI server is running!

### **Create Tasks:** Add new tasks with ease.
```bash
curl -X POST "http://127.0.0.1:8000/create/?todo=Example"
```
- Where ``todo`` is the task to add. 

### **Read Tasks:** View all your tasks in one place.
```bash
curl "http://127.0.0.1:8000"
```

### **Update Tasks:** Modify existing tasks as needed.
```bash
curl -X PUT "http://127.0.0.1:8000/update/1/?todo=New%20Example"
```
- Where `1` is ID of the task and `todo` - is the new task description. 

### **Delete Tasks:** Remove tasks that are no longer necessary.
```bash
curl -X DELETE "http://127.0.0.1:8000/delete/1" 
```
- Where `1` is `ID` of the task to delete. 

