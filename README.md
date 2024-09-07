Here's a well-detailed README template for your Python Flask CRUD API with MySQL, Docker, and middleware:

---

# Library API

The **Library API** is a RESTful CRUD API built using **Flask**, **SQLAlchemy**, and **MySQL** for managing books, authors, and customers in a library system. It also features authentication middleware to protect routes and uses Docker for database setup. The project includes integration and unit tests to ensure reliable functionality.

## Features

- CRUD operations for managing **Books**, **Authors**, and **Customers**.
- **MySQL** database connection with Docker.
- **SQLAlchemy** for ORM (Object-Relational Mapping).
- Basic **Authentication Middleware**.
- Unit and Integration tests using **pytest**.
- Environment variables for easy configuration.
- Docker Compose for seamless database setup.

## Table of Contents

- [Installation](#installation)
- [Project Structure](#project-structure)
- [API Endpoints](#api-endpoints)
- [Running the App](#running-the-app)
- [Running Tests](#running-tests)
- [Docker Setup](#docker-setup)
- [Contributing](#contributing)
- [License](#license)

## Installation

### Prerequisites

Ensure you have the following tools installed on your machine:

- [Python 3.12+](https://www.python.org/)
- [Docker](https://www.docker.com/)
- [MySQL](https://www.mysql.com/)

### Clone the Repository

```bash
git clone https://github.com/yourusername/library-api.git
cd library-api
```

### Virtual Environment Setup

1. Create a virtual environment:

   ```bash
   python -m venv venv
   ```

2. Activate the virtual environment:

   - **MacOS/Linux**:

     ```bash
     source venv/bin/activate
     ```

   - **Windows**:

     ```bash
     venv\Scripts\activate
     ```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Environment Variables

Create a `.env` file in the root directory of the project to manage configuration:

```
FLASK_APP=app.py
FLASK_ENV=development
SQLALCHEMY_DATABASE_URI=mysql+pymysql://user:userpassword@localhost:3306/library_db
```

- Replace `user`, `userpassword`, and `library_db` with your actual database credentials.

### Docker Database Setup

A `docker-compose.yml` file is provided to quickly set up the MySQL database. Run the following command:

```bash
docker-compose up -d
```

This command starts up a MySQL instance with the database `library_db`.

## Project Structure

```
library-api/
│
├── app.py                   # Main Flask application
├── config.py                # Configuration for Flask and SQLAlchemy
├── requirements.txt         # Python dependencies
├── Dockerfile               # Docker setup for the application
├── docker-compose.yml       # Docker Compose file for MySQL setup
├── models/                  # SQLAlchemy models
│   ├── book.py              # Book model
│   ├── author.py            # Author model
│   └── customer.py          # Customer model
│
├── routes/                  # API Routes (Blueprints)
│   ├── book_routes.py       # Book routes
│   ├── author_routes.py     # Author routes
│   └── customer_routes.py   # Customer routes
│
├── middleware/              # Middleware for authentication
│   └── auth_middleware.py   # Authentication middleware
│
├── tests/                   # Unit and integration tests
│   ├── test_books.py        # Unit tests for Book
│   ├── test_authors.py      # Unit tests for Author
│   ├── test_customers.py    # Unit tests for Customer
│   └── test_integration.py  # Integration tests for all models
│
└── .env                     # Environment variables (local use)
```

## API Endpoints

### Books

| Method | Endpoint        | Description                 |
|--------|-----------------|-----------------------------|
| POST   | `/books`         | Create a new book           |
| GET    | `/books`         | Get all books               |
| GET    | `/books/<id>`    | Get a specific book         |
| PUT    | `/books/<id>`    | Update a specific book      |
| DELETE | `/books/<id>`    | Delete a specific book      |

### Authors

| Method | Endpoint        | Description                 |
|--------|-----------------|-----------------------------|
| POST   | `/authors`       | Create a new author         |
| GET    | `/authors`       | Get all authors             |
| GET    | `/authors/<id>`  | Get a specific author       |
| PUT    | `/authors/<id>`  | Update a specific author    |
| DELETE | `/authors/<id>`  | Delete a specific author    |

### Customers

| Method | Endpoint        | Description                 |
|--------|-----------------|-----------------------------|
| POST   | `/customers`     | Create a new customer       |
| GET    | `/customers`     | Get all customers           |
| GET    | `/customers/<id>`| Get a specific customer     |
| PUT    | `/customers/<id>`| Update a specific customer  |
| DELETE | `/customers/<id>`| Delete a specific customer  |

## Running the App

1. Start your Docker MySQL container if not already running:

   ```bash
   docker-compose up -d
   ```

2. Run the Flask app:

   ```bash
   python app.py
   ```

3. Access the API at: [http://127.0.0.1:5000](http://127.0.0.1:5000)

### Running Tests

Run the tests using `pytest`:

```bash
pytest tests/
```

### Available Tests

- **Unit Tests**: Test CRUD operations for Books, Authors, and Customers.
- **Integration Tests**: Test the full API functionality including the database.

## Docker Setup

The project uses Docker to set up the MySQL database for local development.

### Using Docker Compose

To start the MySQL database:

```bash
docker-compose up -d
```

- The database will be available at `localhost:3306`.
- Credentials are set in the `docker-compose.yml` file:
  - Username: `user`
  - Password: `userpassword`
  - Database: `library_db`

To stop the containers:

```bash
docker-compose down
```

## Contributing

Contributions are welcome! If you find any issues or want to contribute improvements, feel free to submit a pull request.

### How to Contribute

1. Fork the repository.
2. Create a feature branch: `git checkout -b my-new-feature`.
3. Commit your changes: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin my-new-feature`.
5. Open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Let me know if you'd like any modifications!