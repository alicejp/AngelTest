# This is a sample Python script.
import math


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def test_question_1():
    # 1. print_team_number
    i = 1
    while i < 15:
        i += 1
        _user_input = int(input())
        team_num = print_team_number(_user_input)
        print(f'team num: {team_num}')

def print_team_number(num):
    _team_num = int((num - 1) / 3) + 1
    return _team_num

def test_question_2():
    # 2. the area of the land, the result should be in between 1..32 bit signed integer
    user_input = input()
    _inputArr = user_input.split(" ")
    # convert string to int
    for j in range(len(_inputArr)):
        _inputArr[j] = int(_inputArr[j])

    # 海龍公式 √s (s-a)(s-b)(s-c) https://www.youtube.com/watch?v=0Bp2TUTwM68
    _s1 = _inputArr[0]
    _s2 = _inputArr[1]
    _s3 = _inputArr[2]
    _area = triangle_area_price(_s1, _s2, _s3)
    print(f'area price: {_area}')

def triangle_area_price(a,b,c):
    _s = (a + b + c) / 2
    _area = math.sqrt(_s * (_s - a) * (_s - b) * (_s - c))
    return math.pow(_area, 2)

def test_question_3():
    # 2. the area of the land, the result should be in between 1..32 bit signed integer
    user_input = input()
    _inputArr = user_input.split(" ")

    # Get the max index number
    _max_index = 0

    # convert string to int
    for j in range(len(_inputArr)):
        # check there is no zero
        if int(_inputArr[j]) == 0:
            print("input error")
            return
        _inputArr[j] = int(_inputArr[j])
        if _inputArr[j] > _inputArr[_max_index]:
            _max_index = j

    # get the power of the max number, and sum up the rest number
    _sum_of_the_other_two = 0
    for k in range(len(_inputArr)):
        if k is _max_index:
            _max_number_power = math.pow(_inputArr[k], 2)
        else:
            _sum_of_the_other_two += math.pow(_inputArr[k], 2)

    # compare them
    _is_zero = _sum_of_the_other_two == _max_number_power
    _result = "yes" if (_is_zero == True) else "no"
    print(_result)

def test_question_4():
    # sum up all the number in between 1 to the user input divisible by 7
    _number_by_the_user = int(input())
    _sum = 0
    for n in range(_number_by_the_user + 1):
        if n % 7 == 0:
            _sum += n
    print(_sum)

def test_question_5():
    user_input = input()
    _inputArr = user_input.split(" ")
    # convert string to int
    for j in range(len(_inputArr)):
        _inputArr[j] = int(_inputArr[j])

    _a = _inputArr[0]
    _b = _inputArr[1]
    _c = _inputArr[2]
    _d = _inputArr[3]
    _time = (_a - _b) / (_c - _d)
    print(int(_time))


def test_question_6():
    # Is it a prime number
    _user_number_input = int(input())
    for i in range(2, _user_number_input):
        if _user_number_input % i == 0:
            print("Composite")
            return

    print("Prime")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')
    test_question_6()






# See PyCharm help at https://www.jetbrains.com/help/pycharm/
