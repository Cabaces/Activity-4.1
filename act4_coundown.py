



while True:
    n = int(input("Enter n: "))
    while n <= 0:
        print("Please enter a positive number.")
        n = int(input("Enter n: "))

    # Count down from n to 1 on one line and finish with "Liftoff!"
    while n >= 1:
        print(n, end=" ")
        n -= 1
    print("Liftoff!")

    # Ask if the user wants to run it again
    choice = input("\nDo you want to run this again? (y/n): ").lower()
    if choice != 'y':
        break
