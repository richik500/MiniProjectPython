import os

def update_customer_record():
    flag = 0
    search = input("Enter Booking ID of Guest: ")
    file1 = open("Record/customer.txt", "r")
    file2 = open("Record/temp.txt", "w")
    flag = 0
    while True:
        content = file1.readline()
        length = len(content)
        if length == 0:
            break
        arr = content.split('-')
        if arr[0] == search:
            print("The Current Guest Details are\n", content)
            print("##########  ##########  ##########  ##########  ##########")
            newName = input("Enter the new Guest Name  or press Enter to continue:  ")
            newMob = input("Enter the new Guest Mobile Number  or press Enter to continue:  ")
            newRoom = input("Enter the new Guest Room Number  or press Enter to continue:  ")
            newCheckin = input("Enter the new Guest Checkin Details  or press Enter to continue:  ")
            newCheckout = input("Enter the new Guest Checkout Details  or press Enter to continue:  ")
            newRent = input("Enter the new Guest Room Rent  or press Enter to continue:  ")
            newTotal = input("Enter the new Guest Total Bill Amount  or press Enter to continue:  ")
            if len(newName) == 0:
                newName = arr[1]
            if len(newMob) == 0:
                newMob = arr[2]
            if len(newRoom) == 0:
                newRoom = arr[3]
            if len(newCheckin) == 0:
                newCheckin = arr[4]
            if len(newCheckout) == 0:
                newCheckout = arr[5]
            if len(newRent) == 0:
                newRent = arr[6]
            if len(newTotal) == 0:
                newTotal = arr[7]
            file2.write(arr[0]+"-"+newName+"-"+newMob+"-"+newRoom+"-"+newCheckin+"-"+newCheckout+"-"+newRent+"-"+newTotal+"\n")
            flag = 1
        else:
            file2.write(content)
    file1.close()
    file2.close()
    if flag == 1:
        print("The Customer Record has been updated successfully \n")
        os.remove("Record/customer.txt")
        os.rename("Record/temp.txt", "Record/customer.txt")
    elif flag == 0:
        print("Customer Record Not Found  \n")
