import unittest
import json


class TestBioThingsSchema(unittest.TestCase):
    def setUp(self):
        with open("./biothings/biothings.jsonld") as in_f:
            self.biothings_schema = json.load(in_f)

    def test_keys(self):
        """Test this JSON-LD doc has only three keys
        """
        self.assertEqual(set(self.biothings_schema.keys()),
                         set(["@context", "@graph", "@id"]))


if __name__ == '__main__':
    unittest.main()
