arr = [1, 2, 3, 4, 5]

try:
    index = int(input("Введите индекс массива: "))
    element = arr[index]
    print(element)
except IndexError:
    print("Индекс выходит за границы массива")
except ValueError:
    print("Введите индекс!")
