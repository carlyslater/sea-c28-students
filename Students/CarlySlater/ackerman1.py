def ackattack(m, n):
    if m == 0: return n + 1
    if m >= 0 and n ==0: return ackattack(m-1, 1)
    if m >= 0 and n >=0: return ackattack(m-1, ackattack(m, n-1))
"""Return the result of ackermans function adjusting for inputs of 0."""

print ackattack(2, 3)
  