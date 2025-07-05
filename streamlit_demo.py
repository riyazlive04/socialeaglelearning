"""import streamlit as st

st.title("My First Streamlit App")
name = st.text_input("Enter your name:")

if st.button("Say Hello"):
    if name:
        st.success(f"Hello, {name}, Welcome to my page!")
    else:
        st.warning("Please enter your name.")"""


import streamlit as st

st.title("Simple Calculator")

# Input fields
num1 = st.number_input("Enter first number", value=0.0)
num2 = st.number_input("Enter second number", value=0.0)

# Operation selection
operation = st.selectbox(
    "Select operation",
    ("Add", "Subtract", "Multiply", "Divide")
)

# Calculate button
if st.button("Calculate"):
    if operation == "Add":
        result = num1 + num2
        st.success(f"Result: {result}")
    elif operation == "Subtract":
        result = num1 - num2
        st.success(f"Result: {result}")
    elif operation == "Multiply":
        result = num1 * num2
        st.success(f"Result: {result}")
    elif operation == "Divide":
        if num2 != 0:
            result = num1 / num2
            st.success(f"Result: {result}")
        else:
            st.error("Error: Division by zero!")
