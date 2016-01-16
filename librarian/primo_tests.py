"""
To run this:

    python -m unittest librarian.primo_tests


"""

import unittest

import json

from . import primo


class ImporterTestCase(unittest.TestCase):
    def test_simple_request(self):
        doc_id = "NNL_ALEPH003440887"
        actual = primo.primo_request(doc_id)
        expected = {}
        with open("noam.json", "w") as f:
            json.dump(actual, f, indent=2)
        self.assertEqual(expected, actual)

    def test_extract_docid(self):
        url = "http://primo.nli.org.il/primo_library/libweb/action/dlDisplay.do?vid=NLI&docId=NNL_MUSIC_AL002674543"
        expected = "NNL_MUSIC_AL002674543"
        actual = primo.extract_doc_id(url)
        self.assertEquals(expected, actual)


if __name__ == '__main__':
    unittest.main()
