def comparator(a : int or float or complex, b : int or float or complex):
    import random
    
    if a != int or b != int:
        if a > b:
            number = random.uniform(b, a)
            if type(number) == complex:
                return f"A random number in the range ({b}, {a}) is {number}. It is a complex number."
            elif type(number) == int:
                return f"A random number in the range ({b}, {a}) is {number}. It is an integer number."
            elif type(number) == float:
                return f"A random number in the range ({b}, {a}) is {number}. It is a complex number."    
        else:
            number = random.uniform(a, b)
            if type(number) == complex:
                return f"A random number in the range ({a}, {b}) is {number}. It is a complex number."
            elif type(number) == int:
                return f"A random number in the range ({a}, {b}) is {number}. It is an integer number."
            elif type(number) == float:
                return f"A random number in the range ({a}, {b}) is {number}. It is a complex number."
    elif a == int and b == int:
        if a > b:
            number = random.randint(b, a)
            return f"A random number in the range ({b}, {a}) is {number}. It is an integer number."
        else:
            number = random.randint(a, b)
            return f"A random number in the range ({a}, {b}) is {number}. It is an integer number."
            
            
print(comparator(190, 67))


