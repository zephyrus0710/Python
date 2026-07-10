num = int(input('enter the number of students'))
for i in range(num):
    print('\nStudent',i+1)
    name = input('enter the name of student')
    marks1 = int(input('enter the marks for s1'))
    marks2 = int(input('enter the marks for s2'))
    marks3 = int(input('enter the marks for s3'))
    totalmarks = marks1 + marks2 + marks3
    avgmarks1 = totalmarks/3
    if avgmarks1 >= 90:
        grade = "Excellent"
    elif avgmarks1 >= 70:
        grade = "Good"
    elif avgmarks1 >= 60:
        grade = "Average"
    elif avgmarks1 >= 40:
        grade = "Below Average"
    else:
        grade = "Poor"

    print('Student Name:',name)
    print('Total Marks:',totalmarks)
    print('Average Marks:',avgmarks1)
    print('Grade:',grade)