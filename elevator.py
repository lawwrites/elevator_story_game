import time as t

def pause_message(message, wait_time):
    print(message)
    t.sleep(wait_time)

def intro():
    pause_message("You have just arrived at your new job!")
    pause_message("You are in the elevator.")

def choose_floor(prompt, option1, option2, option3):
    response = input(prompt)
    while True:
        if option1 in response:
            return response
            break
        elif option2 in response:
            return response
            break
        elif option3 in response:
            return response
            break
        else:
            pause_message(f"You selected {response}. That selection is not possible")
            


def get_choice():
    choice = choose_floor("Please enter the number for the floor you would like to visit:\n" 
                     "1. Lobby, " "2. Human resources, " "3. Engineering department ",
                     "1", "2", "3")
    rooms = {
        "1": "Lobby",
        "2": "Human resources",
        "3": "Engineering room"
        }
    room = rooms[choice]
    
    if choice == "1" or choice == "2" or choice == "3":  
            pause_message(f"You pushed the button for floor {choice}.", 1)
            pause_message(f"After a few moments, you find yourself in the {room}.", 1)

def choose_again():
    choose_next= choose_floor("Where would you like to go next? " +
                              "Please enter the number for the floor you would like to visit:",
                               "1. Lobby", "2. Human resources", "3. Engineering department")
    get_choice() 

def run():
    intro()
    get_choice()
    choose_again()

run()