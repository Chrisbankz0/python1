all_student_scores = []
totals = []
averages = []

number_of_students = int(input("Enter Number of student: "))
number_of_subjects = int(input("Enter Number of subjects: "))
print("Saving >>>>>>>>>>>>>>>")
print("Saved successfully\n")



for student in range(1, number_of_students + 1):
	print(f"\nEntering scores for student {student}")

	student_scores = []
	total = 0.0

	for subject in range (1, number_of_subjects +1):
		score = float(input(f"Enter Scores for each subject {subject}: "))
			
		while score < 0 or score > 100:
			score = int(input("INVALID SCORE. Enter Scores again: "))

		student_scores.append(score)
		total += score



	all_student_scores.append(student_scores)
	totals.append(total)
	averages.append(total / number_of_subjects)

	print("Saving >>>>>>>>>>>>>>>")
	print("Saved successfully")

	sorted_total = sort(total, reverse=True)


print("\nRESULT SHEET")
print("-" * 60)

print(f"{"Student" :<10}", end="")
for num in range(1, number_of_subjects + 1):
	print(f"{"SUB" + str(num):<8}", end="")
print(f"{"TOTAL" :<8} {"AVERAGE" :<10} {"POSITION" :<10}") 
print("-" * 60)


student_number = 1

for student_scores, total, average in zip(all_student_scores, totals, averages):
	print(f"{'Student ' + str(student_number):<10}", end="")
    

	for score in student_scores:
		print(f"{score:<8}", end="")
    
    position = sorted_total.index(total) +1

	print(f"{total:<8}{average:<10.2f}")
    
	student_number += 1
