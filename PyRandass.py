import random
alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "@()[]{}*,;/-_¿?.¡!$<#>&+%="
base = alphabet + numbers + symbols
length = 40
password = "".join(random.sample(base, length))
print(password)