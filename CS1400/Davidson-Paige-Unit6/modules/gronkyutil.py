TITLE = ["One",
         "Two",
         "Three",
         "Four",
         "Five",
         "Six",
         "Seven",
         "Eight",
         "Nine",
         "Ten",
         "Baker",
         "Jester",
         "Page",
         "Scribe",
         "Squire",
         "Armorer",
         "Marshal"]

GANG = ["Jets",
        "Pollos",
        "Slugs",
        "Yokels",
        "Keiths",
        "Elbows"]

def convertCardToId(cardTitle, cardGang):
    return GANG.index(cardGang) * len(TITLE) + TITLE.index(cardTitle)
