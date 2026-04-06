def start():

    # Start the AI agent
    print("Base AI Agent Project Shadow active")

    # Version information
print("AI agent version 0.2")
    # Help instruction
    print("Type help to see commands")

    # Main command loop
    while True:

        # Get user input
        user=input("You: ")

        # Exit command
        if user=="exit":
            break

    
        # Help command
elif user=="help":
    print("Available commands:")
    print("help - show commands")
    print("exit - close agent")
    print("problem - describe your problem")

# Problem command
elif user.startswith("problem"):

    print("Problem received. Analyzing...")

    problem_text = user.replace("problem","")

    print("Possible solutions:")

    print("Break problem into smaller steps")
    print("Research possible approaches")
    print("Take consistent action")

# Unknown command handler
else:
    print("Unknown command. Type help.")
        # Unknown command handler
        else:
            print("Unknown command. Type help.")

# Start agent
start() 
help
exit
problem
show problems
