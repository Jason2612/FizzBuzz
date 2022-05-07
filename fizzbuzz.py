a = input("Nhap 2 chu so nguyen: ")

if a[-1] < a[0]:
    b = input("Số kết thúc cần lớn hơn số bắt đầu: ")
    for i in range(int(b[0]), (int(b[-1]) + 1)):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
else:
    for i in range(int(a[0]), (int(a[-1]) + 1)):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)