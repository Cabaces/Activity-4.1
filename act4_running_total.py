


while True:
    total = 0.0
    count = 0

    price = float(input("Price (0 to stop): "))
    while price != 0:
        total += price
        count += 1
        price = float(input("Price (0 to stop): "))

    # Print the number of items, the total, and the average price to 2 decimals
    print(f"Items: {count} Total: {total:.2f}")
    if count > 0:
        average = total / count
        print(f"Average: {average:.2f}")
    else:
        print("Average: 0.00")

    # Ask if the user wants to run it again
    choice = input("\nDo you want to run this again? (y/n): ").lower()
    if choice != 'y':
        break
