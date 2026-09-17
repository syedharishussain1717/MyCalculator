import streamlit as st


# -----------------------------
# Page Configuration
# -----------------------------

st.set_page_config(
    page_title="Simple Calculator",
    page_icon="🧮",
    layout="centered"
)


# -----------------------------
# Custom Styling
# -----------------------------

st.markdown(
    """
    <style>
    .main {
        padding-top: 2rem;
    }

    .calculator-title {
        text-align: center;
        font-size: 40px;
        font-weight: bold;
        margin-bottom: 10px;
    }

    .calculator-subtitle {
        text-align: center;
        color: gray;
        margin-bottom: 30px;
    }

    .result-box {
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        margin-top: 20px;
        border: 1px solid #ddd;
    }

    .result-text {
        font-size: 32px;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# -----------------------------
# Title
# -----------------------------

st.markdown(
    '<div class="calculator-title">🧮 Simple Calculator</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="calculator-subtitle">'
    'Perform basic mathematical calculations easily.'
    '</div>',
    unsafe_allow_html=True
)


# -----------------------------
# User Input
# -----------------------------

number1 = st.number_input(
    "Enter the first number",
    value=0.0
)

operation = st.selectbox(
    "Select an operation",
    [
        "Addition (+)",
        "Subtraction (-)",
        "Multiplication (×)",
        "Division (÷)"
    ]
)

number2 = st.number_input(
    "Enter the second number",
    value=0.0
)


# -----------------------------
# Buttons
# -----------------------------

calculate_button = st.button(
    "🧮 Calculate",
    use_container_width=True
)

clear_button = st.button(
    "🔄 Clear",
    use_container_width=True
)


# -----------------------------
# Calculation
# -----------------------------

if calculate_button:

    if operation == "Addition (+)":
        result = number1 + number2

    elif operation == "Subtraction (-)":
        result = number1 - number2

    elif operation == "Multiplication (×)":
        result = number1 * number2

    elif operation == "Division (÷)":

        if number2 == 0:
            st.error("❌ Cannot divide by zero.")
            result = None

        else:
            result = number1 / number2

    # Display result
    if result is not None:

        st.markdown(
            f"""
            <div class="result-box">
                <div>Result</div>
                <div class="result-text">{result:g}</div>
            </div>
            """,
            unsafe_allow_html=True
        )


# -----------------------------
# Clear Button
# -----------------------------

if clear_button:
    st.rerun()
