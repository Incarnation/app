from app import app
import unittest
import json


class BasicTestCase(unittest.TestCase):

    # Test GET users
    def test_get_users(self):
        tester = app.test_client(self)
        response = tester.get("/api/users", content_type='application/json')
        added_user = response.json[0]
        self.assertEqual(added_user['email'], "johnwu@gmail.com")
        self.assertEqual(added_user['first_name'], "John")
        self.assertEqual(added_user['last_name'], "Wu")
        self.assertEqual("61a56a765eb6cf68efab7ded",
                         added_user['_id']['$oid'])
        self.assertEqual(response.status_code, 200)

    # Test GET books
    def test_get_books(self):
        tester = app.test_client(self)
        response = tester.get("/api/books", content_type='application/json')
        self.assertEqual(response.status_code, 200)

    # Test create a book
    def test_post_books(self):
        tester = app.test_client(self)
        book_payload = {
            "user_id": "61a56a765eb6cf68efab7ded",
            "book": {
                "title": "book3",
                "author": "author3",
                "isbn": "isbn3",
                "publication_date": "book1_date3"
            }
        }

        response = tester.post('/api/books',
                               headers={"Content-Type": "application/json"
                                        },
                               data=json.dumps(book_payload))

        self.assertEqual(response.status_code, 200)

    # Test GET a single book

    def test_get_book(self):
        tester = app.test_client(self)
        response = tester.get(
            "/api/books/61a5746caebb9239739a8f96", content_type='application/json')
        self.assertEqual(response.status_code, 200)

    # Test UPDATE a book
    def test_update_book(self):
        tester = app.test_client(self)
        book_payload = {
            "user_id": "61a56a765eb6cf68efab7ded",
            "book": {
                "title": "book4",
                "author": "author5",
                "isbn": "isbn6",
                "publication_date": "book1_date7"
            }
        }

        response = tester.put('/api/books/61a5746caebb9239739a8f96',
                              headers={"Content-Type": "application/json"
                                       },
                              data=json.dumps(book_payload))

        self.assertEqual(response.status_code, 200)

    # Test DELETE a book
    def test_delete_book(self):
        tester = app.test_client(self)

        # first create a book
        book_payload = {
            "user_id": "61a56a765eb6cf68efab7ded",
            "book": {
                "title": "book3",
                "author": "author3",
                "isbn": "isbn3",
                "publication_date": "book1_date3"
            }
        }

        response = tester.post('/api/books',
                               headers={"Content-Type": "application/json"
                                        },
                               data=json.dumps(book_payload))

        self.assertEqual(response.status_code, 200)

        # then delete the book
        delete_id = response.json["id"]
        response = tester.delete('/api/books/' + delete_id)
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
