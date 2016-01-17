class MediaType:
    AUDIO = "audio"
    IMAGE = "image"
    ARCHIVE = "archive"
    PHOTO = "photograph"
    MAP = "map"
    TRAVEL = "travel"
    VIDEO  = "video"
    SHEET = "sheet"
    OTHER = "other"

    choices = (
        (AUDIO, "שיר"),
        (IMAGE, "תמונה"),
        (ARCHIVE, "פריט ארכיון"),
        (PHOTO, "צילום"),
        (MAP, "מפה"),
        (TRAVEL, "יומן מסע"),
        (VIDEO, "קטע וידאו"),
        (SHEET, "גליון"),
        (OTHER, "אחר"),
    )

    all = {x[0] for x in choices}
