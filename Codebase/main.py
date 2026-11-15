# =======================================================
# PS64_Hospital_Appointment_Scheduler
# Student: Saurabh Kumar
# Description: Hospital Appointment Booking System
# Features: Add, View, Reschedule, Cancel, Validation
# =======================================================

from datetime import datetime

# ---- GLOBAL VARIABLES ----
appointments = {}  # Saare appointments yaha store honge
next_id_num = 101  # ID A101 se start hoga

# ---- HIDDEN TAG: DATE VALIDATION ----
# Ye function check karta hai ki date sahi hai ya nahi
# Jaise 31-11-2026 galat hai kyuki November me 30 din hote hain
def is_valid_date(date_str):
    try:
        datetime.strptime(date_str, "%d-%m-%Y")
        return True
    except ValueError:
        return False

# ---- HIDDEN TAG: TIME VALIDATION ----
def is_valid_time(time_str):
    try:
        datetime.strptime(time_str, "%H:%M")
        return True
    except ValueError:
        return False

# ---- HIDDEN TAG: SLOT AVAILABILITY CHECK ----
# Ye sabse important logic hai - Ek doctor ka ek time pe ek hi appointment
def check_slot(doctor, date, time, exclude_id=None):
    for aid, app in appointments.items():
        if exclude_id and aid == exclude_id:
            continue
        # Agar same doctor, same date, same time pehle se hai to False
        if app['doctor'] == doctor and app['date'] == date and app['time'] == time:
            return False
    return True

# ---- HIDDEN TAG: 1. ADD APPOINTMENT (Test Case 1 & 2) ----
def add_appointment():
    global next_id_num
    patient = input("Patient: ").strip()
    doctor = input("Doctor: ").strip()
    date = input("Date: ").strip()
    time = input("Time: ").strip()

    # Date validation - Test Case 3(b) ke liye
    if not is_valid_date(date):
        print("Invalid date. Please enter the date as DD-MM-YYYY.")
        return

    if not is_valid_time(time):
        print("Invalid time. Please enter the time as HH:MM.")
        return

    # Slot check - Test Case 3(a) ke liye
    if not check_slot(doctor, date, time):
        print(f"Slot unavailable : {doctor} already has a appointment on {date} at {time}.")
        return

    # Sab sahi hai to ID banao A101, A102...
    app_id = f"A{next_id_num}"
    next_id_num += 1
    appointments[app_id] = {
        'patient': patient,
        'doctor': doctor,
        'date': date,
        'time': time
    }
    print(f"Appointment booked. ID: {app_id} | {patient} | {doctor} | {date} {time}")

# ---- HIDDEN TAG: 2. VIEW ALL APPOINTMENTS ----
def view_all():
    if not appointments:
        print("No appointments.")
        return
    for aid, app in appointments.items():
        print(f"{aid} | {app['patient']} | {app['doctor']} | {app['date']} {app['time']}")
    print(f"Total appointments: {len(appointments)}")

# ---- HIDDEN TAG: 3. RESCHEDULE (Test Case 4a) ----
def reschedule():
    app_id = input("Appointment ID: ").strip()
    if app_id not in appointments:
        print("Appointment ID not found.")
        return
    
    new_date = input("New Date: ").strip()
    new_time = input("New Time: ").strip()

    if not is_valid_date(new_date):
        print("Invalid date. Please enter the date as DD-MM-YYYY.")
        return
    
    doctor = appointments[app_id]['doctor']
    if not check_slot(doctor, new_date, new_time, exclude_id=app_id):
        print(f"Slot unavailable : {doctor} already has a appointment on {new_date} at {new_time}.")
        return

    appointments[app_id]['date'] = new_date
    appointments[app_id]['time'] = new_time
    print(f"Appointment {app_id} rescheduled to {new_date} {new_time}")

# ---- HIDDEN TAG: 4. CANCEL (Test Case 4b) ----
def cancel():
    app_id = input("Appointment ID: ").strip()
    if app_id not in appointments:
        print("Appointment ID not found.")
        return
    del appointments[app_id]
    print(f"Appointment {app_id} cancelled.")

# ---- MAIN MENU DRIVER CODE ----
def main():
    while True:
        print("\n---Hospital Appointment Scheduler ---")
        print("1. Add Appointment")
        print("2. View all")
        print("3. Reschedule")
        print("4. Cancel")
        print("5. Exit")
        choice = input("Menu option: ").strip()

        if choice == '1':
            add_appointment()
        elif choice == '2':
            view_all()
        elif choice == '3':
            reschedule()
        elif choice == '4':
            cancel()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()



