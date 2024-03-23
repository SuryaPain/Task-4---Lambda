data = [10, 501, 22, 37, 100, 999, 87, 351] #1
result = filter(lambda x: x > 4, data)
print(list(result))

List = ["Surya", "hello", 59, "Python"] #2

result = map(lambda x: isinstance(x, (int, str)), List)

print(list(result))

fibonacci = lambda n: (x[0] for x in ((a, a + (lambda a, b: (b, a + b))(a, 0)[0]) for a in range(n))) #3

fib_series = list(fibonacci(50))

print("Fibonacci series (up to 50 elements):", fib_series)



import re #4 a)
def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, email):
        return True
    else:
        return False 
email = "jayasurya2@gmail.com"    
if validate_email(email):
    print("Valid email address.")
else:
    print("Invalid email address.")




import re #4 b)
def validate_mobile_number(number):
    pattern = r'^\+?8801[1-9]\d{8}$'

    if re.match(pattern, number):
        return True
    else:
        return False

mobile_number = "+8801513862794"
if validate_mobile_number(mobile_number):
    print("Valid mobile number.")
else:
    print("Invalid mobile number.")




import re #4 c) 

def validate_telephone_number(number):
    pattern = r'^\+?1?\s?\(?(\d{3})\)?[-.\s]?(\d{3})[-.\s]?(\d{4})$'
    if re.match(pattern, number):
        return True
    else:
        return False

telephone_number = input("+1 (628) 259-5691")
if validate_telephone_number(telephone_number):
    print("Valid telephone number.")
else:
    print("Invalid telephone number.")





import re #4 d)

def validate_password(password):
    
    pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[^A-Za-z0-9]).{16}$'

    if re.match(pattern, password):
        return True
    else:
        return False

password = "G978bw47Jcc5m."
if validate_password(password):
    print("Valid password.")
else:
    print("Invalid password.")