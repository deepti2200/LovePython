#number = 23
#running = True

#while running:
  #guess =int(raw_input("Enter an integer"))
  
#if guess == number:
 # print "Congrats"

#running = False

#elif guess < number:
  
 # print "Little higher"
  
# else:
  #print "Little lower"
   
   
i = 0
numbers = []

while i<6:
      print "At the top i is %d" % i
      numbers.append(i)
      
      i = i + 1
      print "Numbers now: ", numbers
      print "At the bottom i is %d" % i
      
print "The numbers"

for num in numbers:
     print num
         