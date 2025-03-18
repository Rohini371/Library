# Library Management System

This is a Library Management System built using FastAPI. It includes features for managing books, librarians, and customers. The project uses SQLAlchemy for database interactions and includes configurations for ruff and mypy for linting and type checking.

## Requirements

- Python 3.8+
- FastAPI
- Uvicorn
- SQLAlchemy
- Pydantic
- Databases
- Asyncpg
- Ruff
- Mypy
- TailwindCSS

## Installation

1. Clone the repository:
   git clone https://github.com/yourusername/library-management-system.git
   cd library-management-system
   

2. Create and activate a virtual environment:
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   

3. Install the dependencies:
   pip install -r requirements.txt
   
## Configuration

### Ruff

Ruff is configured in the pyproject.toml file:

toml
[tool.ruff]
line-length = 88
select = ["E", "F", "C", "W"]


### Mypy

Mypy is configured in the pyproject.toml and mypy.ini files:

toml
[tool.mypy]
python_version = "3.8"
warn_unused_configs = true
warn_return_any = true
warn_unused_ignores = true


ini
[mypy]
python_version = 3.8
warn_unused_configs = True
warn_return_any = True
warn_unused_ignores = True


## Running the Application

To run the FastAPI application, use the following command:
uvicorn app.main:app --reload

This will start the FastAPI server, and you can access the API at http://127.0.0.1:8000.

## Running Ruff and Mypy

To run ruff and mypy on your project, use the following commands:

ruff .
mypy .

These commands will check your code for linting issues and type errors, respectively.

## Project Structure

Library/
├── app/
│   ├── api/
│   │   └── v1/
│   │       └── endpoints/
│   │           ├── books.py
│   │           ├── librarian.py
│   │           └── customer.py
│   ├── database.py
│   ├── main.py
│   ├── models.py
│   └── templates/
│       └── index.html
├── static/
├── requirements.txt
├── pyproject.toml
├── mypy.ini
└── README.md
