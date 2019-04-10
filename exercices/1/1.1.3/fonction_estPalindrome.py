def estPalindrome(Sentence):
    # remove all spaces
    Trim = Sentence.replace(" ", "")
    # invert lists
    Invert_Trim = Trim[::-1]
#     print("Trim",Trim)
#     print("invert trim",Invert_Trim)

    if Trim == Invert_Trim:
        return True
    else:
        return False
    pass
