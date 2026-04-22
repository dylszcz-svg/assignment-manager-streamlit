import streamlit as st

st.title('Course Management App')
st.header('Assignments')
st.subheader('Assignment Manager')

st.divider()


# load assignments
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

# Add new assignment

st.markdown('# Add New Assignment')

# Input
title = st.text_input('Title', placeholder='ex. Homework 1', help = 'This is the name of the assignment')
description = st.text_area('Description',placeholder='ex. Database design ...')
due_date = st.date_input('Due Date')
assignment_type = st.radio('Type', ['Homework','Lab'])

#assignment_type2 = st.selectbox('Type',['Homework','Lab','Other'])
#if assignment_type2 == 'Other':
#    assignment_type2 = st.text_input('Assignment Type')

#lab = st.checkbox('Lab')

with st.expander('Assignment Preview', expanded = True):
    st.markdown('## Live Preview')
    st.markdown(f'Title: {title}')

btn_save = st.button('Save',width='stretch')
if btn_save:
    st.warning('Working On It...')
