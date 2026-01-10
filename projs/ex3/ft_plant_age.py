def ft_plant_age():
    age = input("Enter the age of the plant in days: ")
    age_days = int(age)
    if age_days <= 60:
        print("Plant needs more time to grow.")
    else:
        print("Plant is ready to harvest!")
