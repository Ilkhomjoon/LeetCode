def convert_binary(num: int) -> str:
    li = []
    result = ""
    while num != 0:
        digit = num % 2
        li.append(digit)
        num //= 2
    
    for i in li[::-1]:
        result += str(i)
        
    return result

print(convert_binary(45))