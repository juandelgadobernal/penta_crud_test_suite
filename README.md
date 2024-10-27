# PENTA CRU TEST SUITE
# CRUD Test Suite for Users Resource

## Overview
This repository contains a test suite to perform and verify CRUD (Create, Read, Update, Delete) operations on a resource using the [CrudCrud API](https://crudcrud.com/). For this implementation, we will manage a resource of **users**.

## API Endpoints
The following API endpoints are used for CRUD operations:

- **POST** `/users` - Create a new user
- **GET** `/users` - Retrieve all users
- **GET** `/users/{id}` - Retrieve a user by ID
- **PUT** `/users/{id}` - Update an existing user by ID
- **DELETE** `/users/{id}` - Delete a user by ID

## Instructions

### 1. Select a Resource
We will manage **users** through CRUD operations.

### 2. Implementation Language
The test suite is implemented in **Python**.

### 3. Testing Framework
We use **pytest** as our testing framework.

### 4. Test Suite Overview
The test suite includes the following tests for CRUD operations on the users resource:

1. **Create User**
   - Test to create a new user with valid JSON payload.
  
2. **Read Users**
   - Test to retrieve all users.
   - Test to retrieve a user by valid ID.
   - Test to handle retrieving a user by invalid ID.
  
3. **Update User**
   - Test to update an existing user with valid JSON payload.
   - Test to handle updating a user with an invalid ID.
  
4. **Delete User**
   - Test to delete a user by valid ID.
   - Test to handle deleting a user with
