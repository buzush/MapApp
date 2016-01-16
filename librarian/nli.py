import re

from django.utils.translation import ugettext_lazy as _

from librarian.consts import MediaType

LINK_TO_RSRC_RE = re.compile(
        r"\$\$([A-Z])([^$]+)"
)


def is_online_resource(record):
    try:
        return record['delivery']['delcategory'] == "Online Resource"
    except KeyError:
        return False


def parse_linktorsrc(s):
    for m in LINK_TO_RSRC_RE.finditer(s):
        if m.group(1) == "U":
            return m.group(2)
    raise Exception("link not found in linktorsrc: {}".format(s))


def parse_record(record):
    display = record['display']
    content_type = display['type'].lower()
    assert content_type in MediaType.all, "Unknown media type: {}".format(
            content_type
    )
    link = parse_linktorsrc(record['links']['linktorsrc'])
    name = display['title']
    creator = display.get('creator') or display.get('contributor')
    performing = display.get('lds12') or display.get('lds35')

    date = display.get('creationdate')

    description = display.get('subject')

    return dict(
            content_type=content_type,
            name=name,
            creator=creator,
            performing=performing,
            description=description,
            link=link,
            date=date,
    )
