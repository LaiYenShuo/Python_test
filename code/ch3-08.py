#Exxlusie Network
#Demostrates logical operators and compound conditions
print("""
        Exclusive Computer Network
                Members only!
""")

security = 0

username = ""
while not username:
    username = input("Username:")

password = ""
while not password:
    password = input("Password:")

if username == "M.Dawson" and password == "secret":
    print("Hi, Mike.")
    security = 5
elif username == "TerryLai" and password == "********":
    print("Hi, Terry.")
    security = 3
elif username == "S.Miyamoto" and password == "mariobros":
    print("What's up, Shigeru?")
    security = 3
elif username == "W.Wright" and password == "thesims":
    print("How goes it, Will?")
    security = 3
elif username == "guest" or password == "guest":
    print("Welcome, guest.")
    security = 1
else:
    print("Login failed. You're not so exclusive.\n")
input("\n\nPress the enter key to exit.")