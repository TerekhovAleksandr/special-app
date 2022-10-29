while True:
    command = input('Введите команду: ')
    if command in '+-*/':
        break
    else:
        print('Ошибка ввода!')

operand = int(input(f"Сколько операндов? "))
print()
number = int(input(f"Введите число 1: "))

result = number

result_str = str(number)

for num in range(operand - 1):
  number = int(input(f"Введите число {num + 2}: "))
  result_str += ' ' + command + ' ' + str(number)
  if command == "+":
    result += number
  elif command == "-":
    result -= number
  elif command == "*":
    result *= number
  elif command == "/":
    result /= number

print(f'{result_str} = {result}')
