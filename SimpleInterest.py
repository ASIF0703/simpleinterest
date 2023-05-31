def calculate_simple_interest(principal, time, gender, senior_citizen):
    if gender == 'female' and senior_citizen:
        rate = 8
    elif gender == 'female' and not senior_citizen:
        rate = 6
    elif gender == 'male' and senior_citizen:
        rate = 7
    elif gender == 'male' and not senior_citizen:
        rate = 5
    else:
        print("Invalid input.")
        return None

    interest = (principal * rate * time) / 100
    return interest



principal = 1000000
time = 5
gender = 'female'
senior_citizen = True

interest = calculate_simple_interest(principal, time, gender, senior_citizen)
if interest is not None:
    print("Simple Interest:", interest)
