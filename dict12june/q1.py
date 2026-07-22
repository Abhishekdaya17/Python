# 1.ASSIGNMENT: HOSPITAL PATIENT RECORD MANAGEMENT SYSTEM:--

# A multi-specialty hospital is currently maintaining patient records manually in registers. As the number of patients is increasing, it has become difficult to search, update, and manage records efficiently.

# The hospital management has decided to develop a simple Patient Record Management System using Python. The system should store patient information in a nested dictionary where:

# Key → Patient ID
# Value → Dictionary containing patient details

# Each patient record should contain:

# Patient Name
# Age
# Gender
# Disease
# Doctor Name
# Sample Data Structure
# {
# 101:{
#     "name":"Ajay",
#     "age":35,
#     "gender":"Male",
#     "disease":"Fever",
#     "doctor":"Dr. Sharma"
# },
# 102:{
#     "name":"Ravi",
#     "age":42,
#     "gender":"Male",
#     "disease":"Diabetes",
#     "doctor":"Dr. Gupta"
# }
# }
# Menu Driven Program

# Display the following menu repeatedly until the user chooses Exit.

# =====================================
#  HOSPITAL PATIENT MANAGEMENT SYSTEM
# =====================================

# 1. Add New Patient
# 2. Search Patient
# 3. Update Patient Disease
# 4. Delete Patient Record
# 5. Display All Patients
# 6. Count Total Patients
# 7. Display Patients By Disease
# 8. Display Oldest Patient
# 9. Display Youngest Patient
# 10. Exit

# Functional Requirements
# 1. Add New Patient

# Accept the following information from the user:

# Patient ID
# Patient Name
# Age
# Gender
# Disease
# Doctor Name

# Store the record in the nested dictionary.

# Validation:
# If the Patient ID already exists, display:

# Patient ID already exists.

# 2. Search Patient

# Accept Patient ID from the user.

# If the patient exists, display complete information.

# Sample Output

# Patient ID : 101
# Name       : Ajay
# Age        : 35
# Gender     : Male
# Disease    : Fever
# Doctor     : Dr. Sharma

# If Patient ID is not found:

# Patient Record Not Found

# 3. Update Patient Disease

# Accept Patient ID.

# If found:

# Ask for new disease.
# Update the disease information.

# Sample Output

# Disease Updated Successfully
# 4. Delete Patient Record

# Accept Patient ID.

# If found:

# Remove the patient record.

# Sample Output

# Patient Record Deleted Successfully

# Otherwise:

# Patient Not Found
# 5. Display All Patients

# Display all patient records in a formatted manner.

# Sample Output

# --------------------------------
# Patient ID : 101
# Name       : Ajay
# Age        : 35
# Disease    : Fever
# Doctor     : Dr. Sharma
# --------------------------------

# Patient ID : 102
# Name       : Ravi
# Age        : 42
# Disease    : Diabetes
# Doctor     : Dr. Gupta
# 6. Count Total Patients

# Display the total number of patients currently stored.

# Sample Output

# Total Patients : 25
# 7. Display Patients By Disease

# Accept a disease name from the user.

# Display all patients suffering from that disease.

# Sample Output

# Enter Disease : Fever

# 101  Ajay
# 108  Aman
# 115  Neha

# If no patient is found:

# No Patient Found
# 8. Display Oldest Patient

# Find and display the patient having the highest age.

# Sample Output

# Oldest Patient Details

# Patient ID : 110
# Name       : Ravi
# Age        : 68
# Disease    : Diabetes
# Doctor     : Dr. Gupta
# 9. Display Youngest Patient

# Find and display the patient having the minimum age.

# Sample Output

# Youngest Patient Details

# Patient ID : 121
# Name       : Riya
# Age        : 4
# Disease    : Viral Fever
# Doctor     : Dr. Mehta
# 10. Exit

# Terminate the application.

# Sample Output

# Thank You For Using Hospital Patient Management System

d = {}

while True:
    print('''=====================================
HOSPITAL PATIENT MANAGEMENT SYSTEM
=====================================

1. Add New Patient
2. Search Patient
3. Update Patient Disease
4. Delete Patient Record
5. Display All Patients
6. Count Total Patients
7. Display Patients By Disease
8. Display Oldest Patient
9. Display Youngest Patient
10. Exit''')

    n = int(input("Enter your choice: "))

    match n:

        
        case 1:
            p_id = int(input("Enter patient id: "))

            if p_id in d:
                print("Patient ID already exists.")
            else:
                name = input("Name: ")
                age = int(input("Age: "))
                gender = input("Gender: ")
                disease = input("Disease: ")
                doctor = input("Doctor: ")

                d[p_id] = {
                    "name": name,
                    "age": age,
                    "gender": gender,
                    "disease": disease,
                    "doctor": doctor
                }

                print("Patient Added Successfully")

        
        case 2:
            p_id = int(input("Enter patient id: "))

            if p_id in d:
                print("\n--- Patient Details ---")
                print("Patient ID:", p_id)
                print("Name:", d[p_id]["name"])
                print("Age:", d[p_id]["age"])
                print("Gender:", d[p_id]["gender"])
                print("Disease:", d[p_id]["disease"])
                print("Doctor:", d[p_id]["doctor"])
            else:
                print("Patient Record Not Found")

        
        case 3:
            p_id = int(input("Enter patient id: "))

            if p_id in d:
                d[p_id]["disease"] = input("Enter new disease: ")
                print("Disease Updated Successfully")
            else:
                print("Patient Not Found")

        
        case 4:
            p_id = int(input("Enter patient id: "))

            if p_id in d:
                d.pop(p_id)
                print("Patient Record Deleted Successfully")
            else:
                print("Patient Not Found")


        case 5:
            if d:
                for k, v in d.items():
                    print("--------------------------------")
                    print("Patient ID:", k)
                    print("Name:", v["name"])
                    print("Age:", v["age"])
                    print("Gender:", v["gender"])
                    print("Disease:", v["disease"])
                    print("Doctor:", v["doctor"])
            else:
                print("No Records Found")

        
        case 6:
            print("Total Patients:", len(d))

        
        case 7:
            dis = input("Enter Disease: ")
            found = False

            for k, v in d.items():
                if v["disease"].lower() == dis.lower():
                    print(k, v["name"])
                    found = True

            if not found:
                print("No Patient Found")

        
        case 8:
            if d:
                oldest_id = None
                max_age = -1

                for k, v in d.items():
                    if v["age"] > max_age:
                        max_age = v["age"]
                        oldest_id = k

                print("\nOldest Patient Details")
                print("Patient ID:", oldest_id)
                print("Name:", d[oldest_id]["name"])
                print("Age:", d[oldest_id]["age"])
                print("Gender:", d[oldest_id]["gender"])
                print("Disease:", d[oldest_id]["disease"])
                print("Doctor:", d[oldest_id]["doctor"])
            else:
                print("No Data")

        
        case 9:
            if d:
                youngest_id = None
                min_age = 999999

                for k, v in d.items():
                    if v["age"] < min_age:
                        min_age = v["age"]
                        youngest_id = k

                print("\nYoungest Patient Details")
                print("Patient ID:", youngest_id)
                print("Name:", d[youngest_id]["name"])
                print("Age:", d[youngest_id]["age"])
                print("Gender:", d[youngest_id]["gender"])
                print("Disease:", d[youngest_id]["disease"])
                print("Doctor:", d[youngest_id]["doctor"])
            else:
                print("No Data")

        
        case 10:
            print("Thank You For Using Hospital Patient Management System")
            break            
            