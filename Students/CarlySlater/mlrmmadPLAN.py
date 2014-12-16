#make the data structures

masterdonor = {name, amount}
name = (firstname, lastname)
amount = [donations]
#problem: dictionaries cannot take mutable lists, but the correlated datastructure must allow more than one value.  :::headdesk:::


def nameprompt(name):
    name = raw_input("Please provide Donor name ")
    if name == "exit":
    break
    elif Full_Name == "list":
    print {donors}
    name = raw_input("Please provide Donor name ")

if name NOT in {donors}:
    {donors}.adds name
    #name input remains the same?  do i need to return it in order to keep this info?

def howmuch():
    donation = raw_input("Please provide Donation Amount")
    while Donation_Amount != a float:
    print "Please enter a numeric value"
    Donation_Amount = raw_input("Please provide Donation Amount")
    {donation}.ammend(Donation_Amount)
    Donation_Insert = Donation_Amount