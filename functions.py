# Fungsi pemanggilan nama
def greet(name):
    return f"Hello, {name}!"

print(greet("Arifian"))


def multiply(a, b):
    return a * b

# Contoh pemanggilan fungsi
result = multiply(9, 6)
print(result) 

def check_even_odd(number):
    if number % 2 == 0:
        return "Genap"
    else:
        return "Ganjil"

# Contoh pemanggilan fungsi
print(check_even_odd(5)) # Ganjil
print(check_even_odd(4)) # Genap

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Contoh pemanggilan fungsi
print(factorial(20)) 
