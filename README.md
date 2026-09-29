# Student-Management-and-Performance-Analysis-System-Using-Python-and-Streamlit

# Student Management and Performance Analysis System

A comprehensive Python-based web application developed using **Streamlit**, **Pandas**, **NumPy**, **Matplotlib**, and **Seaborn** to manage student academic records, calculate performance metrics, and visualize academic data.

Developed as a part of Project-Based Learning (PBL - Report 3) for the subject **Python for Data Science (BE05000231)** at **C. K. Pithawalla College of Engineering and Technology, Surat**, affiliated with **Gujarat Technological University (GTU)**.

---

## 👨‍🎓 Author Details
* **Enrolment No:** 240090107175
* **Name:** Rana Daksh Dineshbhai
* **Branch/Sem:** Computer Engineering, B.E. III (Semester V)
* **Division:** C
* **Academic Year:** 2026-27

---

## 📋 Table of Contents
1. [Abstract](#-abstract)
2. [Introduction](#-introduction)
3. [Problem Statement](#-problem-statement)
4. [Objectives](#-objectives)
5. [Technologies Used](#-technologies-used)
6. [System Requirements](#-system-requirements)
7. [Dataset Description](#-dataset-description)
8. [System Modules](#-system-modules)
9. [System Implementation & Code Snippets](#-system-implementation--code-snippets)
10. [Data Analysis & Visualization](#-data-analysis--visualization)
11. [Beyond-Syllabus Topic: Streamlit](#-beyond-syllabus-topic-streamlit)
12. [Results & Outputs](#-results--outputs)
13. [Advantages & Limitations](#-advantages--limitations)
14. [Future Scope](#-future-scope)
15. [Conclusion](#-conclusion)
16. [References & Resources](#-references--resources)

---

## 📌 Abstract
The **Student Management and Performance Analysis System** is a Python application developed to manage student academic records and perform exploratory data analysis. The system stores student information in a CSV file (`students.csv`) and utilizes **Pandas** for efficient data manipulation, querying, and updating.

The application provides complete CRUD (Create, Read, Update, Delete) operations. It automatically calculates total marks, percentages, and letter grades based on performance in three core subjects: **Python**, **Mathematics**, and **Data Science**, while also tracking student attendance.

A built-in **Data Analysis** module computes descriptive statistics (total students, average percentages, highest/lowest scores, and average subject marks). **Matplotlib** and **Seaborn** generate graphical insights, and **Streamlit** powers a clean, interactive single-page web interface.

---

## 💡 Introduction
Educational institutions handle vast amounts of student data, including ID details, branch information, semester records, subject marks, and attendance percentages. Manual record management is prone to errors and time-consuming. 

This project delivers a computerized solution using Python and data science libraries to automate record management, performance calculation, and visual analytics through an intuitive browser-based interface.

---

## ⚠️ Problem Statement
Manual record keeping leads to inefficiencies in:
* Storing and retrieving student records securely.
* Searching for individual students by ID.
* Modifying incorrect marks or updating attendance.
* Calculating aggregate totals, percentages, and grading scales.
* Generating visual performance trends across subjects and classes.

**Solution:** A lightweight, Python-driven Streamlit application backed by Pandas and CSV storage that automates all administrative and analytical tasks.

---

## 🎯 Objectives
* Develop an intuitive Student Management System in Python.
* Persist student data efficiently using structured CSV files.
* Leverage **Pandas** for data manipulation and **NumPy** for numerical processing.
* Implement full CRUD operations: Add, Search, Update, and Delete.
* Automate total marks, percentage calculation, and grade assignment.
* Compute statistical summaries and render performance visualizations.
* Integrate **Streamlit** as a beyond-syllabus web framework.

---

## 🛠️ Technologies Used
| Technology | Purpose |
| :--- | :--- |
| **Python** | Core programming language for application logic and processing. |
| **Pandas** | Tabular data manipulation, CSV reading/writing, and querying. |
| **NumPy** | Numerical data processing and array operations. |
| **Matplotlib** | Plotting subject averages and percentage distribution charts. |
| **Seaborn** | Advanced statistical visualization for grade distributions. |
| **Streamlit** | Building the interactive single-page web application interface. |
| **CSV (students.csv)** | Lightweight file-based storage backend for 25 student records. |

---

## 💻 System Requirements
* **Hardware:** Modern processor, minimum 4 GB RAM, 500 MB free storage.
* **Software:** Windows / Linux / macOS, Python 3.x, Visual Studio Code (or any Python IDE).
* **Python Libraries:** `streamlit`, `pandas`, `numpy`, `matplotlib`, `seaborn`.
* **Browser:** Any modern web browser to view the Streamlit interface.

---

## 📊 Dataset Description
The system includes a dataset of **25 student records** stored in `students.csv`.

| Field Name | Description | Data Type |
| :--- | :--- | :--- |
| `Student_ID` | Unique enrolment identifier | String / Integer |
| `Name` | Full name of the student | String |
| `Branch` | Academic branch (Computer / IT) | String |
| `Semester` | Current academic semester | Integer |
| `Python` | Python marks (Out of 100) | Float / Integer |
| `Mathematics` | Mathematics marks (Out of 100) | Float / Integer |
| `Data_Science` | Data Science marks (Out of 100) | Float / Integer |
| `Attendance` | Attendance percentage | Float |
| `Total` | Sum of three subject marks | Float |
| `Percentage` | Average score across subjects | Float |
| `Grade` | Letter grade assigned | String |

---

## 📦 System Modules
1. **Record Display:** Displays all current student records in a formatted table upon loading.
2. **Add Student:** Captures student details, calculates totals, percentages, and grades, and appends to CSV.
3. **Search Student:** Quick lookup of student records using their unique `Student_ID`.
4. **Update Student:** Modifies existing subject scores and attendance, automatically recalculating totals and grades.
5. **Delete Student:** Removes student records cleanly using their `Student_ID`.
6. **Data Analysis Module:** Computes total student count, class average percentage, attendance averages, and score extremes.
7. **Data Visualization Module:** Renders interactive graphs for subject averages, percentage spreads, and grade allocations.

---

## ⚙️ System Implementation & Code Snippets

### 1. Adding a Student Record
```python
total = python_marks + maths_marks + ds_marks
percentage = total / 3

new_row = {
    "Student_ID": student_id,
    "Name": name,
    "Branch": branch,
    "Semester": semester,
    "Python": python_marks,
    "Mathematics": maths_marks,
    "Data_Science": ds_marks,
    "Attendance": attendance,
    "Total": total,
    "Percentage": percentage,
    "Grade": get_grade(percentage)
}

df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
df.to_csv(FILE, index=False)
```

### 2. Searching for a Student
```python
result = df[df["Student_ID"].astype(str) == student_id]

if result.empty:
    st.warning("Student not found.")
else:
    st.table(result)
```

### 3. Updating Student Records
```python
total = python_marks + maths_marks + ds_marks
percentage = total / 3

df.loc[idx, "Python"] = python_marks
df.loc[idx, "Mathematics"] = maths_marks
df.loc[idx, "Data_Science"] = ds_marks
df.loc[idx, "Attendance"] = attendance
df.loc[idx, "Total"] = total
df.loc[idx, "Percentage"] = percentage
df.loc[idx, "Grade"] = get_grade(percentage)

df.to_csv(FILE, index=False)
```

### 4. Deleting a Record
```python
if student_id not in df["Student_ID"].astype(str).values:
    st.warning("Student not found.")
else:
    df = df[df["Student_ID"].astype(str) != student_id]
    df.to_csv(FILE, index=False)
    st.success("Student deleted successfully.")
```

---

## 📈 Data Analysis & Visualization
The analysis module utilizes Pandas aggregation methods to output key metrics:
```python
st.metric("Total Students", len(df))
st.metric("Average Percentage", round(df["Percentage"].mean(), 2))
st.metric("Average Attendance", round(df["Attendance"].mean(), 2))
st.metric("Highest Percentage", round(df["Percentage"].max(), 2))
st.metric("Lowest Percentage", round(df["Percentage"].min(), 2))
```

### Visualizations Provided:
1. **Average Subject Marks:** Compares mean performance across Python, Mathematics, and Data Science.
2. **Percentage Distribution:** Displays the spread of student percentages across the class.
3. **Grade Distribution:** Visualizes the count of students achieving each grade category.

---

## 🚀 Beyond-Syllabus Topic – Streamlit
**Streamlit** was integrated as the beyond-syllabus component to transform a command-line script into an interactive web application.

### Why Streamlit?
* Eliminates complex HTML/JS frontend requirements.
* Provides native Python widgets (`st.text_input`, `st.number_input`, `st.selectbox`, `st.button`, `st.table`, `st.pyplot`).
* Enables instant browser deployment and local execution.

### Running the Application
1. Place `app.py` and `students.csv` in the same directory.
2. Open your terminal / VS Code command prompt.
3. Run the following command:
   ```bash
   streamlit run app.py
   ```

---

## 📥 Project Files & Resources
* **Source Code (`app.py`):** [Download / View app.py](https://drive.google.com/file/d/1McwPVYzGic-iE7m7sAx6lL0Ti06rP-CT/view?usp=sharing)
* **Dataset (`students.csv`):** [Download / View students.csv](https://drive.google.com/file/d/1Sa3kPea6GXwous4nIKDFpQl56lKOg3w1/view?usp=sharing)

---

## ✨ Advantages & Limitations

### Advantages
* Clean, responsive single-page web interface.
* Persistent file storage via CSV.
* Automated calculations for totals, percentages, and grades.
* Rich visual analytics using Matplotlib and Seaborn.
* Lightweight setup suitable for academic project-based learning.

### Limitations
* Relies on a flat CSV file instead of a relational database (SQL).
* Lacks user authentication and role-based access control (Admin vs. Student).
* Basic error handling and input validation.

---

## 🔮 Future Scope
* Integrate MySQL or PostgreSQL database connectivity.
* Implement user login and role-based access control.
* Add support for downloadable PDF and Excel performance reports.
* Expand grading rules and support additional subjects.
* Deploy the application to cloud hosting platforms (Streamlit Community Cloud).

---

## 📝 Conclusion
The Student Management and Performance Analysis System successfully demonstrates the integration of Python programming, data manipulation, statistical analysis, and web framework technologies. By automating record keeping and incorporating visual analytics, the application fulfills all requirements for an effective academic PBL project.

---

## 📚 References & Documentation
1. Python Software Foundation. *Python Documentation*. [https://docs.python.org/3/](https://docs.python.org/3/)
2. Pandas Documentation. [https://pandas.pydata.org/docs/](https://pandas.pydata.org/docs/)
3. NumPy Documentation. [https://numpy.org/doc/](https://numpy.org/doc/)
4. Matplotlib Documentation. [https://matplotlib.org/stable/](https://matplotlib.org/stable/)
5. Seaborn Documentation. [https://seaborn.pydata.org/](https://seaborn.pydata.org/)
6. Streamlit Documentation. [https://docs.streamlit.io/](https://docs.streamlit.io/)
7. GTU Python for Data Science Syllabus and PBL Guidelines (2026-27).
