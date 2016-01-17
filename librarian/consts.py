class MediaType:
    AUDIO = "audio"
    IMAGE = "image"
    ARCHIVE = "archive"
    MAP = "map"
    TRV = "travel"
    VID  = "video"
    OTR = "other"

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
