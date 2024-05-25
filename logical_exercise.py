def check_discount():
    # Ask the user to input their age
    age = int(input("Please enter your age: "))

    # Ask the user to input whether they are a student or not
    is_student = input("Are you a student? (yes or no): ").strip().lower()

    # Determine if the person is eligible for a discount
    if age <= 12:
        eligible_for_discount = True
    elif 13 <= age <= 18 and is_student == 'yes':
        eligible_for_discount = True
    else:
        eligible_for_discount = False

    # Print a message indicating whether the person is eligible for a discount or not
    if eligible_for_discount:
        print("You are eligible for a discount on the movie ticket.")
    else:
        print("You are not eligible for a discount on the movie ticket.")

# Run the function
check_discount()
