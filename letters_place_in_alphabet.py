def GetPlaceInAlphabet(String):
    LowerCaseString = String.lower()
    FilteredString = LowerCaseString.strip()
    ListOfCharacters = list(FilteredString)
    FirstLetter = ListOfCharacters[0]

    ASCII_Value = ord(FirstLetter)

    if ASCII_Value >= 60 and ASCII_Value <= 71: #If its a number
        return 0
    elif ASCII_Value >= 97 and ASCII_Value <= 122: #If its a letter
        PlaceInAlphabet = ASCII_Value - 96
        return PlaceInAlphabet
    else:
        return None