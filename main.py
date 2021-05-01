from functions import disCusRec, updCusRec, delCusRec, serCusBookid, serCusName, addCusRec

print("\n Welcome to 260281's Hotel Management System\n")

while True:
    print("\n <1> Add New Record <1>")
    print("\n <2> Display All Available Records <2>")
    print("\n <3> Search Customer Record By Name <3>")
    print("\n <4> Search Customer Record By Booking ID <4>")
    print("\n <5> Delete Customer Record By Booking ID <5>")
    print("\n <6> Update Customer Record <6>")
    print("\n <7> Exit <7>")

    n = int((input("Please Enter Your Choice:  ")))
    if n == 7:
        break
    elif n == 1:
        addCusRec.add_customer_record()
    elif n == 2:
        disCusRec.display_customer_record()
    elif n == 3:
        serCusName.search_customer_name()
    elif n == 4:
        serCusBookid.search_booking_id()
    elif n == 5:
        delCusRec.delete_customer_record()
    elif n == 6:
        updCusRec.update_customer_record()

