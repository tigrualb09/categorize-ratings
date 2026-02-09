def categorize_ratings(rating_list):
    number_of_low_ratings = 0
    number_of_medium_ratings = 0
    number_of_high_ratings = 0
    for i in rating_list:
        if i < 5:
            number_of_low_ratings += 1
        elif i >= 5 and i < 8:
            number_of_medium_ratings += 1
        elif i > 7:
            number_of_high_ratings += 1
    print (f"Low: {number_of_low_ratings}") #one way of printing message + value using acolades
    print (f"Medium: ", number_of_medium_ratings) #another easier way using coma
    print (f"High: ", number_of_high_ratings)

categorize_ratings([1, 3, 5, 7, 8, 9])
