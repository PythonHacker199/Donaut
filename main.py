# Hi guys
# Welcome to Hacker  pyt Chohannel
# today we are here to make  food designer in python
# for  that we need vpython package
from vpython import*
canvas(background=color.white)

# first we will make donaut
donaut=ring(radius=0.5,thickness=0.25,color=vector(401,10,1))
choco=ring(radius=0.55,thickness=0.25,color=vector(400,00,0))
rad =0
while True:
    rate(10)
    donaut.pos=vector(3*cos(rad),sin(rad),0)
    choco.pos=vector(3*cos(rad),sin(rad),0)
    rad=rad+0.03
    # Thank you