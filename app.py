import streamlit as st
from financial_analysis import analyze_finances
from goal_planner import calculate_goal
from ai_advisor import get_ai_advice

st.title("AI Financial Advisor")

st.header("Enter Your Financial Details")

income = st.number_input("Monthly Income (₹)", 0)
expenses = st.number_input("Monthly Expenses (₹)", 0)
savings = st.number_input("Current Savings (₹)", 0)
debt = st.number_input("Outstanding Debt (₹)", 0)

if st.button("Analyze Finances"):

    result = analyze_finances(income, expenses, savings, debt)

        st.subheader("Financial Health")

            st.write(result)

                advice = get_ai_advice(income, expenses, savings, debt)

                    st.subheader("AI Financial Advice")

                        st.write(advice)

                        st.header("Goal Planning")

                        goal = st.number_input("Goal Amount (₹)",0)
                        years = st.number_input("Years to Achieve Goal",1)

                        if st.button("Calculate Goal Plan"):

                            monthly = calculate_goal(goal, years)

                                st.write(f"You need to save ₹{monthly} per month.") 