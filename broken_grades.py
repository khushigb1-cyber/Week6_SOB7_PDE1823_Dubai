# Calculating Grades (ok, let me think about this one)

# Write a program that will average 3 numeric exam grades, return an average test score, a corresponding letter grade, and a message stating whether the student is passing.

# Average	Grade
# 90+	A
# 80-89	B
# 70-79	C
# 60-69	D
# 0-59	F

# Exams: 89, 90, 90
# Average: 90
# Grade: A
# Student is passing.

# Exams: 50, 51, 0
# Average: 33
# Grade: F
# Student iis failing.

exam_one = int(input("Input exam grade one: "))
exam_two = int(input("Input exam grade two: ")) #added int before input to convert input to int
exam_three = int(input("Input exam grade three: ")) #mislabelled as exam_3 when below calls exam_three, also was converting to str instead of int

grades = [exam_one, exam_two, exam_three] #added commas for list
sum = 0
for grade in grades: #wrong loop variable,changed to grades to call our list of exam results
  sum = sum + grade

avg = sum / len(grades) #grades misspelled

if avg >= 90:
    letter_grade = "A"
elif avg >= 80 and avg < 90: #was missing : at end
    letter_grade = "B"
elif avg > 69 and avg < 80:
    letter_grade = "C" #was missing same closing "
elif avg <= 69 and avg >= 60: #wrong range for grade, changed to 60 instead of 65
    letter_grade = "D"
else: #was using elif without condition, changed to else
    letter_grade = "F"

for grade in grades:
    print("Exam: " + str(grade))

print("Average: " + str(avg)) #was printing avg each time exam grade was given, so moved outside block to make it run only once after all grades given
print("Grade: " + letter_grade) #same as avg, was printing every time. both kept out of block so they only run once after all grades given

if letter_grade == "F": #var letter-grade is wrong, changed to letter_grade. also 'is' isn't for str, changed to ==
    print("Student is failing.") #was missing opening & closing brackets
else:
    print("Student is passing.") #was also missing opening and closing brackets

