x=0
def setup():
    size(600,600)
def draw():
    global x
    fill(x,255,255)
    rect(300,300,x,x)
    x=x+1
    if x==230:
        x=0 
