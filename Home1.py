# Задайте натуральное число N. 
# Напишите программу, которая составит список простых множителей числа N


number = int(input('Введите число N: '))
list = [2,3,5,7,11,13,17,19,23,29,31,37,41]
list1 = []

for i in range(13):
    while number % list[i] == 0:
        if number % list[i] == 0:
            list1.append(list[i])
            number /= list[i]
    i+=1

if number != 1:
    list1.append(int(number))

print(list1)