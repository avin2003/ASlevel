def numbers(count):
    if count <= 1:
        return count
    else:
        return numbers(count - 1) + numbers(count - 2)


count = 10
i = 1
while i <= count:
    print(numbers(i))
    i += 1
