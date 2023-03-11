# Learn how to use the Regex
# Learning objectives:
    # 1) re module to import
    # 2) methods to search for matches
    # 3) methods on a match object
    # 4) meta characters
    # 5) more special sequences
    # 6) sets
    # 7) quantifier
    # 8) conditions
    # 9) grouping
    # 10) modification
    # 11) compilation flags
#-------------------------------------------------
# Lesson 2 & 3 - Methods to search for matches &
#                Methods on a match object
#                e.g. match(), search() and finall()
#                e.g. span(), group(), start and end

import re

sample_str = '123abc456789abc123ABC'

# I) Explore findall()
search_pattern = re.compile(r"abc")
find_matches = search_pattern.findall(sample_str)

# use a for loop to iterate the find_matches list
for found_match in find_matches:
    print("Explore I below")
    print(found_match)

# II) Explore match()
# to match pattern at the BEGINGNING of the string
# Remember this only return ONE match because of the
# search of the beginning
search_pattern = re.compile(r"abc")
find_match = search_pattern.match(sample_str)

# Print result if the pattern is found
# The result should be None because 
# the beginning is not pattern 'abc'
print("Explore II below")
print(find_match)


# if we change the pattern to '123'
# then the result shoule be found
search_pattern = re.compile(r"123")
find_match = search_pattern.match(sample_str)
print(find_match)

# II) Explore match()
# Look for 1st match string from the 
# original string where in any location 
search_pattern = re.compile(r"789")
find_match = search_pattern.search(sample_str)
print(find_match)


# III) Learn for group, start, end, span methods
search_pattern = re.compile(r"123")
find_matches = search_pattern.finditer(sample_str)

print("Explore III below")
for found_match in find_matches:
    print(found_match.span(), found_match.start(), found_match.end())

print("with group:")
for found_match in find_matches:
    print(found_match.group())