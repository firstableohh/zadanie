for a in range(1000):
    is_a = True
    for x in range(1000):
        if (((x&39) == 0) or (((x&11) == 0) <= ((x&a) !=0)) ) == False:
            is_a = False
            break

    if is_a:
        print(a)
        break