#!/usr/bin/python

from graphics import *

HEIGHT	= 720
WIDTH	= 1080

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
	l1 = Line(Point(WIDTH * (1/3), 0), Point(WIDTH * (1/3), HEIGHT))
	l2 = Line(Point((WIDTH * (2/3)), 0), Point(WIDTH * (2/3), HEIGHT))
	l3 = Line(Point(0, HEIGHT * (1/3)), Point(WIDTH, HEIGHT * (1/3)))
	l4 = Line(Point(0, HEIGHT * (2/3)), Point(WIDTH, HEIGHT * (2/3)))
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
	l1 = Line(Point(WIDTH * (1/9), 0), Point(WIDTH * (1/9), HEIGHT))
	l2 = Line(Point(WIDTH * (2/9), 0), Point(WIDTH * (2/9), HEIGHT))
	l3 = Line(Point(WIDTH * (4/9), 0), Point(WIDTH * (4/9), HEIGHT))
	l4 = Line(Point(WIDTH * (5/9), 0), Point(WIDTH * (5/9), HEIGHT))
	l5 = Line(Point(WIDTH * (7/9), 0), Point(WIDTH * (7/9), HEIGHT))
	l6 = Line(Point(WIDTH * (8/9), 0), Point(WIDTH * (8/9), HEIGHT))
	l7 = Line(Point(0, HEIGHT * (1/9)), Point(WIDTH, HEIGHT * (1/9)))
	l8 = Line(Point(0, HEIGHT * (2/9)), Point(WIDTH, HEIGHT * (2/9)))
	l9 = Line(Point(0, HEIGHT * (4/9)), Point(WIDTH, HEIGHT * (4/9)))
	l10 = Line(Point(0, HEIGHT * (5/9)), Point(WIDTH, HEIGHT * (5/9)))
	l11 = Line(Point(0, HEIGHT * (7/9)), Point(WIDTH, HEIGHT * (7/9)))
	l12 = Line(Point(0, HEIGHT * (8/9)), Point(WIDTH, HEIGHT * (8/9)))
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
	p1 = Point(((WIDTH * ((n1 % 3)/3)) + (WIDTH * ((n2 % 3)/9))), ((HEIGHT * ((n1 // 3)/3)) + (HEIGHT * ((n2 // 3)/9))))
	p2 = Point(p1.getX() + (WIDTH / 9), p1.getY() + (HEIGHT / 9))
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
	p1 = Point((WIDTH * ((n1 % 3)/3)) + (WIDTH * ((n2 % 3)/9)) + (WIDTH / 18), ((HEIGHT * ((n1 // 3)/3)) + (HEIGHT * ((n2 // 3)/9) + HEIGHT / 18)))
	c = Circle(p1, HEIGHT/ 20)
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
	if len(arrundo) :
		arrundo[-1][0].undraw()
		arrundo[-1][0].setOutline(color)
		arrundo[-1][0].draw(win)
		if arrundo[-1][1] :
			arrundo[-1][1].undraw()
			arrundo[-1][1].setOutline(color)
			arrundo[-1][1].draw(win)

def click_me(win, turn) :
	global last
	a = win.checkMouse()
	if a :
		arrredo.clear()
		x = (((a.getX() / WIDTH) * 3) // 1) + 3 * (((a.getY() / HEIGHT) * 3) // 1)
		y = ((((a.getX() / WIDTH) * 9) // 1) % 3) + 3 * (((((a.getY() / HEIGHT) * 9) // 1)) % 3)
		if bgrid[int(x)][int(y)] is not 3 or (last is not -1 and int(x) is not int(last)) :
			print("ERROR APE")
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
			bgrid[int(x)][int(y)] = turn % 2
			check_square(win, x, turn)
	return (turn)

def check_keys(win, turn) :
	global last
	t = win.checkKey()
	if t :
		if t == 'u' and len(arrundo) > 0:
			zz = arrundo[-1]
			zz[0].undraw()
			if zz[1] is not 0 :
				zz[1].undraw()
			tmp1 = arrundo.pop()
			bgrid[int(arrcoor[-1][0])][int(arrcoor[-1][1])] = 3
			tmp2 = arrcoor.pop()
			last = arrcoor[-1][1]
			arrredo.append(tmp1)
			arrcooa.append(tmp2)
			turn -= 1
			color_last_one(win, 'cyan')
		if t == 'r' and len(arrredo) > 0 :
			zz = arrredo[-1]
			zz[0].draw(win)
			if zz[1] is not 0 :
				zz[1].draw(win)
			tmp1 = arrredo.pop()
			arrundo.append(tmp1)
			bgrid[int(arrcooa[-1][0])][int(arrcooa[-1][1])] = turn % 2
			last = arrcooa[-1][1]
			tmp2 = arrcooa.pop()
			arrcoor.append(tmp2)
			turn += 1
			color_last_one(win, 'cyan')
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
	

def main() :
	won = False
	turn = 1
	win = GraphWin("Super tic tac toe", WIDTH, HEIGHT)
	win.setBackground(color_rgb(29, 72, 81))
	init_sgrid(win)
	init_bgrid(win)
	while won == False :
		turn = click_me(win, turn)
		turn = check_keys(win, turn)
		won = check_map()
	if winner == 0 :
		c = Circle(Point(WIDTH / 2, HEIGHT / 2), HEIGHT - 20)
		c.setOutline('cyan')
		c.setWidth(4)
		c.draw(win)
	else :
		p1 = Point(0, 0)
		p2 = Point(WIDTH, HEIGHT)
		p3 = Point(0, HEIGHT)
		p4 = Point(WIDTH, 0)
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
