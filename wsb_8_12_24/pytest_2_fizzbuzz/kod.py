def fizzbuss(i):
    if isinstance(i, (int, float)) and i > 0:
        i = int(i)
        if i % 15 == 0:
            return 'FizzBuzz'
        if i % 3 == 0:
            return 'Fizz'
        if i % 5 == 0:
            return 'Buzz'
        return i
    else:
        return None



# 9 % 3 == 0