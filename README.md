# 🦸 Superheroes Flask API

This is a Flask-based API for managing a collection of superheroes, their powers, and the strength of those powers.

---

## 🚀 Features

- View all superheroes
- View details of a single hero  
- Assign powers to heroes with strength levels
- View and manage all powers

---

## 🛠 Tech Stack

- **Python 3.8+**
- **Flask**
- **Flask-SQLAlchemy**


---

## ⚙️ Setup Instructions

1. **Clone the repo** 

    ```bash
    git clone https://github.com/phil-ogutu/superheroes.git
    cd superheroes
    ```

2. **Create venv and Install dependancies:**

    ```bash
    pipenv install
    ```

3. **Run venv:**

    ```bash
    pipenv shell
    ```

4. **Set up the database:**

    ```bash
    flask db init
    flask db migrate -m "Initial migration"
    flask db upgrade head
    ```

5. **Seed the database (optional):**

    ```bash
    python seed.py
    ```

6. **Run the server:**

    ```bash
    cd server
    flask run
    ```
