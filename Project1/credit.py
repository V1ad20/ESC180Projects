"""ESC180 Project 1
By: Vlad Surdu and Seok-Gyu (Brian) Kang
Due: 10/12/2022"""

def initialize():
    '''Declare and initilize all global variables.'''
    # stores the amount owed in two parts, with one being the amount that
    # accrues interest and the other not accruing interest
    global cur_balance_owing_intst, cur_balance_owing_recent
    # stores the date of the last simulation operation
    global last_update_day, last_update_month
    # stores the last two countries in which there were transactions
    global last_country, last_country2
    # boolean variable that tracks the status of the credit card
    # (active or frozen)
    global activated
    #interest rate accrued each month. Constant and does not change
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
    '''Return True if c1, c2, and c3 are all different countries. If any
    overlap, return False.'''
    return not(c1 == c2 or c2 == c3 or c1 == c3)

def card_status(c1, c2, c3):
    '''Check c1, c2, and c3 to see if they are all different countries. If so,
    deactivate the card. Return True if card is active, False if frozen.'''
    global activated

    if not activated:
        return activated
    elif activated and (not all_three_different(c1, c2, c3)):
        return activated
    else:
        activated = False
        return activated
        
def purchase(amount, day, month, country):
    '''Complete a purchase of amount on a specified day, month, and country.
    Return "error" if card is deactivated or if there was a simulation
    operation on a date later than day, month.'''
    global cur_balance_owing_intst, cur_balance_owing_recent
    global last_update_day, last_update_month
    global last_country, last_country2

    if not card_status(country, last_country, last_country2):
        last_update_day = day
        last_update_month = month

        return "error"
    elif not date_same_or_later(day, month, last_update_day, last_update_month):
        return "error"
    else:
        update(month)
        cur_balance_owing_recent += amount

    last_update_day = day
    last_update_month = month
    last_country2 = last_country
    last_country = country

def update(month):
    '''Update the balances owing accruing and not accruing interest, applying
    interest based off the month of the latest simulation operation.'''
    global last_update_month
    global cur_balance_owing_intst, cur_balance_owing_recent
    global MONTHLY_INTEREST_RATE

    #month_diff is greater than or equal to zero
    month_diff = month - last_update_month

    if (month_diff >= 1):
        # apply interest on the balance owing interest, and apply interest on
        # balance not owing interest if applicable, when the difference in
        # months of this and last transaction is greater than or equal to 1.
        # Move the balance not owing interest to balance owing interest and
        # then set it to 0.
        cur_balance_owing_intst *= (1 + MONTHLY_INTEREST_RATE) ** month_diff
        cur_balance_owing_recent *= (1 + MONTHLY_INTEREST_RATE) ** \
            (month_diff - 1)
        cur_balance_owing_intst += cur_balance_owing_recent
        cur_balance_owing_recent = 0

        last_update_month = month

def amount_owed(day, month):
    '''Return the amount owed as of day, month. Return "error" if there was a
    simulation operation on a date later than day, month.'''
    global last_update_day, last_update_month
    global cur_balance_owing_intst, cur_balance_owing_recent

    if not date_same_or_later(day, month, last_update_day, last_update_month):
        return "error"

    update(month)

    last_update_day = day
    last_update_month = month

    return(cur_balance_owing_intst + cur_balance_owing_recent)
    
def pay_bill(amount, day, month):
    '''Pay off the balance owed by amount, by first paying off the balance
    accruing interest and then the balance not accuring interest. Return
    "error" if there was a simulation operation on a date later than day,
    month.'''
    global last_update_day, last_update_month
    global cur_balance_owing_intst, cur_balance_owing_recent

    if not date_same_or_later(day, month, last_update_day, last_update_month):
        return "error"

    update(month)

    if cur_balance_owing_intst < amount:
        # If the payment is bigger than balance accruing interest, first pay
        # off balance accuring interest and use the rest to pay off balance
        # not accuring interest.
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
