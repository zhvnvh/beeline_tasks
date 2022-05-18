def is_palindrome(num):
    arr = []
    flag = True

    while num > 0:
        piece = num%10
        arr.append(int(piece))
        num = (num - piece)/10

    for i in range(0, int(len(arr)/2)):
        if arr[i] != arr[-i-1]:
            flag = False
            break
    return(flag)

if __name__ == "__main__":
    print("Enter number:")
    print(is_palindrome(int(input())))