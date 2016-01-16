"""
To run this:

    python -m unittest librarian.nli_tests


"""

import json
import unittest

from librarian import nli


class NLITestCase(unittest.TestCase):
    def parse_doc(self, doc_id):
        with open("test_data/{}.json".format(doc_id)) as f:
            d = json.load(f)
        result = nli.parse_record(d)
        return result

    def test_simple_request(self):
        doc_id = "NNL_MUSIC_AL002674543"
        result = self.parse_doc(doc_id)

        doc_id = "NNL_ALEPH003440887"
        result = self.parse_doc(doc_id)

    def test_parse_linktosrc(self):
        s = "$$Uhttp://rosetta.nli.org.il/delivery/action/cmsResolver.do?cmsSystem=NNL01&cmsRecordId=002674543&orderBy=dc:title$$Elinktorsrclocal"
        actual = nli.parse_linktorsrc(s)
        expected = "http://rosetta.nli.org.il/delivery/action/cmsResolver.do?cmsSystem=NNL01&cmsRecordId=002674543&orderBy=dc:title"
        self.assertEquals(expected, actual)


if __name__ == '__main__':
    unittest.main()
