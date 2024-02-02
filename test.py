# list comprehension

# Example 1
squares = [x**2 for x in range(10)]
print(squares)


# Example 2
name = "Hello world"
number = [x*2 for x in name if x.isdigit()]
print(number)

# Example 3
def total(initial=5, *numbers, **keywords):  # * is used for tuple and ** is used for dictionary
    print(initial)
    print(number)
    print(keywords)
    
print('First time')
total(10, 1, 2, vegetables=5, fruits=100)
print('second time')
total(10, 1, 2, vegetables=50)