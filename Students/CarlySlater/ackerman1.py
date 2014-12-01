def ackattack(m, n):
#    if m<0 or n<0: print "none"
#   the above line of code appears to be unecessary in this configuration
    if m == 0: return n + 1
    if m >= 0 and n ==0: return ackattack(m-1, 1)
    if m >= 0 and n >=0: return ackattack(m-1, ackattack(m, n-1))
"""Return the result of ackermans function adjusting for inputs of 0."""

if __name__ == "__main__": 
    assert ackattack(2, 3) == 11
    assert ackattack(0,0) == 1
    assert ackattack(1,0) == 2
    assert ackattack(2,0) == 3
    assert ackattack(3,0) == 5
    assert ackattack(0,1) == 2
    assert ackattack(0,2) == 3
    assert ackattack(0,3) == 4
    assert ackattack(0,4) == 5
    assert ackattack(1,1) == 3
    assert ackattack(2,1) == 5
    assert ackattack(3,1) == 13
    assert ackattack(1,2) == 4
    assert ackattack(1,3) == 5
    assert ackattack(1,4) == 6
    assert ackattack(2,2) == 7
    assert ackattack(3,2) == 29
    assert ackattack(2,3) == 9
    assert ackattack(2,4) == 11
    assert ackattack(3,3) == 61
    assert ackattack(3,4) == 125
    print "All tests passed"



print a(1,1)