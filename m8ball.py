#
# magic 8 ball program for CSI-106
# written by Michael Toth (and everyone else in the class!)

# add your function with your initials behind the name m8ball. For instance,
# my name is Michael Toth, my function is m8ballmt()

# Mediapath should be set here for your machine
mediaPath = "/Users/Kristina/csi106/magic8ball"
setMediaPath(mediaPath)

# FUNCTIONS
# ADD YOUR FUNCTION HERE
# YOU WILL NEED TO CHANGE YOUR PATH FOR THE PICTURE FILE TO USE THE
# SAME ONE AS IN m8ballmt()

def m8ballmt():
  f="magic-8-ball-6.jpg"
  p=makePicture(f)
  s=makeStyle(sansSerif,bold,18)
  addTextWithStyle(p,120,130,"NO",s,white)
  repaint(p)
def m8ballkm():
  f="magic-8-ball-6.jpg"
  p=makePicture(f) 
  s=makeStyle(sansSerif,bold,18) 
  addTextWithStyle(p,115,100,"Yes",s,white) 
  addTextWithStyle(p,85,130,"Definately",s,white) 
  repaint(p)

# END OF FUNCTIONS

# ADD YOUR FUNCTION NAME TO THIS LIST.
# For instance, if your function name is m8ballsw, [m8ballmt] should change
# to [m8ballmt, m8ballsw]
phrases=[m8ballmt, m8ballkm]

import random
sel=random.randint(0,len(phrases)-1)

phrases[sel]()
    
