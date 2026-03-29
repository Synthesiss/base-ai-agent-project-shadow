def start():

    # Start the AI agent
    print("Base AI Agent Project Shadow active")

    # Version information
    print("AI agent version 0.1")

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

        # Unknown command handler
        else:
            print("Unknown command. Type help.")

# Start agent
start() 
