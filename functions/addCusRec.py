def add_customer_record():
    print("Enter The Guest Details\n")
    id = input("Enter Booking ID: ")
    name = input("Enter Guest Name: ")
    mob = input("Enter Guest Mobile Number: ")
    room = input("Enter Guest Room Number: ")
    ckin = input("Enter Guest Checkin Details: ")
    ckout = input("Enter Guest Checkout Details: ")
    rent = input("Enter Rent: ")
    total = input("Enter Total Bill Amount: ")
    file = open("Record/customer.txt","a")
    file.write(id+"-"+name+"-"+mob+"-"+room+"-"+ckin+"-"+ckout+"-"+rent+"-"+total+"\n")
    file.close()
