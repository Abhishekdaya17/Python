def generate_bill():

    pid = input("Enter Patient ID: ")

    consultation = float(input("Enter Consultation Charges: "))
    medicine = float(input("Enter Medicine Cost: "))
    test = float(input("Enter Test Charges: "))

    total = consultation + medicine + test

    print("\n------ BILL ------")
    print("Patient ID :", pid)
    print("Consultation :", consultation)
    print("Medicine :", medicine)
    print("Test :", test)
    print("----------------------")
    print("Total Bill :", total)