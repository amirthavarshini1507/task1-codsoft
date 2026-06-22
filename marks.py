print("===== STUDENT RESULT MANAGEMENT SYSTEM =====")

students = []

while True:

    print("\n1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Calculate Average")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        name = input("Enter Student Name: ")

        mark1 = int(input("Enter Mark 1: "))
        mark2 = int(input("Enter Mark 2: "))
        mark3 = int(input("Enter Mark 3: "))

        total = mark1 + mark2 + mark3
        average = total / 3

        if average >= 90:
            grade = "A+"
        elif average >= 80:
            grade = "A"
        elif average >= 70:
            grade = "B"
        elif average >= 60:
            grade = "C"
        else:
            grade = "D"

        student = {
            "name": name,
            "mark1": mark1,
            "mark2": mark2,
            "mark3": mark3,
            "total": total,
            "average": average,
            "grade": grade
        }

        students.append(student)

        print("Student Added Successfully!")

    elif choice == "2":

        if len(students) == 0:
            print("No Students Found")

        else:
            print("\n----- STUDENT RECORDS -----")

            for s in students:

                print("\nName:", s["name"])
                print("Mark 1:", s["mark1"])
                print("Mark 2:", s["mark2"])
                print("Mark 3:", s["mark3"])
                print("Total:", s["total"])
                print("Average:", round(s["average"], 2))
                print("Grade:", s["grade"])

    elif choice == "3":

        search_name = input("Enter Student Name: ")

        found = False

        for s in students:

            if s["name"].lower() == search_name.lower():

                print("\nStudent Found")
                print("Name:", s["name"])
                print("Total:", s["total"])
                print("Average:", round(s["average"], 2))
                print("Grade:", s["grade"])

                found = True

        if found == False:
            print("Student Not Found")

    elif choice == "4":

        if len(students) == 0:
            print("No Student Data Available")

        else:

            grand_total = 0

            for s in students:
                grand_total = grand_total + s["average"]

            class_average = grand_total / len(students)

            print("Class Average:", round(class_average, 2))

    elif choice == "5":

        print("Thank You!")
        break

    else:
        print("Invalid Choice")