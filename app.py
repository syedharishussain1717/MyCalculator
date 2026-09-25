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
# Custom CSS
# -----------------------------

st.markdown(
    """
    <style>

    /* Main page */
    .main {
        padding-top: 2rem;
    }

    /* Calculator title */
    .title {
        text-align: center;
        font-size: 42px;
        font-weight: bold;
        margin-bottom: 5px;
    }

    /* Subtitle */
    .subtitle {
        text-align: center;
        color: #777777;
        font-size: 17px;
        margin-bottom: 30px;
    }

    /* Calculator container */
    .calculator-box {
        padding: 30px;
        border-radius: 18px;
        border: 1px solid #dddddd;
        background-color: #ffffff;
        box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.08);
    }

    /* Result box */
    .result-box {
        padding: 25px;
        margin-top: 25px;
        margin-bottom: 15px;
        border-radius: 15px;
        text-align: center;
        background-color: #f5f7fa;
        border: 1px solid #dddddd;
    }

    .result-label {
        font-size: 16px;
        color: #777777;
    }

    .result-value {
        font-size: 38px;
        font-weight: bold;
        margin-top: 5px;
    }

    /* Footer */
    .footer {
        text-align: center;
        color: #888888;
        font-size: 14px;
        margin-top: 30px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# -----------------------------
# Header
# -----------------------------

st.markdown(
    '<div class="title">🧮 Simple Calculator</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'A simple and interactive calculator built with Python and Streamlit.'
    '</div>',
    unsafe_allow_html=True
)


# -----------------------------
# Calculator Section
# -----------------------------

st.markdown(
    '<div class="calculator-box">',
    unsafe_allow_html=True
)

st.subheader("Calculate")

# First number
number1 = st.number_input(
    "First Number",
    value=0.0,
    step=1.0
)

# Operation
operation = st.selectbox(
    "Choose Operation",
    [
        "Addition (+)",
        "Subtraction (-)",
        "Multiplication (×)",
        "Division (÷)"
    ]
)

# Second number
number2 = st.number_input(
    "Second Number",
    value=0.0,
    step=1.0
)

st.markdown("</div>", unsafe_allow_html=True)


# -----------------------------
# Buttons
# -----------------------------

st.write("")

col1, col2 = st.columns(2)

with col1:
    calculate_button = st.button(
        "🧮 Calculate",
        use_container_width=True
    )

with col2:
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
                <div class="result-label">Result</div>
                <div class="result-value">{result:g}</div>
            </div>
            """,
            unsafe_allow_html=True
        )


# -----------------------------
# Clear Button
# -----------------------------

if clear_button:

    st.rerun()


# -----------------------------
# Footer
# -----------------------------

st.markdown(
    """
    <div class="footer">
        Built with Python 🐍 and Streamlit 🚀
    </div>
    """,
    unsafe_allow_html=True
)

