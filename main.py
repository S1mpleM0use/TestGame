from MainCharacter import MainCharacter

char = MainCharacter(name = input("Your name: "), age = int(input("Your age: ")), height = int(input("Your height: ")))

print('The night today feels oddly special. Why not go out for a walk? It should be fine\n')

print('Go for a walk? Y | N')
match input():
    case 'Y':
        print("You're tired of sitting in one place all day, so you get up and go out the door\n\n")
        Walk = 1
    case 'N':
        print("It's cold outside, so why bother? It's better to play some Minecraft anyway\n\n")
        Walk = 0


match Walk:
    case 1:
        print("""It's quite chilly outside, but the stars shine exquisitely 
        and the moon's light engulfs the sleeping town.""")
        print("You start walking, but then a particular shadow caught your attention.")
        print('Investigate? Y | N')
        match input():
            case "Y":
                Shadow = 1
            case 'N':
                Shadow = 0
    case 0:
        print("Without any further thought, you start up the world you've been playing for over a\
        year already. You've got to mine some stone to finish the megabase, automate some farms and all.")
        print("""Then, without any warnings, your PC shuts down. You notice, that it's not only your PC,
              but all electricity in the house.""")
        print("Do you want to check the electrical panel? Y | N")
        match input():
            case "Y":
                Check_Electricity = 1
            case 'N':
                Check_Electricity = 0
