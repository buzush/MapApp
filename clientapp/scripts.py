import requests

def primo_getfilelink(collection,item_id):
    """
    get the url link to item, based on collection and item id from NLI
    """

    url="http://primo.nli.org.il/PrimoWebServices/xservice/search/full?institution=NNL&docId={0}{1}&json=true".format(collection,item_id)
    general_results = requests.get(url)
    return (general_results.json(),url)