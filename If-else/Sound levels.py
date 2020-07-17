
sound_level = int(input("Enter the sound level : "))

if sound_level == 130:
    print("This noise is of Jackhammer")

elif sound_level == 106:
    print("This noise is of Gas lawnmower")

elif sound_level == 70:
    print("This noise is of Alarm Clock")

elif sound_level == 40:
    print("This noise is of Quiet room")

elif 106 < sound_level < 130:
    print("This noise is of between Gas lawnmower and Jackhammer ")

elif 70 < sound_level < 106:
    print("This noise is of between Alarm clock and Gas lawnmower ")

elif 40 < sound_level < 70:
    print("This noise is of between Quiet room and Alarm clock ")

else:
    print("Error : please enter correct value")