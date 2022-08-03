import numpy as np
import pendulum as pend
import pandas as pd

def backhrs(hour):
    if hour <= 40:
        return hour, 0
    else:
        return 40, hour - 40

pend.week_starts_at(wday=1)

most_recent = pend.datetime(2022, 7, 18)
end_date = pend.datetime(2023, 1, 29)

msrfout = most_recent.to_formatted_date_string()
esrfout = end_date.to_formatted_date_string()

timfr = pend.period(most_recent, end_date)

hourly, ot_rate, tax = 24.00, 1.5, .25
gross = ((hourly * 40) * 2) + ((hourly * 10) * ot_rate)
net = gross - (gross * tax)

hours_spread = np.random.choice([37.5, 40.0, 42.5, 45.0, 47.5, 50.0], p=[.2, .3, .2, .1, .1, .1],
                                size=timfr.in_weeks() + 1)

work_weeks_dict = []

hrspridx = 0
for dt in timfr.range('weeks'):
    wk_hours = backhrs(hours_spread[hrspridx])
    reg = wk_hours[0] * hourly
    ot = wk_hours[1] * hourly * ot_rate

    this_week = {
        "Week": 1 + hrspridx,
        "Wk Beg": dt.to_formatted_date_string(),
        "Wk End": dt.add(days=6).to_formatted_date_string(),
        "Reg Hrs": wk_hours[0],
        "OT Hrs": wk_hours[1],
        "Tot Hrs": hours_spread[hrspridx],
        "Reg Pay": reg,
        "OT Pay": ot,
        "Taxes": tax * (ot + reg),
        "Gross": ot + reg,
        "Net": (ot + reg) - ( tax * (ot + reg ) )
    }
    work_weeks_dict.append(this_week)
    hrspridx += 1

df = pd.DataFrame(work_weeks_dict)

wk1_idx = 0
wk2_idx = 1

pay_periods_dict = []

while wk1_idx < len(work_weeks_dict):

    wk1 = work_weeks_dict[wk1_idx]
    wk2 = work_weeks_dict[wk2_idx]

    this_pay_period = {
        "Pay Period": pay_periods_dict.__len__() + 1,
        "Wk Beg": wk1.get("Wk Beg"),
        "Wk End": wk2.get("Wk End"),
        "Reg Hrs": wk1.get("Reg Hrs") + wk2.get("Reg Hrs"),
        "OT Hrs": wk1.get("OT Hrs") + wk2.get("OT Hrs"),
        "Tot Hrs": wk1.get("Tot Hrs") + wk2.get("Tot Hrs"),
        "Reg Pay": wk1.get("Reg Pay") + wk2.get("Reg Pay"),
        "OT Pay": wk1.get("OT Pay") + wk2.get("OT Pay"),
        "Taxes": wk1.get("Taxes") + wk2.get("Taxes"),
        "Gross": wk1.get("Gross") + wk2.get("Gross"),
        "Net": wk1.get("Net") + wk2.get("Net"),
    }

    pay_periods_dict.append(this_pay_period)
    wk1_idx += 2
    wk2_idx += 2

fd = pd.DataFrame(pay_periods_dict)
fd['Net'].sum()