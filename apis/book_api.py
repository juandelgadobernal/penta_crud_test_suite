import requests

class BookAPI:
    """
    A class to interact with the Book API for CRUD operations on book records.
    """
    def __init__(self, access_token):
        """
        Initialize the API instance with  access token and base URL.
        :param access_token: str: The access token for authentication with the API.
        """
        self.access_token = access_token
        self.entity = "books"
        self.base_url = f"https://crudcrud.com/api/{self.access_token}/{self.entity}"

    def create_book(self, book_data):
        """
        Creates a new book record
        :param book_data: JSON Data
        :return: str: The unique ID of the created book
        """
        response = requests.post(self.base_url, json=book_data)
        if response.status_code == 201:
            return response.json()["_id"]
        else:
            raise Exception(f"Failed to create book: {response.text}")

    def read_books(self):
        """
        Retrieves all book records from the API.
        :return: list: A list of dictionaries, each representing a book.
        """
        response = requests.get(self.base_url)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to retrieve books: {response.text}")

    def update_book(self, book_id, updated_data):
        """
        Updates an existing book record with new data.
        :param book_id: str: unique ID of the book to be updated.
        :param updated_data: dict: A dictionary with the updated book details.
        :return: None
        """
        response = requests.put(f"{self.base_url}/{book_id}", json=updated_data)
        if response.status_code == 200:
            print(" ")
            print(f"Book ID {book_id} has been updated.")
        else:
            print(" ")
            print(f"Book ID {book_id} has NOT been updated.")

    def update_book_verification(self, book_id):
        """
        Verifies the updated data of a specific book
        :param book_id: str: The unique ID of the book to verify
        :return: The response object containing the book details.
        """
        response = requests.get(f"{self.base_url}/{book_id}")
        assert response.status_code == 200, f"Error retrieving the updated book: {response.text}"
        if response.status_code == 200:
            return response

    def delete_book(self, book_id):
        """
        Deletes a specific book record from the API.
        :param book_id: str: The unique ID of the book to be deleted
        :return: bool: True if the book was successfully deleted
        """
        response = requests.delete(f"{self.base_url}/{book_id}")
        if response.status_code == 200:
            print(f"Successfully deleted book with ID: {book_id}")
        else:
            print(f"Failed to delete book with ID: {book_id}, Status Code: {response.status_code}")
        return response.status_code == 200
