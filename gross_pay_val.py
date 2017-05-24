#S.McDonald 10/11/2016
#Gross Pay: get the number of hours worked and calculate a Gross Pay

try:
    #input
    #get the hours
    hours = int(input("Enter the hours worked for the week: "))
    #validate the input for 'hours'
    while hours < 0 or hours > 168:
        print("Invalid number of hours entered.")
        hours = int(input("Enter the hours worked for the week: "))

    #get the pay rate
    rate = float(input("Enter the hourly pay rate: "))
    #validate the input for 'pay rate'
    #while rate < 8.39:
        #print("Invalid number of rate of pay entered.")
    #rate = float(input("Enter the hourly pay rate: "))


    #processing
    #calculate gross pay
    gross_pay = hours * rate


    #output
    #display the output
    print("Gross pay: $", format(gross_pay, ',.2f'))
    
except ZeroDivisionError:
    print("ERROR: CANNOT DIVIDE BY ZERO!")

except ValueError:
    print("ERROR: HOURS WORKED & HOURLY PAY MUST BE VALID INTEGERS!")

except:
    print("ERROR: CHECK YOUR DATA!")
