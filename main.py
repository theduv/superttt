#!/usr/bin/python

from graphics import *

HEIGHT	= 720
WIDTH	= 1080

SHEIGHT	= HEIGHT * 0.8
SWIDTH	= WIDTH * 0.8

wflag = 0
last = 4
winner = 3

arrundo = []
arrredo = []
arrcoor	= []
arrcooa	= []
arrcheck = [3, 3, 3, 3, 3, 3, 3, 3, 3]

sgrid0 = [3, 3, 3, 3, 3, 3, 3, 3, 3]
sgrid1 = [3, 3, 3, 3, 3, 3, 3, 3, 3]
sgrid2 = [3, 3, 3, 3, 3, 3, 3, 3, 3]
sgrid3 = [3, 3, 3, 3, 3, 3, 3, 3, 3]
sgrid4 = [3, 3, 3, 3, 3, 3, 3, 3, 3]
sgrid5 = [3, 3, 3, 3, 3, 3, 3, 3, 3]
sgrid6 = [3, 3, 3, 3, 3, 3, 3, 3, 3]
sgrid7 = [3, 3, 3, 3, 3, 3, 3, 3, 3]
sgrid8 = [3, 3, 3, 3, 3, 3, 3, 3, 3]
bgrid = [sgrid0, sgrid1, sgrid2, sgrid3, sgrid4, sgrid5, sgrid6, sgrid7, sgrid8]


def init_bgrid(win) :
    l1 = Line(Point(SWIDTH * (1/3), 0), Point(SWIDTH * (1/3), SHEIGHT))
    l2 = Line(Point((SWIDTH * (2/3)), 0), Point(SWIDTH * (2/3), SHEIGHT))
    l3 = Line(Point(0, SHEIGHT * (1/3)), Point(SWIDTH, SHEIGHT * (1/3)))
    l4 = Line(Point(0, SHEIGHT * (2/3)), Point(SWIDTH, SHEIGHT * (2/3)))
    l1.setFill('white')
    l1.setWidth(4)
    l2.setFill('white')
    l2.setWidth(4)
    l3.setFill('white')
    l3.setWidth(4)
    l4.setFill('white')
    l4.setWidth(4)
    l1.draw(win)
    l2.draw(win)
    l3.draw(win)
    l4.draw(win)

def init_sgrid(win) :
    l1 = Line(Point(SWIDTH * (1/9), 0), Point(SWIDTH * (1/9), SHEIGHT))
    l2 = Line(Point(SWIDTH * (2/9), 0), Point(SWIDTH * (2/9), SHEIGHT))
    l3 = Line(Point(SWIDTH * (4/9), 0), Point(SWIDTH * (4/9), SHEIGHT))
    l4 = Line(Point(SWIDTH * (5/9), 0), Point(SWIDTH * (5/9), SHEIGHT))
    l5 = Line(Point(SWIDTH * (7/9), 0), Point(SWIDTH * (7/9), SHEIGHT))
    l6 = Line(Point(SWIDTH * (8/9), 0), Point(SWIDTH * (8/9), SHEIGHT))
    l7 = Line(Point(0, SHEIGHT * (1/9)), Point(SWIDTH, SHEIGHT * (1/9)))
    l8 = Line(Point(0, SHEIGHT * (2/9)), Point(SWIDTH, SHEIGHT * (2/9)))
    l9 = Line(Point(0, SHEIGHT * (4/9)), Point(SWIDTH, SHEIGHT * (4/9)))
    l10 = Line(Point(0, SHEIGHT * (5/9)), Point(SWIDTH, SHEIGHT * (5/9)))
    l11 = Line(Point(0, SHEIGHT * (7/9)), Point(SWIDTH, SHEIGHT * (7/9)))
    l12 = Line(Point(0, SHEIGHT * (8/9)), Point(SWIDTH, SHEIGHT * (8/9)))
    l1.setFill('white')
    l2.setFill('white')
    l3.setFill('white')
    l4.setFill('white')
    l5.setFill('white')
    l6.setFill('white')
    l7.setFill('white')
    l8.setFill('white')
    l9.setFill('white')
    l10.setFill('white')
    l11.setFill('white')
    l12.setFill('white')
    l1.draw(win)
    l2.draw(win)
    l3.draw(win)
    l4.draw(win)
    l5.draw(win)
    l6.draw(win)
    l7.draw(win)
    l8.draw(win)
    l9.draw(win)
    l10.draw(win)
    l11.draw(win)
    l12.draw(win)

def	draw_cross(win, n1, n2, color) :
    p1 = Point(((SWIDTH * ((n1 % 3)/3)) + (SWIDTH * ((n2 % 3)/9))), ((SHEIGHT * ((n1 // 3)/3)) + (SHEIGHT * ((n2 // 3)/9))))
    p2 = Point(p1.getX() + (SWIDTH / 9), p1.getY() + (SHEIGHT / 9))
    p3 = Point(p2.getX(), p1.getY())
    p4 = Point(p1.getX(), p2.getY())
    l1 = Line(p1, p2)
    l2 = Line(p3, p4)
    l1.setFill(color)
    l2.setFill(color)
    l1.draw(win)
    l2.draw(win)
    und = [0, 0]
    und[0] = l1
    und[1] = l2
    arrundo.append(und)
    arrcoor.append([n1, n2])

def draw_circle(win, n1, n2, color) :
    p1 = Point((SWIDTH * ((n1 % 3)/3)) + (SWIDTH * ((n2 % 3)/9)) + (SWIDTH / 18), ((SHEIGHT * ((n1 // 3)/3)) + (SHEIGHT * ((n2 // 3)/9) + SHEIGHT / 18)))
    c = Circle(p1, SHEIGHT/ 20)
    c.setOutline(color)
    c.draw(win)
    und = [0, 0]
    und[0] = c
    und[1] = 0
    arrundo.append(und)
    arrcoor.append([n1, n2])

def draw_something(win, n1, n2, turn, color) :
    if turn % 2 :
        draw_circle(win, n1, n2, color)
    else :
        draw_cross(win, n1, n2, color)

def draw_them(win, turn, a, b, c, d) :
    arrcheck[int(a)] = turn % 2
    global wflag
    wflag = 1
    draw_something(win, a, b, turn, 'green2')
    draw_something(win, a, c, turn, 'green2')
    draw_something(win, a, d, turn, 'green2')

def check_square(win, x, turn) :
    if arrcheck[int(x)] is not 3 :
        return ()
    square = bgrid[int(x)]
    if square[0] == square[1] and square[1] == square[2] and square[0] is not 3 :
        draw_them(win, turn, x, 0, 1, 2)
    elif square[2] == square[5] and square[5] == square[8] and square[2] is not 3 :
        draw_them(win, turn, x, 2, 5, 8)
    elif square[6] == square[7] and square[7] == square[8] and square[6] is not 3 :
        draw_them(win, turn, x, 6, 7, 8)
    elif square[0] == square[3] and square[3] == square[6] and square[0] is not 3 :
        draw_them(win, turn, x, 0, 3, 6)
    elif square[0] == square[4] and square[4] == square[8] and square[0] is not 3 :
        draw_them(win, turn, x, 0, 4, 8)
    elif square[2] == square[4] and square[4] == square[6] and square[2] is not 3 :
        draw_them(win, turn, x, 2, 4, 6)
    elif square[1] == square[4] and square[4] == square[7] and square[1] is not 3 :
        draw_them(win, turn, x, 1, 4, 7)
    elif square[3] == square[4] and square[4] == square[5] and square[3] is not 3 :
        draw_them(win, turn, x, 3, 4, 5)

def color_last_one(win, color) :
    if len(arrundo) and wflag == 0 :
        arrundo[-1][0].undraw()
        arrundo[-1][0].setOutline(color)
        arrundo[-1][0].setWidth(2)
        arrundo[-1][0].draw(win)
        if arrundo[-1][1] :
            arrundo[-1][1].undraw()
            arrundo[-1][1].setOutline(color)
            arrundo[-1][1].setWidth(2)
            arrundo[-1][1].draw(win)

def click_me(win, turn) :
    global last
    global wflag
    a = win.checkMouse()
    if a :
        arrredo.clear()
        x = (((a.getX() / SWIDTH) * 3) // 1) + 3 * (((a.getY() / SHEIGHT) * 3) // 1)
        y = ((((a.getX() / SWIDTH) * 9) // 1) % 3) + 3 * (((((a.getY() / SHEIGHT) * 9) // 1)) % 3)
        if bgrid[int(x)][int(y)] is not 3 or (last is not -1 and int(x) is not int(last)) :
            print("ERROR")
            print(x, last)
        else :
            last = y
            if turn % 2 :
                color_last_one(win, 'black')
                draw_cross(win, x, y, 'cyan')
            else :
                color_last_one(win, 'black')
                draw_circle(win, x, y, 'cyan')
            turn += 1
            wflag = 0
            bgrid[int(x)][int(y)] = turn % 2
            check_square(win, x, turn)
    return (turn)

def fun_undo (win, turn) :
    zz = arrundo[-1]
    zz[0].undraw()
    if zz[1] is not 0 :
        zz[1].undraw()
    tmp1 = arrundo.pop()
    if len(arrcoor) :
        bgrid[int(arrcoor[-1][0])][int(arrcoor[-1][1])] = 3
    tmp2 = arrcoor.pop()
    arrredo.append(tmp1)
    arrcooa.append(tmp2)
    if len(arrcoor) :
        last = arrcoor[-1][1]
    turn -= 1
    return (turn)

def fun_redo(win, turn) :
    zz = arrredo[-1]
    zz[0].draw(win)
    if zz[1] is not 0 :
        zz[1].draw(win)
    color_last_one(win, 'black')
    tmp1 = arrredo.pop()
    arrundo.append(tmp1)
    bgrid[int(arrcooa[-1][0])][int(arrcooa[-1][1])] = turn % 2
    tmp2 = arrcooa.pop()
    arrcoor.append(tmp2)
    last = arrcoor[-1][1]
    turn += 1
    color_last_one(win, 'cyan')
    return (turn)

def check_keys(win, turn) :
    global last
    t = win.checkKey()
    if t :
        if t == 'u' and len(arrundo) :
            turn = fun_undo(win, turn)
        if t == 'r' and len(arrredo) :
            turn = fun_redo(win, turn)
        if t == 'p' :
            print(bgrid)
        if t == 'q' :
            win.close()
            exit (0)
    return (turn)

def check_map() :
    global winner
    if arrcheck[0] == arrcheck[1] and arrcheck[1] == arrcheck[2] and arrcheck[0] is not 3 :
        winner = arrcheck[0]
    elif arrcheck[2] == arrcheck[5] and arrcheck[5] == arrcheck[8] and arrcheck[2] is not 3 :
        winner = arrcheck[2]
    elif arrcheck[6] == arrcheck[7] and arrcheck[7] == arrcheck[8] and arrcheck[6] is not 3 :
        winner = arrcheck[6]
    elif arrcheck[0] == arrcheck[3] and arrcheck[3] == arrcheck[6] and arrcheck[0] is not 3 :
        winner = arrcheck[0]
    elif arrcheck[0] == arrcheck[4] and arrcheck[4] == arrcheck[8] and arrcheck[0] is not 3 :
        winner = arrcheck[0]
    elif arrcheck[2] == arrcheck[4] and arrcheck[4] == arrcheck[6] and arrcheck[2] is not 3 :
        winner = arrcheck[2]
    elif arrcheck[1] == arrcheck[4] and arrcheck[4] == arrcheck[7] and arrcheck[1] is not 3 :
        winner = arrcheck[1]
    elif arrcheck[3] == arrcheck[4] and arrcheck[4] == arrcheck[5] and arrcheck[3] is not 3 :
        winner = arrcheck[3]
    if winner is not 3 :
        return (True)
    return (False)


def color_cursquare(win, sq, color) :
    p1 = Point(((sq % 3) * (1/3) * SWIDTH), ((sq // 3) * (1/3) * SHEIGHT))
    p2 = Point(p1.getX() + SWIDTH / 3, p1.getY() + SHEIGHT / 3)
    r = Rectangle(p1, p2)
    r.setOutline(color)
    r.setWidth(4)
    r.draw(win)

def get_names() :
    win = GraphWin("START", WIDTH / 2, HEIGHT / 2)
    win.setBackground(color_rgb(29, 72, 81))
    label = Text(Point((WIDTH / 2) * 0.2, (HEIGHT / 2) * 0.1), "Player names :")
    label.setStyle('italic')
    label.setSize(10)
    label.draw(win)
    text1 = Entry(Point((WIDTH / 2) * 0.2, (HEIGHT / 2) * 0.2), 20)
    text1.draw(win)
    text2 = Entry(Point((WIDTH / 2) * 0.2, (HEIGHT / 2) * 0.3), 20)
    text2.draw(win)
    win.getMouse()
    players = [0, 0]
    players[0] = text1.getText()
    players[1] = text2.getText()
    print(players)
    win.close()

def main() :
    get_names()
    won = False
    turn = 1
    win = GraphWin("STTT", WIDTH, HEIGHT)
    win.setBackground(color_rgb(29, 72, 81))
    init_sgrid(win)
    init_bgrid(win)
    color_cursquare(win, last, 'blue')
    while won == False :
        tmp = last
        turn = click_me(win, turn)
        turn = check_keys(win, turn)
        won = check_map()
        if tmp is not last :
            color_cursquare(win, tmp, 'white')
            color_cursquare(win, last, 'blue')
    if winner % 2 :
        c = Circle(Point(SWIDTH / 2, SHEIGHT / 2), SHEIGHT - 20)
        c.setOutline('cyan')
        c.setWidth(4)
        c.draw(win)
    else :
        p1 = Point(0, 0)
        p2 = Point(SWIDTH, SHEIGHT)
        p3 = Point(0, SHEIGHT)
        p4 = Point(SWIDTH, 0)
        l1 = Line(p1, p2)
        l2 = Line(p3, p4)
        l1.setOutline('cyan')
        l2.setOutline('cyan')
        l1.setWidth(4)
        l2.setWidth(4)
        l1.draw(win)
        l2.draw(win)
    while 1 :
        if win.checkKey() == 'q' :
            win.close()

main()
