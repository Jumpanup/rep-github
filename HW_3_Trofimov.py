print("#1") #exercise 1

def my_div(num_1=None, num_2=None):
    '''
    This function divides the first number by the second number
    :param num_1:   -- number_1
    :param num_2:   -- number_2
    :return:        -- data type is float
    '''
    try:
        num_1 = float(input("Enter first number: "))
        num_2 = float(input("Enter second number: "))
        res = num_1 / num_2
        print("Function arguments", num_1, num_2)
    except ZeroDivisionError:
        res = None
        print("Error. You cannot divide by zero.")
    return res

print("Result:", my_div())

print("#2") #exercise 2

def user_info(name=None, surname=None, bdate=None, city=None, email=None, phone=None):
    '''
    This function return some data of user
    :param name:    -- user name
    :param surname: -- user surname
    :param bdate:   -- user birth date
    :param city:    -- user city
    :param email:   -- user email
    :param phone:   -- user phone number
    :return:        -- data type is string with separator "|"
    '''
    print(str(f'{surname} | {name} | {bdate} | {city} | {email} | {phone}'))

user_info(name="Artem", surname="Trofimov", bdate="03.04.1989", city="Kaluga", email="tr@ya.ru", phone="9641498898")

print("#3") #exercise 3

def sum_of_two_biggest(val_1, val_2, val_3):
    '''
    This function summing two biggest values
    :param val_1: -- first value
    :param val_2: -- second value
    :param val_3: -- third value
    :return:      -- data type is number (float or int)
    '''
    print("Function arguments: ", val_1, val_2, val_3)
    max_tmp = 0

    if val_1 == val_2 and val_2 == val_3: # exception - if all values are equal, then sum of any two values
        max_tmp = val_1 + val_2
    else:
        if val_2 > val_1 and val_3 > val_1: # compare with first value
            max_tmp = val_2 + val_3
        if val_1 > val_2 and val_3 > val_2: # compare with second value
            max_tmp = val_1 + val_3
        if val_1 > val_3 and val_2 > val_3: # compare with third value
            max_tmp = val_1 + val_2

    return max_tmp

print("Result:", sum_of_two_biggest(7, 2, 7))

print("#4.1") #exercise 4.1 with **

def my_exp(x=None, y=None):
    '''
    This function elevates X in Y
    :param x:
    :param y:
    :return:
    '''
    try:
        x = float(input("Enter first number: "))
        y = int(input("Enter negative degree: "))
        print("Function arguments: ", x, y)
        while x == 0 or y >= 0:
            x = float(input("Enter first number: "))
            y = int(input("Enter negative degree: "))
    except ValueError:
        return "Error. You must to input numbers."

    return x ** y

print("Result:", my_exp())

print("#4.2") #exercise 4.2 with cycle

def my_exp_cycle(x=None, y=None):
    '''
    This function elevates X in Y
    :param x:
    :param y:
    :return:
    '''
    res = 1
    counter = 0
    try:
        x = float(input("Enter first number: "))
        y = int(input("Enter negative degree: "))
        print("Function arguments: ", x, y)
        while x == 0 or y >= 0:
            x = float(input("Enter first number: "))
            y = int(input("Enter negative degree: "))
        while counter < abs(y): # elevating in negative degree in the cycle
            res = res * 1 / x
            counter = counter + 1
    except ValueError:
        return "Error. You must to input numbers."

    return res

print("Result:", my_exp_cycle())

print("#5") #exercise 5

tmp = 0 # creating int variable

try:
    while True:
# Пока пользователь будет вводить цифры для каждой из них будет применяться int,
# если введет не цифру, то срабатывает исключение и показываться сумма
        for item in map(int, input("Enter numbers: ").split()):
            tmp = tmp + item
        print(tmp)
except ValueError:
    print(tmp)

print("#6") #exercise 6

def upper_text(word):
    '''
    This function will return a word with a capital letter.
    :param word:    -- the word in lower case
    :return:        -- data type string
    '''
    return word[0].upper() + word[1:] # the first letter is a capital letter and other are small letters

user_text = input("Enter several words through space: ").split() # creating a word list

lst = [upper_text(word) for word in user_text] # the upper_text is used for each word

user_text = " ".join(lst) # rewriting the user_text variable

print(user_text)

#end hw