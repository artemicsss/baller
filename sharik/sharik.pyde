sizeEllipse=900
def setup():
    size(600,400)
def draw():
    global sizeEllipse
    translate(300,200)
    ellipse(0,0,sizeEllipse,sizeEllipse)
    sizeEllipse=sizeEllipse -1
    if sizeEllipse==0:
        noLoop()
        
