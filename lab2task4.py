# Завдання №1

op = open('my_file.txt', 'w+')
for li in range(1,11) :
    op.write(str(li) + "-ий рядок" + '\n')
op.close()

# Завдання №2

op = open('my_file.txt', 'r')
for line in range(5) :
    print(op.readline())
op.close()

# Завдання №3

with open('my_file.txt') as a:
    for line in range(5) :
        print(a.readline())
print("end")