import random
def start():

    # Start the AI agent
    print("Base AI Agent Project Shadow active")

    # Version information
    print("AI agent version 0.5")

    # Help instruction
    print("Type help to see commands")

    # Main command loop
    while True:

        # Get user input
        user = input("You: ")

        # Exit command
        if user == "exit":
            break

        # Help command
        elif user == "help":
            print("Available commands:")
            print("help - show commands")
            print("exit - close agent")
            print("problem - describe your problem")
            print("show problems - view saved problems")
            print("nft idea - generate NFT idea")
            print("nft traits - generate NFT traits")
            print("nft tweet - generate NFT tweet")
            print("nft metadata - generate NFT metadata")
            print("show nft ideas - view saved NFT ideas")

        # Problem command
        elif user.startswith("problem"):

            print("Problem received. Analyzing...")

            problem_text = user.replace("problem", "").strip()

            print("Possible solutions:")
            print("Break problem into smaller steps")
            print("Research possible approaches")
            print("Take consistent action")
            print("Track progress daily")
            print("Stay consistent")

            with open("memory.txt", "a") as file:
                file.write(problem_text + "\n")

            print("Problem saved to memory")

        # Show problems
        elif user == "show problems":

            with open("memory.txt", "r") as file:
                print("Saved problems:")
                print(file.read())

        # NFT idea
        elif user.startswith("nft idea"):

            theme = user.replace("nft idea", "").strip()

            if theme == "":
                theme = "Genesis"

            print("Generating NFT idea...")
names = ["Shadow", "Cyber", "Void", "Phantom"]

collection = random.choice(names)

print("Collection Name:", collection, theme.title())            print("Concept: A unique NFT collection inspired by", theme)

            with open("nft_memory.txt", "a") as file:
                file.write("Shadow " + theme.title() + "\n")

            print("NFT idea saved")

        # NFT traits
        elif user.startswith("nft traits"):

            print("Generating NFT traits...")
            print("Eyes: glowing / cyber / blindfold")
            print("Outfit: hoodie / armor / robe")
            print("Background: city / temple / void")
            print("Weapon: sword / staff / none")
            print("Aura: fire / shadow / lightning")

        # NFT tweet
        elif user.startswith("nft tweet"):

            print("The shadows are rising...")
            print("Shadow Genesis is coming to Base.")
            print("Mint soon. Stay ready.")
            print("#NFT #Base #Web3")

        # NFT metadata
        elif user.startswith("nft metadata"):

            print("Generating NFT metadata...")
            print('{')
            print('"name": "Shadow Genesis #1",')
            print('"description": "A unique NFT from the Shadow Genesis collection",')
            print('"image": "ipfs://image-link",')
            print('"attributes": [')
            print('{"trait_type": "Eyes", "value": "Glowing"}')
            print(']')
            print('}')

        # Show NFT ideas
        elif user == "show nft ideas":

            with open("nft_memory.txt", "r") as file:
                print("Saved NFT ideas:")
                print(file.read())

        # Unknown command
        else:
            print("Unknown command. Type help.")


# Start agent
start()
