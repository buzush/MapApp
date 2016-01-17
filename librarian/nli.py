import re

from librarian.consts import MediaType

COLLECTIONS = {
    'NLI_aleksanrowicz_Ros': 'מאגר תצלומי זאב אלכסנדרוביץ',
    'NNL01_Schwad': 'אוסף הפורטרים של אברהם שבדרון',
    'NNL01_Wahrman': 'אוסף עקב ורמן',
    'NNL03_Bitmuna': 'ביתמונה',
    'NNL03_PENN': 'מאגר לנקין',
    'NNL_Ephemera': 'מסע בזמן',
    'NNL_MAPS': 'אוסף המפות',
    'NNL_MUSIC_AL': 'ארכיון המוסיקה',
    'NNL_Zalmania_ROS': 'הצלמניה',
}

LINK_TO_RSRC_RE = re.compile(r"\$\$([A-Z])([^$]+)")
DOCID_RE = re.compile(r"^(.+)(\d+)$")


def is_online_resource(record):
    try:
        return record['delivery']['delcategory'] == "Online Resource"
    except KeyError:
        return False


def parse_linktorsrc(s):
    for m in LINK_TO_RSRC_RE.finditer(s):
        if m.group(1) == "U":
            return m.group(2)
    raise KeyError("link not found in linktorsrc: {}".format(s))


def parse_record(record):
    display = record['display']
    content_type = display['type'].lower()
    assert content_type in MediaType.all, "Unknown media type: {}".format(
            content_type
    )
    try:
        link = parse_linktorsrc(record['links']['linktorsrc'])
    except KeyError:
        link = record['display'].get('lds42')

    name = display['title']
    creator = display.get('creator') or display.get('contributor')
    performing = display.get('lds12') or display.get('lds35')

    date = display.get('creationdate')

    description = display.get('subject')

    collection_code = record['control']['sourceid']

    return dict(
            doc_id=record['control']['recordid'],
            collection_code=collection_code,
            collection_title=COLLECTIONS.get(collection_code, collection_code),
            content_type=content_type,
            name=name,
            creator=creator,
            performing=performing,
            description=description,
            link=link,
            date=date,
    )


def split_doc_id(doc_id):
    m = DOCID_RE.match(doc_id)
    if not m:
        raise ValueError("Bad docid: {}".format(doc_id))
    return m.groups(1), m.groups(2)
