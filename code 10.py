# if else if program
marks = int(input("Enter your marks : "))
if 90 <= marks <= 100:
    print("Grade O")
elif 80 <= marks < 90:
    print("Grade E")
elif 70 <= marks < 80:
    print("Grade A")
elif 60 <= marks < 70:
    print("Grade B")
elif 50 <= marks < 60:
    print("Grade C")
else:
    print("Grade D")