def start():

    print("Base AI Agent Project Shadow active")
    print("Type help to see commands")

    while True:

        user=input("You: ")

        if user=="exit":
            break

        elif user=="help":
            print("Available commands:")
print("help - show commands")
print("exit - close agent")

        else:
            print("Unknown command")

start()
