appointments = []

def book_appointment():

    appointment = {}

    appointment["appointment_id"] = input("Enter Appointment ID: ")
    appointment["patient_id"] = input("Enter Patient ID: ")
    appointment["doctor_id"] = input("Enter Doctor ID: ")
    appointment["date"] = input("Enter Appointment Date: ")
    appointment["time"] = input("Enter Appointment Time: ")

    appointments.append(appointment)

    print("Appointment Booked Successfully")


def show_appointments():

    if len(appointments) == 0:
        print("No Appointments Found")
        return

    for a in appointments:
        print("----------------------")
        print("Appointment ID :", a["appointment_id"])
        print("Patient ID :", a["patient_id"])
        print("Doctor ID :", a["doctor_id"])
        print("Date :", a["date"])
        print("Time :", a["time"])