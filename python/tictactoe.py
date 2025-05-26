list=[0,1,2,3,4,5,6,7,8]
def grid():
    print(" ",list[0]," | ",list[1]," | ",list[2]," ")
    print("-----------------")
    print(" ",list[3]," | ",list[4]," | ",list[5]," ")
    print("-----------------")
    print(" ",list[6]," | ",list[7]," | ",list[8]," ")
grid()
def play():
    for i in range(5):
        playerX=input("player X choose position(1 to 9) first: ")
        #print(playerX)
        list[int(playerX)-1]="X"
        grid()
        if(i==5):
            break
        playerO=input("player O choose position: ")
        #print(playerX)
        list[int(playerO)-1]="O"
        grid()
play()

