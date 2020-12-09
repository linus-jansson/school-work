###############################################
# Författare: Linus Jansson 2F
# Uppgift 4
# Programet löser alla nollställen för en ekvation mellan två intervall
###############################################

def f(x):
    # 1x^5 - 3x^4 - 4x^3 + 12x^2 - 0x^1 - 2x^0
    return x**5 - 3*x**4 - 4*x**3 + 12*x**2 - 2

def hasSignChanged(a, b):
    # Checks if the value of f(a) * f(b) is negative or not
    return f(a) * f(b) < 0

# splits interval into n pieces and searches for sign change, i.e. ontaining zeros,
# stores and returns "candidate intervals" as list (as left limit, since intervals are uniform)
def findCandidateIntervals(left, right, n): 
    candidate_intervals = []
    x = left
    
    for i in range(0, n):
        
        if hasSignChanged(x, x + delta_x):
            # DEBUG som skriver ut intervallen som den letat mellan ifall det skett ett teckenskifte
            # print(i, hasSignChanged(x, x + delta_x), x, delta_x)

            candidate_intervals.append(x)
            
        x += delta_x

    return candidate_intervals
  
# halves single interval in search for single zero, returns zero
def findSingleZero(a, b):
    # Simple bisection method to find zero between two intervals
    while b - a > 0.001:
        m = (a + b) / 2

        # If signed has changed. the new a or b is set as m to; to narrow down the search
        if hasSignChanged(a, m):
            b = m
        else:
            a = m

    return m

# performs findSingleZero on each candidate interval, 
# returns found zeros as list  
def findMultipleZeros(intervals, d_x):
    zeros = []
    
    # For every interval find the zero
    for n in range( 0, len(intervals) ):
        # Search between every interval + delta_x
        zeros.append(round(findSingleZero(intervals[n], intervals[n] + d_x), 3))
    
    return zeros

# Checl of tje zero found is actually or close to zero if the you pass in x as zero in the function
def verifyZeros(zeros):
    print ("\nVerifierar nollställen i f(x):\n")
    
    for i in range( 0, len(zeros) ):
        print(f"\tf({zeros[i]}) = {round(f(zeros[i]), 3)}")
  
# Defining the varibles used to calculate the zeros
intervals = str(input("Mellan två intervall ska den leta mellan? (-4 4)> ")).split(" ")
no_of_intervals = int(input("Hur många intervall ska den kolla mellan? (32, 64, 128, 256) > "))
delta_x = ( int(intervals[1]) - int(intervals[0]) ) / no_of_intervals

found_zeros = findMultipleZeros(findCandidateIntervals(int(intervals[0]), int(intervals[1]), no_of_intervals), delta_x)

print(f"\nHittade nollställen: {found_zeros}")
verifyZeros(found_zeros)