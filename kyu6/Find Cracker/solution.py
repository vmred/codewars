# Someone was hacking the score.
# Each student's record is given as an array
# The objects in the array are given again as an array of scores for each name and total score. ex>
from dataclasses import dataclass
from typing import List


# array = [
# ["name1", 445, ["B", "A", "A", "C", "A", "A"]],
# ["name2", 140, ["B", "A", "A", "A"]],
# ["name3", 200, ["B", "A", "A", "C"]]
# ]
# The scores for each grade is:

# A: 30 points
# B: 20 points
# C: 10 points
# D: 5 points
# Everything else: 0 points
# If there are 5 or more courses and all courses has a grade of B or above, additional 20 points are awarded.
# After all the calculations, the total score should be capped at 200 points.

# Returns the name of the hacked name as an array when scoring with this rule.

@dataclass
class Student:
    name: str
    total_score: int
    scores: List[str]


scores = {'A': 30, 'B': 20, 'C': 10, 'D': 5}


def calculate_score(values: List[str]):
    score = 0
    if len(values) >= 5 and sorted(set(values)) in [['A', 'B'], ['A'], ['B']]:
        score += 20
    score += sum(scores.get(k, 0) for k in values)
    return score


def find_hack(arr):
    hackers = []
    for student in [Student(a[0], a[1], a[2]) for a in arr]:
        calculated_score = calculate_score(student.scores)
        calculated_score = calculated_score > 200 and 200 or calculated_score
        if calculated_score != student.total_score:
            hackers.append(student.name)

    return hackers
