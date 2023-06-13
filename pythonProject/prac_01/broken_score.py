

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