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

def m8ballkp():
  f = "game_8ball_big.jpg"
  p=makePicture(f)
  s=makeStyle(sansSerif,bold,14)
  addTextWithStyle(p,173,140,"MY",s,white)
  addTextWithStyle(p,155,160,"SOURCES",s,white)
  addTextWithStyle(p,175,180,"SAY",s,white)
  addTextWithStyle(p,183,194,"NO",s,white)
  repaint(p)

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
  addTextWithStyle(p,85,130,"Definitely",s,white) 
  repaint(p)

# END OF FUNCTIONS

# ADD YOUR FUNCTION NAME TO THIS LIST.
# For instance, if your function name is m8ballsw, [m8ballmt] should change
# to [m8ballmt, m8ballsw]
<<<<<<< HEAD

phrases=[m8ballmt, m8ballkp]
=======
phrases=[m8ballmt, m8ballkm]
>>>>>>> a518cd7654681fba9daf80b85b9205f77f73f724

import random
sel=random.randint(0,len(phrases)-1)

phrases[sel]()
    
