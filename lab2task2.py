# Практичне завдання №2

# Завдання №1

from cgitb import reset


i_am = ["Alex"]
print(i_am)

indexId = id(i_am)
print(indexId)

i_am = ["Alex"] + ["Masovets"]
print(i_am)

indexId = id(i_am)
print(indexId)

# Завдання №2

naturalNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = naturalNumbers[:5:]
print(result)

result = naturalNumbers[4::]
print(result)

result = naturalNumbers[::3]
print(result)
