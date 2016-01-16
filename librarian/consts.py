class MediaType:
    AUDIO = "audio"
    IMAGE = "image"
    ARCHIVE = "archive"
    PHOTO = "photograph"

    MAP = "MAP"
    TRV = "TRV"
    VID = "VID"
    OTR = "OTR"

    choices = (
        (AUDIO, "שיר"),
        (IMAGE, "תמונה"),
        (ARCHIVE, "פריט ארכיון"),
        (PHOTO, "צילום"),
        (MAP, "מפה"),
        (TRV, "יומן מסע"),
        (VID, "קטע וידאו"),
        (OTR, "אחר"),
    )

    all = {x[0] for x in choices}
