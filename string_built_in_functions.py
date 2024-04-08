# Capitalize
new_string = "hello world!"
print(new_string.capitalize())

#Casefold will return all characters even
new_string = "heLLo wOrld!"
print(new_string.casefold())

#center will put string where you need (num of characters)
new_string = "hello world!"
print(new_string.center(20))

# count (will count nomber of what you are looking for in string)
new_string = "hello world!"
print(new_string.count("w"))

# encode (get bite version of string)
new_string = "hello world!"
print(new_string.encode(encoding='UTF-8', errors='strict'))

#endswith (check for ending with certain character)
new_string = "hello world!"
print(new_string.endswith('!'))

#expand tabs for needed spacelenght
new_string = "hel\tlo wo\trld!"
print(new_string.expandtabs(20))

# find substring in string (by index number)
new_string = "hello world!"
position: int = new_string.find('world!')
print(position)
print(new_string[position:])

#format will place needed text instead of curly braces
text: str = '{subject} is doing {action}.'
print(text.format(subject='Cat',action='meow'))

text: str = '{} is doing {}.'
print(text.format('Cat', 'meow'))

#formatmap will map dictionary to a formatted values in the string
coordinates = {'x':10, 'y':-5}
text = 'Coordinates: ({x}, {y})'
print(text.format_map(coordinates))

#index will find index but if doent find what you need will return error
text = 'Astronautd recently found banana on the Moon'
position = text.index('banana')
print(position)
print(text[position:])

#isalnum checks if characters re alpfa numeric (letters and numbers only)
text = 'Hellothere'
print(text.isalnum())

#isaphla check only for letters
text = 'Helloworld'
print(text.isalpha())

#isascci check only for ascci characters (no special characters such as trade mark etc)
text = 'Hello world ¥'
print(text.isascii())

#isdecimal checks if string is a decimal (also is digit and numeric)
text = '123'
print(text.isdecimal())
#isdigit check if string is digit (if ys its also numeric)
text = ''
print(text.isdigit())
#isnumeric checks if its numeric
text = '1234567'
print(text.isnumeric())

#isidentifier checks if it's a python identifier
text = 'text-sample'
text2 = 'text_sample'
print(text.isidentifier())
print(text2.isidentifier())

#islower checks if characters are lower case
text = 'abCdefg'
print(text.islower())

#isprintable checks if string is printable
text = 'hello world \n'
print(text.isprintable())

#isspace checks if string is just spaces
text = '          '
text2 = '         is            '
print(text.isspace())
print(text2.isspace())

#istitle check if each word is capitalized
text = 'The Video'
text2 = 'the Video'
print(text.istitle())
print(text2.istitle())

#isupper checks for all uppers
text = 'Hello'
text2 = 'HELLO'
print(text.isupper())
print(text2.isupper())

#join will join elements with the separator you choose
text = '-'
print(text.join(['one', 'two', 'three']))
print('-' .join(['one', 'two', 'three']))

#ljust will adjust to the left with num of characters you choose
text = 'Hello'
print(text.ljust(20, '-'))

#lower turns everything to lower case
text = 'Hello WORLD'
print(text.lower())

#lstrip will remove what you need from the string (choose part of the text)
text = "Hello world it's been great"
print(text.lstrip('world'))

#maketrans and translate go together
text = 'Hello world 123'
table = text.maketrans('w', '👀')

print(table)
print(text.translate(table))

#patrition will put string apart when you choose to
text = '2+3=5'
print(text.partition('='))

#removeprefix will remore prefix
text = 'hellothereworld'
print(text.removeprefix('hell'))

#removesuffix removing suffix
text = 'hellothereworld'
print(text.removesuffix('orld'))

#replace will replace substring you choose to what you choose
text = 'Hello World Im Igor and my brother is Igor'
print(text.replace('Igor', 'Vova', 1))

#rindex will find index from the right
text = 'Hello there B'
print(text.rindex('e'))

#rjust will adjust to the right with amount of characters you choose
text = 'hello'
print(text.rjust(20, '_'))
