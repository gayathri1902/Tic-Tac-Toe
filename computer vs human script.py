import random

#printing the grid
def PrintGrid(grid):
    ColNum="  "
    for colnum in range(1,4):
        ColNum+=str(colnum)+" "
    print(ColNum)
    for index,row in enumerate(grid):
        RowPrint=""
        print(str(index+1),end=" ")
        for cell in row:
            RowPrint+=str(cell)+"|"
        print(RowPrint)


#input from user
def UserInput(grid):
    while True:
        turn=input("Enter your position (row,col):")
        turn=turn.split(",")
        try:
            Xpos=int(turn[0])
            Ypos=int(turn[1])
        except :
            print("the input should 2 numbers seperated by comma and not a string")
            continue
        if (Xpos>3 or Xpos<1) or (Ypos>3 or Ypos<1):
            print("The input for x and y should be in range [1,3]")
        elif grid[Xpos-1][Ypos-1]!=BLANK:
            print("That position is occupied")
        else:
            grid[Xpos-1][Ypos-1]=CROSS
            break

#checking the winner 
def CheckWinner(grid,xo):
    successGrid=[[[0,0],[0,1],[0,2]],[[1,0],[1,1],[1,2]],[[2,0],[2,1],[2,2]]
                ,[[0,0],[1,0],[2,0]],[[0,1],[1,1],[2,1]],[[0,2],[1,2],[2,2]]
                 ,[[1,1],[2,2],[0,0]],[[0,2],[1,1],[2,0]]]
    
    for element in successGrid:
        returnValue=True
        for win in element:
            if (grid[win[0]][win[1]]== xo and returnValue):
                returnValue=True
            else:
                returnValue=False
                break
        if returnValue==True:
            break
    return returnValue
    
def copyGrid(grid):
    copy = []
    for index,row in enumerate(grid):
        copy.append([])
        for cell in row:
            copy[index].append(cell)
    return copy
    

#computer input
    
def CompTurn(grid):    
    PosMove=[]
    for row in range (3):
        for col in range (3):
            copy=copyGrid(grid)
            if copy[row][col]==BLANK :
                copy[row][col]=ZERO
                if CheckWinner(copy,ZERO):
                    return row,col

    for row in range (3):
        for col in range (3):
            copy=copyGrid(grid)
            if copy[row][col]==BLANK:
                copy[row][col]=CROSS
                if CheckWinner(copy,CROSS):
                    return row,col
    
    for i in range (3):
        for j in range (3):
            if copy[i][j]==BLANK:
                PosMove.append([i,j])
    if len(PosMove)>0:
        move=random.choice(PosMove)
        return move[0],move[1]
    return None
                    
#main
BLANK=" "
ZERO="O"
CROSS="X"
count=0

grid=[[BLANK for row in range (3)] for col in range(3)]
PrintGrid(grid)

while not CheckWinner(grid,CROSS) and not CheckWinner(grid,ZERO):
    if count>=9:
        break
    count+=1
    UserInput(grid)
    PrintGrid(grid)
    if (not CheckWinner(grid,CROSS)) and (CompTurn(grid)!=None):
        print("The computers turn...")
        row,col=CompTurn(grid)
        grid[row][col]=ZERO
        PrintGrid(grid) 
    else:
        break
     
if CheckWinner(grid,CROSS):
    print("you win")
elif CheckWinner(grid,ZERO):
    print("computer wins")
else:
    print("draw")
    
    
        

    
                
                
        


    
    







    
        
    


    
    
    
              
