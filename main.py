def rot(num):
    num = str(num)
    numeric = list(num)
    for i in range(len(numeric)):
        if numeric[i] == '6':
            numeric[i] = '9'
            print("".join(numeric))
            break
        elif i == len(numeric)-1:
            print("".join(numeric))

if __name__ == "__main__":
    num = 999
    rot(num)
