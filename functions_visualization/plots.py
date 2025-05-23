import random
import math
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
from scipy.stats import skew, kurtosis

# PLOT SKILL BASED ON AGE


def plot_skill_based_on_age(ages, age_skills):
    plt.figure(figsize=(10, 6))
    plt.plot(ages, age_skills, marker="o", linestyle="-", color="b", label="Soldier")

    plt.title("Survival Skill vs Age", fontsize=16)
    plt.xlabel("Age", fontsize=12)
    plt.ylabel("Survival Skill", fontsize=12)
    plt.grid(True)
    plt.xticks(ages)
    plt.legend()
    plt.show()


# Plot Background vs Skill


def plot_background_vs_skill(backgrounds, bg_skills):
    plt.figure(figsize=(10, 6))
    plt.bar(backgrounds, skills, color="skyblue")

    plt.title("Survival Skill by Background", fontsize=16)
    plt.xlabel("Background", fontsize=12)
    plt.ylabel("Survival Skill", fontsize=12)
    plt.xticks(rotation=45)
    plt.grid(axis="y")
    plt.show()
