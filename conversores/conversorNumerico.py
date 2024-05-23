def decimal_para_binario(num, array=list()):
    array.insert(0, str(num%2))
    if int(num/2) == 1:
        array.insert(0, str(int(num/2)))
    else: 
        decimal_para_binario((int(num/2)), array)
    return ''.join(array)


def decimal_para_hexadecimal(num, array=list()):
    match (num % 16):
        case 10:
            array.insert(0, "A")
        case 11:
            array.insert(0, "B")
        case 12:
            array.insert(0, "C")
        case 13:
            array.insert(0, "D")
        case 14:
            array.insert(0, "E")
        case 15:
            array.insert(0, "F")
        case _:
            array.insert(0, str(num % 16))
    if int(num/16) != 0:
        decimal_para_hexadecimal((int(num/16)), array)
    return ''.join(array)
    

print("Binario: ", decimal_para_binario(20315))
print("Hexadecimal: ", decimal_para_hexadecimal(20315))