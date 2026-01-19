def primeno(num=7):
    if num <= 1:
        return "Not Prime"

    for i in range(2, num):
        if num % i == 0:
            return "Not Prime"
    return "Prime"


if __name__ == "__main__":
    result = primeno()
    print("Prime:", result)
