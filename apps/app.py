import streamlit as st


# Step 1: Header First (Text Elements)

st.title("Course Management")
st.header("Course Management Dashboard")
st.caption("MISY350")
st.divider()

# Step 2: Define Assignments List (Data Continuity)

assignments = [
    {
        'id':"HW1",
        'title':'Introduction to Database',
        'description':'Basics of database design',
        'points':100,
        'type':'homework'
    },
    {
        'id':"HW2",
        'title':'Normalization',
        'description':'Normalize the table designs',
        'points':100,
        'type':'lab'
    }
]

# Step 3: Add New Assignment Section (Inputs & Layout)

st.subheader("Add New Assignment")
with st.container(border = True):
    col1,col2 = st.columns([2,1])

    with col1:
        with st.container(border = True):
            st.markdown('### Assignment Details')
            title = st.text_input('Assignment Title', placeholder = 'Homework')
            description = st.text_input("Assignment Description")
            points = st.number_input('Points')
    with col2:
        st.markdown('**Time & Type**')
        due_date = st.date_input('Due Date')
        type = st.radio('Type',('Homework','Lab'))