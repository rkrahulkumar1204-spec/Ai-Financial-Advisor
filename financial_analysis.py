def analyze_finances(income, expenses, savings, debt):

        savings_rate = (savings / income) * 100
            expense_ratio = (expenses / income) * 100
                debt_ratio = (debt / income) * 100

                    result = {
                            "Savings Rate (%)": round(savings_rate,2),
                                    "Expense Ratio (%)": round(expense_ratio,2),
                                            "Debt-to-Income (%)": round(debt_ratio,2)
                                                }

                                                    return result