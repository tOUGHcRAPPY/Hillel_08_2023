team: list[dict] = [
    {"name": "John", "age": 20, "number": 1},
    {"name": "Mark", "age": 33, "number": 3},
    {"name": "Cavin", "age": 17, "number": 12},
]

"""This function should print all players to the client"""
def show_players(players: list[dict]) -> None:
    for player in players:
        print(player)

# show_players(team)

# """This function takes info about the new player from user's input."""
# def new_player_info():
#     new_player = {"name": str, "age": int, "number": int}
#     new_player["name"] = input("Enter new player's name: ")
#     new_player["age"] = int(input("Enter new player's age: "))
#     new_player["number"] = int(input("Enter new player's number: "))
#     print(new_player)
#     return new_player

# new_player_info()


# """This function adds the new player using inputs from 'def new_player_info()'."""
# def add_player():
#     new_player = new_player_info()
#     team.append(new_player)
#     for player in team:
#         print(player)

# add_player()

  
"""This function adds the new player."""
def add_player(num: int, name: str, age: int) -> None:
    new_player = {
        "name": name,
        "age": age,
        "number": num
	}
    team.append(new_player)
    print(f"the new player is {new_player}")
    return new_player

# add_player(num=17, name="Cris", age=31)
# show_players(team)
# print(len(team))


"""This function removes the player by his/her number."""
def remove_player(players: list[dict], num: int) -> None:
    for player in team:
        if player["number"] == num:
            team.remove(player)
            print(f"The removed player is {player}")
    return player

# remove_player(players=team, num=17)
# print(len(team))


def main():
    show_players(team)

    add_player(num=17, name="Cris", age=31)
    add_player(num=17, name="Bob", age=39)
    remove_player(players=team, num=17)

    show_players(team)
    
main()


if __name__ == "__main__":
    main()
else:
    raise SystemExit("This module in only for running")
