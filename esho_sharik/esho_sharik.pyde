x=0
def setup():
    size(600,600)
def draw():
    global x
    background(0)
    translate(300,300)
    ellipse(0,0,x,x)
    x=x +1
    if x==400:
        x=0
