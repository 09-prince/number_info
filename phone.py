
import phonenumbers
from phonenumbers import timezone,geocoder,carrier

print("This python project gives you a basic information about the number!")

while True:
    user=input("Enter start if you want to start or quit if you want to quite: ").lower()
    if user=="start":
        phn_number=input("Enter number with country code: ")
        number=phonenumbers.parse(phn_number)
        about=phonenumbers.is_valid_number(number)
        print(about)
        if about==True:
                time_zone=timezone.time_zones_for_number(number)
                name=carrier.name_for_number(number,"en")
                geo=geocoder.description_for_number(number,"en")
                print(number)
                print(time_zone)
                print(name)
                print(geo)
        elif about==False:
                print("Your number is not valid")
        else:
                print("Wrong format or you enter wrong number")
    elif user=="quit":
        break
    else:
        print("You enter wrong input please select right input!?")

