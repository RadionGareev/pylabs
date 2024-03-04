from os import system
# Crearea dicționarului student
student = {
    "firstname": "John",
    "lastname": "Doe",
    "age": 20,
    "grade_1": 8.5,
    "grade_2": 7.3,
    "grade_3": 6.9
}
system('cls')
# Afisarea cheilor și valorilor din dicționar
for key, value in student.items():
    if key.startswith("grade"):
        print(f"{key}: {value:.2f}")
    else:
        print(f"{key}: {value}")

# Calcularea mediei celor 3 note
average_grade = (student["grade_1"] + student["grade_2"] + student["grade_3"]) / 3
print(f"Media notelor: {average_grade:.2f}")

# Verificarea dacă studentul a trecut examenul
if average_grade >= 5.00:
    print("Studentul a trecut examenul!")
else:
    print("Studentul nu a trecut examenul.")
