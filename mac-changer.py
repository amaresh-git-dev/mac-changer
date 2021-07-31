import subprocess

def logo():
	

	print("""

		                          _                                 
		                         | |                                
	  _ __ ___   __ _  ___ ______ ___| |__   __ _ _ __   __ _  ___ _ __ 
	 | '_ ` _ \ / _` |/ __|______/ __| '_ \ / _` | '_ \ / _` |/ _ \ '__|
	 | | | | | | (_| | (__      | (__| | | | (_| | | | | (_| |  __/ |   
	 |_| |_| |_|\__,_|\___|      \___|_| |_|\__,_|_| |_|\__, |\___|_|   
		                                             __/ |          
		                  @amaresh-git-dev          |___/  
		                                                     

	""") 

logo()

mac = print("* press 1 for check current mac address")
print1 = print("* press 2 for change current mac")
print2 = print("* press 3 to reset your parmanent mac")

choice = int(input("Enter your choice: "))

if choice == 1:
	subprocess.call("sudo macchanger -s eth0",shell=True)
	
elif choice == 2:
	subprocess.call("sudo macchanger -a eth0",shell=True)

elif choice == 3:
	subprocess.call("sudo macchanger -p eth0",shell=True)

else:
	print("Wrong option")