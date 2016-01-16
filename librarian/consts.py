class MediaType:
    AUDIO = "audio"
    IMAGE = "image"
    ARCHIVE = "archive"

    MAP = "MAP"
    TRV = "TRV"
    VID = "VID"
    OTR = "OTR"

    choices = (
        (AUDIO, "שיר"),
        (IMAGE, "תמונה"),
        (ARCHIVE, "פריט ארכיון"),
        (MAP, "מפה"),
        (TRV, "יומן מסע"),
        (VID, "קטע וידאו"),
        (OTR, "אחר"),
    )

    all = {x[0] for x in choices}
