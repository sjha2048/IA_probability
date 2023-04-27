

def probability_of_event(n):
  # If n is less than 4, return the first fraction from the series
    if n < 4:
        numerator = 2**(n-1)
        denominator = 2**n
        return str(numerator) + '/' + str(denominator)
  # Otherwise, calculate the probability fraction

    a = 2
    b = 1
    c = 1
    prev_count = 4
    curr_count = 8

    
    # Loop through numbers 4 to n and calculate the fraction
    for i in range(4, n+1):
        temp = c
        c = b
        b = a
        a = prev_count
        prev_count = curr_count
        curr_count = (curr_count - temp) * 2 + temp
    # Return the fraction as a string    
    numerator = a + b + c
    denominator = curr_count
    return str(numerator) + '/' + str(denominator)

print(probability_of_event(10))
print(probability_of_event(5))

print(probability_of_event(22))


