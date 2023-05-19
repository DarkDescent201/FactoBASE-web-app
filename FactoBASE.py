#### Library Import ####
import math
from os import system as sys
from time import sleep as pause
""" from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from hoverable import HoverBehavior
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior """



#### Functions ####
# Gets user input on conversion type and initial numbers.
def get_user_input():
    conversion_choice = 99
    while True:
        if not conversion_choice:
            print("Please enter a choice.\n")
            pause(2)
            pass
        elif conversion_choice == '4':
            return('4', '4', '4', '4')
        else:
            pass
        print("\nPlease make the following selections:")
        try:
            conversion_choice = input("""
(1) Convert from numerical base to FactoBASE!
(2) Convert from FactoBASE! to a numerical base.
(3) Convert from one numerical base to another.
(4) EXIT
---->  """)
            print("")
            if conversion_choice == '4':
                continue
            elif int(conversion_choice) not in [1,2,3,4]:
                raise ValueError
            else:
                pass
        except ValueError:
            print("\nThat is not a valid selection.\nThe only valid options are 1, 2, 3, and 4.\n")
            pause(2)
            continue
        try:
            if conversion_choice == '1':
                userbase_choice = input("""
Select your desired numerical base.  This must be an integer > 1.
This is the base you are providing your number in.
---->  """)
                print("")
                userbase_choice_2 = '99'
            elif conversion_choice == '2':
                userbase_choice = input("""
Select your desired numerical base.  This must be an integer > 1.
This is the base you will receive your answer in.
---->  """)
                print("")
                userbase_choice_2 = '99'
            elif conversion_choice == '3':
                userbase_choice = input("""
Select your first numerical base. This must be an integer > 1.
This is the base you will provide your input number in.
---->  """)
                userbase_choice_2 = input("""
Select your second numberical base.  This must be an integer > 1.
This is the base you will receive your answer in.
---->  """)
                print("")
            if int(userbase_choice) < 2 or int(userbase_choice_2) < 2:
                raise ValueError
            else:
                pass
        except ValueError:
            print("\nThat is not a valid selection.\n Only integers greater than or equal to 2 are valid.\n")
            pause(2)
            continue
        try:
            number_input = int(input("Please enter your number.\n---->  "))
            number_choice = str(number_input)
            return(conversion_choice, userbase_choice, number_choice, userbase_choice_2)
        except ValueError:
            print("\nPlease enter a number.\n")
            pause(2)
            continue

# Takes the numerical base value and the starting number and converts them to a decimal number.
def numbase_to_decimal(base_num, input_num):
    bas = int(base_num)
    num_rev = input_num[::-1]
    total = 0
    place_pos = 0
    for target_digit in num_rev:
        dig = int(target_digit)
        total += dig * (bas ** place_pos)
        place_pos += 1
    decimal_value = str(total)
    return(decimal_value)

# Takes the starting FactoBASE! number and converts it to a decimal number.
def factobase_to_decimal(facto_num):       # WARNING:  Simplified version, does not digit-check for digits over 9
    run_tot = 0
    place_pos = len(facto_num)
    for digit in facto_num:
        num = int(digit)
        run_tot += num * math.factorial(place_pos)
        place_pos -= 1
    return(str(run_tot))

# Finds the length of user's numerical base number.
def find_numbase_length(base_num, dec_num):
    bas =  int(base_num)
    num = int(dec_num)
    place_pos = 0
    while bas ** place_pos <= num:
        place_pos +=1
    numbase_length = str(place_pos)
    return(numbase_length)

# Convert a number from its decimal form to userbase number.
def decimal_to_numbase(dec_num, base_num, numb_len):
    length = int(numb_len)
    bas = int(base_num)
    dec = int(dec_num)
    numbase_result= ""
    for place_pos in range(length,0,-1):
        place_val = 0
        exponent = place_pos -1
        while place_val * (bas ** exponent) <= dec:
            place_val += 1
        place_val -= 1
        numbase_result += f"{place_val} "
        dec -= place_val * (bas ** exponent)
    if dec != 0:
        print(f"\nThere has been an error!  Numbase process reached its end but {dec = }\n")
        pause(3)
        return("## ERROR##")
    else:
        return(numbase_result)

# Finds the length of a Factobase number.
def find_factobase_length(dec_num):
    num = int(dec_num)
    place_pos = 1
    while math.factorial(place_pos) <= num:
        place_pos += 1
    place_pos -= 1
    factobase_length = str(place_pos)
    return(factobase_length)

# Converts from a decimal number to a FactoBASE! number.
def decimal_to_factobase(dec_num, factobase_len):
    length = int(factobase_len)
    num = int(dec_num)
    factobase_result= ""
    for place_pos in range(length,0,-1):
        place_val = 0
        while place_val * math.factorial(place_pos) <= num:
            place_val += 1
        place_val -= 1
        num -= place_val * math.factorial(place_pos)
        factobase_result += f"{place_val} "
    if num != 0:
        print(f"\nThere has been an error!  The FactoBASE! process has completed but {num = }\n")
        pause(3)
        return("## ERROR ##")
    else:
        return(factobase_result)

# Main Function
def main():
    while True:
        sys("clear")
        userchoice, numbase, usernum, numbase2 = get_user_input()
        if userchoice == '4':
            print("\nExiting now!\n")
            pause(1)
            break
        elif userchoice == '1':
            dec_val = numbase_to_decimal(numbase, usernum)
            facto_len = find_factobase_length(dec_val)
            factobase_result = decimal_to_factobase(dec_val, facto_len)
            dec_val2 = "{:,}".format(int(dec_val))
            print(f"""
Here are your results:

The number you provided was:            {usernum}
Given in:                               base-{numbase}
Its decimal value is:                   {dec_val2}    (length = {len(dec_val)})

The FactoBASE! result is:               {factobase_result}
Its length is:                          {facto_len} places.

Press 'Enter' to continue...
""")
            input("")
        elif userchoice == '2':
            dec_val = factobase_to_decimal(usernum)
            numb_len = find_numbase_length(numbase, dec_val)
            numbase_result = decimal_to_numbase(dec_val, numbase, numb_len)
            dec_val2 = "{:,}".format(int(dec_val))
            print(f"""
Here are your results:

The number you provided was:                {usernum}
Given in:                                   FactoBASE!
Its decimal value is:                       {dec_val2}    (length = {len(dec_val)})

Your base-{numbase} result is:                      {numbase_result}
Its length is:                              {numb_len} places.

Press 'Enter' to continue...
""")
            input("")
        elif userchoice == '3':
            dec_val_1 = numbase_to_decimal(numbase, usernum)
            numb_len = find_numbase_length(numbase2, dec_val_1)
            numbase_result = decimal_to_numbase(dec_val_1, numbase2, numb_len)
            dec_val_2 = "{:,}".format(int(dec_val_1))
            print(f"""
Here are your results:

The number you provided was:            {usernum}
Given in:                               base-{numbase}
Its decimal value is:                   {dec_val_2}    (length = {len(dec_val_1)})

Your base-{numbase2} result is:                  {numbase_result}
Its length is:                          {numb_len}

Press 'Enter' to continue...
            """)
            input("")
        else:
            print(f"\nThere has been an error.  An invalid choice was given, {userchoice = }\n")
            print("Press 'Enter' to continue...")
            input("")



#### Initialize ####
if __name__ == "__main__":
    main()