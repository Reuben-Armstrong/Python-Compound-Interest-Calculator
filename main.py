# Python compound interest calculator

# Title
print('------------------------------------------------------------------------------')
print(' Compound Interest Calculator')
print('------------------------------------------------------------------------------')

# Loop to check for invalids with: try: ...   except ValueError: ...
while True:
    try:
        print('')
        principle = float(input('Enter the initial principle (Starting Amount): '))
        if principle <= 0:
            print('Principle can not be less than or equal to zero.')
            continue

        rate = float(input('Enter the interest rate (Percent a year): '))
        if rate <= 0:
            print('Interest rate can not be less than or equal to zero.')
            continue
        
        time = int(input('Enter the amount of time in years (How long): '))
        if time <= 0:
            print('Time can not be less or than or equal to zero.')
        
        break # exit loop

    except ValueError:
        print('That is not a valid number! Try again.') # For non-numbers

# Calculation for final amount
total = principle * ((1 + (rate / 100)) ** time)
extra = total - principle

# Output
print('')
print('------------------------------------------------------------------------------')
print(f' Your Final Amount is: ${total:.2}')
print(f' Your Amount goes up by ${extra:.2}')
print('------------------------------------------------------------------------------')
print('')
input('Press the Enter Key to Exit...')