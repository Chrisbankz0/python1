def main_menu():
    while True:
        print("""

   MTN - TECHTRIBE EDITION


1. Phonebook
2. Messages
3. Chat
4. Call Register
5. Tones
6. Settings
7. Call Divert
8. Games
9. Calculator
10. Reminders
11. Clock
12. Profiles
13. SIM Services
0. Exit
""")

        choice = input("Enter choice: ")

        if choice == "1":
            phonebook_menu()
        elif choice == "2":
            messages_menu()
        elif choice == "3":
            chat_menu()
        elif choice == "4":
            call_register_menu()
        elif choice == "5":
            tones_menu()
        elif choice == "6":
            settings_menu()
        elif choice == "7":
            call_divert_menu()
        elif choice == "8":
            print("Opening Games...\n")
        elif choice == "9":
            print("Opening Calculator")
        elif choice == "10":
            print("Opening Reminders...\n")
        elif choice == "11":
            clock_menu()
        elif choice == "12":
            print("Opening Profiles")
        elif choice == "13":
            print("Opening SIM Services...\n")
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid option!\n")



# PHONEBOOK MENU


def phonebook_menu():
    while True:
        print("""
PHONEBOOK

1. Search
2. Service Nos
3. Add name
4. Erase
5. Edit
6. Assign tone
7. Send b'card
8. Options
9. Speed dials
10. Voice tags
0. Back
""")

        choice = input("Enter choice: ")

        if choice == "1":
            print("Searching...\n")
        elif choice == "2":
            print("Service numbers...\n")
        elif choice == "3":
            print("Adding name...\n")
        elif choice == "4":
            print("Erasing...\n")
        elif choice == "5":
            print("Editing...\n")
        elif choice == "6":
            print("Assigning tone...\n")
        elif choice == "7":
            print("Sending business card...\n")
        elif choice == "8":
            phonebook_options()
        elif choice == "9":
            print("Speed dials...\n")
        elif choice == "10":
            print("Voice tags...\n")
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid option!\n")


def phonebook_options():
    while True:
        print("""
PHONEBOOK OPTIONS


1. Type of view
2. Memory status
0. Back
""")

        choice = input("Enter choice: ")

        if choice == "1":
            print("Type of view...\n")
        elif choice == "2":
            print("Memory status...\n")
        elif choice == "0":
            break
        else:
            print("Invalid option!\n")




# MESSAGES MENU


def messages_menu():
    while True:
        print("""
MESSAGES

1. Write messages
2. Inbox
3. Outbox
4. Picture messages
5. Templates
6. Smileys
7. Message settings
8. Info service
9. Voice mailbox number
10. Service command editor
0. Back
""")

        choice = input("Enter choice: ")

        if choice == "1":
            print("Writing message")
        elif choice == "2":
            print("Opening inbox")
        elif choice == "3":
            print("Opening outbox...\n")
        elif choice == "4":
            print("Picture messages...\n")
        elif choice == "5":
            print("Templates...\n")
        elif choice == "6":
            print("Smileys...\n")
        elif choice == "7":
            message_settings_menu()
        elif choice == "8":
            print("Info service...\n")
        elif choice == "9":
            print("Voice mailbox number...\n")
        elif choice == "10":
            print("Service command editor...\n")
        elif choice == "0":
            break
        else:
            print("Invalid option!\n")


def message_settings_menu():
    while True:
        print("""
MESSAGE SETTINGS

1. Set 1
2. Common
0. Back
""")

        choice = input("Enter choice: ")

        if choice == "1":
            message_set_menu()
        elif choice == "2":
            message_common_menu()
        elif choice == "0":
            break
        else:
            print("Invalid option!\n")


#this is message setting number 7 set

def message_set_menu():
    while True:
        print("""
SET SETTINGS

1. Message Center number
2. Message sent as
3. Message validity
0. Back
""")

        choice = input("Enter choice: ")

        if choice == "1":
            print("message center number....\n")
        elif choice == "2":
            print("message sent as....\n")
        elif choice == "3":
            print("message Validity....\n")
        elif choice == "0":
            break
        else:
            print("Invalid option!\n")



#this is message common number 7 set

def message_common_menu():
    while True:
        print("""
COMMON SETTINGS

1. Delivery reports
2. Reply via same center
3. Character support
0. Back
""")

        choice = input("Enter choice: ")

        if choice == "1":
            print("Delivery reports....")
        elif choice == "2":
            print("Reply via same center....")
        elif choice == "3":
            print("Character support....")
        elif choice == "0":
            break
        else:
            print("Invalid option!\n")




# this is for chat menu

def chat_menu():
    while True:
        print("""
CHAT

1. Start Chat
0. Back
""")
        choice = input("Enter choice: ")

        if choice == "1":
            print("Starting chat...\n")
        elif choice == "0":
            break
        else:
            print("Invalid option!\n")



# CALL REGISTER MENU

def call_register_menu():
    while True:
        print("""
CALL REGISTER

1. Missed calls
2. Received calls
3. Dialled numbers
4. Erase recent call lists
5. Show call duration
6. Show call costs
7. Call cost settings
8. Prepaid credit
0. Back
""")

        choice = input("Enter choice: ")

        if choice == "1":
            print("Missed calls...\n")
        elif choice == "2":
            print("Received calls...\n")
        elif choice == "3":
            print("Dialled numbers...\n")
        elif choice == "4":
            print("Erasing call lists...\n")
        elif choice == "5":
            show_call_duration_menu()
        elif choice == "6":
            Show_Call_menu()
        elif choice == "7":
            Call_cost_settings_menu()
        elif choice == "8":
            print("Prepaid credit...\n")
        elif choice == "0":
            break
        else:
            print("Invalid option!\n")

#inside number 5 of number 4

def show_call_duration_menu():
    while True:
        print("""
SHOW CALL DURATION

1. Last call duration 
2. All call's duration
3. Receieved call's duration
4. Dialled call's duration
5. Clear timers
0. Back
""")

        choice = input("Enter choice: ")

        if choice == "1":
            print("Last call duration...\n")
        elif choice == "2":
            print("All call's duration...\n")
        elif choice == "3":
            print("Dialled numbers...\n")
        elif choice == "4":
            print("Erasing call lists...\n")
        elif choice == "5":
            print("Clear timers...\n")
        elif choice == "0":
            break
        else:
            print("Invalid option!\n")



def show_call_cost_menu():
    while True:
        print("""
SHOW CALL COST

1. Last call cost 
2. All call's cost
3. Clear counters
0. Back
""")

        choice = input("Enter choice: ")

        if choice == "1":
            print("Last call duration...\n")
        elif choice == "2":
            print("All call's duration...\n")
        elif choice == "3":
            print("Dialled numbers...\n")
        elif choice == "4":
            print("Erasing call lists...\n")
        elif choice == "5":
            print("Clear timers...\n")
        elif choice == "0":
            break
        else:
            print("Invalid option!\n")

#call register number 7

def Call_cost_settings_menu():
    while True:
        print("""
CALL COST SETTINGS

1. call cost limit 
2. Show cost in
0. Back
""")

        choice = input("Enter choice: ")

        if choice == "1":
            print("call cost limit...\n")
        elif choice == "2":
            print("Show cost in...\n")
        elif choice == "0":
            break
        else:
            print("Invalid option!\n")


# TONES MENU

def tones_menu():
    while True:
        print("""
TONES

1. Ringing tone
2. Ringing volume
3. Incoming call alert
4. Composer
5. Message alert tone
6. Keypad tones
7. Warning and game tones
8. Vibrating alert
9. Screen saver
0. Back
""")

        choice = input("Enter choice: ")

        if choice == "0":
            break
        else:
            print("Feature not implemented.\n")



# SETTINGS MENU

def settings_menu():
    while True:
        print("""
SETTINGS

1. Call settings
2. Phone settings
3. Security settings
4. Restore factory settings
0. Back
""")

        choice = input("Enter choice: ")

        if choice == "1":
            call_setting_menu()
        elif choice == "2":
            phone_settings_menu()
        elif choice == "3":
            Security_settings_menu()
        elif choice == "4":
            print("Restoring factory settings...\n")
        elif choice == "0":
            break
        else:
            print("Invalid option!\n")

def call_setting_menu():
    while True:
        print("""
SETTINGS

1. Automatic redial
2. Speed dialling
3. Call waiting options
4. Own number sending
5. Phone line in use
6. Automatic answer
0. Back
""")

        choice = input("Enter choice: ")

        if choice == "1":
            print("Automatic redial...\n")
        elif choice == "2":
            print("Speed dialling...\n")
        elif choice == "3":
            print("Call waiting options...\n")
        elif choice == "4":
            print("Own number sending...\n")
        elif choice == "5":
            print("Phone line in use...\n")
        elif choice == "6":
            print("Automatic answer...\n")
        elif choice == "0":
            break
        else:
            print("Invalid option!\n")



def phone_settings_menu():
    while True:
        print("""
SETTINGS

1. Language
2. Cell info display
3. Welcome note
4. Network selection
5. Light
6. Confirm SIM service actions
0. Back
""")

        choice = input("Enter choice: ")

        if choice == "1":
            print("Language...\n")
        elif choice == "2":
            print("Cell info display...\n")
        elif choice == "3":
            print("Welcome note...\n")
        elif choice == "4":
            print("Network selection...\n")
        elif choice == "5":
            print("Light...\n")
        elif choice == "6":
            print("Confirm SIM service actions...\n")
        elif choice == "0":
            break
        else:
            print("Invalid option!\n")



def Security_settings_menu():
    while True:
        print("""
SETTINGS

1. Pin code settings
2. Call barring service
3. Fixed dialling
4. Closed user group
5. Phone security
6. Change access codes
0. Back
""")

        choice = input("Enter choice: ")

        if choice == "1":
            print("Pin code settings...\n")
        elif choice == "2":
            print("Call barring service...\n")
        elif choice == "3":
            print("Fixed dialling...\n")
        elif choice == "4":
            print("Closed user group...\n")
        elif choice == "5":
            print("Phone security...\n")
        elif choice == "6":
            print("Change access codes...\n")
        elif choice == "0":
            break
        else:
            print("Invalid option!\n")



# CALL DIVERT MENU

def call_divert_menu():

    while True:
        print("""
CALL DIVERT

1. Divert all voice calls
2. Divert when busy
3. Divert when not answered
4. Divert when phone off
5. Divert all data calls
6. Cancel all diverts
0. Back
""")

        choice = input("Enter choice: ")

        if choice == "0":
            break
        else:
            print("Feature not implemented.\n")


# CLOCK MENU

def clock_menu():
    while True:
        print("""
CLOCK
-----
1. Alarm clock
2. Clock settings
3. Date setting
4. Stopwatch
5. Countdown timer
6. Auto update of date and time
0. Back
""")

        choice = input("Enter choice: ")
        if choice == "1":
            print("Alarm clock...\n")
        elif choice == "2":
            print("Clock settings...\n")
        elif choice == "3":
            print("Date setting...\n")
        elif choice == "4":
            print("Stopwatch...\n")
        elif choice == "5":
            print("Countdown timer...\n")
        elif choice == "6":
            print("Auto update of date and time...\n")
        if choice == "0":
            break
        else:
            print("Feature not implemented.\n")






main_menu()
