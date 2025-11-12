import os
import streamlit as st
import numpy as np
from futurebank.models import UserProfile, PortfolioConfig, SimulationConfig, Goal, Loan
from futurebank.simulate import simulate
from futurebank.advice import maybe_llm

st.set_page_config(page_title='FutureBank Sim', layout='wide')

st.title('💸 FutureBank Sim – AI‑Powered Personal Wealth Predictor')

with st.sidebar:
    st.header('Profile')
    start_age = st.number_input('Start Age', 18, 80, 21)
    horizon_years = st.slider('Horizon (years)', 3, 40, 10)
    monthly_income = st.number_input('Monthly Income', 0, 1_000_000, 40000, step=1000)
    monthly_expenses = st.number_input('Monthly Expenses', 0, 1_000_000, 20000, step=1000)
    savings_rate = st.slider('Savings Rate', 0.0, 0.9, 0.35, 0.01)
    inflation = st.slider('Inflation (annual)', 0.0, 0.25, 0.06, 0.005)
    tax_rate = st.slider('Tax Rate (flat)', 0.0, 0.5, 0.05, 0.01)

    st.subheader('Portfolio')
    exp_ret = st.slider('Expected Return (annual)', 0.00, 0.40, 0.12, 0.01)
    vol = st.slider('Volatility (annual)', 0.00, 0.60, 0.18, 0.01)
    n_paths = st.select_slider('Monte Carlo Paths', options=[1000, 2000, 5000, 10000, 20000], value=10000)

st.subheader('Goals')
goals = []
cols = st.columns(3)
with cols[0]:
    if st.checkbox('Car Goal'):
        goals.append(Goal(name='Car', year=2, amount=700000.0))
with cols[1]:
    if st.checkbox('Masters Goal'):
        goals.append(Goal(name='Masters', year=4, amount=2000000.0))
with cols[2]:
    if st.checkbox('House Down Payment'):
        goals.append(Goal(name='House', year=6, amount=3000000.0))

st.subheader('Loans')
loans = []
if st.checkbox('Add Education Loan Example'):
    loans.append(Loan(name='EduLoan', principal=500000.0, annual_rate=0.12, years=5))

profile = UserProfile(
    start_age=start_age,
    horizon_years=horizon_years,
    monthly_income=monthly_income,
    monthly_expenses=monthly_expenses,
    savings_rate=savings_rate,
    inflation=inflation,
    tax_rate=tax_rate,
    goals=goals,
    loans=loans
)
portfolio = PortfolioConfig(expected_return=exp_ret, volatility=vol)
cfg = SimulationConfig(n_paths=n_paths, seed=42)

if st.button('Run Simulation', type='primary'):
    with st.spinner('Simulating...'):
        result = simulate(profile, portfolio, cfg)
    st.success('Done!')

    # Percentiles chart (use Streamlit's built-in matplotlib support)
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots(figsize=(10,4))
    ax.plot(result.times, result.percentiles['p5'], label='P5')
    ax.plot(result.times, result.percentiles['p25'], label='P25')
    ax.plot(result.times, result.percentiles['p50'], label='Median')
    ax.plot(result.times, result.percentiles['p75'], label='P75')
    ax.plot(result.times, result.percentiles['p95'], label='P95')
    ax.set_xlabel('Months')
    ax.set_ylabel('Wealth')
    ax.set_title('Wealth Over Time (Percentiles)')
    ax.legend()
    st.pyplot(fig)

    st.subheader('Goal Success Probability')
    for g, p in result.goal_success.items():
        st.metric(label=g, value=f"{p*100:.1f}%" )

    st.subheader('Advice')
    adv = maybe_llm(profile, portfolio, result)
    st.code(adv['advice'])
