"""The Credit Card Simulator starter code
You should complete every incomplete function,
and add more functions and variables as needed.
Ad comments as required.

Note that incomplete functions have 'pass' as the first statement:
pass is a Python keyword; it is a statement that does nothing.
This is a placeholder that you should remove once you modify the function.

Author: Michael Guerzhoy.  Last modified: Oct. 3, 2022
"""

# You should modify initialize()
def initialize():
    global cur_balance_owing_intst, cur_balance_owing_recent
    global last_update_day, last_update_month
    global last_country, last_country2
    global activated # track account active or frozen
    global MONTHLY_INTEREST_RATE
    
    cur_balance_owing_intst = 0
    cur_balance_owing_recent = 0
    
    last_update_day, last_update_month = -1, -1
    
    last_country = None
    last_country2 = None    

    activated = True
    
    MONTHLY_INTEREST_RATE = 0.05

def date_same_or_later(day1, month1, day2, month2):
    '''Take in two set of dates day1, month2 and day2, month2, and return True
    if the first date is the same or later than second date. If it
    is before, return False.'''
    if month1 > month2:
        return True
    elif month1 == month2 and day1 >= day2:
        return True
    else:
        return False
    
def all_three_different(c1, c2, c3):
    return not(c1 == c2 or c2 == c3 or c1 == c3)

def card_status(c1, c2, c3):
    '''status of card, if it is deactivated then return False, if active and
    countries are not 3 different return True, if countries are all three
    different then deactivated and return False'''
    global activated

    if not activated: # if the card is frozen, return False
        return activated
    elif activated and (not all_three_different(c1, c2, c3)): #if the card isn't frozen and the countries aren't all different return True
        return activated
    else:
        activated = False
        return activated
        
def purchase(amount, day, month, country):
    '''runs a purchase with amount on day month country, if the date is on same day
    or later and also not all three different countries past 3 transactions
    it just does the purchase, if not return string saying error
    RECOMMENT'''
    global cur_balance_owing_intst, cur_balance_owing_recent
    global last_update_day, last_update_month
    global last_country, last_country2
    if not(date_same_or_later(day, month, last_update_day, last_update_month) and card_status(country, last_country, last_country2)):
        return "error"
    else:
        update(month)
        cur_balance_owing_recent += amount

    last_update_day = day # purchase complete, setting the last transaction details
    last_update_month = month
    last_country2 = last_country
    last_country = country

def update(month):
    global last_update_month
    month_diff = month - last_update_month

    if (month_diff >= 1):
        global cur_balance_owing_intst
        global cur_balance_owing_recent
        global MONTHLY_INTEREST_RATE

        cur_balance_owing_intst *= (1 + MONTHLY_INTEREST_RATE) ** month_diff
        cur_balance_owing_recent *= (1 + MONTHLY_INTEREST_RATE) ** (month_diff - 1)
        cur_balance_owing_intst += cur_balance_owing_recent
        cur_balance_owing_recent = 0

        last_update_month = month

def amount_owed(day, month):
    global last_update_day, last_update_month
    global cur_balance_owing_intst, cur_balance_owing_recent # CHECK IF NEED TO DO THIS AFTER RUNNING UPDATE

    if not date_same_or_later(day, month, last_update_day, last_update_month):
        return "error"

    update(month)

    last_update_day = day
    last_update_month = month

    return(cur_balance_owing_intst + cur_balance_owing_recent)
    
def pay_bill(amount, day, month):
    global last_update_day, last_update_month
    global cur_balance_owing_intst, cur_balance_owing_recent # CHECK IF NEED TO DO THIS AFTER RUNNING UPDATE

    if not date_same_or_later(day, month, last_update_day, last_update_month):
        return "error"

    update(month)

    if cur_balance_owing_intst < amount: # if the payment is bigger than balance accruing interest
        cur_balance_owing_intst -= amount
        cur_balance_owing_recent += cur_balance_owing_intst
        cur_balance_owing_intst = 0
    else:
        cur_balance_owing_intst -= amount

    last_update_day = day
    last_update_month = month

    return(cur_balance_owing_intst + cur_balance_owing_recent)
        

# Initialize all global variables outside the main block.
initialize()	
    
if __name__ == '__main__':
    # Describe your testing strategy and implement it below.
    # What you see here is just the simulation from the handout, which
    # doesn't work yet.
    initialize()

    purchase(80, 8, 1, "Canada")
    print("Now owing:", amount_owed(8, 1))      # 80.0
    pay_bill(50, 2, 2)
    print("Now owing:", amount_owed(2, 2))      # 30.0     (=80-50)
    print("Now owing:", amount_owed(6, 3))      # 31.5     (=30*1.05)
    purchase(40, 6, 3, "Canada")
    print("Now owing:", amount_owed(6, 3))      # 71.5     (=31.5+40)
    pay_bill(30, 7, 3)
    print("Now owing:", amount_owed(7, 3))      # 41.5     (=71.5-30)
    print("Now owing:", amount_owed(1, 5))      # 43.65375 (=1.5*1.05*1.05+40*1.05)
    purchase(40, 2, 5, "France")
    print("Now owing:", amount_owed(2, 5))      # 83.65375 
    print(purchase(50, 3, 5, "United States"))  # error    (3 diff. countries in a row)
                                                
    print("Now owing:", amount_owed(3, 5))      # 83.65375 (no change, purchase declined)
    print(purchase(150, 3, 5, "Canada"))        # error    (card disabled)
    print("Now owing:", amount_owed(1, 6))      # 85.8364375 (43.65375*1.05+40)