#Inputs
name=input("Please insert your name: ")
temp=int(input("Please insert the temperature of the house: "))
season=input("In which season of the year are you ? [Summer - Winter]: ")
"seasons" == "Summer"
"seasonw" == "Winter"
#Summer
if "seasons" == "Summer" and temp >= -10 or temp <= 9:
    print("The temperature is in extremely low levels ! :( Consider increasing it !") 
elif "seasons" == "Summer" and temp >= 10 or temp <= 19: 
    print("Good ! The temperature is in normal levels :) ")
elif "seasons" == "Summer" and temp >= 20 or temp <= 27: 
    print("The temperature is high :( Consider lowing it down")
elif "seasons" == "Summer" and temp >= 28: 
    print("Be careful !! The temperature is in extremely high levels ! Low it down !!")
#Winter
elif "seasonw" == "Winter" and temp >= -10 or temp <= 9:
    print("Be careful !! The temperature is extremely low ! Increase it immediately !!")  
elif "seasonw" == "Winter" and temp >= 10 or temp <= 19: 
    print("The temperature is in low levels :( Consider increasing it !")
elif "seasonw" == "Winter" and temp >= 20 or temp <= 27: 
    print("Good ! The temperature is in normal levels :) ")
elif "seasonw" == "Winter" and temp >= 28: 
    print("The temperature is high :( Consider lowing it down")
