def main():
    for i in range(2, 101):
        if (i % 2) == 0:
            if (i == 2):
                print(i, "is a prime number")
            else:
                print(i, "is not a prime number")
        elif (i % 3) == 0:
            if (i == 3):
                print(i, "is a prime number")
            else:
                print(i, "is not a prime number")
        elif (i % 5) == 0:
            if (i == 5):
                print(i, "is a prime number")
            else:
                print(i, "is not a prime number")
        elif (i % 7) == 0:
            if (i == 7):
                print(i, "is a prime number")
            else:
                print(i, "is not a prime number")
        else:
            print(i, "is a prime number")

if __name__ == "__main__":
    main()