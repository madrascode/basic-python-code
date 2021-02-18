def leap(num):

    if num % 4 == 0: # Then its an LEAP Year
        if num % 100 == 0: # if its an century then its not Leap Year
            if num % 400 == 0: # if that century is 4th century then its leap year
                print('Leap Year')
            else:
                print("Ordinary Year")
        else:
            print("Leap Year")
    else:
        print("Ordinary Year")

leap(2020)