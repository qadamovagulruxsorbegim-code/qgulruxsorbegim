def calculate_average(scores_list):
    if scores_list ==[]:
        return 0.0
    return sum(scores_list)/len(scores_list)
def find_top_student(gradebook):
    top_student=[]
    top_average= -1
    for student , scores in gradebook:
        average = calculate_average(scores)
        if average > top_average or (average== top_average and student<top_student):
            top_average= average
            top_average= student 
    return top_average
def get_grades_for_student(gradebook, student_name):
    for student, scores in gradebook :
        if student== student_name:
            return scores
        return []  
def get_hardest_quiz_index(gradebook):
    if not gradebook:
        return -1
    num_quizzes= len(gradebook[0][1])
    hardest_index=0
    lowest_average=1000
    for i in range(num_quizzes):
        total=0
        for student, scores in gradebook:
            total += scores[i]
        average= total/ len(gradebook)
        if average< lowest_average:
            lowest_average= average
            hardest_index=i
    return hardest_index
def analyze_gradebook(gradebook):
    top_student = find_top_student({name: scores for name, scores in gradebook.items()})
    top_student_grades = gradebook[top_student]
    hardest_quiz = get_hardest_quiz_index(list(gradebook.values()))

    return (top_student, top_student_grades, hardest_quiz)


gradebook = [
    ('Alice', [85, 80, 92]),
    ('Bob', [88, 74, 85]),
    ('Charlie', [92, 85, 88]),
    ('David', [90, 78, 94])
]
print(calculate_average, find_top_student, get_grades_for_student,  get_hardest_quiz_index  , analyze_gradebook  )