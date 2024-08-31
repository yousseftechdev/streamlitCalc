import streamlit as st
import math

# Title
st.title("Scientific Calculator")

# User input for expression
expression = st.text_input("Enter your expression:", "")

# Function to safely evaluate mathematical expressions
def evaluate_expression(expr):
    try:
        # Evaluate the expression safely
        result = eval(expr, {"__builtins__": None}, {"math": math})
        return round(result, 6)
    except Exception as e:
        raise ValueError(f"Invalid input: {e}")

# Buttons for common mathematical operations
if st.button("Calculate"):
    try:
        result = evaluate_expression(expression)
        st.success(f"Result: {result}")
    except Exception as e:
        st.error(f"Error: {e}")

# Scientific operations
st.subheader("Scientific Operations")

col1, col2, col3 = st.columns(3)

def display_result(label, value):
    try:
        st.success(f"{label}({expression}) = {round(value, 6)}")
    except Exception as e:
        st.error(f"Error: {e}")

with col1:
    if st.button("sin"):
        try:
            result = math.sin(math.radians(float(expression)))
            display_result("sin", result)
        except ValueError as e:
            st.error(f"Error: {e}")

    if st.button("cos"):
        try:
            result = math.cos(math.radians(float(expression)))
            display_result("cos", result)
        except ValueError as e:
            st.error(f"Error: {e}")

    if st.button("tan"):
        try:
            result = math.tan(math.radians(float(expression)))
            display_result("tan", result)
        except ValueError as e:
            st.error(f"Error: {e}")

with col2:
    # Button to show log base input
    show_log_base = st.button("Show Log Base Input")

    # Manage visibility of the log base input
    if "show_log_base" not in st.session_state:
        st.session_state.show_log_base = False
    
    if show_log_base:
        st.session_state.show_log_base = not st.session_state.show_log_base
    
    # Show log base input if the button is clicked
    if st.session_state.show_log_base:
        log_base = st.number_input("Enter the base for log (default is 10):", value=10, step=1)

        if st.button("log"):
            try:
                # Calculate logarithm with specified base
                if log_base == 10:
                    result = math.log10(float(expression))
                elif log_base == math.e:
                    result = math.log(float(expression))
                else:
                    result = math.log(float(expression), log_base)
                display_result(f"log (base {log_base})", result)
            except ValueError as e:
                st.error(f"Error: {e}")

    if st.button("ln"):
        try:
            result = math.log(float(expression))
            display_result("ln", result)
        except ValueError as e:
            st.error(f"Error: {e}")

    if st.button("sqrt"):
        try:
            result = math.sqrt(float(expression))
            display_result("sqrt", result)
        except ValueError as e:
            st.error(f"Error: {e}")

with col3:
    if st.button("exp"):
        try:
            result = math.exp(float(expression))
            display_result("exp", result)
        except ValueError as e:
            st.error(f"Error: {e}")

    if st.button("x^2"):
        try:
            result = float(expression) ** 2
            display_result("squared", result)
        except ValueError as e:
            st.error(f"Error: {e}")

    if st.button("x^3"):
        try:
            result = float(expression) ** 3
            display_result("cubed", result)
        except ValueError as e:
            st.error(f"Error: {e}")

# Note on usage
st.write("##### Note: Enter a number or mathematical expression in the input box, then click the desired operation.")
