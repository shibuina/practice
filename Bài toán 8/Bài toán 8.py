class School:
    def __init__(self):
        self.students = []
        self.instructors = []
        self.subjects = []
        self.classes = []
    def read_data(self):
        with open(r"C:\Users\Dell\Desktop\Học\CSD202\practice\Bài toán 8\Classes.txt", 'r') as classes_file:
            for line in classes_file:
                line = line.strip().split(':')
                self.classes.append(line)
        with open(r"C:\Users\Dell\Desktop\Học\CSD202\practice\Bài toán 8\Instructors.txt", 'r',encoding="utf8") as instructor_file:
            for line in instructor_file:
                line = line.strip().split(':')
                self.instructors.append(line)
        with open(r"C:\Users\Dell\Desktop\Học\CSD202\practice\Bài toán 8\Students.txt", 'r',encoding="utf8") as student_file:
            for line in student_file:
                line = line.strip().split(':')
                self.students.append(line)
        with open(r"C:\Users\Dell\Desktop\Học\CSD202\practice\Bài toán 8\Subjects.txt", 'r') as subject_file:
            for line in subject_file:
                line = line.strip().split(':')
                self.subjects.append(line)
        for student in self.students:
            print(f"{student}\n")
        for instructor in self.instructors:
            print(f"{instructor}\n")
        for subject in self.subjects:
            print(f"{subject}\n")
        for cl in self.classes:
            print(f"{cl}\n")
        
    def value_of_subjects(self):
        subj_val = []
        for id_subj in self.subjects:
            point = 0
            for id_class in self.classes:
                if id_subj[0] == id_class[1]:
                    point += float(id_subj[2])
            subj_val.append([id_subj, point])
        return subj_val
    def find_students_learn_subject(self,subj_code):
        count = 0
        for subj in self.subjects:
            if subj[0] == subj_code:
                name = subj[1]
        for classes in self.classes:
            if classes[1] == subj_code:
                count+=1
        return f"{name} {count}"
    def find_students_learn_instructor(self,ins_code):
        count = 0
        for ins in self.instructors:
            if ins[0] == ins_code:
                name = ins[1]
        for classes in self.classes:
            if classes[2] == ins_code:
                count+=1
        return f"{name} {count}"
    def find_students_subjects(self,student_code):
        subjects = []
        for stu in self.students:
            if stu[0] == student_code:
                name = stu[1]
        for classes in self.classes:
            if classes[3] == student_code:
                for subj in self.subjects:
                    if classes[1] == subj[0]:
                        if subj[1] not in subjects:
                            subjects.append(subj[1])
        return f"{name} {subjects}"



    def sort(self):
        array = self.value_of_subjects()
        for i in range(len(array)):
            for j in range(i, len(array)):
                if array[j][1] > array[i][1]:
                    array[i], array[j] = array[j], array[i]
        return array
main = School()
main.read_data()
for subj_val in main.sort()[:10]:
    print(f"{subj_val}\n")
print(main.find_students_learn_subject("S01"))
print(main.find_students_learn_instructor("I01"))
print(main.find_students_subjects("s01"))