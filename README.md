# Personal Blogging Platform API

A RESTful API for a personal blogging platform built with Flask and MongoDB. This API supports basic CRUD operations, such as creating, reading, updating, and deleting blog posts, and allows filtering posts by keywords.

---

## Features

- **Create Blog Post**: Add a new blog post to the database.
- **Read Blog Posts**: Retrieve all blog posts or a specific post by ID.
- **Update Blog Post**: Update an existing blog post.
- **Delete Blog Post**: Remove a blog post by ID.
- **Filter Blog Posts**: Search blog posts by keywords in their title, content, or category.

---

## Tech Stack

- **Backend Framework**: Flask (Python)
- **Database**: MongoDB
- **Other Tools**: Flask-RESTful, PyMongo

---

## Prerequisites

Before running this project, ensure you have the following installed:

[![Python](https://img.shields.io/badge/python-%203.10%20|%203.11%20|%203.12|%203.13-blue?logo=python&logoColor=white)](https://www.python.org/downloads/)

[![MongoDB](https://img.shields.io/badge/MongoDB-v4.4%20|%20v5.0%20|%20v6.0-brightgreen?logo=mongodb&logoColor=white)](https://www.mongodb.com/try/download/community)

---

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/personal-blogging-platform-api.git
   cd personal-blogging-platform-api
   ```
2. **Requirements**:

   ```bash
   pip install -r src/requirements.txt
   ```

3. **Configure MongoDB**:

   - Copy the .env.sample file and create a .env file:

   ```bash
   cp src/.env.sample src/.env
   ```

   - Add your MongoDB connection string to the .env file.

4. **Running**

   ```bash
   python src/app.py
   ```

## 📬 Contact

For any inquiries or contributions, feel free to reach out:

- **Email:** nguyencaodien2003@gmail.com
- **GitHub:** [CaoDien2003](https://github.com/YourGitHubUsername)
- **LinkedIn:** [Điền Cao](https://www.linkedin.com/in/nguyencaodien/)
