# PENTA CRUD TEST SUITE
Develoed a test suite to perform and verify CRUD (Create, Read, Update, Delete) operations on a resource of "BOOKS" using the [CrudCrud API](https://crudcrud.com/).
NOTE: Each created resource is automatically assigned a unique identifier for easy reference. Please see [CrudCrud API](https://crudcrud.com/) docs for more information.

## API Endpoints
The following API endpoints are used for CRUD operations:

- **POST** `/books` - Create a new book
- **GET** `/books` - Retrieve all books
- **GET** `/books/{id}` - Retrieve a book by ID
- **PUT** `/books/{id}` - Update an existing book (First one)
- **DELETE** `/books/{id}` - Delete a books by ID

## Instructions

### 1. Implementation Language
The test suite is implemented in **Python**.

### 2. Testing Framework
We use **pytest** as our testing framework.

### 3. Libraries Used
The following libraries are utilized in this project:

- **requests**: For making HTTP requests to the CrudCrud API.
- **pytest**: For structuring and running the test suite.
- **json**: For handling JSON data in Python.

### 4. Page Object Model (POM)
In this implementation, we follow the **Page Object Model (POM)** design pattern to encapsulate the API endpoints and their operations. This enhances maintainability and readability by separating the test logic from the API interaction logic. Each resource (e.g., `User`) can be represented as a class that contains methods for CRUD operations.

### 5. Test Suite Overview
The test suite includes the following tests for CRUD operations on the users resource:

1. **Create book**
2. **Read books**
3. **Update book**
4. **Delete books**
  
# Project Structure
## Directory and File Descriptions
- **main.py**: File to run the test suite.
- **README.md**: Contains project overview, setup instructions, and usage details.
- **requirements.txt**: Lists the Python packages required for the project.
- **apis/**: This directory contains the methods for interacting with user-related API endpoints
- **tests/**: This directory contains the test files.
- **utils/**: Contains extra help functions and utilities
- **data/**: This directory contains JSON data files.
- **venv/**: Contains the virtual environment

## Usage

To run the **main.py** file, navigate to your project directory in the terminal and execute:

```bash
python main.py
