Student Management and Performance Analysis System Using Python and Streamlit

Project Description

The Student Management and Performance Analysis System is a Python-based application developed to manage student academic records and perform basic data analysis.

The system stores student information in a CSV file named "students.csv" and uses Pandas for reading, searching, updating, deleting, and processing student records. It automatically calculates total marks, percentage, and grade based on Python, Mathematics, and Data Science marks.

The project also provides performance analysis and graphical visualization using Matplotlib and Seaborn. Streamlit is used to convert the Python program into a simple single-page web application.

---

Features

- Display all student records.
- Add new student records.
- Search students using Student ID.
- Update existing student information.
- Delete student records.
- Automatically calculate total marks.
- Automatically calculate percentage.
- Automatically generate grades.
- Calculate average percentage.
- Calculate average attendance.
- Find highest and lowest percentage.
- Calculate average marks for each subject.
- Display grade distribution.
- Generate performance graphs.
- Store updated records in "students.csv".
- Simple single-page web interface using Streamlit.

---

Technology Used

Technology| Purpose
Python| Main programming language
Pandas| Data handling and CSV processing
NumPy| Numerical processing
Matplotlib| Data visualization and graphs
Seaborn| Statistical visualization
Streamlit| Web-based user interface
CSV| Student data storage

---

Beyond-Syllabus Topic

Streamlit

Streamlit is used as the beyond-syllabus topic in this project.

Streamlit allows the Python application to be converted into an interactive web-based application without requiring a separate front-end framework.

The project uses Streamlit for:

- Application title and headings
- Text input
- Number input
- Selection controls
- Buttons
- Tables
- DataFrames
- Success and error messages
- Performance metrics
- Graph display

The application can be started using:

streamlit run app.py

---

Database / Data Storage

The current project does not use a traditional database such as MySQL, MongoDB, or PostgreSQL.

Instead, student records are stored in a CSV file:

students.csv

Pandas is used to read, modify, and save the CSV data.

Dataset Fields

Field| Description
Student_ID| Unique student identifier
Name| Student name
Branch| Student branch
Semester| Current semester
Python| Python marks
Mathematics| Mathematics marks
Data_Science| Data Science marks
Attendance| Attendance percentage
Total| Total marks
Percentage| Average percentage
Grade| Automatically generated grade

The dataset contains 25 student records.

---

Data Analysis

The system performs basic descriptive data analysis using Pandas and NumPy.

The following information is calculated:

- Total number of students
- Average percentage
- Average attendance
- Highest percentage
- Lowest percentage
- Average Python marks
- Average Mathematics marks
- Average Data Science marks
- Number of students in each grade category

Performance Calculation

Total marks are calculated as:

total = python_marks + maths_marks + ds_marks

Percentage is calculated as:

percentage = total / 3

The grade is then generated automatically according to the percentage.

---

Data Visualization

The project uses Matplotlib and Seaborn for data visualization.

The application provides three main visualizations.

1. Average Subject Marks

Compares the average marks obtained in:

- Python
- Mathematics
- Data Science

2. Percentage Distribution

Displays the distribution of student percentages in the dataset.

3. Grade Distribution

Displays the number of students in each grade category.

These graphs make the numerical analysis easier to understand.

---

Machine Learning

Machine Learning is not implemented in the current version of the project.

The current project focuses on:

- Data management
- Data processing
- Descriptive analysis
- Statistical calculations
- Data visualization
- Streamlit application development

Future Machine Learning Scope

Machine Learning can be added in a future version for:

- Student performance prediction
- Grade prediction
- Performance classification
- At-risk student identification

Possible algorithms include:

- Linear Regression
- Logistic Regression
- Decision Tree
- Random Forest

These Machine Learning algorithms are not used in the current implementation.

---

Installation

1. Install Python

Install Python 3.x on your computer.

Check the installation using:

python --version

---

2. Open the Project

Open the project folder in Visual Studio Code.

The folder should contain:

Student-Management-System/
│
├── app.py
├── students.csv
└── README.md

---

3. Install Required Libraries

Open the VS Code terminal and run:

pip install streamlit pandas numpy matplotlib seaborn

---

4. Run the Application

Run the following command:

streamlit run app.py

The Streamlit application will open in a web browser.

---

5. Important

Keep "app.py" and "students.csv" in the same folder.

Project Folder
│
├── app.py
└── students.csv

This is required because the application reads and updates student data from "students.csv".
