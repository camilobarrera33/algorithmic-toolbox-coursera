def fibonacci_number(n):
    array = []
    array.append(0)
    array.append(1)

    for i in range(2, n + 1):
        array.append(array[i-1] + array[i-2])

    return array[n]


if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci_number(input_n))
