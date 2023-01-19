def NumDeLet(n):
    num = {
        0: "zero",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine"
    }
    result = []
    n = str(n)
    palabra = ""
    for digit in n:
        palabra += num [int(digit)]
    result.append(palabra)
    while True:
        word = ""
        for digit in str(len(result[-1])):
            word += num[int(digit)]
        result.append(word)
        if len(result[-1]) == 4:
            break
    final_num = int(len(result[-1]))
    final_word = num[final_num]
    result.append(final_word)
    return result
print(NumDeLet(60))
print(NumDeLet(1))
