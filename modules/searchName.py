def search_customer_name():
    search = input("Enter Guest Name: ")
    file = open("Record/customer.txt", "r")
    flag = 0
    while True:
        content = file.readline()
        length = len(content)
        if length == 0:
            break
        arr = content.split("-")
        if arr[1] == search:
            print("\n The record has been found ")
            print("Booking ID: ", arr[0])
            print("Name: ", arr[1])
            print("Mob No.: ", arr[2])
            print("Room No.: ", arr[3])
            print("Checkin Details: ", arr[4])
            print("Checkout Details: ", arr[5])
            print("Rent: ", arr[6])
            print("Total Amount: ", arr[7])
            flag = 1
            break
    if flag == 0:
        print("\n Customer Record Not Found \n")
    file.close()
