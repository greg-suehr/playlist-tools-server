import unittest

from datastore import load_from_datastore, load_from_service, clean_datastore


import sqlite3 
from datetime import datetime
class load_from_datastore_tester(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        self.conn = sqlite3.connect('test.db')
        self.c = self.conn.cursor()

        # Create a stub table
        try:
            self.c.execute("""CREATE TABLE test (id INTEGER PRIMARY key, a TEXT, b TEXT, 
                                                 created_date TEXT, expire_date_TEXT)""")
        except sqlite3.OperationalError: pass  # this is "table test already exists"
        
        self.c.execute("""INSERT INTO test VALUES (1, 'a', 'b', 
                          '2019-01-01 00:00:00.000000', '2999-01-01 00:00:00.000000')""")
        self.c.execute("""INSERT INTO test VALUES (2, 'a', 'c', 
                          '2019-01-01 00:00:00.000000', '2999-01-01 00:00:00.000000')""")

        super(load_from_datastore_tester, self).__init__(*args, **kwargs)

    def test_datastore_hit_one_int_id_int_key(self):
        results = load_from_datastore(self.c, 'test', [1])

        self.assertIsInstance(results, list)
        self.assertIsEqual(len(results), 1)
                               
    def test_datastore_hit_one_string_id_int_key(self):
        results = load_from_datastore(self.c, 'test', ['1'])

        self.assertIsInstance(results, list)
        self.assertIsEqual(len(results), 1)

    def test_datastore_hit_all(self):
        results = load_from_datastore(self.c, 'test', ['1', '2'])

        self.assertIsInstance(results, list)
        self.assertIsEqual(len(results), 2)

    def test_datastore_hit_some(self):
        results = load_from_datastore(self.c, 'test', ['1', '2', '2999'])

        self.assertIsInstance(results, list)
        self.assertIsEqual(len(results), 2)

    def test_datastore_handle_duplicates_quietly(self):
        results = load_from_datastore(self.c, 'test', ['1', '1'])

        self.assertIsInstance(results, list)
        self.assertIsEqual(len(results), 1) # TODO: needs documented

    def test_datastore_miss(self):
        results = load_from_datastore(self.c, 'test', ['2999'])

        self.assertIsInstance(results, list)
        self.assertIsEqual(len(results), 0) # TODO: needs documented



class load_from_service_tester(unittest.TestCase):
    def test_service_miss(self):
        self.assertEqual(0,1)


class clean_datastore_tester(unittest.TestCase):
    def test_none_expired(self):
        self.assertEqual(0,1)

    def test_all_expired(self):
        self.assertEqual(0,1)

    def test_only_first_expired(self):
        self.assertEqual(0,1)

    def test_all_but_first_expired(self):
        self.assertEqual(0,1)

    def test_fragmented_expired(self):
        self.assertEqual(0,1)


if __name__ == '__main__':
    unittest.main()