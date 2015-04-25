def add(a,b):
     print "Adding %d + %d" % (a,b)
     return a+b
    
def subtract(a,b):
      print "Subtracting %d - %d" % (a,b)
      return a - b
      
      
def multiply(a,b):
      print "Multiplying  %d * %d" % (a,b)
      return a * b
      
      
def divide(a,b):
      print "dividing %d - %d" % (a,b)
      return a / b
      
print "let's do Math with just function:"
     
age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
id = divide(100, 2)

print "Age: %d, height: %d, weight: %d, id %d)" % (age, height, weight, id)
 
print "here is a puzzle"
  
waht = add(age, subtract(height, multiply(weight, divide (id, 2))))
  
print "That becomes :", waht, "Can you do it by hand?"



'''This is a multi-line string. This is the first line.
This is the second line.
"What's your name?," I asked.
He said "Bond, James Bond."
'''
  