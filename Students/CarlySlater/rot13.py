import string


rot13 = string.maketrans("abcdefghijklmABCDEFGHIJKLMnopqrstuvwxyzNOPQRSTUVWXYZ", "nopqrstuvwxyzNOPQRSTUVWXYZabcdefghijklmABCDEFGHIJKLM")

def translateytimes(phrase=None):
    if phrase is None:
        phrase = (raw_input("enter phrase for translation    "))
    phrase = string.translate(phrase, rot13)
    print phrase
    return phrase

if __name__ == '__main__':
#should ask for input and translate it.

    assert translateytimes("It's my birthday!") == "Vg'f zl oveguqnl!"
    #print translateytimes
    #print translateytimes is to test the test function.  kept here in case i screw with it more later
    print "all tests passed"

translateytimes()