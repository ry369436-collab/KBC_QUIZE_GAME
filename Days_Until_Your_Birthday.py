print("Hello Dear!!")
birthday=[]
birthdate=birthday.append((input("enter birthdate in the format(DD):")))
birthmonth=birthday.append((input("enter birthmonth in the format(MM):")))

from datetime import date
today=date.today()
formatted_date=today.strftime('%d')
formatted_month=today.strftime('%m')

if((int(birthday[0])>0 and int(birthday[0]) <=31) and  (int(birthday[1])>0 and int(birthday[1])<13)):
    if(formatted_date==birthday[0]and formatted_month==birthday[1]):
        print("Happy Birthday!!")
    elif(formatted_date<birthday[0] and formatted_month==birthday[1]):
        days_left=int(birthday[0])-int(formatted_date)
        print("Your birthday is in,days:",days_left)  
    elif(formatted_date>birthday[0] and formatted_month==birthday[1]):
        days_left=int(birthday[0])+30-int(formatted_date)
        months_left=int(birthday[1])+11-int(formatted_month)
        print("Your birthday is in,months:",months_left,",days:",days_left)          

    elif(formatted_date<birthday[0] and formatted_month<birthday[1]):
        days_left=int(birthday[0])-int(formatted_date)
        months_left=int(birthday[1])-int(formatted_month)
        print("Your birthday is in,months:",months_left,",days:",days_left)

    elif(formatted_date>birthday[0] and formatted_month<birthday[1]):
        days_left=int(birthday[0])+30-int(formatted_date)
        months_left=int(birthday[1])-int(formatted_month)-1
   
        print("Your birthday is in,months:",months_left,",days:",days_left)
    elif(formatted_date<birthday[0] and formatted_month>birthday[1]):
        days_left=int(birthday[0])-int(formatted_date)
        months_left=int(birthday[1])+12-int(formatted_month)-1
 
        print("Your birthday is in,months:",months_left,",days:",days_left)
    else:
        days_left=int(birthday[0])+30-int(formatted_date)
        months_left=int(birthday[1])+11-int(formatted_month)
        print("Your birthday is in,months:",months_left,",days:",days_left)    
else:
    print("not a valid input")   
