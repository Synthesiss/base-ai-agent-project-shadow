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
    print("nft metadata - generate NFT metadata")
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
        print("NFT idea saved")

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
with open("nft_memory.txt","a") as file:
    file.write("Shadow "+theme.title()+"\n")# NFT traits
elif user.startswith("nft traits"):

    print("Generating NFT traits...")

    print("Eyes: glowing / cyber / blindfold")
    print("Outfit: hoodie / armor / robe")
    print("Background: city / temple / void")
    print("Weapon: sword / staff / none")
    print("Aura: fire / shadow / lightning")
# NFT tweet
elif user.startswith("nft tweet"):

    print("Generating NFT tweet...")

    print("The shadows are rising...")
    print("Something powerful is coming to Base.")
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
elif user=="show nft ideas":

    with open("nft_memory.txt","r") as file:
        print("Saved NFT ideas:")
        print(file.read())
# Unknown command
else:
    print("Unknown command. Type help.")

start()
