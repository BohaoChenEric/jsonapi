# This file contains unit tests for the JSON functions in jsonapi.py.

import unittest
from jsonapi.jsonapi import parse_json, create_json

class TestJSONParsing(unittest.TestCase):
    def test_json_parsing(self):
        # Test JSON parsing function
        json_data = '{"key": "value"}'
        parsed_data = parse_json(json_data)
        self.assertEqual(parsed_data, {'key': 'value'})

class TestJSONCreation(unittest.TestCase):
    def test_json_creation(self):
        # Test JSON creation function
        data_dict = {'new_key': 'new_value'}
        json_data = create_json(data_dict)
        self.assertEqual(json_data, '{"new_key": "new_value"}')

if __name__ == '__main__':
    unittest.main()