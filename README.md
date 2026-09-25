# 🧮 Simple Streamlit Calculator

A simple and interactive calculator web application built using **Python** and **Streamlit**.

The application allows users to enter two numbers, select a mathematical operation, and instantly view the calculated result.

## 🚀 Features

* ➕ Addition
* ➖ Subtraction
* ✖️ Multiplication
* ➗ Division
* ⚠️ Division-by-zero error handling
* 🔄 Clear/Reset option
* 🎨 Clean and modern user interface
* 📱 Responsive layout
* ☁️ Deployable using Streamlit Community Cloud

## 🛠️ Technologies Used

* **Python**
* **Streamlit**
* **Git**
* **GitHub**
* **Streamlit Community Cloud**

## 📁 Project Structure

```text
simple-streamlit-calculator/
│
├── app.py
├── requirements.txt
└── README.md
```

### `app.py`

Contains the main Streamlit application, including the calculator interface and calculation logic.

### `requirements.txt`

Contains the Python dependencies required to run the application.

### `README.md`

Contains information and documentation about the project.

## 💻 Run the Project Locally

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/simple-streamlit-calculator.git
```

Replace `YOUR_USERNAME` with your GitHub username.

### 2. Open the project folder

```bash
cd simple-streamlit-calculator
```

### 3. Install the required dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Run the Streamlit application

```bash
streamlit run app.py
```

If the `streamlit` command is not recognized, use:

```bash
python -m streamlit run app.py
```

The application will open in your browser at:

```text
http://localhost:8501
```

## 🧮 How to Use

1. Enter the first number.
2. Select an operation.
3. Enter the second number.
4. Click **Calculate**.
5. The result will be displayed below the calculator.
6. Click **Clear** to reset the calculator.

### Example

```text
First Number: 20
Operation: Addition (+)
Second Number: 10

Result: 30
```

## ⚠️ Error Handling

The calculator checks for division by zero.

For example:

```text
20 ÷ 0
```

will display:

```text
Cannot divide by zero.
```

instead of producing an invalid result.

## ☁️ Deployment

This application can be deployed for free using **Streamlit Community Cloud**.

Basic deployment process:

```text
Local Project
     ↓
Git
     ↓
GitHub
     ↓
Streamlit Community Cloud
     ↓
Public Web Application
```

After deployment, Streamlit Community Cloud provides a public URL that can be shared with others.

## 📌 Future Improvements

Possible future features include:

* 📜 Calculation history
* 🔢 Scientific calculator functions
* 📊 More mathematical operations
* 🌙 Dark/light theme
* ⌨️ Keyboard input
* 🧮 Calculator-style number buttons

## 👨‍💻 Learning Purpose

This project was created as a beginner Python project to practice:

* Python variables
* Conditional statements
* User input
* Basic arithmetic
* Error handling
* Streamlit UI development
* Git and GitHub
* Cloud deployment

## 📄 License

This project is open for learning and educational purposes.
