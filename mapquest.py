import urllib.parse
import requests
from colorama import Fore
from colorama import Style
from texttable import Texttable

main_api = "https://www.mapquestapi.com/directions/v2/route?"
map_api = "https://www.mapquestapi.com/staticmap/v5/map?"
map_api_zoom = "&zoom=16&type=hyb&size=1600,1200@2x"
key = "a7i9vjVY2Qt2Ace15kn8xgHLmfGQEul1"
t = Texttable()

def printDir():
        if "Welcome" not in each["narrative"] and myUnits == "1":
            print((each["narrative"]) + "\n")
        if "Welcome" not in each["narrative"] and myUnits == "2" or myUnits.isalpha():
            print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)") + "\n")
        if "Welcome" in each["narrative"]:
            print(f"{Style.BRIGHT}{Fore.GREEN}\n\nFinally! {Style.RESET_ALL}" + (each["narrative"]) + "\n")

def printCardinalDir():
        if "Arrive" not in each["narrative"]:
            print(f"{Fore.YELLOW}[NOW HEADING " + (each["directionName"]).upper() + f"]{Style.RESET_ALL}")
        if "Arrive" in each["narrative"]:
            print(
                f"{Style.BRIGHT}{Fore.BLUE} ---------------------------------------------------------------------{Style.RESET_ALL}")
            print(
                f"{Style.BRIGHT}{Fore.BLUE}|{Style.RESET_ALL}                       {Style.BRIGHT}{Fore.CYAN}Welcome to {dest}, {name}!{Style.RESET_ALL}                   {Style.BRIGHT}{Fore.BLUE}|{Style.RESET_ALL}")
            print(
                f"{Style.BRIGHT}{Fore.BLUE} ---------------------------------------------------------------------{Style.RESET_ALL}\n")


print(f"{Style.BRIGHT}{Fore.BLUE} --------------------------------------------------------------------{Style.RESET_ALL}")
print (f"{Style.BRIGHT}{Fore.BLUE}|            {Fore.CYAN}                  MapQuest!                            {Style.RESET_ALL}{Style.BRIGHT}{Fore.BLUE} |{Style.RESET_ALL}")
print(f"{Style.BRIGHT}{Fore.BLUE} --------------------------------------------------------------------{Style.RESET_ALL}")

print (f"\n{Style.BRIGHT}{Fore.YELLOW}Instructions:{Style.RESET_ALL} Remember to enter {Style.BRIGHT}{Fore.RED}'q'{Style.RESET_ALL} or {Style.BRIGHT}{Fore.RED}'quit'{Style.RESET_ALL} to {Style.BRIGHT}{Fore.RED}exit{Style.RESET_ALL} the program!\n")



name = input("Enter your name: ")
print(f"\n{Style.BRIGHT}{Fore.YELLOW}Hello, {Style.BRIGHT}{Fore.BLUE}{name}{Style.RESET_ALL}{Style.BRIGHT}{Fore.YELLOW}. Let us start the MapQuest!{Style.RESET_ALL}")
if name == "quit" or name == "q":
        exit()

while True:
    myUnits = input("Choose a unit of measurement: 1 (Miles), 2 (Kilometers): ")
    if myUnits == "quit" or myUnits == "q":
        break
    orig = input("Starting Location: ")
    if orig == "quit" or orig == "q":
        break

    dest = input("Destination: ")
    if dest == "quit" or dest == "q":
        break

    url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest})
    myMapURL = map_api + urllib.parse.urlencode({"key":key, "center":dest}) + map_api_zoom
    json_data = requests.get(url).json()

    print(f"{Style.BRIGHT}{Fore.YELLOW}\n\nURL to your directions: {Style.RESET_ALL}" + (url))
    print(f"{Style.BRIGHT}{Fore.YELLOW}\nSattelite image to your destination: {Style.RESET_ALL}" + (myMapURL))


    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]

    if json_status == 0:

        print(f"{Style.BRIGHT}{Fore.GREEN}\n======================================================================={Style.RESET_ALL}")
        print("Directions from " + (orig.upper()) + " to " + (dest.upper()))
        print("\t   Trip Duration:   " + (json_data["route"]["formattedTime"]))

        if myUnits == "1":
            print("\t   Miles:      " + str("{:.2f}".format((json_data["route"]["distance"]))))
        elif myUnits == "2":
            print("\t   Kilometers:      " + str("{:.2f}".format((json_data["route"]["distance"])*1.61)))
        else:
            print("\t   Kilometers:      " + str("{:.2f}".format((json_data["route"]["distance"])*1.61)))
        # print("Fuel Used (Ltr): " + str("{:.2f}".format((json_data["route"]["fuelUsed"])*3.78)))

        print(f"{Style.BRIGHT}{Fore.GREEN}=======================================================================\n{Style.RESET_ALL}")
        for each in json_data["route"]["legs"][0]["maneuvers"]:
            printDir()
            printCardinalDir()
        print(f"{Style.BRIGHT}{Fore.GREEN}=======================================================================\n{Style.RESET_ALL}")

    elif json_status == 402:
        print(f"\n{Style.BRIGHT}{Fore.RED}*****************************************************************{Style.RESET_ALL}")
        print(f"{Style.BRIGHT}{Fore.RED}Status Code: {str(json_status)}; Invalid user inputs for one or both locations.{Style.RESET_ALL}")
        print(f"{Style.BRIGHT}{Fore.RED}*****************************************************************{Style.RESET_ALL}\n")

    elif json_status == 611:
        print(f"\n{Style.BRIGHT}{Fore.RED}*****************************************************************{Style.RESET_ALL}")
        print(f"{Style.BRIGHT}{Fore.RED}Status Code: {str(json_status)}; Missing an entry for one or both locations.{Style.RESET_ALL}")
        print(f"{Style.BRIGHT}{Fore.RED}*****************************************************************{Style.RESET_ALL}\n")

    else:
        print(f"\n{Style.BRIGHT}{Fore.RED}*****************************************************************{Style.RESET_ALL}")
        print(f"{Style.BRIGHT}{Fore.RED}For Status Code: {str(json_status)}; Refer to:{Style.RESET_ALL}")
        print(f"{Style.BRIGHT}{Fore.RED}https://developer.mapquest.com/documentation/directions-api/status-codes{Style.RESET_ALL}")
        print(f"{Style.BRIGHT}{Fore.RED}*****************************************************************{Style.RESET_ALL}\n")