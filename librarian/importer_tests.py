"""
To run this:

    python -m unittest librarian.importer_tests


"""

import unittest

from . import importer


class ImporterTestCase(unittest.TestCase):
    def test_simple_request(self):
        doc_id = "NNL_ALEPH003440887"
        actual = importer.primo_request(doc_id)
        expected = {}
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
