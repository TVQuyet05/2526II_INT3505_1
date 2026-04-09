import unittest

from flask import json

from openapi_server.models.book import Book  # noqa: E501
from openapi_server.models.new_book import NewBook  # noqa: E501
from openapi_server.test import BaseTestCase


class TestBooksController(BaseTestCase):
    """BooksController integration test stubs"""

    def test_books_get(self):
        """Test case for books_get

        List books
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/books',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_books_id_delete(self):
        """Test case for books_id_delete

        Delete a book
        """
        headers = { 
        }
        response = self.client.open(
            '/books/{id}'.format(id='id_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_books_id_get(self):
        """Test case for books_id_get

        Get a book by ID
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/books/{id}'.format(id='id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_books_id_put(self):
        """Test case for books_id_put

        Update a book
        """
        new_book = {"author":"Robert C. Martin","genre":"Software Engineering","publishedYear":2008,"title":"Clean Code"}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/books/{id}'.format(id='id_example'),
            method='PUT',
            headers=headers,
            data=json.dumps(new_book),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_books_post(self):
        """Test case for books_post

        Create a book
        """
        new_book = {"author":"Robert C. Martin","genre":"Software Engineering","publishedYear":2008,"title":"Clean Code"}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/books',
            method='POST',
            headers=headers,
            data=json.dumps(new_book),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
