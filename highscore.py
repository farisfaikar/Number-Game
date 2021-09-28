import json


def write_highscore():
    highscore_file = open('highscore.txt', 'w')
    highscore_file.write("You won and this should store the player's name and time\n"
                         "in a list or a dictionary")
    highscore_file.close()


def read_highscore():
    highscore_file = open('highscore.txt', 'r')
    hf = highscore_file.readlines()
    hs_list = []
    for line in hf:
        hs_list.append(line.strip())

    print(hs_list)
