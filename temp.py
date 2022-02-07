name=input("Please insert your name: ")
temp=input("Please insert the temperature of the house: ")
season=input("In which season of the year are you ? [Summer - Winter]: ")
"season" == "Summer"
"season" == "Winter" 
if "season" == "Summer" and "temp" <= 19 and "temp" > 10: 
    print("The temperature is in normal levels :) ")
elif "season" == "Summer" and "temp" >= 20 and "temp" <= 27: 
    print("The temperature is high :( Consider lowing it down")
elif "season" == "Summer" and "temp" > 28: 
    print("Be careful !! The temperature is in extremely high levels ! Low it down !!")
elif "season" == "Winter" and "temp" <= 19 and "temp" > 10: 
    print("The temperature is in extremely low levels ! Consider raising it")
elif "season" == "Winter" and "temp" >= 20 and "temp" <= 27: 
    print("The temperature is in normal levels :) ")
elif "season" == "Winter" and "temp" > 28: 
    print("The temperature is high :( Consider lowing it down")
else:
    while season != "Summer" and season != "Winter":
        print("Wrong season inserted :( Please try again.")
        season=input("Please insert season: ")

