from graphics import *

HEIGHT  = 720
WIDTH   = 1080

def get_names() :
    win = GraphWin("START", WIDTH / 2, HEIGHT / 2)
    win.setBackground(color_rgb(29, 72, 81))
    label = Text(Point((WIDTH / 2) * 0.5, (HEIGHT / 2) * 0.1), "PLAYERS :")
    label.setFace('helvetica')
    label.setSize(20)
    label.draw(win)
    text1 = Entry(Point((WIDTH / 2) * 0.5, (HEIGHT / 2) * 0.2), 20)
    text1.draw(win)
    text2 = Entry(Point((WIDTH / 2) * 0.5, (HEIGHT / 2) * 0.3), 20)
    text2.draw(win)
    win.getMouse()
    players = [0, 0]
    players[0] = text1.getText()
    players[1] = text2.getText()
    win.close()
    return (players)
