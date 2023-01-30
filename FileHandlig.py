with open("demofile3.txt", "w") as f:
    f.writelines(["\nSee you soon!", "\nOver and out."])

with open("demofile3.txt", "r") as f:
    print(f.read())
    print(f.fileno(),f.name,f.tell(),f.mode)