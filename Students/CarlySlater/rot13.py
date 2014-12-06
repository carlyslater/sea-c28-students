import string


rot13 = string.maketrans("abcdefghijklmABCDEFGHIJKLMnopqrstuvwxyzNOPQRSTUVWXYZ", "nopqrstuvwxyzNOPQRSTUVWXYZabcdefghijklmABCDEFGHIJKLM")

def translateytimes():
    phrase = string.translate((raw_input("enter phrase for translation    ")), rot13)
    print phrase

translateytimes()


#if __name__ == '__main__'
#should ask for input and translate it.