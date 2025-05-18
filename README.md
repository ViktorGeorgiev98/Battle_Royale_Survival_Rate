# 🧠 Battle Royale Survival Simulation

A statistical and probabilistic simulation project modeling survival chances in a Battle Royale-style game. Built in **Python + Jupyter Notebook** as a final project for the **"Maths for Developers"** course at SoftUni.

## 🎯 Project Overview

This project simulates 100-player Battle Royale scenarios and analyzes survival probabilities using:

- ✅ **Monte Carlo simulations**
- ✅ **Markov Chains**
- ✅ **Bayesian updates**
- ✅ **Probabilistic modeling**
- ✅ **Data visualization (Matplotlib & Seaborn)**

It explores how different **professions**, **strategies**, **age**, **gender**, and **dynamic events** (e.g., injuries, disease, zone shrinking) affect a player's chance to survive.

---

## 📌 Key Features

- **Player Diversity**: Each player has a unique combination of:
  - Gender & Age
  - Profession (e.g. Soldier, Doctor, Programmer, MMA Fighter)
  - Strategy (e.g. Aggressive, Hiding, Balanced)

- **Realistic Game Events**:
  - Injuries and illnesses
  - Item discovery (weapons, medkits)
  - Team formations based on shared traits
  - Zone shrinkage eliminating players outside the safe area

- **Simulation Mechanics**:
  - 1000 simulations run 100 times for high statistical confidence
  - Survival stats calculated per profession & strategy
  - Confidence intervals, skewness, kurtosis and distribution metrics

---

## 📊 Statistical Summary

| Metric                        | Value                    |
|------------------------------|--------------------------|
| Mean survival chance         | 0.0091                   |
| Standard deviation           | 0.0000947 (very low)     |
| Median                       | 0.009095                 |
| Min/Max                      | 0.00881 / 0.00932        |
| Skewness                     | -0.30 (slightly left-skewed) |
| Kurtosis                     | ~0 (near-normal)         |

✔️ Results are stable, statistically consistent, and aligned with theoretical expectations.

---

## 🔍 Key Insights

- **Programmers and Doctors** using **hiding/balanced strategies** tend to survive longer by avoiding conflict.
- **Soldiers and Fighters** with **aggressive or balanced strategies** outperform in combat-heavy environments.
- Bayesian updates dynamically adjust survival chances as events unfold.

These patterns mimic real-life logic: smart players think strategically, and trained combatants thrive in hostile environments.

---

## 🧰 Technologies Used

- Python 3
- Jupyter Notebook
- NumPy, Pandas
- Matplotlib, Seaborn
- Scipy.stats for statistical metrics

---

📚 Educational Value
This project demonstrates how mathematics, probability theory, and programming can be used to model complex, dynamic systems. It serves as a strong example of using simulations to gain insights into real-world-like scenarios.

🧠 Author
Viktor Georgiev – Senior RPA/QA Developer | Python & AI Enthusiast

📜 License
Apache License 2.0.

💡 Future Ideas
Add real-time visual animations of player movements

Introduce dynamic alliances and betrayals

Extend to team-based Battle Royale scenarios

