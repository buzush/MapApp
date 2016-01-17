class MediaType:
    AUDIO = "audio"
    IMAGE = "image"
    ARCHIVE = "archive"
    PHOTO = "photograph"
    MAP = "map"
    SHEET = "sheet"
    OTHER = "other"

    TRV = "TRV"
    VID = "VID"

    choices = (
        (AUDIO, "שיר"),
        (IMAGE, "תמונה"),
        (ARCHIVE, "פריט ארכיון"),
        (PHOTO, "צילום"),
        (MAP, "מפה"),
        (TRV, "יומן מסע"),
        (VID, "קטע וידאו"),
        (SHEET, "גליון"),
        (OTHER, "אחר"),
    )

    all = {x[0] for x in choices}
