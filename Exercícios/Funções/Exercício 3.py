def fahrenheit_celcius(f):
    c = (f - 32) / 1.8
    return c


def celcius_fahrenheit(c):
    f = (c * 1.8) + 32
    return f


print(fahrenheit_celcius(86))
print(celcius_fahrenheit(30))
