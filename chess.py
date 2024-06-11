def is_valid_queen_move(start, end):
    if start[0] == end[0] or start[1] == end[1] or abs(ord(start[0]) - ord(end[0])) == abs(int(start[1]) - int(end[1])):
        return True
    else:
        return False

def is_valid_knight_move(start, end):
    dx = abs(ord(start[0]) - ord(end[0]))
    dy = abs(int(start[1]) - int(end[1]))
    
    if (dx == 1 and dy == 2) or (dx == 2 and dy == 1):
        return True
    else:
        return False

try:
    queen_start = "d1"
    queen_end = input("Введите ход для ферзя: ")

    if is_valid_queen_move(queen_start, queen_end):
        print("Ферзь может попасть на клетку", queen_end, "одним ходом")
    else:
        print("Ферзь не может попасть на клетку", queen_end, "одним ходом")
        
    knight_start = "b1"
    knight_end = input("Введите ход для коня: ")
    
    if is_valid_knight_move(knight_start, knight_end):
        print("Конь может попасть на клетку", knight_end, "одним ходом")
    else:
        print("Конь не может попасть на клетку", knight_end, "одним ходом")
except Exception as e:
    print("Ошибка:", e)
