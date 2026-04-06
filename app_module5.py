import streamlit as st
import time
import json
from pathlib import Path
import uuid

st.set_page_config(
    page_title = "Course Management",
    layout = "centered",
    initial_sidebar_state = "collapsed"
)

st.title("Course Management App")
st.divider()

# loading data

assignments = [
    {
        "id": "HW1",
        "title": "Intro to Database",
        "description": "basics of database design",
        "points": 100,
        "type": "homework"
    },
    {
        "id": "HW2",
        "title": "Normalization",
        "description": "normalizing",
        "points": 100,
        "type": "homework"
    }
]

json_path = Path("assignments.json")

# Load the data from a json file if it exists

def load_data(json_path):
    if json_path.exists():
        with open(json_path, "r", encoding="utf-8") as f:
            return json.load(f)


# session state initialization

if "page" not in st.session_state:
    st.session_state["page"] = "Assignments Dashboard"

if "draft" not in st.session_state:
    st.session_state["draft"] = {}

if st.session_state["page"] == "Assignment Dashboard":
    col1,col2 = st.columns([3,1])
    with col1:
        st.subheader("Assignments")
        
    with col2:
        if st.button("Add New Assignment", key = "add_new_assignemnt_btn",
                     use_container_width= True, type = "primary"):
            st.session_state["page"] = "Add New Assignment"
            st.rerun()

    st.dataframe(assignments)


elif st.session_state["page"] == "Add New Assignment":
    col1,col2 = st.columns([3,1])
    with col1:
        st.subheader("Add New Assignment")
    with col2:
        if st.button("Back", key="back_btn", use_container_width=True):
            st.session_state["page"] = "Assignments Dashboard" 
            st.rerun()
    
    st.session_state['draft']['title'] = st.text_input("Title", key = "title_txt")
    st.session_state['draft']['description'] = st.text_area("Description", placeholder="normalization is covered here",
                            help="Here you are entering the assignment details", key = "desc")
    st.session_state["draft"]['points'] = st.number_input("Points", key = "pnts")
    st.session_state['draft']['assignment_type'] = st.selectbox("Type", ["Select an option", "Homework", "Lab", "other"],
                                                                key = "assignment_type_selector")

    if st.button("Save", key = "save_btn", use_container_width=True, type = "primary"):
        with st.spinner("In Progress..."):
            assignments.append(
                {
                    "id" : str(uuid.uuid4()),
                    "title" : st.session_state["draft"]["title"],
                    "description" : st.session_state["draft"]["description"],
                    "points" : st.session_state["draft"]["points"],
                    "type" : st.session_state["draft"]["type"]
                }
            )

            with open(json_path, "w", encoding="utf-8") as f:
                    json.dump(assignments, f, indent=4)

            st.success("New Assignment is recorded!")
            st.info("This is a new assignment")
                
            time.sleep(2)
            st.session_state["page"] = "Assignments Dashboard"
            st.session_state["draft"] = {}
            st.rerun()



elif st.session_state["page"] == "Edit Assignment":
    pass