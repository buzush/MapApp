from urllib.parse import urlparse, parse_qs

import requests

BASE_URL = "http://primo.nli.org.il/PrimoWebServices/xservice/search/full"


def extract_doc_id(url):
    qs = urlparse(url).query
    d = parse_qs(qs)
    ids = d.get('doc') or d.get('docId')
    if not ids:
        raise KeyError("doc id not found in url: {}".format(url))
    return ids[0]


def primo_request(doc_id):
    params = {
        "institution": "NNL",
        "docId": doc_id,
        "json": "true"
    }
    r = requests.get(BASE_URL, params)
    r.raise_for_status()
    d = r.json()
    doc = d['SEGMENTS']['JAGROOT']['RESULT']['DOCSET']['DOC']['PrimoNMBib'][
        'record']
    return doc
