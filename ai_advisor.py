import google.generativeai as genai

genai.configure(api_key="AIzaSyCM8RgxI-y6Rwp8kWrFcMgcfdQbUTHDTUk")

model = genai.GenerativeModel("gemini-2.0-flash")

def get_ai_advice(income, expenses, savings, debt):

    prompt = f"""
        Give financial advice for a person with:
            Income: ₹{income}
                Expenses: ₹{expenses}
                    Savings: ₹{savings}
                        Debt: ₹{debt}

                            Suggest budgeting, debt strategy and investment plan.
                                """

                                    response = model.generate_content(prompt)

                                        return response.text 