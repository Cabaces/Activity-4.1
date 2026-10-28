


while True:
    correct_pin = "1234"
    attempts = 0
    max_attempts = 3
    access_granted = False

    while attempts < max_attempts:
        pin = input("PIN: ")
        if pin == correct_pin:
            print("Access granted")
            access_granted = True
            break
        else:
            attempts += 1

    if not access_granted:
        print("Card blocked")

    # Ask if the user wants to run it again
    choice = input("\nDo you want to run this again? (y/n): ").lower()
    if choice != 'y':
        break
