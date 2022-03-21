# print("hello world")
# # input("enter name\n")
# user_input = input("enter name\n")
# print(user_input)
no_of_hour = 24
unit = "hour"


def number_of_days(day, month):
    return f"number of days {no_of_hour * day} {unit} {month}"


my_days = number_of_days(3, "january")
print(my_days)
my_days_2 = number_of_days(2, "february")
print(my_days_2)
number_of_days(3, "march")


def scope_check(month):
    print(f"{no_of_hour} {unit}")
    print("scope_check")
    print(month)


scope_check("january")


# user_input = input()
# print(user_input)

def calculate(a, b):
    # return is a keyword that returns value
    sum = a + b
    return sum


# returned value is assigned to a varaiable and stored i
my_value = calculate(2, 3)
my_second_value = calculate(3, 4)
my_third_value = calculate(4, 5)
print(my_value)
print(my_second_value)
print(my_third_value)


def days_to_units(day):
    condition_check = day > 0
    print(type(condition_check))
    if day > 0:
        return f"number of days {no_of_hour * day} {unit} "
    elif day == 0:
        return "zero day entered"
    else:
        return "number is negative,so convert"

user_input = input("enter")
    # input() takes string value by default, so convert to use
if user_input.isdigit():
    # isdigit()checks input is digit or not
    user_num = float(user_input)
    my_result = days_to_units(user_num)
    print(my_result)
else:
 print("hey user, enter genuine integer")

