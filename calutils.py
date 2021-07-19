def is_leap_year(year):
    return (year%4)==0 and (year%100)!=0 or (year%400)==0


def month_name(number):
    if number==1:
        return 'January'
    elif number==2:
        return 'February'
    elif number==3:
        return 'March'
    elif number==4:
        return 'April'
    elif number==5:
        return 'May'
    elif number==6:
        return 'June'
    elif number==7:
        return 'July'
    elif number==8:
        return 'August'
    elif number==9:
        return 'September'
    elif number==10:
        return 'October'
    elif number==11:
        return 'November'
    elif number==12:
        return 'December'


def days_in_month(month_number,year):
    if is_leap_year(year)==True or is_leap_year(year)==False:
        
        if month_number==4 or month_number==6 or month_number==9 or month_number==11:
            return '30'
        elif month_number==1 or month_number==3 or month_number==5 or month_number==7 or month_number==8 or month_number==10 or month_number==12:
            return '31'
        if is_leap_year(year)==False:
            month_number==2
            return '28'
        
        elif is_leap_year(year)==True:
            month_number==2
            return '29'


def first_day_of_year(year):
    day = (year-1)%4
    day = 1+ 5*day
    day = day +4*((year-1)%100)
    day = day +6*((year-1)%400)
    day = day%7
    
    if day==0:
        return '0'
    elif day==1:
        return '1'
    elif day==2:
        return '2'
    elif day==3:
        return '3'
    elif day==4:
        return '4'
    elif day==5:
        return '5'
    elif day==6:
        return '6'
        


def first_day_of_month(month_number,year):
    first_day= 12 + 2*month_number
    first_day= first_day + ((3*month_number+1) //5)
    first_day= first_day + year + (year//4)
    first_day= first_day -(year//100)+ (year//400) +2
    first_day= (first_day%7)
    
    if first_day==0:
        return '2'
    elif first_day==1:
        return '3'
    elif first_day==2:
        return '4'
    elif first_day==3:
        return '5'
    elif first_day==4:
        return '6'
    elif first_day==5:
        return '0'
    elif first_day==6:
        return '1'
  


    

        
        
        
    





        

        
    