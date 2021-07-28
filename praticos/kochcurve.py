def koch(n):
    if n == 0:
        return 'F'
    tmp = koch(n-1)
    return tmp + 'L' + tmp + 'R' + tmp + 'L' + tmp
#return koch(n-1) + 'L' + koch(n-1) + 'R' + koch(n-1) + 'L' + koch(n-1)
from turtle import Screen,Turtle
def drawKoch(n):
    s = Screen()
    t = Turtle()
    directions = koch(n)
    for move in directions:
        if move == 'F':
            t.forward(300/3**n) #https://integrada.minhabiblioteca.com.br/#/books/9788521630937/epubcfi/6/38%5B%3Bvnd.vst.idref%3Dchapter10%5D!/4/302/2/4/30/2/2/2%400:0
        if move == 'L':
            t.lt(60)
        if move == 'R':
            t.rt(120)
    s.bye()