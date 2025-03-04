import random

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def __repr__(self):
        return f"{self.name}: {self.grade}"

def quicksort_students(students):
    """
    Ordena a lista de objetos Student pelo atributo 'grade' usando QuickSort.
    """
    if len(students) <= 1:
        return students

    # Escolhe o pivô: nesse exemplo, o primeiro elemento
    pivot = students[0].grade
    left = [s for s in students if s.grade < pivot]
    equal = [s for s in students if s.grade == pivot]
    right = [s for s in students if s.grade > pivot]

    return quicksort_students(left) + equal + quicksort_students(right)

def main():
    # Cria uma lista de estudantes com nomes e notas aleatórias
    names = ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank", "Grace", "Heidi"]
    students = [Student(name, random.randint(0, 100)) for name in names]

    print("Lista original:")
    for student in students:
        print(student)

    sorted_students = quicksort_students(students)

    print("\nLista ordenada por nota:")
    for student in sorted_students:
        print(student)

if __name__ == "__main__":
    main()

