## FastAPI Setup Guide

This guide will walk you through setting up and running a basic FastAPI application. FastAPI is a modern, high-performance web framework for building APIs with Python 3.7+ using standard Python type hints.

---

### 1. Prerequisites

Ensure you have **Python 3.7+** installed. Check your version with:

```bash
python --version
# or
python3 --version
```

---

### 2. Project Setup

It's recommended to use a virtual environment for dependency management.

**Create a Virtual Environment**

Navigate to your project directory and run:

- **macOS/Linux:**
    ```bash
    python3 -m venv venv
    ```
- **Windows:**
    ```bash
    python -m venv venv
    ```

**Activate the Virtual Environment**

- **macOS/Linux:**
    ```bash
    source venv/bin/activate
    ```
- **Windows:**
    ```bash
    .\venv\Scripts\activate
    ```

---

### 3. Install Dependencies

With the virtual environment active, install FastAPI and Uvicorn:

```bash
pip install fastapi "uvicorn[standard]"
```

- `fastapi`: The core framework.
- `uvicorn`: ASGI server to run your app (`[standard]` adds recommended extras).

---

### 4. Create Your First FastAPI App

Create a file named `main.py` and add:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
        return {"message": "Hello, World!"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
        return {"item_id": item_id, "q": q}
```

---

### 5. Run the Development Server

Start your app with:

```bash
uvicorn main:app --reload
```

- `main`: Refers to `main.py`.
- `app`: The FastAPI instance.
- `--reload`: Auto-reloads on code changes (for development).

You should see output indicating the server is running at [http://127.0.0.1:8000](http://127.0.0.1:8000).

---

### 6. Access Your API

- [http://127.0.0.1:8000](http://127.0.0.1:8000): Returns `{"message": "Hello, World!"}`
- [http://127.0.0.1:8000/items/5?q=somequery](http://127.0.0.1:8000/items/5?q=somequery): Returns `{"item_id":5,"q":"somequery"}`

---

### 7. Interactive API Documentation

FastAPI provides interactive docs:

- **Swagger UI:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

### 8. Deactivate the Virtual Environment

When finished, deactivate with:

```bash
deactivate
```

---

## My Awesome FastAPI Project 🚀

A simple REST API for managing a to-do list, built with FastAPI.

---

## Features ✨

- **Fast**: Built on Starlette and Pydantic for high performance.
- **Automatic Docs**: Interactive API documentation (Swagger UI and ReDoc).
- **Modern Python**: Fully typed with Python 3.8+ type hints.
- **Easy to Use**: Intuitive and simple to start with.

---

## ⚙️ Setup and Installation

### Prerequisites

- **Python 3.8+**
- **pip**

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/your-project-name.git
cd your-project-name
```