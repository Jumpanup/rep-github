if __name__ == '__main__':
    print("HW_4, EX_1 by Trofimov Artem :")

print("----------------")

def salary(hours, rate, bonus):
    return (hours * rate) + bonus

from sys import argv

h = int(argv[1])
r = int(argv[2])
b = int(argv[3])

print("Hours = ", h)
print("Rate = ", r)
print("Bonus = ", b)
print("----------------")
print("Salary = ", salary(h, r, b))



