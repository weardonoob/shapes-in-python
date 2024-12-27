import pgzrun
WIDTH=500
HEIGHT=500
TITLE = "shapes py"

RED = (255,0,0)
BOX = Rect((40,300),(100,50))
alien=Actor("pink alien img")


def draw():
    screen.clear()
    screen.fill("white")
    screen.draw.circle((150,250), 65,(144,120,255))
    screen.draw.filled_circle((315,250),50,(240,12,240))
    screen.draw.rect(BOX,RED)
    screen.draw.filled_rect(BOX,RED)
    #screen.draw.text("Text color", (50, 30), color="orange")
    screen.draw.text("hello",(400,300), color="orange")
    alien.draw()
pgzrun.go()