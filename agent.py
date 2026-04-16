# Help command
elif user=="help":
    print("Available commands:")
    print("help - show commands")
    print("exit - close agent")
    print("problem - describe your problem")
    print("show problems - view saved problems")
print("nft idea - generate NFT project idea")
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

    theme = user.replace("nft idea","")

    print("Generating NFT idea based on theme:", theme)

    print("Collection Name: Shadow "+theme.strip().title())
    print("Concept: A unique NFT collection inspired by", theme)
    print("Theme:", theme) 
elif user.startswith("nft traits"):

    print("Generating NFT traits...")

    print("Traits:")
    print("- Eyes: glowing / cyber / blindfold")
    print("- Outfit: hoodie / armor / robe")
    print("- Background: city / temple / void")
print("- Weapon: sword / staff / none")
print("- Aura: fire / shadow / lightning")
elif user.startswith("nft tweet"):

    print("Generating NFT tweet...")

    print("The shadows are rising...")
    print("Something powerful is coming to Base.")
    print("Stay ready.")
    print("#NFT #Base #Web3")
        else:
            print("Unknown command. Type help.")

# Start agent
start() 
