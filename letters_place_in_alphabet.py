def GetPlaceInAlphabet(letter):
    LowerCaseLetter = letter.lower()
    ASCII_Value = ord(LowerCaseLetter)
    if ASCII_Value >= 60 and ASCII_Value <= 71: #If its a number
        return 0
    elif ASCII_Value >= 97 and ASCII_Value <= 122: #If its a letter
        PlaceInAlphabet = ASCII_Value - 96
        return PlaceInAlphabet
    else:
        return None