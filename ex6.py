#-*-coding: utf-8 -*-
print "Mary had a little lamb."
print "Its fleece was white as %s." % 'snow'
print "And everywhere that Mary went."
print "." * 10 # what'd that do?

end1 ="C"
end2 ="h"
end3 ="e"
end4 ="e"
end5 ="s"
end6 ="e"
end7 ="B"
end8 ="u"
end9 ="r"
end10 ="g"
end11 ="e"
end12= "r"

#watch the comma at end..try removing it
print end1 + end2 +end3 +end4 +end5 +end6,
print end7 + end8 + end9 + end10 + end11 + end12

# This is exercise 8

formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
"I had this thing.",
"That you could type uo right",
"But it din't sign",
"So I said goodnight"
)

# example 9: Printing Print Printing
days = "Mon Tues Wed Thur Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

print "He are the days:", days
print "Here are the months:", months

print """
There's something going on here.
With teh three double quotation
"""

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\nona line."
backlash_cat = "I'm \\a\\ cat."

fat_cat ="""
i'll do a list:
\t* cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backlash_cat
print fat_cat




