round_for = int(input("Enter the number of students: "))
name = []
score = []
students = []
for i in range(round_for):
    name_input= input("Enter student name: ")
    name.append(name_input)
    score_input = float(input("Enter student score: "))
    score.append(score_input)
    students.append((name_input, score_input)) 

print("--Unsorted Scores--")
for name, score in students:
    print(f"{name}: {score}")

def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i][1]<alist[i+1][1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp


bubbleSort(students)
print("--Sorted Scores (Bubble Sort)--")
for name, score in students:
    print(f"{name}: {score}")


top3 = students[:3]
print("--Top 3 Highest Scores--")
for name, score in top3:
    print(f"{name}: {score}")

def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i][1]> alist[i+1][1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
bubbleSort(students)

bottom_3_students = students[:3]
print("--Top 3 Lowest Scores--")
for name, score in bottom_3_students:
    print(f"{name}: {score}")

def sequential_Search(alist, item):
    pos = 0
    found = False
    count = 0 
    names_found = [] 
    
    while pos < len(alist):
        if alist[pos][1] == item:
            count += 1
            names_found.append(alist[pos][0])  
            found = True
        pos = pos + 1  
    

    if found:
        print(f"There are people who get points {item}. Number of people: {count}")
        for name in names_found:
            print(f"- {name}")
    else:
        print(f"No students found with score {item}")
    
    return found


searh = float(input("Enter the score to search: "))  
sequential_Search(students, searh)
