import sys
import random
import time 
import os

os.system('cls' if os.name == 'nt' else 'clear')

def animated(text):
  for x in text:
    sys.stdout.write(x)
    sys.stdout.flush()
    time.sleep(0.001)
   
logo = '''
\033[92m$$$$$$$\   $$$$$$\  $$\    $$\ $$$$$$$$\ $$\   $$\ 
$$  __$$\ $$  __$$\ $$ |   $$ |$$  _____|$$$\  $$ |
$$ |  $$ |$$ /  $$ |$$ |   $$ |$$ |      $$$$\ $$ |
$$$$$$$  |$$$$$$$$ |\$$\  $$  |$$$$$\    $$ $$\$$ |
$$  __$$< $$  __$$ | \$$\$$  / $$  __|   $$ \$$$$ |
$$ |  $$ |$$ |  $$ |  \$$$  /  $$ |      $$ |\$$$ |
$$ |  $$ |$$ |  $$ |   \$  /   $$$$$$$$\ $$ | \$$ |
\__|  \__|\__|  \__|    \_/    \________|\__|  \__|
                                                   
                                                   
                                                   
$$$$$$$$\ $$$$$$$$\  $$$$$$\  $$\   $$\            
\__$$  __|$$  _____|$$  __$$\ $$ |  $$ |           
   $$ |   $$ |      $$ /  \__|$$ |  $$ |           
   $$ |   $$$$$\    $$ |      $$$$$$$$ |           
   $$ |   $$  __|   $$ |      $$  __$$ |           
   $$ |   $$ |      $$ |  $$\ $$ |  $$ |           
   $$ |   $$$$$$$$\ \$$$$$$  |$$ |  $$ |           
   \__|   \________| \______/ \__|  \__|\033[0m
'''
line = '''\033[1;1;1;1;1;1;1;1;1;1;91m
------------------------------------------------------\033[0m\033[1;1;1;1;1;1;1;1;1;1;92m------------------------------------------------------\033[0m\033[1;1;1;1;1;1;1;1;1;1;91m------------------------------------------------------\033[0m\033[1;1;1;1;1;1;1;1;1;1;92m------------------------------------------------------\033[0m
'''
animated(logo)
animated(line)

text = "\n\n\n\033[91m[\033[0m\033[1;92m1\033[0m\033[91m]\033[0m\033[1;1;1;1;1;1;1;1;1;91m𝙏𝙊𝙊𝙇 𝙉𝘼𝙈𝙀: 𝙐𝙣𝙞𝙂𝙚𝙣\033[0m\n\033[91m[\033[0m\033[1;92m2\033[0m\033[91m]\033[0m\033[1;1;1;1;1;1;1;1;1;91m𝘼𝙐𝙏𝙃𝙊𝙍: 𝙍𝘼𝙑𝙀𝙉𝙏𝙀𝘾𝙃\033[0m\n\n\n\033[1;1;1;1;1;1;93m𝚆𝙴𝙻𝙲𝙾𝙼𝙴 𝚃𝙾 𝙽𝚄𝙼𝙶𝙴𝙽\033[0m\n"

def animated(text):
  for x in text:
    sys.stdout.write(x)
    sys.stdout.flush()
    time.sleep(0.02)

animated(text)

password = "RAVEN@99#"

user_input = input("Enter password: ")

if user_input == password:
    print("✅ Access Granted! Tool running...")
else:
    print("❌ Wrong password! Access Denied.")
    sys.exit()

def make_username(name):
    base = name.lower()
    number = str(random.randint(10, 99))
    symbols = ["_", ".", "-", ""]
    symbol = random.choice(symbols)
    username = base + symbol + number
    return username

print("""
[1]NumGen 
[2]UserGen
""")

choice = input("Enter your choice: ")

def phoneNumber(operator):
    endNum = random.randint(10000000, 99999999)
    number = f"01{operator}{endNum}"
    print(number)

if choice == "1":
    print('''\033[1;1;1;1;1;1;92m
              CHOICE YOUR OPERATOR
              [1]GRAMEENPHONE 
              [2]BANGLALINK 
              [3]ROBI
              [4]TELETOLK
              [5]SKITO\033[0m
''')
    op = input('Enter your choice: ')
    amount = int(input('How many number you want: '))

    if op == "1":
        for i in range(amount):
            phoneNumber(7)
    elif op == "2":
        for i in range(amount):
            phoneNumber(9)
    elif op == "3":
        for i in range(amount):
            phoneNumber(8)
    elif op == "4":
        for i in range(amount):
            phoneNumber(5)
    elif op == "5":
        for i in range(amount):
            phoneNumber(3)
    else:
        print("Wrong input")

elif choice == "2":
    name = input("Enter your name: ")
    amount = int(input("How many name you want: "))

    print("\nHere are some username suggestions:\n")
    for i in range(amount):
        print(make_username(name))

else:
    print("Wrong choice")