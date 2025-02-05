# **Personal Blogging Platform API**

A lightweight backend API built with Flask for managing blog posts and user authentication. This project uses JWT-based authentication and PostgreSQL as its database. The API is designed for personal or small-scale blogging platforms.

---

## **Features**

- **Authentication**

  - Secure user login and registration using JWT tokens.
  - Role-based access control (`admin` vs `user`).

- **Blog Management**

  - Create, update, delete, and fetch blog posts.
  - View all posts or specific posts by ID.

- **Security**

  - Password hashing for secure storage.
  - Protected endpoints using JWT-based middleware.

- **Database**
  - PostgreSQL for storing users and blog data.
  - Predefined SQL queries for efficient operations.

---

## **Prerequisites**

To run this project, ensure you have the following installed:

1. **Python**: Version 3.8 or higher.
2. **PostgreSQL**: A running instance of PostgreSQL.
3. **Virtual Environment** (optional but recommended).

---

## **Installation**

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-repo-url.git
   cd Personal-Blogging-Platform-API
   ```
