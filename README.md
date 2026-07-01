# Developer Guidelines
## To push to github without running multiple commands
- Use the gitpush.ps1 script and
Run the following type of command:
```
.\gitpush.ps1 -CommitMessage "Message For Commit Here"
```

## Introduction
A lightweight and scalable **FastAPI**-based REST API for managing issues, bugs, feature requests, and task tracking. This project provides a clean backend foundation for issue management systems with support for CRUD operations, validation, and extensible architecture.

## Features

- RESTful API built with FastAPI
- Create, read, update, and delete issues
- Input validation using Pydantic
- Automatic interactive API documentation
- Modular project structure
- Environment-based configuration
- Database integration (SQLAlchemy or equivalent)
- Error handling with meaningful HTTP responses
- Ready for containerization and deployment
- Easily extensible for authentication, comments, labels, and attachments

## Tech Stack

- **Python 3.10+**
- **FastAPI**
- **Pydantic**
- **SQLAlchemy** (if applicable)
- **Uvicorn**
- **PostgreSQL** (depending on configuration)

## Getting Started

### Clone the Repository

```bash
git clone https://github.com/<your-username>/issue-tracker-api.git
cd issue-tracker-api
```

### Create a Virtual Environment

**Linux/macOS**

```bash
python -m venv venv
source venv/bin/activate
```

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```