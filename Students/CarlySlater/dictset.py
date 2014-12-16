import itertools


tester = {'name': 'Chris' , 'city': 'Seattle' , 'cake': 'Chocolate'}

print tester

tester.pop('cake')

print tester

tester.setdefault('fruit','Mango')

key_view = tester.viewkeys()
value_view = tester.viewvalues()

print key_view
print value_view
print tester

cake_test ='cake' in tester
print cake_test

Mango_test = "Mango" in tester.itervalues()
print Mango_test



numlist = (range (16))
print numlist

hexlist = map(hex, numlist)
print hexlist

numhex = dict(zip(numlist, hexlist))

print numhex
print ""
print ""
print "now for aatester times"
print ""
print ""



#tester list - zip dict using number of 'a's in each value.


aatester = {}
for key, val in tester.items():
    aatester[key]=val.count('a')

print aatester
