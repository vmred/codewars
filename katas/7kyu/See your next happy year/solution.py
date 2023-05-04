# Scenario
# You're saying good-bye your best friend , See you next happy year .

# Happy Year is the year with only distinct digits , (e.g) 2018

# Task
# Given a year, Find The next happy year or The closest year You'll see your best friend  !alt !alt

# Notes
# Year Of Course always Positive .
# Have no fear , It is guaranteed that the answer exists .
# It's not necessary that the year passed to the function is Happy one .
# Input Year with in range (1000  ≤  y  ≤  9000)


def next_happy_year(year):
    def is_distinct(v):
        return all(v.count(i) == 1 for i in v)

    while True:
        year += 1
        if is_distinct(str(year)):
            return year
