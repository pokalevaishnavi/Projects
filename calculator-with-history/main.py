import streamlit as st
import math

HISTORY_FILE = "history.txt"

def show_history():
    try:
        with open(HISTORY_FILE, "r") as file:
            lines = file.readlines()
        if not lines:
            st.info("No history found!")
        else:
            for line in reversed(lines):
                st.write(line.strip())
    except FileNotFoundError:
        st.info("No history found!")

def clear_history():
    open(HISTORY_FILE, "w").close()
    st.success("History cleared!")

def save_to_history(expression, result):
    with open(HISTORY_FILE, "a") as file:
        file.write(expression + "=" + str(result) + "\n")

def calculate_expression(expression):
    try:
        expression = expression.replace("^", "**")
        expression = expression.replace("√", "math.sqrt")
        result = eval(expression, {"math": math})
        if int(result) == result:
            result = int(result)
        save_to_history(expression, result)
        return result
    except ZeroDivisionError:
        return "Error: Division by 0"
    except:
        return "Invalid expression"

st.title("🧮 Simple Calculator")

expression = st.text_input("Enter your calculation:", placeholder="e.g., 8 + 7, (2+3)*4, √16 + 2, 2^3")

col1, col2 = st.columns(2)

with col1:
    if st.button("Calculate"):
        result = calculate_expression(expression)
        st.success(f"Result: {result}")

with col2:
    if st.button("Clear History"):
        clear_history()

if st.checkbox("Show History"):
    show_history()
