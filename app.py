import streamlit as st 

# Initialize session state if it doesn't exist
if 'task_list' not in st.session_state:
    st.session_state.task_list = []
if 'new_task' not in st.session_state:
    st.session_state.new_task = ""

st.title("✅ To-Do List")

# Task input section
with st.container():
    # Use custom CSS to fix alignment
    st.markdown("""
        <style>
        .stButton > button {
            margin-top: 25px;
        }
        </style>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([3, 1])
    with col1:
        task = st.text_input(
            "Enter a new task",
            key="task_input",
            value=st.session_state.new_task,
            placeholder="Type your task here..."
        ).strip()
    
    with col2:
        add_button = st.button("Add Task", type="primary")

    if add_button and task:  # Only add non-empty tasks
        if task not in st.session_state.task_list:  # Prevent duplicates
            st.session_state.task_list.append(task)
            st.session_state.new_task = ""  # Clear input after adding
            st.rerun()
        else:
            st.warning("This task already exists!")

# Display tasks
if not st.session_state.task_list:
    st.info("No tasks yet. Add some tasks to get started!")
else:
    st.write("### Your Tasks")
    for i, task in enumerate(st.session_state.task_list):
        col1, col2 = st.columns([4, 1])
        with col1:
            st.write(f"{i+1}. {task}")
        with col2:
            if st.button("Delete", key=f"delete_{i}"):
                st.session_state.task_list.pop(i)
                st.rerun()

    # Add clear all button
    if st.button("Clear All Tasks", type="secondary"):
        st.session_state.task_list = []
        st.rerun()
    
st.sidebar.title("options")




