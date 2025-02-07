
import datetime

bookings={}

total_cars=10
code = 0
count_cars=0


def help():
    help_text="""
    boking:make a booking
    display:show all boking
    search:search booking
    cancel:cancel bokking
    details:details booking
    exit:\n"""
    print(help_text)


def validate_date(input_date):

    c=input_date.count("-")

    if c != 2 or len(input_date) !=10 or input_date[4] !="-" or input_date[7] !="-" :
        return False, "invalid format(YYY-MM-DD)"
    
    parts=input_date.split("-")
    if not(parts[0].isdigit() and parts[1].isdigit() and parts[2].isdigit()):
        return False,"should be number"
    
    year,month,day=list(map(int,parts))
    if year <1 or not (1<= month <= 12 ) or not (1 <=day <= 31):
        return False,"invalid date"
    
    return True,"valid date"


def find_days(start_date,end_date):
    if start_date == end_date:
        return 0
    else:
        new_start_date = start_date + datetime.timedelta(days=1)
        return 1 +find_days(new_start_date,end_date)


def booking():
    global total_cars,code
    if len(booking) >= total_cars:
        print("all cars are booked")
        return
    name =input("enter you name:")
    start_date=input("start date:")
    end_date=input("end date:")


    is_valid,msg=validate_date(start_date)
    if not is_valid:
        print(msg)
        return


    is_valid,msg=validate_date(end_date)
    if not is_valid:
        print(msg)
        return


    start_date = datetime.datetime.strptime(start_date,"%Y-%m-%d").date
    end_date =datetime.datetime.strptime(end_date,"%Y-%m-%d").date
    count_days= end_date - start_date
    count_days = count_days.days
    res = find_days(start_date , end_date)
    print(res,count_days)


    if start_date > end_date:
        print("error")
        return
    
    new_booking={
        "name":name ,
        "start_date":start_date,
        "end_date":end_date,
        "days":count_days
    }

    print(new_booking)
    bookings[code] =new_booking
    code +=1
    print("done")


def cancel(code_del):
    booking.pop(code_del,"not found")
    """if code_del in bookings:
        bookings.pop(code_del)
        print("cancell")
    else:
        print("not foud")"""


def display():
    if len(bookings) !=0:
        for code,booking in bookings.items():
            print(str(code))
            print(f"name:{booking['name']}")
            print(f"start_date:{booking['start_date']}")
            print(f"end_date:{booking['end_date']}")
            print(f"days:{booking['days']}")
    else:
        print("empti")


def search_by_code(code_s):
    if code_s in bookings:
        booking=bookings[code_s]
        print(str(code_s))
        print(f"name:{booking['name']}")
        print(f"start_date:{booking['start_date']}")
        print(f"end_date:{booking['end_date']}")
        print(f"days:{booking['days']}")
    else:
        print("not found")


def search_by_name(name):
    for code,booking in bookings.items:
        if booking["name"]==name:
            print(str(code_s))
            print(f"name:{booking['name']}")
            print(f"start_date:{booking['start_date']}")
            print(f"end_date:{booking['end_date']}")
            found=True
    if not found:
        print(f"{name}:not found!")


def search():
    cmd =input("search by 'name' or 'code' :")
    if cmd =="name":
        name=input("name for search:")
        search_by_name(name)
    if cmd =="code":
        code_s=int(input("code for search:"))
        search_by_code(code_s)
    else:
        print("not found")


def details():
    num_booked_cars=len(bookings)
    num_available_cars=total_cars - num_booked_cars
    print(f"total number of cars:{total_cars}")
    print(f"number of booked:{num_booked_cars}")
    print(f"number of available:{num_available_cars}")


while True:
    command = input("enter you option:")
    if command =="help":
        help()
    elif command =="booking":
        booking()
    elif command =="display":
        display()
    elif command =="search":
        code_s =int(input("enter  your code "))
        search(code_s)
    elif command =="cancel":
        code_del =int(input("enter your code:"))
        cancel(code_del)

    elif command =="details":
        details()
    elif command =="exit":
        break
    elif command =="":
        continue
    else:
        print("command not found")
