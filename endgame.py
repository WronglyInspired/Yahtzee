def getScores(ctgys):
    upper_scores = []
    lower_scores = []
    # upper row
    for key, v in playerCtgys.items():
        if v["row"] == "upper":
            upper_scores.append(v["value"])
    upper_scores = sum(upper_scores)
    # upper row bonus
    if upper_scores >= 63:
        upper_bonus = 35
    else:
        upper_bonus = 0
    # lower row
    for key, v in playerCtgys.items():
        if v["row"] == "lower":
            lower_scores.append(v["value"])
    lower_scores = sum(lower_scores)
    total_score = upper_scores + upper_bonus + lower_scores
    return upper_scores, upper_bonus, lower_scores, total_score


playerCtgys = {  # ctgys is shorthand for categories
    "1": {"value": 4, "row": "upper", "rule": "True", "pts": "playerDice.count(1) * 1"},
    "2": {"value": 8, "row": "upper", "rule": "True", "pts": "playerDice.count(2) * 2"},
    "3": {"value": 9, "row": "upper", "rule": "True", "pts": "playerDice.count(3) * 3"},
    "4": {"value": 4, "row": "upper", "rule": "True", "pts": "playerDice.count(4) * 4"},
    "5": {"value": 15, "row": "upper", "rule": "True", "pts": "playerDice.count(5) * 5"},
    "6": {"value": 36, "row": "upper", "rule": "True", "pts": "playerDice.count(6) * 6"},
    "t": {"value": 9, "row": "lower", "rule": "findKind(3, playerDice)", "pts": "sum(playerDice)"},
    # triples / three of a kind
    "q": {"value": 36, "row": "lower", "rule": "findKind(4, playerDice)", "pts": "sum(playerDice)"},
    # quadruples / four of a kind
    "f": {"value": 25, "row": "lower", "rule": "findKind(2, playerDice, '==') and findKind(3, playerDice)",
          "pts": "25"},
    # full house
    "s": {"value": 0, "row": "lower", "rule": "findStraight(4, playerDice)", "pts": "30"},  # small straight
    "l": {"value": 40, "row": "lower", "rule": "findStraight(5, playerDice)", "pts": "40"},  # large straight
    "c": {"value": 26, "row": "lower", "rule": "True", "pts": "sum(playerDice)"},  # chance
    "y": {"value": 0, "row": "lower", "rule": "findKind(5, playerDice)", "pts": "50"},  # how to check this rule?
}

player_scores = getScores(playerCtgys)
print(player_scores)
