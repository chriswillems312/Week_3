day_to_jail = int(input("At which day number are you going to jail?, 0 = sunday"))
days_in_jail = int(input("How many days do you have to be in jail?"))

day_out_of_jail = ((day_to_jail + days_in_jail) % 7)

if day_out_of_jail == 0 :
    print("You will leave jail on a Sunday")
elif day_out_of_jail == 1 :
    print("You will leave jail on a Monday")
elif day_out_of_jail == 2 :
    print("You will leave jail on a Tuesday")
elif day_out_of_jail == 3 :
    print("You will leave jail on a Wednesday")
elif day_out_of_jail == 4 :
    print("You will leave jail on a Thursday")
elif day_out_of_jail == 5 :
    print("You will leave jail on a Friday")
elif day_out_of_jail == 6 :
    print("You will leave jail on a Saturday")