import pytest
from apis.book_api import BookAPI
from utils.books_utils import load_data

ACCESS_TOKEN = "36be288aaa7642a28c6cfcd60a016dd6"
book_api = BookAPI(ACCESS_TOKEN)
create_books_data_path = '../data/create_books.json'
update_books_data_path = '../data/update_books.json'

@pytest.fixture
def create_book():
    """
    Fixture to create a book
    :return: function: Function to create a book
    """
    def _create_book(book_data):
        """
        Create the book with the provided data.
        :param book_data: A dict data of the books
        :return: str: ID of the created books
        """
        return book_api.create_book(book_data)
    return _create_book

@pytest.mark.parametrize("book_data", load_data(create_books_data_path))
def test_create_books(create_book, book_data):
    """
    Test to create multiple books using the "create_book" ficture
    :param create_book: functon: Fixture function to create book
    :param book_data: A dict data of the books
    :return:
    :assert: Book ID is None
    """
    book_id = create_book(book_data)
    print(f"Book with ID {book_id} has been created with data: {book_data}")
    assert book_id is not None, f"Book ID should not be None for book: {book_data['name']}"

def test_read_books():
    """
    Test reading list fo books
    :return:
    :assert: Expect a list of Books
    """
    books = book_api.read_books()
    #print("")
    print("\nJSON List of all Books")
    for item in books:
        print(item)
    assert isinstance(books, list), "Expected a list of books"

def test_update_book():
    """
    Test updating an existing book --The first one in the list as example
    :return:
    :asserts: Updated fields (name and author) match the expected values.
    """
    books = book_api.read_books()
    if books:
        first_book_id = books[0]["_id"]
        updated_data = load_data(update_books_data_path)
        book_api.update_book(first_book_id, updated_data)
        test_read_books()
        updated_book_response = book_api.update_book_verification(first_book_id)
        updated_book_validation = updated_book_response.json()
        assert updated_book_validation["name"] == updated_data["name"], "The name was not updated correctly."
        assert updated_book_validation["author"] == updated_data["author"], "The author was not updated correctly."

def test_all_books_deleted():
    """
    Test delete all books
    :return:
    :assert: No books remain after deletion.
    """
    books = book_api.read_books()
    if not books:
        print("\nNo books available to delete.")
        return
    else:
        print("")

    for book in books:
        book_api.delete_book(book["_id"])
    final_books = book_api.read_books()
    assert len(final_books) == 0, f"Some books were not deleted. Remaining books: {final_books}"
