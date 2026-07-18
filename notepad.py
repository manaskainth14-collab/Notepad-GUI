import streamlit as st
st.title("Notepad")
user_names  = st.text_input("What is your name?")
if user_names:
    st.text(f"Welcome {user_names.title()} to our interactive notepad")
with open("names.txt", "a") as file:
    file.write(user_names + "\n")


text = st.text_area("Enter Here")
if st.button("Save"):
    with open("data.txt", "a") as file:
        file.write(text + "\n")
    st.success("Your content is saved")
    preview = st.radio("Want to preview", ["Yes", "No"])
    if preview == "Yes":
        with open("data.txt", "r") as file:
            st.text(file.read())
    elif preview == "No":
        pass
if st.button("Clear All"):
    with open("data.txt", "w") as file:
        pass
    st.success("The content is now deleted", icon="🚨")
    
