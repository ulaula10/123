d = 1
a = 1
def setup():
    size(1000,1000)
    
    
    
    

def draw():
    
    global a,d
    
    ellipse(500,500, a,d)
    if keyPressed == True:
        if key == 'd':
            
            d = d + 1
    
    if keyPressed == True:
        if key == 'a':
            a = a + 1
        d = d - 1
        
mouseClicked():
