import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Function to calculate savings at retirement
def calculate_savings(age, retirement_age, monthly_savings, interest_rate):
    years_to_save = retirement_age - age
    months_to_save = years_to_save * 12
    total_savings = 0
    monthly_interest_rate = interest_rate / 100 / 12

    savings_over_time = []

    for month in range(months_to_save):
        total_savings += monthly_savings
        total_savings *= (1 + monthly_interest_rate)
        savings_over_time.append(total_savings)

    return total_savings, savings_over_time

# Streamlit app layout
st.title("Retirement Savings Calculator")

# Input fields
age = st.number_input("Enter your current age", min_value=0, max_value=100, value=30)
retirement_age = st.number_input("Enter your retirement age", min_value=age, max_value=100, value=65)
monthly_savings = st.number_input("Enter your monthly savings ($)", min_value=0.0, value=500.0)
interest_rate = st.number_input("Enter the expected annual interest rate (%)", min_value=0.0, max_value=100.0, value=5.0)

# Calculate savings
if st.button("Calculate"):
    total_savings, savings_over_time = calculate_savings(age, retirement_age, monthly_savings, interest_rate)

    st.write(f"Total savings at retirement: ${total_savings:,.2f}")

    # Plot the savings growth
    months = np.arange(1, len(savings_over_time) + 1)
    plt.figure(figsize=(10, 6))
    plt.plot(months, savings_over_time, label="Savings Growth", color="blue")
    plt.title("Savings Growth Over Time")
    plt.xlabel("Months")
    plt.ylabel("Total Savings ($)")
    plt.grid(True)
    plt.legend()

    st.pyplot(plt)

# Streamlit footer
st.write("This app helps you calculate the amount you need to save for retirement based on your inputs.")
