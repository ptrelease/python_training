import re

name = 'Barnaby Cedrick Forsyth'


# pattern = re.compile(r"\s* \s*")
pattern = re.compile(r"\s*")
print('splitting name by spaces:')
print(pattern.split(name))
# should show ['Barnaby', 'Cedrick', 'Forsyth'], i.e splits by spaces into a list

pattern = re.compile(r"\s* \s*")
print('sub commas for stars')
print(pattern.sub('*', name))
# Now spaces are stars
