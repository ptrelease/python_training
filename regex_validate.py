import re

phoneno = input('phoneno: ')

# ^00           check starts with 00
# (\d {1,3})    check that the next 1-3 chars are digits (denoting international dialling code)
# [ /]          then check for a space or /
# (\d{2,4})     then check validate city  code betwen two and 4 digits.
# [ /]          then check for a space or /
# ((\d{8})|(\d{4}[ /]\d{4}))$ finally check for one group of EXACTLY 8 or two groups of 4.

pattern = r"^00" \
          r"(\d{1,3})" \
          r"[ /]" \
          r"(\d{2,4})" \
          r"[ /]" \
          r"((\d{8})|(\d{4}[ /]\d{4}))$"

pattern = re.compile(pattern)
if pattern.match(phoneno):
    print(phoneno)
else:
    print('invalid')

# 0077 8787 9898/8988 or 0077 8787 98988988 are passing examples.