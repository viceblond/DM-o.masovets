print("Завдання 1\n")

# Рядок перетворений в коментар, моє ім'я та прізвище в форматі Title-2 <title>Масовець Олександр</title>

print("Рядок перетворений в коментар, моє імя та прізвище в форматі Title-2 - 'Масовець Олександр'\n")

print("----------------------\n")

print("Завдання 2\n")

intVar = 5 
print(intVar)
print(type(intVar))

floatVar = -1.456
print(floatVar)
print(type(floatVar))

strVar = "John Johnson"
print(strVar)
print(type(strVar))

listVar = [13, 15.64, "Hello", True]
print(listVar)
print(type(listVar))

boolVar = False
print(boolVar)
print(type(boolVar))

tupleVar = ("x", "Toyota")
print(tupleVar)
print(type(tupleVar))

print("------------------------")

print("Завдання 3\n")

# ввести з консолі число 2.71 в змінну 'e'

e = 2.71

е = float(input())

print(e)

print("------------------------")

# вивести в консоль 'е' в ступені 5

e = 5

e = int(input(5))

print(e)

print("------------------------")

# Параметр ', ' та 'sep' (separator) повинні бути для того, щоб відділяти значення на один пробіл

name = str
surname = str

print("{} {} - це студент".format(name, surname))
print("Результат буде = {}".format(42 / 5 + 4))
b = True
print("{} - {} хлопець!".format(name, b))
print("{} {}".format(surname, name))

print("------------------------")

print("Завдання 4\n")

x = int(input("Введіть x: "))

if x == -20:
    print(x)
elif x == 31.5:
    print(x)
elif x == 4:
    print(x)
else:
    print("Неможливо визначити значення змінної. Спробуйте ще раз")

print("------------------------")

student = str(input("Студент"))
pupil = str(input("Школяр"))
baby = str(input("Малятко"))

if student:
    print("Це студент. Йому 18 років")
elif pupil:
    print("Це школяр. Йому 14 років")
elif baby:
    print("Це малятко. Йому 3 рочки")
else:
    print("Введення невизначено")

print("------------------------")

# приклад цикла з 'for' та 'if'
for i in range(10):
    if i % 2 != 0:
        print (-i)
    else:
        pass

# Змінна 'і' беребирається як елемент 10 разів. 
# В умовному операторі if йде перевірка, що якщо змінна 'і' ділиться на 2 та не довірнює нулю, то виводиться
# у від'ємному (негативному) значенні.
# В інакшому випадку буде виведено Null-значення.