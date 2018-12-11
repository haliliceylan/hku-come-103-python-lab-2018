
def calc_average(score1, score2, score3, score4, score5):
    return (score1 + score2 + score3 + score4 + score5) / 5


def determine_grade(score):
    if score <= 100 and score >= 90:
        return 'A'
    elif score < 90 and score >= 80:
        return 'B'
    elif score < 80 and score >= 70:
        return 'C'
    elif score < 70 and score >= 60:
        return 'D'
    elif score < 60:
        return 'F'


def main():
    score1 = int(input("Enter the score1: "))
    score2 = int(input("Enter the score2: "))
    score3 = int(input("Enter the score3: "))
    score4 = int(input("Enter the score4: "))
    score5 = int(input("Enter the score5: "))
    avg_score = calc_average(score1, score2, score3, score4, score5)
    print(format("Score", "10s"), format(
        "Score", "10s"), format("Letter Grade", "15s"))
    print("-"*33)
    print(format("Score 1", "10s"), format(score1, "<10d"),
          format(determine_grade(score1), "15s"))
    print(format("Score 2", "10s"), format(score2, "<10d"),
          format(determine_grade(score2), "15s"))
    print(format("Score 3", "10s"), format(score3, "<10d"),
          format(determine_grade(score3), "15s"))
    print(format("Score 4", "10s"), format(score4, "<10d"),
          format(determine_grade(score4), "15s"))
    print(format("Score 5", "10s"), format(score5, "<10d"),
          format(determine_grade(score5), "15s"))
    print("-"*33)
    print("average of all scores is", avg_score,
          "and grade is", determine_grade(avg_score))


if __name__ == "__main__":
    main()
    pass
