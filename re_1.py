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
#---------------------------
# Lesson 1 - The intro of re
import re

sample_str = '123abc456789abc123ABC'

# if we want to look for a pattern 'abc',
# just create a pattern to look for 'abc'
# remember the search is case sensitive!!!
search_pattern = re.compile(r"abc") # little character 'r' here means raw string. i.e. the original string itself

# create a list object 'find_matches' to
# collect the result (if any)
find_matches = search_pattern.finditer(sample_str)

# use a for loop to iterate the find_matches list
for found_match in find_matches:
    print(found_match)

######## -------- for the above searching can be replaceed
######## -------- by the following codes
find_matches = re.finditer(r'abc', sample_str)
for found_matches in find_matches:
    print(found_matches)  # get the same result as above

