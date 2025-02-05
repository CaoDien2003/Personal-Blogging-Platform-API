# Personal Blogging Platform API

## Overview

The **Personal Blogging Platform API** is a backend-only RESTful API built with Flask. It provides functionality to manage user authentication and blog posts, with role-based access control.

- **Admin Role**: Can create, update, and delete blog posts.
- **User Role**: Can only view blog posts.

---

## Features

- **User Authentication**:

  - Secure login using JWT tokens.
  - User registration with hashed passwords.
  - Role-based access control (`admin` and `user` roles).

- **Blog Management**:

  - Admins can create, update, and delete blog posts.
  - Both admins and users can view blog posts.

- **Database Integration**:

  - PostgreSQL database for user and blog data storage.

- **Secure API**:
  - JWT-based authentication to secure endpoints.

---

## Getting Started

### Prerequisites

Ensure the following are installed before running the project:

[![Python](https://img.shields.io/badge/python-3.8%2B-blue?logo=python&logoColor=white)](https://www.python.org/downloads/)

[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-v12%2B-blue?logo=postgresql&logoColor=white)](https://www.postgresql.org/download/)

---

### Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/CaoDien2003/Personal-Blogging-Platform-API.git
   cd Personal-Blogging-Platform-API
   ```

2. **Set Up a Virtual Environment**:

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   # On Windows: .venv\Scripts\activate
   ```

3. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure the Database**:

   - Rename the `app/storage/config.sample.py` file to `config.py`:
     ```bash
     mv app/storage/config.sample.py app/storage/config.py
     ```
   - Add your PostgreSQL database credentials to the `config.py` file:
     ```python
     DB_CONFIG = {
         'DB_NAME': 'your_db_name',
         'DB_USER': 'your_db_user',
         'DB_PASSWORD': 'your_db_password',
         'DB_HOST': 'localhost',
         'DB_PORT': '5432'
     }
     ```

5. **Run Database Migrations** (Optional if using a fresh DB setup):

   ```sql
   CREATE TABLE users (
       id SERIAL PRIMARY KEY,
       username VARCHAR(255) UNIQUE NOT NULL,
       password VARCHAR(255) NOT NULL,
       role VARCHAR(50) NOT NULL
   );

   CREATE TABLE blogs (
       id SERIAL PRIMARY KEY,
       title TEXT NOT NULL,
       author VARCHAR(255) NOT NULL,
       content TEXT NOT NULL
   );
   ```

---

### Running the Application

1. Start the Flask development server:

   ```bash
   python run.py
   ```

2. The server will run at:
   - **Localhost**: `http://127.0.0.1:5000`

---

## API Endpoints

### **Authentication**

| Method | Endpoint         | Description                     | Authorization |
| ------ | ---------------- | ------------------------------- | ------------- |
| POST   | `/auth/login`    | Log in and receive a JWT token. | None          |
| POST   | `/auth/register` | Register a new user.            | None          |

---

### **Blogs**

| Method | Endpoint      | Description                  | Authorization |
| ------ | ------------- | ---------------------------- | ------------- |
| GET    | `/blogs`      | Fetch all blog posts.        | None          |
| GET    | `/blogs/<id>` | Fetch a specific blog by ID. | None          |
| POST   | `/blogs`      | Create a new blog post.      | Admin         |
| PUT    | `/blogs/<id>` | Update an existing blog.     | Admin         |
| DELETE | `/blogs/<id>` | Delete a blog post.          | Admin         |

---

## Example Usage

### **Login**

**Request**:

```bash
POST /auth/login
Content-Type: application/json
{
    "username": "admin",
    "password": "admin123"
}
```

**Response**:

```json
{
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

---

### **Create a Blog Post (Admin Only)**

**Request**:

```bash
POST /blogs
Authorization: Bearer <JWT-TOKEN>
Content-Type: application/json
{
    "title": "My First Blog",
    "content": "This is the content of my blog."
}
```

**Response**:

```json
{
  "message": "Blog created successfully",
  "id": 1
}
```

---

## Contributing

Contributions are welcome! Follow these steps to contribute:

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature/your-feature
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add your feature"
   ```
4. Push to your branch:
   ```bash
   git push origin feature/your-feature
   ```
5. Submit a pull request.

---

## Contact

For inquiries or feedback, feel free to reach out:

- **Email**: nguyencaodien2003@gmail.com
- **GitHub**: [CaoDien2003](https://github.com/YourGitHubUsername)
- **LinkedIn**: [Điền Cao](https://www.linkedin.com/in/nguyencaodien/)
