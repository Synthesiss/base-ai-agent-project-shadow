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

print("Collection Name:", collection, theme.title())           
concepts = [
    "A dark futuristic NFT collection",
    "A mysterious Web3 warrior universe",
    "A cyberpunk inspired NFT project",
    "A legendary digital empire"
]

concept = random.choice(concepts)
print("Concept:", concept)

            with open("nft_memory.txt", "a") as file:
                file.write("Shadow " + theme.title() + "\n")

            print("NFT idea saved")

        # NFT traits
        elif eyes = ["glowing", "cyber", "blindfold"]
outfits = ["hoodie", "armor", "robe"]
backgrounds = ["city", "temple", "void"]
auras = ["fire", "shadow", "lightning"]

print("Eyes:", random.choice(eyes))
print("Outfit:", random.choice(outfits))
print("Background:", random.choice(backgrounds))
print("Aura:", random.choice(auras))
rarities = ["Common", "Rare", "Epic", "Legendary"]

print("Rarity:", random.choice(rarities))

        # NFT tweet
elif tweets = [
    "The shadows are rising...",
    "A new legend is coming to Base.",
    "Web3 will never be the same.",
    "The next NFT era begins now."
]

tweet = random.choice(tweets)

print(tweet)
print("#NFT #Base #Web3")

        # NFT metadata
        elif user.startswith("nft metadata"):

            print('{')
print('"name": "Shadow Genesis #1",')
print('"description": "AI generated NFT from Base AI Agent",')
print('"image": "ipfs://image-link",')
print('"attributes": [')
print('{"trait_type": "Eyes", "value": "Cyber"},')
print('{"trait_type": "Aura", "value": "Shadow"}')
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
