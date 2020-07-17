one_human_year = 7
two_human_year = 10.5

year = float(input("Enter the number of human years : "))

if year == 1:
    print("%d human years is equals to %0.1f dog years" %(year, one_human_year))

elif year == 2:
    print("%d human years is equals to %0.1f dog years" %(year, two_human_year))

elif year > 2:
    additional_year_after_two_years = year - 2
    dog_year_in_additional_year = additional_year_after_two_years * 4
    dog_year_after_additional_human_year = 10.5 + dog_year_in_additional_year
    print("%d human years is equals to %0.1f dog years" %(year, dog_year_after_additional_human_year))

else:
    print("Error %d is not a valid value" % (year))