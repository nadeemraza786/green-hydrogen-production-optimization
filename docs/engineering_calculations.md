# Engineering Calculations

This note documents calculations that can be derived directly from the reported optimum.

## Reported optimum

PV capacity = 2,587.18 kWp

Battery capacity = 504.45 kWh

Electrolyzer minimum power = 200 kW

Electrolyzer maximum power = 1,000 kW

Annual hydrogen production = 33,533.53 kg/year

Minimum LCOH₂ = 7.47 EUR/kg

## 1. PV to electrolyzer nameplate ratio

PV to electrolyzer ratio

= PV capacity / electrolyzer maximum power

= 2,587.18 / 1,000

= **2.587 kWp per kW electrolyzer**

This indicates substantial PV oversizing relative to the 1 MW electrolyzer nameplate capacity.

## 2. Ideal battery support duration

At maximum electrolyzer load

= Battery energy / Electrolyzer power

= 504.45 kWh / 1000 kW

= **0.504 h**

At minimum electrolyzer load

= 504.45 kWh / 200 kW

= **2.522 h**

These are ideal energy only durations. Real battery efficiency, reserve SOC, inverter losses and power limits would reduce usable duration.

## 3. Average hydrogen production

Average per day

= 33,533.53 / 365

= **91.87 kg/day**

Average per month

= 33,533.53 / 12

= **2794.46 kg/month**

Year average per hour

= 33,533.53 / 8760

= **3.828 kg/h**

These are annualized averages and do not represent the instantaneous electrolyzer production rate.

## 4. Hydrogen yield per installed PV capacity

= Annual hydrogen production / PV capacity

= 33,533.53 / 2,587.18

= **12.96 kg H₂ per kWp PV per year**

## 5. Annual levelized hydrogen cost equivalent

= LCOH₂ × annual hydrogen output

= 7.47 EUR/kg × 33,533.53 kg/year

= **EUR 250,495.47 per year**

This is a levelized cost equivalent based on the reported LCOH₂ and annual production. It is not the same as annual cash operating expenditure.

## Equations used in the underlying engineering model

Hourly power available to the electrolyzer can be represented as

P_available(t) = P_PV(t) + P_battery,discharge(t) − P_battery,charge(t)

Electrolyzer operating logic can be represented conceptually as

P_el(t) = 0, if P_available(t) < P_min

P_el(t) = min(P_available(t), P_max), otherwise

Hydrogen production is generally calculated from electrolyzer energy consumption as

m_H2(t) = P_el(t) Δt / SEC_H2

where SEC_H2 is the electrolyzer specific electricity consumption in kWh/kg.

The supplied project material does not include a documented SEC value, battery efficiency, SOC limits, component CAPEX breakdown or lifetime assumptions. Therefore those quantities are not invented in this repository.

The economic objective is

minimize LCOH₂(PV size, battery size)

subject to the hourly plant energy balance and electrolyzer operating constraints.
