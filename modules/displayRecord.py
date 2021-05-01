def display_record():
    print("\n\n List Of Available Customer Records\n\n")
    print("BOOKING ID---GUEST NAME---GUEST MOBILE NUMBER---GUEST ROOM NUMBER---GUEST CHECKIN DETAILS---GUEST CHECKOUT DETAILS---RENT---TOTAL BILL\n")
    file = open("Record/customer.txt", "r")
    while True:
        content = file.readline()
        length = len(content)
        if length == 0:
            break
        print(content.strip())
    file.close()