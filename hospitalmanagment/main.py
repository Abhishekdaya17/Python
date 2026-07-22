from patient.patient_module import *
from doctor.doctor import *
from appointment import *
from billing.billing import *

while True:

    print("""
========== Hospital Management System ==========

1. Add Patient

2. Display Patients

3. Search Patient

4. Add Doctor

5. Display Doctors

6. Book Appointment

7. Show Appointments

8. Generate Bill

9. Exit

""")

    choice = int(input("Enter Choice : "))

    match choice:

        case 1:
            add_patient()

        case 2:
            display_patients()

        case 3:
            search_patient()

        case 4:
            add_doctor()

        case 5:
            display_doctors()

        case 6:
            book_appointment()
        

        case 7:
            show_appointments()

        case 8:
            generate_bill()

        case 9:
            print("Thank You...")
            break

        case _:
            print("Invalid Choice") 