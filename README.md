# 🎓 Semester Setup Automation

A simple Python project that helps students **automatically create a folder structure** for their semester.
It saves time and keeps your subjects organized with subfolders like **Books, Notes, Projects, and Assignments**.

---

## ✨ Features

* Create a main folder for the semester.
* Add multiple subjects (comma-separated).
* Each subject contains organized subfolders:

  * `Books`
  * `Notes`
  * `Projects`
  * `Assignments`
* Automatically replaces invalid characters in folder names.

---

## 📂 Files

* **`config.py`** → Configuration (base directory, subfolders, sanitization rules).
* **`structure.py`** → Main script to build the semester folder structure.

---

## 🛠️ How It Works

1. Run the Python script (`structure.py`).
2. Enter your semester name (e.g., `Semester 5`).
3. Enter your subjects (comma-separated, e.g., `OOAD, Web, OS`).
4. Done! A complete folder structure is created on your computer.

**Example Structure:**

```
D:\
└── Semester 5
    ├── OOAD
    │   ├── Books
    │   ├── Notes
    │   ├── Projects
    │   └── Assignments
    ├── OS
    │   ├── Books
    │   ├── Notes
    │   ├── Projects
    │   └── Assignments
    └── Web
        ├── Books
        ├── Notes
        ├── Projects
        └── Assignments
```

---

## 📌 Example Run

```
Enter Semester Name: Semester 4
Enter subjects (comma separated): DSA, DBMS, OS

✅ Semester setup created at: D:\Semester 4
```
