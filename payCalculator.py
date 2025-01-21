def calculatePay():
    # This first line is provided for you
    try:
        hrs = float(input("Enter Hours:"))
        rate = float(input("Enter Rate:"))
    
        if hrs > 40:
            overtime_hrs = hrs - 40
            overtime_pay = overtime_hrs * rate * 1.5
            regular_pay = 40 * rate
            pay = overtime_pay + regular_pay
        
        else:
            pay = hrs * rate
    
        print(f"Pay: {pay}")
    except:
        print("Error, please enter numeric input")

    
    # end assignment

## if you want to test locally before you try to sync
## run > python payCalculator.py

#Ignore this for now. 
if __name__ == "__main__":
    calculatePay()
