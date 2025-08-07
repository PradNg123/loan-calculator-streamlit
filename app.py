import streamlit as st
import math

st.set_page_config(page_title="Loan / EMI / SIP Calculator", layout="centered")

st.title("💰 Financial Calculator")
option = st.sidebar.selectbox("Choose Calculator", ["EMI Calculator", "Loan Amount Calculator", "SIP Calculator"])

if option == "EMI Calculator":
    st.header("📄 EMI Calculator")

    loan_amount = st.number_input("Loan Amount (₹)", value=100000)
    annual_rate = st.number_input("Annual Interest Rate (%)", value=8.0)
    tenure_years = st.number_input("Loan Tenure (years)", value=5)

    if st.button("Calculate EMI"):
        r = annual_rate / 12 / 100
        n = tenure_years * 12
        emi = loan_amount * r * ((1 + r) ** n) / (((1 + r) ** n) - 1)
        st.success(f"Your Monthly EMI is ₹{emi:,.2f}")

elif option == "Loan Amount Calculator":
    st.header("📄 Loan Amount Calculator")

    emi = st.number_input("EMI Amount (₹)", value=2000)
    annual_rate = st.number_input("Annual Interest Rate (%)", value=8.0)
    tenure_years = st.number_input("Tenure (years)", value=5)

    if st.button("Calculate Loan Amount"):
        r = annual_rate / 12 / 100
        n = tenure_years * 12
        loan_amount = emi * (((1 + r) ** n - 1) / (r * (1 + r) ** n))
        st.success(f"You can get a loan of ₹{loan_amount:,.2f}")

elif option == "SIP Calculator":
    st.header("📈 SIP Calculator")

    monthly_investment = st.number_input("Monthly Investment (₹)", value=5000)
    annual_rate = st.number_input("Expected Annual Return (%)", value=12.0)
    tenure_years = st.number_input("Investment Period (years)", value=10)

    if st.button("Calculate SIP"):
        r = annual_rate / 12 / 100
        n = tenure_years * 12
        future_value = monthly_investment * (((1 + r) ** n - 1) * (1 + r)) / r
        st.success(f"Your SIP investment will grow to ₹{future_value:,.2f}")
