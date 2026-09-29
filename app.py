import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

FILE = "students.csv"

columns = [
    "Student_ID", "Name", "Branch", "Semester",
    "Python", "Mathematics", "Data_Science",
    "Attendance", "Total", "Percentage", "Grade"
]

# Load CSV
if os.path.exists(FILE):
    df = pd.read_csv(FILE)
else:
    df = pd.DataFrame(columns=columns)

# Page setup
st.set_page_config(
    page_title="Student Management System",
    layout="wide"
)

st.title("Student Management System")

# =================================================
# STUDENT RECORDS
# =================================================

st.header("Student Records")

if len(df) > 0:
    st.table(df)
else:
    st.write("No student records available.")

st.divider()

# =================================================
# OPERATIONS
# =================================================

st.header("Operations")

operation = st.radio(
    "Select Operation",
    [
        "Add",
        "Search",
        "Update",
        "Delete",
        "Analysis",
        "Graph"
    ],
    horizontal=True
)

# =================================================
# ADD STUDENT
# =================================================

if operation == "Add":

    st.subheader("Add Student")

    student_id = st.text_input("Student ID")
    name = st.text_input("Name")

    branch = st.selectbox(
        "Branch",
        ["Computer", "IT"]
    )

    semester = st.number_input(
        "Semester",
        min_value=1,
        max_value=8,
        value=5
    )

    python_marks = st.number_input(
        "Python Marks",
        min_value=0,
        max_value=100,
        value=0
    )

    mathematics = st.number_input(
        "Mathematics Marks",
        min_value=0,
        max_value=100,
        value=0
    )

    data_science = st.number_input(
        "Data Science Marks",
        min_value=0,
        max_value=100,
        value=0
    )

    attendance = st.number_input(
        "Attendance",
        min_value=0,
        max_value=100,
        value=0
    )

    if st.button("Add Student"):

        if student_id == "" or name == "":
            st.error("Please enter Student ID and Name.")

        elif student_id in df["Student_ID"].astype(str).values:
            st.error("Student ID already exists.")

        else:

            total = (
                python_marks +
                mathematics +
                data_science
            )

            percentage = total / 3

            if percentage >= 90:
                grade = "A+"
            elif percentage >= 80:
                grade = "A"
            elif percentage >= 70:
                grade = "B"
            elif percentage >= 60:
                grade = "C"
            elif percentage >= 50:
                grade = "D"
            else:
                grade = "F"

            new_student = {
                "Student_ID": student_id,
                "Name": name,
                "Branch": branch,
                "Semester": semester,
                "Python": python_marks,
                "Mathematics": mathematics,
                "Data_Science": data_science,
                "Attendance": attendance,
                "Total": total,
                "Percentage": round(percentage, 2),
                "Grade": grade
            }

            df = pd.concat(
                [df, pd.DataFrame([new_student])],
                ignore_index=True
            )

            df.to_csv(FILE, index=False)

            st.success("Student added successfully.")

            st.rerun()

# =================================================
# SEARCH STUDENT
# =================================================

elif operation == "Search":

    st.subheader("Search Student")

    search_id = st.text_input("Enter Student ID")

    if st.button("Search"):

        result = df[
            df["Student_ID"].astype(str) == search_id
        ]

        if len(result) > 0:
            st.table(result)
        else:
            st.error("Student not found.")

# =================================================
# UPDATE STUDENT
# =================================================

elif operation == "Update":

    st.subheader("Update Student")

    update_id = st.text_input("Enter Student ID")

    if st.button("Find Student"):

        result = df[
            df["Student_ID"].astype(str) == update_id
        ]

        if len(result) > 0:
            st.session_state["update_id"] = update_id
        else:
            st.error("Student not found.")

    if "update_id" in st.session_state:

        sid = st.session_state["update_id"]

        index = df[
            df["Student_ID"].astype(str) == sid
        ].index[0]

        current = df.loc[index]

        name = st.text_input(
            "Name",
            value=str(current["Name"])
        )

        python_marks = st.number_input(
            "Python Marks",
            0,
            100,
            int(current["Python"])
        )

        mathematics = st.number_input(
            "Mathematics Marks",
            0,
            100,
            int(current["Mathematics"])
        )

        data_science = st.number_input(
            "Data Science Marks",
            0,
            100,
            int(current["Data_Science"])
        )

        attendance = st.number_input(
            "Attendance",
            0,
            100,
            int(current["Attendance"])
        )

        if st.button("Update Student"):

            total = (
                python_marks +
                mathematics +
                data_science
            )

            percentage = total / 3

            if percentage >= 90:
                grade = "A+"
            elif percentage >= 80:
                grade = "A"
            elif percentage >= 70:
                grade = "B"
            elif percentage >= 60:
                grade = "C"
            elif percentage >= 50:
                grade = "D"
            else:
                grade = "F"

            df.loc[index, "Name"] = name
            df.loc[index, "Python"] = python_marks
            df.loc[index, "Mathematics"] = mathematics
            df.loc[index, "Data_Science"] = data_science
            df.loc[index, "Attendance"] = attendance
            df.loc[index, "Total"] = total
            df.loc[index, "Percentage"] = round(
                percentage, 2
            )
            df.loc[index, "Grade"] = grade

            df.to_csv(FILE, index=False)

            del st.session_state["update_id"]

            st.success("Student updated successfully.")

            st.rerun()

# =================================================
# DELETE STUDENT
# =================================================

elif operation == "Delete":

    st.subheader("Delete Student")

    delete_id = st.text_input("Enter Student ID")

    if st.button("Delete Student"):

        if delete_id in df["Student_ID"].astype(str).values:

            df = df[
                df["Student_ID"].astype(str) != delete_id
            ]

            df.to_csv(FILE, index=False)

            st.success("Student deleted successfully.")

            st.rerun()

        else:
            st.error("Student not found.")

# =================================================
# ANALYSIS
# =================================================

elif operation == "Analysis":

    st.subheader("Student Analysis")

    if len(df) > 0:

        st.write(
            "Total Students:",
            len(df)
        )

        st.write(
            "Average Percentage:",
            round(df["Percentage"].mean(), 2)
        )

        st.write(
            "Average Attendance:",
            round(df["Attendance"].mean(), 2)
        )

        st.write(
            "Highest Percentage:",
            round(df["Percentage"].max(), 2)
        )

        st.write(
            "Lowest Percentage:",
            round(df["Percentage"].min(), 2)
        )

        st.write(
            "Average Python Marks:",
            round(df["Python"].mean(), 2)
        )

        st.write(
            "Average Mathematics Marks:",
            round(df["Mathematics"].mean(), 2)
        )

        st.write(
            "Average Data Science Marks:",
            round(df["Data_Science"].mean(), 2)
        )

        st.subheader("Grade Count")

        grade_count = df["Grade"].value_counts()

        st.table(grade_count)

    else:
        st.write("No data available.")

# =================================================
# GRAPH
# =================================================

elif operation == "Graph":

    st.subheader("Graphs")

    if len(df) > 0:

        # Average Subject Marks
        st.write("Average Subject Marks")

        subjects = [
            "Python",
            "Mathematics",
            "Data Science"
        ]

        averages = [
            df["Python"].mean(),
            df["Mathematics"].mean(),
            df["Data_Science"].mean()
        ]

        fig, ax = plt.subplots()

        ax.bar(subjects, averages)

        ax.set_xlabel("Subjects")
        ax.set_ylabel("Average Marks")
        ax.set_title("Average Subject Marks")

        st.pyplot(fig)

        # Percentage Distribution
        st.write("Percentage Distribution")

        fig, ax = plt.subplots()

        ax.hist(df["Percentage"], bins=5)

        ax.set_xlabel("Percentage")
        ax.set_ylabel("Students")
        ax.set_title("Percentage Distribution")

        st.pyplot(fig)

        # Grade Distribution
        st.write("Grade Distribution")

        grade_count = df["Grade"].value_counts()

        fig, ax = plt.subplots()

        sns.barplot(
            x=grade_count.index,
            y=grade_count.values,
            ax=ax
        )

        ax.set_xlabel("Grade")
        ax.set_ylabel("Students")
        ax.set_title("Grade Distribution")

        st.pyplot(fig)

    else:
        st.write("No data available.")

st.divider()

st.caption("Python for Data Science - PBL 3")