# arcanoid
bx=250
by=500
bxs=0
bys=-0
rx=260
ry=580
rx2=123
ry2=234
rx3=466
ry3=234
rx4=533
ry4=142
rx5=134
ry5=134
rx6=389
ry6=398
rx7=156
ry7=188
rx8=222
ry8=222
rx9=333
ry9=333
rx0=444
ry0=444
def setup():
    size(600,600)
def draw():
    global bx,by,bxs,bys,rx,ry,rx2,ry2,rx3,ry3,rx4,ry4,rx5,ry5,rx6,ry6,rx7,ry7,rx8,ry8,rx9,ry9,rx0,ry0
    rect(10,10,580,590)
    rect(rx,ry,70,10)
    ellipse(bx,by,10,10)
    rect(rx2,ry2,30,30)
    rect(rx3,ry3,30,30)
    rect(rx4,ry4,30,30)
    rect(rx5,ry5,30,30)
    rect(rx6,ry6,30,30)
    rect(rx7,ry7,30,30)
    rect(rx8,ry8,30,30)
    rect(rx9,ry9,30,30)
    rect(rx0,ry0,30,30)
    bx+=bxs
    by+=bys
    if keyPressed:
        if key == 'p':
            bxs=-2
            bys=2
        if key == 'd' and rx+70<=589:
            rx=rx+2
        if key == 'a' and rx>=11:
            rx=rx-2
    if bx<=rx+70 and by<=ry+10 and bx>=rx and by>=ry:
        bys=-bys
    if bx<=rx2+30 and by<=ry2+30 and bx>=rx2 and by>=ry2:
        bys=-bys
        rx2=999
        ry2=999
    if bx<=rx3+30 and by<=ry3+30 and bx>=rx3 and by>=ry3:
        bys=-bys
        rx3=999
        ry3=999
    if bx<=rx4+30 and by<=ry4+30 and bx>=rx4 and by>=ry4:
        bys=-bys
        rx4=999
        ry4=999  
    if bx>=rx5+30 and by>=ry5+30 and bx<=rx5 and by<=ry5:
        bys=-bys
        rx5=999
        ry5=999 
    if bx>=rx6+30 and by>=ry6+30 and bx<=rx6 and by<=ry6:
        bys=-bys
        rx6=999
        ry6=999      
    if bx<=rx7+30 and by<=ry7+30 and bx>=rx7 and by>=ry7:
        bys=-bys
        rx7=999
        ry7=999      
    if bx<=rx8+30 and by<=ry8+30 and bx>=rx8 and by>=ry8:
        bys=-bys
        rx8=999
        ry8=999      
    if bx<=rx9+30 and by<=ry9+30 and bx>=rx9 and by>=ry9:
        bys=-bys
        rx9=999
        ry9=999      
    if bx<=rx0+30 and by<=ry0+30 and bx>=rx0 and by>=ry0:
        bys=-bys
        rx0=999
        ry0=999                                          
    if bx<=16:
        bxs=-bxs
    if by<=16:
        bys=-bys  
    if bx>=584:
        bxs=-bxs      
    if by>=590:
        bys=0
        bxs=0
        bx=250
        by=500    
