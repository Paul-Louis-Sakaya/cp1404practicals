


def main():
    score = float(input("Enter score: "))

    if score < 0:
        print("Invalid score")
    else:
        if score > 100:
            print("Invalid score")
        elif 50 <= score < 90:
            print("Pass")
        elif score >= 90:
            print("Excellent")
        elif score < 50:
            print("Bad")
main()



def calculate_results(score):
    score = float(input("Enter your score: "))

    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

calculate_results()
