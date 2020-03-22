import unittest
import json
from my_json import to_json

STR = "EKME"
BOOL = ["TruE", True, False, "false", 1, 0]
OBJECT = {"home": [2, 3, "cat", "dog"]}


class TestJsonMethods(unittest.TestCase):
    def test_str(self):
        self.assertEqual(to_json(STR), json.dumps(STR))

    def test_bool(self):
        self.assertEqual(to_json(BOOL), json.dumps(BOOL))

    def test_object(self):
        self.assertEqual(to_json(OBJECT), json.dumps(OBJECT))

    def test_for_error(self):
        with self.assertRaises(TypeError):
            to_json(self)
