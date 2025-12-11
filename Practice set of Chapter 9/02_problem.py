import random

def game():
    print("you are playing a game...")
    score = random.randint(1, 100)
    #fetch the hiscore from a file
    with open("hiscore.txt") as f:
        hiscore = f.read()
        if (hiscore!=""):
            hiscore = int(hiscore)
        else:
                hiscore = 0   

    print(f"your score: {score}")

    if(score>hiscore or hiscore==""):
        print("you have the highest score!")

        #write the new hiscore to the file
        with open("hiscore.txt","w") as f:
            f.write(str(score))

    return score

game()

