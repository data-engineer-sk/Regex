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
#--------------------------------------------

# Lesson 4 & 5 - Meta characters & more special sequences
#                All meta characters: 
#                . ^ $ * + ? { } [ ] \ | ( )
#
#   . Any character (except newline character)
#   ^ Starts with "^hello"
#   $ Ends with "world$"
#   * Zero or more occurrences "aix*"
#   + One or more occurrences "aix+"
#   { } Exactly the specified number of occurrences "al{2}"
#   [ ] A set of characters "[a-m]"
#   \ Special sequence (or escape special characters) "\d"
#   | Either or "falls|stays"
#   ( ) Capture and group
#
#   More to explore :-
#   \d : Matches any decimal digit: [0-9]
#   \D : Matches any non-digit character
#   \s : Matches any whitespace character. i.e. (space " " tab "\t" newline "\n")
#   \S : Matches any non-whitespace character
#   \w : Matches any alphanumeric (word) character.  i.e. [a-zA-Z0-9]
#   \W : Matches any non-alphanumeric character
#   \b : Matches where the specificed characters are at the beginning or the end of a word r"\^air" r"air\b"
#   \B : Matches where the specificed characters are present, but NOT at the beginning (or at the end) of a word r"\Bain" or r"ain\B"
#
#   Quantifier:
#   * : 0 or more
#   + : 1 or more
#   ? : 0 or 1, -> optinal character
#   {4} : exact number
#   {4,6} : range numbers (min, max)
#

import re

sample_str = '123abc.456789.abc123...ABC'

# I) Explore . to search for all
print("I) Explore . to search for all")
search_pattern = re.compile(r".")
find_matches = search_pattern.finditer(sample_str)
for found_matches in find_matches:
    print(found_matches.group())

# II) Explore \. to search the position of '.'
print()
print("II) Explore \. to search for '.' there")
search_pattern = re.compile(r"\.")
find_matches = search_pattern.finditer(sample_str)
for found_matches in find_matches:
    print(found_matches)

# III) Explore \. to search the position of '.'
print()
print("III) Explore ^ to search for start with '^123'")
search_pattern = re.compile(r"^123")
find_matches = search_pattern.finditer(sample_str)
for found_matches in find_matches:
    print(found_matches)

# IV) Explore \. to search the position of '.'
print()
print("IV) Explore $ to search for end with 'ABC'")
search_pattern = re.compile(r"ABC$")
find_matches = search_pattern.finditer(sample_str)
for found_matches in find_matches:
    print(found_matches)

# V) Explore any digit 
sample_str_2 = 'hello 123_ heyho hohey'
print()
print("V) Explore any digit")
search_pattern = re.compile(r"\d")
find_matches = search_pattern.finditer(sample_str_2)
for found_matches in find_matches:
    print(found_matches)

# VI) Explore any non-digit 
sample_str_2 = 'hello 123_ heyho hohey'
print()
print("VI) Explore any non-digit")
search_pattern = re.compile(r"\D")
find_matches = search_pattern.finditer(sample_str_2)
for found_matches in find_matches:
    print(found_matches)


# VII) Explore any white-spaces characters
sample_str_2 = 'hello 123_ heyho hohey'
print()
print("VII) Explore any white-spaces characters")
search_pattern = re.compile(r"\s")
find_matches = search_pattern.finditer(sample_str_2)
for found_matches in find_matches:
    print(found_matches)

# VIII) Explore any white-space characters
sample_str_3 = 'Secret Agency \t-\t James Bon is @777 plane\n'
print()
print("VIII) Explore any alphnumeric characters.  *no space or special character")
search_pattern = re.compile(r"\w")
find_matches = search_pattern.finditer(sample_str_3)
for found_matches in find_matches:
    print(found_matches)

# IX) Explore any non-alphnumeric characters only.  ie. all space or special character
sample_str_3 = 'Secret Agency \t-\t James Bon is @777 plane\n'
print()
print("IX) Explore any non-alphnumeric characters only.  ie. all space or special character")
search_pattern = re.compile(r"\W")
find_matches = search_pattern.finditer(sample_str_3)
for found_matches in find_matches:
    print(found_matches)

# X) Explore any starting special characters only
sample_str_4 = 'Good Morning Hong Kong, British, and Americal.  Welcome Britishman as well!'
print()
print("X) Explore any starting special characters only")
search_pattern = re.compile(r"\bGood Morning")
find_matches = search_pattern.finditer(sample_str_4)
for found_matches in find_matches:
    print(found_matches)

print()
search_pattern = re.compile(r"\bBritish")
find_matches = search_pattern.finditer(sample_str_4)
for found_matches in find_matches:
    print(found_matches)