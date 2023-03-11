# Learn how to use the Regex
# Learning objectives:
    # 1) re module to import
    # 2) methods to search for matches
    # 3) methods on a match object
    # 4) meta characters
    # 5) more special sequences
    # 6) sets - a pattern between a [ ]
    # 7) quantifier
    # 8) conditions
    # 9) grouping  
    # 10) modification
    # 11) compilation flags
#--------------------------------------------

# Lesson 6 & 7- Sets & quantifier
#               All meta characters: 
#               . ^ $ * + ? { } [ ] \ | ( )
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
#   {4} : exact number.  i.e. look for exact number 4
#   {4,6} : look for a exact numbers in a range of numbers (min, max)
#

import re

sample_str1 = 'hello @World 123_ secret-agency'

# I) Explore to use [] to look for sets to search non-numerical characters
print("I) Explore to use [] to look for sets of specified characters")
search_pattern = re.compile(r"[a-zA-Z]") # Search for a-z and A-Z only
find_matches = search_pattern.finditer(sample_str1)
for found_matches in find_matches:
    print(found_matches.group())

print("II) Explore to use [] to look for sets of specified characters")
search_pattern = re.compile(r"[0-9]") # Search for 0 to 9 only
find_matches = search_pattern.finditer(sample_str1)
for found_matches in find_matches:
    print(found_matches.group())

#   Recap Quantifier:
#   * : 0 or more
#   + : 1 or more
#   ? : 0 or 1, -> optinal character
#   {4} : exact number.  i.e. look for exact number 4
#   {4,6} : look for a exact numbers in a range of numbers (min, max)
#
print("III) Explore the digit characters")
sample_str2 = 'hello_123'
search_pattern = re.compile(r"\d") 
find_matches = search_pattern.finditer(sample_str2)
for found_matches in find_matches:
    print(found_matches.group())

print("IV) Explore to find and group more chararcters together")
search_pattern = re.compile(r"\d*") 
find_matches = search_pattern.finditer(sample_str2)
for found_matches in find_matches:
    print("find the length of digit : " + str(len(found_matches.group())) + " for search string \'" + sample_str1 +"\'")
    print(found_matches.group())

print("IV) Explore to find and group more chararcters together")
search_pattern = re.compile(r"\d+") 
find_matches = search_pattern.finditer(sample_str2)
for found_matches in find_matches:
    print("find the length of digit : " + str(len(found_matches.group())) + " for search string \'" + sample_str1 +"\'")
    print(found_matches.group())

print("V) Explore to use '?' to search for the optional character '_'")
search_pattern = re.compile(r"_?\d+") 
find_matches = search_pattern.finditer(sample_str2)
for found_matches in find_matches:
    print("find the length of digit : " + str(len(found_matches.group())) + " for search string \'" + sample_str1 +"\'")
    print(found_matches.group())

print("VI) Explore to find the exact numbers of digit in te string")
sample_str3 = 'hello123 123459, 7799 and 888 are in this list'
search_pattern = re.compile(r"\d{4}") # search for the digit the length = 4 only
find_matches = search_pattern.finditer(sample_str3)
for found_matches in find_matches:
    print(found_matches.group())


# Below apply the special exercises for searching a various data format string
#
# Given the following sample_date string format
sample_dates = """
                01.04.2022

                2022.04.01

                hello
                2022-04-01
                2022-05-23
                2022-06-11
                2022-07-12
                2022-08-18

                2023/01/02

                2023_01_08
                2023_02_23

                #$+*9-
                
                2023/02/27

                2023.03.21

            """

# Follow select the special searching pattern on date field
print()
print("VII) Explore to filters the differet date formats")
search_pattern = re.compile(r"\d\d\d\d.\d\d.\d\d") # '.' stands for any characters
find_matches = search_pattern.finditer(sample_dates)
for found_matches in find_matches:
    print(found_matches.group())

# May also try the following search patterns:
# search_pattern = re.compile(r"\d\d\d\d-\d\d-\d\d")
# search_pattern = re.compile(r"\d\d\d\d[-/]\d\d[-/]\d\d")
# search_pattern = re.compile(r"\d\d\d\d[-/]0[56][-/]\d\d")
# search_pattern = re.compile(r"\d\d\d\d[-/]0[5-7][-/]\d\d")
# search_pattern = re.compile(r"\d\{4}[-/]0[5-7][-/]\d{2}")

