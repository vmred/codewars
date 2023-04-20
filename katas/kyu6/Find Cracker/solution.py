# Someone was hacking the score.
# Each student's record is given as an array
# The objects in the array are given again as an array of scores for each name and total score. ex>

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


scores_map = {'A': 30, 'B': 20, 'C': 10, 'D': 5}
max_score, bonus = 200, 20
apply_bonus = set('AB')


def calculate_score(values):
    return min(
        max_score, sum(scores_map.get(k, 0) for k in values) + bonus * (len(values) > 4 and set(values) <= apply_bonus)
    )


def find_hack(arr):
    return [name for name, total_score, scores in arr if total_score != calculate_score(scores)]
