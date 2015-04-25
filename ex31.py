print "You enter a dark room with two doors. Do you go through door ! or door #1?"

door = raw_input(">")

if door == "1":
     print "There's a giant bear eating a cheese cake. What do you do?"
     print "1. Take the cake"
     print "2.Scream at the bear."
     
     bear = raw_input(">")
     
     if bear == "1":
        print "The bar eats your facee off. Good job!"
     elif bear == "2":
        print "The bear eats your lef off"
     else:
      print "Well, doing %s is probably better. Bear runs away." % bear
      
elif door == "2":
     print "You stare at the endless abyss at Cthulhu's retina"
     print "1. Blueberries."
     print "2. Yellow jacket clothespins"
     print "3. Understanding revolvers yelling melodies."
     
     insanity = raw_input(">")
     
     if insanity =="1" or insanity == "2":
          print "Your body survives powered by a mind of jello"
     else:
          print "The insanity rots your eyes into a pool of muck"
          
else:
  print " You fall and die"
                  
     