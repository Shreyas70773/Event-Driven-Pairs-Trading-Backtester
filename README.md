
# 📈 Adaptive Statistical Arbitrage: A Robust Pairs Trading System

**Author**: Shreyas Sunil  
**Date**: July 28, 2025

---

## Project Summary

This repository documents the complete research and engineering journey of a statistical arbitrage "pairs trading" strategy, moving beyond a basic prototype to develop an adaptive, institution-grade backtesting framework in Python. The project follows a rigorous quantitative research workflow: from an initial hypothesis to a naive strategy, through failure and diagnosis, and ultimately to a robust, validated system tested on out-of-sample 2024 market data.

---

## Table of Contents

- Project Overview  
- Core Quantitative Concepts  
- The Technology Stack  
- The Research Journey: A Three-Act Narrative  
- Final Validated Results  
- How to Run the Simulation  
- Conclusion and Key Learnings  

---

## 1. Project Overview

The objective was to simulate and validate a classic statistical arbitrage strategy based on cointegrated stock pairs. The core hypothesis: if two stocks exhibit cointegration, short-term deviations from their equilibrium relationship present repeatable profit opportunities.

To test this, a custom event-driven backtesting engine was built from scratch. It processes data sequentially, one day at a time, ensuring decisions are made with no future data leakage. Over time, the initial static strategy evolved into an adaptive system with quarterly rebalancing, robust filters, and hard risk controls.

---

## 2. Core Quantitative Concepts

- **Statistical Arbitrage**: A strategy class that profits from relative mispricings between securities, independent of market direction.  
- **Cointegration (Engle-Granger Test)**: Identifies long-term equilibrium relationships between non-stationary time series.  
- **Stationarity (ADF Test)**: Filters for spreads that are mean-reverting.  
- **Z-Score**: Measures deviations from the mean in standard deviations; used for trade triggers.  
- **Lookahead Bias**: Avoided by using an event-driven design where no future data is accessed.  
- **Sharpe Ratio**: Measures risk-adjusted return.  
- **Maximum Drawdown**: Quantifies the largest equity loss from peak to trough.  
- **Regime Change**: Structural market shifts that invalidate past statistical relationships.

---

## 3. The Technology Stack

- Python 3.10+  
- `pandas`, `numpy`: Time-series processing and numerical analysis.  
- `yfinance`: Daily historical data acquisition.  
- `statsmodels`: Cointegration and ADF testing.  
- `multiprocessing`: Parallel processing for pair selection.  
- `matplotlib`, `seaborn`: Visualization.  
- Jupyter Notebook: Research and experimentation environment.  

---

## 4. The Research Journey: A Three-Act Narrative

### Act I: The Naive Strategy and the Illusion of Success
- **Method**: Fixed pair list from 2020–2021, 30-day Z-score, no transaction cost.  
- **Observation**: Sharpe Ratio of 0.91 appeared promising.  
- **Flaw**: Unrealistic assumptions—ignored friction, no adaptivity.

### Act II: The Failure – Uncovering Fragility
- **Test 1**: Added 0.05% commission → Sharpe turned negative.  
- **Test 2**: Used broader universe with 40-day lookback → Max Drawdown hit -57.53%.  
- **Diagnosis**: Strategy was overfit and static, unable to cope with 2023 regime change.

### Act III: The Re-Engineering – Building a Robust System
- **Solution 1**: Introduced hard stop-loss at Z = 3.0 to cap loss on structural breaks.  
- **Solution 2**: Implemented rolling quarterly re-formation using the past year’s data.  
- **Solution 3**: Added ADF stationarity filter post-cointegration to refine trade quality.  

These changes transformed a fragile model into a resilient, adaptive strategy.

---

## 5. Final Validated Results

### ✅ Backtest (2022–2023)
| Metric         | Value     |
|----------------|-----------|
| Sharpe Ratio   | 1.23      |
| Annualized Return | 22.90%  |
| Max Drawdown   | -19.56%   |

### 🔍 Walk-Forward (2024)
| Metric         | Value     |
|----------------|-----------|
| Sharpe Ratio   | 0.82      |
| Annualized Return | 9.71%  |
| Max Drawdown   | -7.71%    |

The walk-forward test confirms that performance generalizes beyond the development period.

---

## 6. How to Run the Simulation

### Install Dependencies:
```bash
pip install yfinance statsmodels numpy pandas matplotlib seaborn
```

### File Structure:
```
Event-Driven Pairs Trading/
├── main.ipynb         # Main notebook
├── mp_helpers.py      # Modular functions
```

### Run:
Open `main.ipynb` in Jupyter and execute cells sequentially. The final section performs a full adaptive backtest (2022–2024) and visualizes equity curves and metrics.

---

## 7. Conclusion and Key Learnings

This project achieved its technical objective: to build and validate a statistical arbitrage strategy. However, its broader value lies in the rigorous research process and the insights gained from failure and recovery. The final strategy is not just profitable—it is robust, adaptable, and designed to survive in real-world conditions.

### Key Takeaways:

1. **Risk Management Has Greater Impact Than Alpha Optimization**  
   The naive model’s profits vanished when minimal transaction costs were added. The most effective improvement was not better pair selection, but the implementation of a hard stop-loss. This one change reduced drawdowns from -57% to -19%, proving that drawdown control is a precondition for strategy viability.

2. **Markets Are Non-Stationary; Adaptive Models Are Essential**  
   Cointegration relationships from 2020–2021 were no longer valid in 2023. The adaptive quarterly rebalancing system allowed the strategy to discard outdated relationships and identify new ones using only recent data, aligning the model with evolving market structure.

3. **Inactivity is a Strategic Decision**  
   The system intentionally avoided trades in early 2024, recognizing from its filters that no high-confidence pairs were present. This disciplined behavior avoided unnecessary losses and preserved capital. Rules for when not to trade are as important as rules for entry and exit.

4. **Clean Backtests Are Misleading Without Sensitivity Testing**  
   An initial Sharpe Ratio of 0.91 was invalidated by a trivial cost input. Only by running sensitivity analyses across costs, parameters, and regimes did the real weaknesses emerge. This highlights the danger of over-interpreting backtest outputs without robustness checks.

5. **Layered Filtering Improves Signal Quality**  
   The final pipeline applied multiple filters:
   - **Correlation**: Coarse pre-selection.  
   - **Cointegration Test**: Statistical confirmation.  
   - **ADF Stationarity Filter**: Ensures mean-reversion quality.

   Each filter reduced false positives and improved portfolio reliability, demonstrating that no single test is sufficient.

---

## Final Thoughts

This project illustrates the full lifecycle of quantitative strategy development—from hypothesis generation to production-grade implementation. Its ultimate lesson is not about signal generation, but about robust system design. In an environment defined by uncertainty and non-stationarity, resilience, adaptivity, and disciplined execution matter more than model complexity or initial alpha.
