# put your python code here
# inputs part
first_class_student_count = abs(int(input()))
second_class_student_count = abs(int(input()))
third_class_student_count = abs(int(input()))

# calculation part
first_class_desk_count = (first_class_student_count // 2) + (first_class_student_count % 2)
second_class_desk_count = (second_class_student_count // 2) + (second_class_student_count % 2)
third_class_desk_count = (third_class_student_count // 2) + (third_class_student_count % 2)

# total
total_desk_count = first_class_desk_count + second_class_desk_count + third_class_desk_count
print(total_desk_count)
