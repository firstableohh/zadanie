for x in ['0','1', '2', '3', '4','5', '6','7','8','9','A','B','C','D','E']:
    s = int(f'97968{x}13', 15) + int(f'7{x}213',15)
    if s % 14 == 0: 
        print(x, s, s //14) 
        break