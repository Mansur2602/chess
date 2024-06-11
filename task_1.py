def plus_two(number):
        
        result = number + 2
        print(result)
       


try:
    number = int(input("Введите число: "))
    plus_two(number)
except ValueError:
     print("Ожидаемый тип данных — число!")