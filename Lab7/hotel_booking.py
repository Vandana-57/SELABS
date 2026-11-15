def nights_stayed(days):
    parts = days.split('-')
    if len(parts) != 2:
        raise ValueError("Enter check-in and check-out as day-day")

    try:
        check_in, check_out = map(int, parts)
    except ValueError:
        raise ValueError("Days must contain numbers")

    if check_in < 1 or check_out <= check_in:
        raise ValueError("Invalid check-in or check-out days")

    return check_out - check_in


def room_floor(room_code):
    parts = room_code.split('-')

    if len(parts) != 2 or not parts[0].isalpha():
        raise ValueError("Invalid room code")

    if not parts[1].isdigit():
        raise ValueError("Room number must contain digits")

    return int(parts[1][0])


def booking_label(names_csv):
    names = [n.strip() for n in names_csv.split(',')]

    if not names_csv.strip() or any(not name for name in names):
        raise ValueError("Guest names cannot be empty")

    lead = names[0]
    return lead[0].upper() + lead[1:] + " +" + str(len(names) - 1)


def main():
    print("==== Running nights_stayed ====")
    user_input = input("Enter check-in and check-out day (e.g. 12-15): ")
    result = nights_stayed(user_input)
    print("Nights:", result)

    print("\n==== Running room_floor ====")
    user_input = input("Enter a room code (e.g. D-305): ")
    result = room_floor(user_input)
    print("Floor:", result)

    print("\n==== Running booking_label ====")
    user_input = input("Enter guest names as CSV (e.g. ravi, priya): ")
    result = booking_label(user_input)
    print("Booking Label:", result)


if __name__ == "__main__":
    main()
