# FastAPI Blog API

A simple blog API built with [FastAPI](https://fastapi.tiangolo.com/), [SQLAlchemy](https://www.sqlalchemy.org/), and SQLite.  
This project demonstrates CRUD operations for blog posts and user creation, with validation logic.

## Features

- FastAPI for high-performance APIs
- SQLAlchemy ORM with SQLite database
- Pydantic models for data validation
- User and Blog management
- Custom validation for using Regular Expressions

## Project Structure

```
fastapi-postgres/
│
├── blog/
│   ├── __init__.py
│   ├── database.py
│   ├── main.py         # Main FastAPI app and endpoints
│   ├── models.py       # SQLAlchemy models
│   ├── schemas.py      # Pydantic schemas
│   ├── validity.py     # Custom validation functions
│
├── blog.db             # SQLite database file
├── pyproject.toml      # Project dependencies
└── README.md           # (You are here)
```

## Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/fastapi-postgres.git
   cd fastapi-postgres
   ```

2. **Create and activate a virtual environment:**

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -e .
   ```

   Or, if you use requirements.txt:

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application:**

   ```bash
   uvicorn blog.main:app --reload
   ```

5. **Access the API docs:**
   - Open [http://localhost:8000/docs](http://localhost:8000/docs) in your browser.

## API Endpoints

### Blog

- `POST /blog`  
  Create a new blog post.

- `GET /blog`  
  Get all blog posts.

- `GET /blog/{id}`  
  Get a single blog post by ID.

- `PUT /blog/{id}`  
  Update a blog post by ID.

- `DELETE /blog/{id}`  
  Delete a blog post by ID.

### User

- `POST /user`  
  Create a new user (with email and name validation).

## Custom Validation

- Email and name validation are handled in `blog/validity.py` and used in the user creation endpoint.
