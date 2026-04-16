# Help command
elif user=="help":
    print("Available commands:")
    print("help - show commands")
    print("exit - close agent")
    print("problem - describe your problem")
    print("show problems - view saved problems")

# Problem command
elif user.startswith("problem"):

    print("Problem received. Analyzing...")

    problem_text = user.replace("problem","")

    print("Possible solutions:")
    print("Break problem into smaller steps")
    print("Research possible approaches")
    print("Take consistent action")
    print("Track progress daily")
    print("Stay consistent")

    with open("memory.txt","a") as file:
        file.write(problem_text+"\n")

    print("Problem saved to memory")

# Show problems command
elif user=="show problems":

    with open("memory.txt","r") as file:
        print("Saved problems:")
        print(file.read())

# Unknown command
else:
    print("Unknown command. Type help.")
print("Research possible approaches")

print("Take consistent action")

    problem_text = user.replace("problem","")

    print("Possible solutions:")

    print("Break problem into smaller steps")
    print("Research possible approaches")
    print("Take consistent action")
print("Track progress daily")

print("Stay consistent")
with open("memory.txt","a") as file:

    file.write(problem_text+"\n")
    print("Problem saved to memory")

# Unknown command handler
else:
    print("Unknown command. Type help.")
        # Unknown command handler
   elif user.startswith("nft idea"):

    print("Generating NFT project idea...")

    print("Collection Name: Shadow Reapers")
    print("Concept: Dark warriors emerging from the shadow realm")
    print("Theme: Mystery, power, and darkness") 
        else:
            print("Unknown command. Type help.")

# Start agent
start() 
