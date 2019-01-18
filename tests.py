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

    def test_general_values(self):
        """Test some values within schema that should be consistent
        """
        for _doc in self.biothings_schema['@graph']:
            self.assertEqual(_doc["http://schema.org/isPartOf"],
                             {"@id": "http://schema.biothings.io"})
            self.assertIn(_doc["@type"], ["rdfs:Class", "rdf:Property"])
            self.assertEqual(_doc["@id"][:27], "http://schema.biothings.io/")
            self.assertEqual(_doc["@id"][27:], _doc["rdfs:label"])
            self.assertEqual(len(_doc["rdfs:label"].split(' ')), 1)

    def test_class_specific_features(self):
        """Test features belong to schema classes
        """
        all_classes = [_doc["@id"] for _doc in self.biothings_schema["@graph"] if _doc["@type"] == "rdfs:Class"] + ["http://schema.org/Thing"]
        for _doc in self.biothings_schema["@graph"]:
            if _doc["@type"] == "rdfs:Class":
                self.assertTrue(_doc["rdfs:label"][0].isupper())
                if _doc["rdfs:subClassOf"]["@id"] != "http://schema.org/Thing":
                    self.assertTrue(_doc["rdfs:subClassOf"]["@id"][27].isupper())
                self.assertIn(_doc["rdfs:subClassOf"]["@id"], all_classes)

    def test_property_specific_features(self):
        all_classes = [_doc["rdfs:label"] for _doc in self.biothings_schema["@graph"] if _doc["@type"] == "rdfs:Class"] + ["Thing"]


if __name__ == '__main__':
    unittest.main()
