ten_things = "Apples oranges crows telephone light sugar"

print "wait there are not 10 things in that list. Let's fix that."

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
       next_one = more_stuff.pop()
       print "Adding: ", next_one
       stuff.append(next_one)
       print "There are %d items now." % len(stuff)
       
print "there we go: ", stuff
    
print "Let's do some things with stuff."

print stuff[1]
print stuff[-1]
print stuff.pop()
print ' '.join(stuff)
print '#'.join(stuff[3:5])    



number = 23
guess = int(raw_input('Enter an integer : '))
if guess == number:
 # New block starts here
 print 'Congratulations, you guessed it.'
 print '(but you do not win any prizes!)'
 # New block ends here
elif guess < number:
 # Another block
 print 'No, it is a little higher than that'
 # You can do whatever you want in a block ...
else:
 print 'No, it is a little lower than that'
 # you must have guessed > number to reach here
print 'Done'
# This last statement is always executed,
# after the if statement is executed.








# This is the list data structure
shoplist = ['apple','mango','carrot','banana']

print "I have", len(shoplist), "items to purchase"

print "these items are:",
for item in shoplist:
  print item,

print "\nI also have to buy rice"
shoplist.append("rice")
print "My shopping list is now", shoplist

print "I will sort my list now"
shoplist.sort()
print "Sorted shopping list is", shoplist

print "The first item I will buy is", shoplist[0]
olditem = shoplist [0]
del shoplist[0]

print "I bought the", olditem
print "My shopping list is now", shoplist


# This is the tuple data structure

zoo = ("python", "elephant", "penguine")
print "Number of animals in teh zoo is", len(zoo)

new_zoo = "monkey", "camel", zoo
print "Number of cages in the new zoo is", len(new_zoo)
print "All animals in new zoo are:", new_zoo
print "Animals brought from old zoo are", new_zoo[2]
print "Last animal brought from old zoo is", new_zoo[2][2]
print "Number of animals in the new zoo is", len(new_zoo) -1+len(new_zoo[2])


# This is the dictionary data structure

#ab is short for address book

ab ={ "Deepti": "deeptisharma1002@gmail.com",
	  "wagner":"waglubin@gmail.com",
	  "padma": "padma@gmail.com",
	  'Matsumoto' : 'matz@ruby-lang.org',
 'Spammer' : 'spammer@hotmail.com' 
	  }
print "Deepti's address is", ab["Deepti"]
	  
del ab["Spammer"]

print "there are %r contacts in address book" % (len(ab))

for name, address in ab.items():
   print "Contact %r at address %r" % (name, address)
 
ab["Guido"] = "guido@python.org"


#This the sequence data structure

shoplist =[ "apple", "mango", "carrot", "banana"]
name = "Deepti"

print "Item 0 is", shoplist[0]
print "Item 1 is", shoplist[1]
print "Item 2 is", shoplist[2]
print "Item 3 is", shoplist[3]
print "Item -1 is", shoplist[-1]
print "Item -2 is", shoplist[-2]
print "Character 0 is ", name[0]


print "Item 1 to 3 is", shoplist[1:3]
print "Item 2 to end is ", shoplist[2:]
print "item 1 to -1 is", shoplist[1:-1]
print "Item start to end is", shoplist[:]

print "Character 1 to 3 is", name[1:3]
print "Character 2 to end is", name[2:]
print "Character 1 to -1 is", name[1:-1]
print "Character start  to end is", name[:]
   





















