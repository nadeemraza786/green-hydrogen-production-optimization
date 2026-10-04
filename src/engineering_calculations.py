from pathlib import Path
import pandas as pd
import numpy as np

PV_KWP = 2587.18
BATTERY_KWH = 504.45
ELY_MIN_KW = 200.0
ELY_MAX_KW = 1000.0
LCOH_EUR_KG = 7.47
H2_KG_YEAR = 33533.53

metrics = {
    "PV_to_electrolyzer_nameplate_ratio_kWp_per_kW": PV_KWP / ELY_MAX_KW,
    "battery_support_at_min_electrolyzer_power_h": BATTERY_KWH / ELY_MIN_KW,
    "battery_support_at_max_electrolyzer_power_h": BATTERY_KWH / ELY_MAX_KW,
    "average_hydrogen_production_kg_per_day": H2_KG_YEAR / 365,
    "average_hydrogen_production_kg_per_month": H2_KG_YEAR / 12,
    "average_hydrogen_production_kg_per_hour_year_average": H2_KG_YEAR / 8760,
    "hydrogen_yield_per_installed_PV_kg_per_kWp_year": H2_KG_YEAR / PV_KWP,
    "annual_levelized_hydrogen_cost_equivalent_EUR": H2_KG_YEAR * LCOH_EUR_KG,
}

for key, value in metrics.items():
    print(f"{key}: {value:.4f}")
