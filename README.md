# 🎓 Student Management and Performance Analysis System

A Python-based single-page web application built for managing student academic records, automating performance calculations, running exploratory data analysis, and visualizing trends[span_1](start_span)[span_1](end_span). 

Developed as part of the **Python for Data Science (BE05000231)** Project-Based Learning (PBL - Report 3) curriculum at **C. K. Pithawalla College of Engineering and Technology, Surat**, under **Gujarat Technological University (GTU)**[span_2](start_span)[span_2](end_span).

---

## 📌 Project Description
The **Student Management and Performance Analysis System** is designed to streamline how educational institutions and instructors handle student information[span_3](start_span)[span_3](end_span). Traditionally, managing student records, calculating total marks, determining percentages, tracking attendance, and generating performance graphs manually are tedious and error-prone tasks[span_4](start_span)[span_4](end_span). 

This project provides an automated, lightweight, and user-friendly web interface that performs complete **CRUD operations** (Create, Read, Update, Delete) on student records, computes descriptive statistics, and presents academic trends visually[span_5](start_span)[span_5](end_span).

---

## ✨ Features
* **Interactive Record Management:** Instantly view all student records in a clean tabular format upon loading[span_6](start_span)[span_6](end_span).
* **Automated Calculations:** Automatically computes total marks, percentage averages, and letter grades as soon as subject scores are entered[span_7](start_span)[span_7](end_span).
* **Student Search (`Student_ID`):** Quickly look up specific student records using their unique enrolment identifier[span_8](start_span)[span_8](end_span).
* **Record Updates & Deletion:** Easily modify existing scores or remove outdated records, with automatic recalculation of performance metrics[span_9](start_span)[span_9](end_span).
* **Built-in Statistical Analysis:** Generates class summaries, including total student count, class average percentage, attendance averages, and score extremes[span_10](start_span)[span_10](end_span).

---

## 🛠️ Technologies Used
* **Programming Language:** Python[span_11](start_span)[span_11](end_span)
* **Data Manipulation & Processing:** Pandas[span_12](start_span)[span_12](end_span), NumPy[span_13](start_span)[span_13](end_span)
* **Data Visualization:** Matplotlib[span_14](start_span)[span_14](end_span), Seaborn[span_15](start_span)[span_15](end_span)
* **Web Interface Framework:** Streamlit (Beyond-Syllabus Topic)[span_16](start_span)[span_16](end_span)
* **Data Storage:** CSV File (`students.csv`)[span_17](start_span)[span_17](end_span)

---

## 🚀 Beyond-Syllabus Topic: Streamlit
While standard Python console scripts are functional, they lack user-friendliness. **Streamlit** was implemented as a beyond-syllabus web framework to convert the script into a responsive, single-page browser application[span_18](start_span)[span_18](end_span). It replaces command-line prompts with native UI components such as text inputs, selection boxes, buttons, metrics, and data tables[span_19](start_span)[span_19](end_span).

---

## 🗄️ Database / Data Storage
Rather than using a complex SQL database server (which is unnecessary for a small academic PBL scope), the project utilizes a structured **CSV file (`students.csv`)** containing **25 student records**[span_20](start_span)[span_20](end_span). 
* **Pandas** acts as the data connector, reading from and writing back changes directly to `students.csv` to ensure data persistence across sessions[span_21](start_span)[span_21](end_span).

---

## 📊 Data Analysis & Visualization
The application features dedicated modules for analyzing and plotting performance data[span_22](start_span)[span_22](end_span):
* **Statistical Analysis Metrics:** Evaluates class performance metrics using Pandas aggregation functions (e.g., mean percentages, attendance averages, max/min scores)[span_23](start_span)[span_23](end_span).
* **Graphical Visualizations:** 
  1. *Average Subject Marks Chart:* Compares mean performance across Python, Mathematics, and Data Science using Matplotlib[span_24](start_span)[span_24](end_span).
  2. *Percentage Distribution Plot:* Visualizes how student score percentages are distributed across the class[span_25](start_span)[span_25](end_span).
  3. *Grade Distribution Chart:* Uses Seaborn to render categorical counts of student letter grades[span_26](start_span)[span_26](end_span).

---

## ⚙️ Installation & Setup Instructions

Follow these steps to set up and run the project locally on your machine:

### 1. Clone or Download the Repository
Ensure you have the project files (`app.py` and `students.csv`) in the same working directory[span_27](start_span)[span_27](end_span).

### 2. Install Python Dependencies
Open your terminal (or VS Code terminal) and install the required data science and web framework packages[span_28](start_span)[span_28](end_span):
```bash
pip install streamlit pandas numpy matplotlib seaborn
