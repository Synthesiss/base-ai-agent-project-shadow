# Help command
elif user=="help":
    print("Available commands:")
    print("help - show commands")
    print("exit - close agent")
    print("problem - describe your problem")
    print("show problems - view saved problems")
    print("nft idea - generate NFT idea")
    print("nft traits - generate NFT traits")
    print("nft tweet - generate NFT tweet")

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

# Show problems
elif user=="show problems":

    with open("memory.txt","r") as file:
        print("Saved problems:")
        print(file.read())

# NFT idea
elif user.startswith("nft idea"):

    theme = user.replace("nft idea","").strip()

    if theme == "":
        theme = "Genesis"

    print("Generating NFT idea...")
    print("Collection Name: Shadow "+theme.title())
    print("Concept: A unique NFT collection inspired by", theme)
# NFT traits
elif user.startswith("nft idea"):

    theme = user.replace("nft idea","").strip()

    if theme == "":
        theme = "Genesis"

    print("Generating NFT idea...")
    print("Collection Name: Shadow "+theme.title())
    print("Concept: A unique NFT collection inspired by", theme)
# NFT tweet
elif user.startswith("nft tweet"):

    print("Generating NFT tweet...")

    print("The shadows are rising...")
    print("Something powerful is coming to Base.")
    print("#NFT #Base #Web3")

# Unknown command
else:
    print("Unknown command. Type help.")

start()
