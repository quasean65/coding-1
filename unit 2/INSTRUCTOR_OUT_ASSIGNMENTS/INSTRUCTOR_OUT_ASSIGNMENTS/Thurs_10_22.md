def vending_machine():
    # Dictionary mapping the item codes to the items
    menu = {
        "B3": "Nacho Chips",
        "G4": "BBQ Chips",
        "G7": "Plain Chips",
        "D3": "Water",
        "G5": "Cola Soda"
    }
    
    print("--- Vending Machine Menu ---")
    print("B3: Nacho Chips")
    print("G4: BBQ Chips")
    print("G7: Plain Chips")
    print("D3: Water")
    print("G5: Cola Soda")
    print("----------------------------")
    
    while True:
        # Prompt the user for an item code or to quit
        user_input = input("Enter a vending machine code (or 'q' to stop): ").strip().upper()
        
        # Check if the user wants to quit
        if user_input == 'Q':
            print("Thank you for using the vending machine. Goodbye!")
            break
            
        # Check if the input is a valid code in the menu
        if user_input in menu:
            print(f"Dispensing: {menu[user_input]}\n")
        else:
            print("Invalid code. Please try again.\n")

# Run the function
if __name__ == "__main__":
    vending_machine()
