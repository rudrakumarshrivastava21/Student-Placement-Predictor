Name-RUDRA KUMAR SHRIVASTAVA
REG NO.-25BCE11105
AI & ML PROJECT

# Student-Placement-Predictor

# Student Placement Predictor (AI/ML Project)

## Project Overview
This project is a core part of my **Fundamentals of AI and ML** course. The goal was to build a predictive model that can determine a student's placement probability based on two primary factors: **CGPA** and **IQ Level**. 

Instead of just guessing, this tool uses historical data to find patterns and provide a logical "Placed" or "Not Placed" result.

---

## Key Features
- **Binary Classification**: Categorizes students into two clear outcomes.
- **High Efficiency**: Uses a lightweight algorithm, making it run instantly on any machine.
- **Data Validation**: Implemented a 80-20 split to ensure the model isn't just "memorizing" data but actually learning.

---

##  Tech Stack & Tools
- **Programming Language:** Python 3.13
- **Primary Libraries:** - `Pandas`: For structured data handling and CSV manipulation.
  - `Scikit-learn`: For implementing the Logistic Regression algorithm and accuracy metrics.
- **IDE:** PyCharm (Professional/Community)

---

## Machine Learning Methodology
The project follows a standard Data Science workflow:

1. **Data Collection**: A dataset of student records (`placement_data.csv`) was created.
2. **Preprocessing**: Features (CGPA, IQ) were separated from the Target (Placement).
3. **Model Selection**: **Logistic Regression** was chosen because it is the industry standard for binary classification tasks.
4. **Training & Testing**: The model was trained on 80% of the data and validated on the remaining 20%.
5. **Evaluation**: The model successfully achieved a high accuracy rate, confirming its reliability.



---

##  Project Structure
- `main.py`: The core Python script with the ML logic and prediction code.
- `placement_data.csv`: The dataset containing academic and recruitment history.
- `README.md`: Project documentation and setup guide (this file).

---

## How to Run This Project
Follow these simple steps to get the project running on your local machine:

1. **Clone the Repository:** Download the ZIP or use Git to clone this repo.
2. **Install Dependencies:** Open your terminal/command prompt and run:
   ```bash
   pip install pandas scikit-learn
