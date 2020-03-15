# escape characters
spam = 'Say hi to Bob\'s mother.'
print(spam)

'''
\' single quote
\" double quote
\t tab
\n newline(line break)
\\ backslash
'''

print("Hello there!\nHow are you?\nI\'m doing fine.")

# raw string
print(r'That is Carol\'s cat.')
# a raw string completely ignores all escape characters and prints any backlash
# that appears in the string

# multiline strings with triple quotes
print(''' Dear Alice,

Eve's cat has been arrester for catnapping, cat burglary, and extortion.

Sincerely,
Bob''')

# slicing strings (like lists)
spam = "Hello world!"
print(spam[0])
print(spam[4])
print(spam[-1])
print(spam[0:5])
print(spam[:5])
print(spam[6:])

# the in and not in operators with strings

print("Hello" in "Hello world!")
print(" " in spam)
print("HELLO" in "Hello world!")


