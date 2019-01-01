# Program 4.4: Program to Demonstrate the Return of Multiple Values from a
# Function Definition


def world_war():
    alliance_world_war = input("Which alliance won World War 2?")
    world_war_end_year = input("When did World War 2 end?")
    return alliance_world_war, world_war_end_year


def main():
    alliance, war_end_year = world_war()
    print(f"The war was won by {alliance} and the war ended in {war_end_year}")


if __name__ == "__main__":
    main()



