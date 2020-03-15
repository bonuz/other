# useful string methods

spam = "Hello world!"
spam = spam.upper()

print(spam)

spam = spam.lower()

print(spam)

# validate with upper/lower

print("How are you?")
feeling = input()
print(feeling)
print(feeling.lower())
if feeling.lower == "great":
    print("I feel great too")
else:
    print("I hope the rest of your day is good.")

# isupper() and islower()

spam = "Hello world!"
print(spam.islower())
print(spam.isupper())
print("HELLO".isupper())
print("abc123123".islower())
print("123123".islower())
print("123123".isupper())

# chain methods

print("HELLO".lower().upper())

# isX string methodsimp
'''
isalpha() : returns true if the string consists only of letters and is not blank.
isalnum() : returns true if the string consists only of letters and numbers
and is not blank.
isdecimal() : returns true if the string consists only of numeric characers
and is not blank.
isspace() : returns true if the string consists only of spaces, tabs, and newlines
and is not blan.
istitle() : returns true if the string consists only of words that begin with
and uppercase letter followed by only lowercase letters.
'''

# the startswith() and endswith() methods

print("Hello world!".startswith("Hello"))
print("Hello world!".endswith("world!"))
print("abc123".endswith("12"))

# removing whitespaces with strip(), rstrip() and lstrip()
# works like trim() in sql

print("   HELLO WORLD   ".strip())
print("   HELLO WORLD   ".rstrip())
print("   HELLO WORLD   ".lstrip())
