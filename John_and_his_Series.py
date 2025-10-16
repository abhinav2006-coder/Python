a = int(input("Enter the first term of the series: "))
d = int(input("Enter the common difference: "))
n = int(input("Enter the number of terms: "))

# nth term of the arithmetic series
nth_term = a + (n - 1) * d
print("The nth term of the arithmetic series is:", nth_term)

# Sum of the first n terms of the arithmetic series
sum_n_terms = n * (a + nth_term) // 2
print("The sum of the first n terms of the arithmetic series is:", sum_n_terms)
