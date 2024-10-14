sort_name_grade = {}
grades = [[5,3,3,5,4],[2,2,2,3],[4,5,5,2],[4,4,3],[5,5,5,4,5]]
students = {'johnny','Bilbo','Steve','Khendrik','Aaron'}
students_list = list(students)
students_list.sort()
for count,name in enumerate(students_list):
    average = sum(grades[count]) / len(grades[count])
    sort_name_grade[name] = average
print(sort_name_grade)