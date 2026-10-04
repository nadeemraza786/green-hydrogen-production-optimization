from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
FIG = ROOT / "figures"
FIG.mkdir(exist_ok=True)

PV_KWP = 2587.18
BATTERY_KWH = 504.45
ELY_MIN_KW = 200.0
ELY_MAX_KW = 1000.0
LCOH_EUR_KG = 7.47
H2_KG_YEAR = 33533.53

# Battery support duration
power = np.linspace(ELY_MIN_KW, ELY_MAX_KW, 161)
duration = BATTERY_KWH / power
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(power, duration, linewidth=2.2)
ax.scatter([ELY_MIN_KW, ELY_MAX_KW],
           [BATTERY_KWH / ELY_MIN_KW, BATTERY_KWH / ELY_MAX_KW], s=70)
ax.set_title("Battery Support Duration Across Electrolyzer Load")
ax.set_xlabel("Electrolyzer power (kW)")
ax.set_ylabel("Ideal battery support duration (h)")
ax.grid(alpha=0.25)
fig.tight_layout()
fig.savefig(FIG / "05_battery_support_duration.png", dpi=240, bbox_inches="tight")
plt.close(fig)

# Derived engineering KPI sheet
fig, ax = plt.subplots(figsize=(12, 7))
ax.axis("off")
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
cards = [
    (0.18, 0.76, "PV / Electrolyzer Ratio", f"{PV_KWP/ELY_MAX_KW:.2f}", "kWp per kW"),
    (0.50, 0.76, "Battery Support at 1 MW", f"{BATTERY_KWH/ELY_MAX_KW:.2f}", "hours ideal"),
    (0.82, 0.76, "Battery Support at 200 kW", f"{BATTERY_KWH/ELY_MIN_KW:.2f}", "hours ideal"),
    (0.18, 0.34, "Average H₂ Production", f"{H2_KG_YEAR/365:.1f}", "kg/day"),
    (0.50, 0.34, "H₂ Yield per PV Capacity", f"{H2_KG_YEAR/PV_KWP:.2f}", "kg/(kWp·year)"),
    (0.82, 0.34, "Levelized Annual H₂ Cost", f"€{H2_KG_YEAR*LCOH_EUR_KG:,.0f}", "LCOH₂ × annual H₂"),
]
for x, y, title, val, unit in cards:
    ax.text(x, y+0.11, title, ha="center", va="center", fontsize=12, fontweight="bold")
    ax.text(x, y, val, ha="center", va="center", fontsize=20,
            bbox=dict(boxstyle="round,pad=0.55", fc="white", ec="black", lw=1.5))
    ax.text(x, y-0.10, unit, ha="center", va="center", fontsize=10)
ax.set_title("Derived Engineering Metrics from the Reported Optimum", fontsize=18, pad=18)
fig.tight_layout()
fig.savefig(FIG / "06_derived_engineering_metrics.png", dpi=240, bbox_inches="tight")
plt.close(fig)
