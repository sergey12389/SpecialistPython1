# # Дан шестизначный номер билета. Определить, является ли билет счастливым.
# # Решение реализовать в виде функции.
# # Билет считается счастливым, если сумма его первых и последних цифр равны.
#
def lucky_ticket(ticket_number):
    number1 = ticket_number % 1000  # Берем последние 3 числа
    suma1 = 0
    while number1 > 0:
        digit1 = number1 % 10
        suma1 = suma1 + digit1
        number1 = number1 // 10
    number2 = ticket_number // 1000  # Берем первые 3 числа
    suma2 = 0
    while number2 > 0:
        digit2 = number2 % 10
        suma2 = suma2 + digit2
        number2 = number2 // 10
    return suma1 == suma2

# Тестируем функцию
print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))

# number = int(input('d:'))
# number1=number%1000 # Берем последние 3 числа
# suma1 = 0
# while number1>0:
#     digit1=number1%10
#     suma1=suma1+digit1
#     number1 = number1 // 10
# number2=number//1000 # Берем первые 3 числа
# suma2 = 0
# while number2>0:
#     digit2=number2%10
#     suma2=suma2+digit2
#     number2 = number2 // 10
# if suma1==suma2:
#     print('lucky')
# else:
#     print('unlucky')

# number = int(input('d:'))
# number1=number%1000
# print(number1)
