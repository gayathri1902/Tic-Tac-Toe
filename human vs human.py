import pygame as pg,sys
from pygame.locals import *
import time

pg.init()

#global_variables
winner= None
draw1=False
xo='X'
TTT=[[None]*3,[None]*3,[None]*3]
width=501
breath=501
clock=pg.time.Clock()


# TicTacToe_board:
background_color=(255,255,255)
line_color=(0,0,0)

screen= pg.display.set_mode((501,600))
screen.fill(background_color)

pg.draw.line(screen,line_color,(167,0),(167, 501),7)
pg.draw.line(screen,line_color,(334,0),(334, 501),7)
pg.draw.line(screen,line_color,(0,167),(501, 167),7)
pg.draw.line(screen,line_color,(0,334),(501, 334),7)
pg.draw.line(screen,line_color,(0,0),(501,0),7)
pg.draw.line(screen,line_color,(0,501),(501,501),7)
pg.draw.line(screen,line_color,(0,0),(0,501),7)
pg.draw.line(screen,line_color,(501,501),(501,0),7)

pg.display.update()
time.sleep(2)

# x_and_o
x_image=pg.image.load("x.png")
o_image=pg.image.load("o.png")

x_image=pg.transform.scale(x_image,(165,165))
o_image=pg.transform.scale(o_image,(165,165))



#Draw_x_and_o
def draw(row,col):
    global TTT,xo
    if col==1:
        x_pos=0
    if col==2:
        x_pos=168
    if col==3:
        x_pos=335

    if row==1:
        y_pos=0
    if row==2:
        y_pos=168
    if row==3:
        y_pos=335

    TTT[row-1][col-1]= xo

    if xo=='X':
        screen.blit(x_image,(x_pos,y_pos))
        xo='O'
        pg.display.update()
        
    else:
        screen.blit(o_image,(x_pos,y_pos))
        xo='X'
        pg.display.update()



#mouse_click
def mouse_click():
    global xo
    if pg.mouse.get_pressed() :
        x,y=pg.mouse.get_pos()

    #column of mouse click
    if x<167:
        col=1
    elif 167<x<334:
        col=2
    elif x>334:
        col=3
    else:
        col=None

    #row of mouse click
    if y<167:
        row=1
    elif 167<y<334:
        row=2
    elif y>334:
        row=3
    else:
        row=None
        
    print(row,col)  
    if(row is not None  and col is not None and TTT[row-1][col-1] is None):
        #draw the x or o on screen
        draw(row,col)
        check_winner()



#draw_status #message 

def draw_status():
    global draw1,winner
    font = pg.font.Font('freesansbold.ttf', 35)
    if winner==None and draw1==False:
        message= xo.upper()+"'s turn"
    elif draw1==True:
        message= "game draw"
    else:
        message= winner+" has won"
    
    text = font.render(message, True, (0,0,0),(255,255,255))
    textRect = text.get_rect()  
    textRect.center = (250,550)
    screen.blit(text, textRect)
    pg.display.flip()

#check_win

def check_winner():
    global TTT,winner,draw1
    #check row
    for row in range (0,3):
        if(TTT[row][0]== TTT[row][1]==TTT[row][2] and TTT[row][0]!=None and winner==None):
            winner=TTT[row][0]
            if row==0:
                pg.draw.line(screen,(255,0,0),(0,83),(501,83),4)
            if row==1:
                pg.draw.line(screen,(255,0,0),(0,250),(501,250),4)
            if row==2:
                pg.draw.line(screen,(255,0,0),(0,417),(501,417),4)
                
            break
    #check column
    for col in range(0,3):
        if(TTT[0][col]== TTT[1][col]==TTT[2][col] and TTT[0][col]!=None and winner==None):
            winner=TTT[0][col]
            if col==0:
                pg.draw.line(screen,(255,0,0),(83,0),(83,501),4)
            if col==1:
                pg.draw.line(screen,(255,0,0),(250,0),(250,501),4)
            if col==2:
                pg.draw.line(screen,(255,0,0),(417,0),(417,501),4)
            break

    #check diagonal
    if (TTT[0][0]==TTT[1][1]==TTT[2][2]) and (TTT[0][0]!=None and winner==None):
        winner=TTT[0][0]
        pg.draw.line(screen,(255,0,0),(501,501),(0,0),4)
    if (TTT[0][2]==TTT[1][1]==TTT[2][0]) and (TTT[2][0]!= None and winner==None):
        winner=TTT[0][2]
        pg.draw.line(screen,(255,0,0),(0,501),(501,0),4)
        
    #draw
    if all(all(row) for row in TTT) and winner==None:
        draw1=True
        draw_status()
        

#reset_game
def reset_game():
    #global draw1,winner,TTT
    draw1=False
    xo='X'
    TTT=[[None]*3,[None]*3,[None]*3]
    winner=None


#Main_code
running=True
while running:
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            sys.exit()
        elif event.type is MOUSEBUTTONDOWN and winner==None and draw1==False:
            # the user clicked; place an X or O
            mouse_click()
            draw_status()
        if(winner is not None or draw1==True):
            reset_game()
            pg.display.update()
            clock.tick(30)


def drawBox():
    Square_Size=10
    XO_Depth=3

    for i in range(0,XO_Depth):
        for j in range ( 0, XO_depth):
            w.add(canvas())


        



 
