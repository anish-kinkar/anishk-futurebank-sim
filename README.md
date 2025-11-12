# FutureBank Sim – AI‑Powered Personal Wealth Predictor

An end‑to‑end, student‑friendly but **fancy & uncommon** finance project that runs on **Google Colab** and deploys as a **Streamlit** app.
It performs **Monte Carlo simulations** of personal wealth over time, supports multiple goals, loans, and dynamic spending,
and produces **scenario‑based advice** (rule‑based by default; LLM integration optional).

## ✨ Features
- Monthly cash‑flow model (income, tax, expenses, inflation, savings rate).
- Portfolio simulator: expected return, volatility, rebalancing, drawdowns.
- Multi‑goal planning: e.g., car in Year 2, masters in Year 4, house down‑payment in Year 6.
- Loans with amortization and early repayments.
- 10K‑path Monte Carlo with percentiles and failure probability for each goal.
- Explainable, rule‑based **Advice Engine** (LLM plug‑in optional).
- **Colab Notebook** for reproducibility and **Streamlit** UI for deployment.

## 🧱 Project Structure
```
futurebank-sim/
├─ futurebank/
│  ├─ models.py
│  ├─ simulate.py
│  ├─ advice.py
│  ├─ visuals.py
│  └─ __init__.py
├─ app_streamlit.py
├─ FutureBank_Sim_Demo.ipynb
├─ requirements.txt
├─ LICENSE
├─ .gitignore
└─ README.md
```

## 🚀 Quickstart (Colab)
1. Open `FutureBank_Sim_Demo.ipynb` in **Google Colab**.
2. Run all cells – it installs dependencies, imports the local modules, and runs example simulations.
3. Tweak inputs to match your profile and re‑run.

## 🌐 Deploy (Streamlit Cloud)
1. Push this folder to a **public GitHub repo** (e.g., `anishk/futurebank-sim`).
2. On [streamlit.io](https://streamlit.io/), choose *New app* → select your repo → `app_streamlit.py` → deploy.
3. Set optional secrets (if you enable LLM advice): in Streamlit Cloud → *App settings* → *Secrets* :
   ```toml
   OPENAI_API_KEY="sk-..."
   GOOGLE_API_KEY="..."
   ```

## 🔌 Optional: LLM Advice
By default, advice is rule‑based (offline). To enable LLM‑powered narratives, set the environment variable
`OPENAI_API_KEY` or `GOOGLE_API_KEY`. The app will automatically switch to the LLM mode if a key is found.

## 🧪 Testing Locally
```bash
pip install -r requirements.txt
streamlit run app_streamlit.py
```

## 📄 License
MIT
