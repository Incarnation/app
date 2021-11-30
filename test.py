from app import app
import unittest
import json


class BasicTestCase(unittest.TestCase):
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

    def test_get_books(self):
        tester = app.test_client(self)
        response = tester.get("/api/books", content_type='application/json')
        self.assertEqual(response.status_code, 200)

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

    def test_get_book(self):
        tester = app.test_client(self)
        response = tester.get(
            "/api/books/61a57799d052a6348ed7d0bd", content_type='application/json')
        self.assertEqual(response.status_code, 200)

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

        response = tester.put('/api/books/61a5a716346017b73c69023b',
                              headers={"Content-Type": "application/json"
                                       },
                              data=json.dumps(book_payload))

        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
