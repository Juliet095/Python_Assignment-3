student_names = ['Sandra', 'Patricia','Phionah',  'Anita']
student_marks = [80,56,78,90]

#print ,Sandra, Patricia,Phionah and Anitah
#Add Masha at the forth position.
#update the name phionah to phionah Aladina
#Display the length of the student list.
#print all the students names using a for loop.
#calculate the total marks for the student marks variable

student_names =['Sandra', 'Patricia','Phionah',  'Anita']
print(student_names, type(student_names))
 
student_names.insert(4,"Masha")
print(student_names)


student_names[2]="Phionah Aladina"
print(student_names)

student_names =['Sandra', 'Patricia','Phionah',  'Anita']
print(len(student_names))

student_names =['Sandra', 'Patricia','Phionah',  'Anita']
for student_name in student_names:
    print(student_name)

student_marks = [80,56,78,90]
total_marks =  sum (student_marks)
print(total_marks)