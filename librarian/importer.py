import requests

BASE_URL = "http://primo.nli.org.il/PrimoWebServices/xservice/search/full"


def primo_request(doc_id):
    params = {
        "institution": "NNL",
        "docId": doc_id,
        "json": "true"
    }
    r = requests.get(BASE_URL, params)
    r.raise_for_status()
    return r.json()


def get_primo_data(doc_id):
    # TODO: use `primo_request` above and extract relavant data only.
    return {
        'name': "name {}".format(doc_id),
        'desc': "desc desc {}".format(doc_id),
    }
