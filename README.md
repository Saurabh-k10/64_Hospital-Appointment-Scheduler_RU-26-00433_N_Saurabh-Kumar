# 🏥 Hospital Appointment Scheduler (PS 64)

A Python-based console application designed to manage hospital appointments efficiently. It allows users to book, view, reschedule, and cancel patient appointments while checking date validity and doctor slot availability.

## 👨‍💻 Student Details

| Field | Details |
|---|---|
| **Name** | Saurabh Kumar |
| **ERP Number** | RU-26-00433 |
| **Course** | B.Tech – CSE Core |
| **Section** | N |
| **Session** | 2026–27 |
| **University** | Rungta International Skills University |
| **Problem Statement** | PS 64 |
| **Semester** | First Semester |

## 📌 Project Overview

The Hospital Appointment Scheduler is a menu-driven Python application developed for clinic receptionists to manage patient appointments.

The system stores appointment information in a Python dictionary and automatically generates unique appointment IDs starting from `A101`.

## ✨ Features

- ➕ **Add Appointment:** Book a new patient appointment.
- 📋 **View All:** Display all booked appointments.
- 🔄 **Reschedule:** Change an existing appointment's date and time.
- ❌ **Cancel:** Cancel an appointment using its ID.
- 📅 **Date Validation:** Validate dates using Python's datetime module.
- ⏰ **Time Validation:** Check the entered time format.
- 🚫 **Slot Availability:** Prevent duplicate appointments for the same doctor, date, and time.
- 🆔 **Automatic ID Generation:** Generate IDs such as A101, A102, A103.

## 🛠️ Technologies Used

- Python 3
- datetime module
- Dictionaries
- Functions
- Loops and Conditional Statements
- CRUD Operations

## 📂 Project Structure

```text
PS64_Hospital_Appointment_Scheduler/
│
├── main.py
├── README.md
└── screenshots/
    ├── booking.png
    └── test_cases.png
```

## ▶️ How to Run the Project

**Step 1:** Clone the repository.

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

**Step 2:** Open the project folder.

```bash
cd PS64_Hospital_Appointment_Scheduler
```

**Step 3:** Run the Python program.

```bash
python3 main.py
```

## 🖥️ Application Menu

```text
--- Hospital Appointment Scheduler ---

1. Add Appointment
2. View All
3. Reschedule
4. Cancel
5. Exit

Menu option:
```

## 🧪 Test Cases

| Test Case | Description | Expected Result |
|---|---|---|
| TC 1 | Normal appointment booking | Appointment A101 booked |
| TC 2 | Boundary time booking (16:30) | Appointment A102 booked |
| TC 3(a) | Duplicate doctor slot | Slot unavailable |
| TC 3(b) | Invalid date (31-11-2026) | Invalid date message |
| TC 4(a) | Reschedule appointment A101 | Appointment updated |
| TC 4(b) | Cancel appointment A102 | Appointment cancelled |
| TC 4(c) | View all appointments | Updated appointment list |

## 📸 Project Screenshots

Screenshots of the program execution and test cases are included in the `screenshots` folder.

## 📚 Learning Outcomes

Through this project, I learned:

- How to use Python dictionaries to store data.
- How to create and use functions.
- How to implement CRUD operations.
- How to validate dates and times using datetime.
- How to use loops and conditional statements.
- How to identify and prevent duplicate appointment slots.
- How to test and debug a Python application.

## 🚀 Future Improvements

- Add permanent data storage using files or a database.
- Develop a graphical user interface.
- Add patient search functionality.
- Improve appointment validation and scheduling.

## 👨‍🎓 Developed By

**Saurabh Kumar**  
B.Tech – Computer Science and Engineering (CSE Core)  
Rungta International Skills University  
Session: 2026–27

---

⭐ If you find this project useful, feel free to explore the repository!
