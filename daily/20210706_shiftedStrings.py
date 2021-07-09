# You are given two strings, A and B. Return whether A can be shifted some number of times to get B.

# Eg. A = abcde, B = cdeab should return true because A can be shifted 3 times to the right to get B. A = abc and B= acb should return false.

# def is_shifted(a, b):
#   # Fill this in.
  
# print is_shifted('abcde', 'cdeab')
# # True

def is_shifted(a,b):
    if len(a) != len(b):
        return False
    if len(a) <2:
        return a == b
    
    shift_clock = ""
    shift_anticlock = ""
    l = len(b)

    shift_anticlock = (shift_anticlock + b[l - 2:] + b[0: l -2] )
    shift_clock = shift_clock + b[2:] + b[0:2]

    return (a == shift_clock or a == shift_anticlock)

print(is_shifted('abcde', 'deabc'))