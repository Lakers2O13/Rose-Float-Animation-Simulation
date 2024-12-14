import pandas as pd

def pid_table():
    pid_table_data = [
        {"DMX_512 Addr": 0, "Prop Gain": 0.500, "Int Gain": 0.500, "Der Gain": 0.500, "Rev Out": "Yes"},
        {"DMX_512 Addr": 1, "Prop Gain": 0.500, "Int Gain": 0.500, "Der Gain": 0.500, "Rev Out": "No"},
        {"DMX_512 Addr": 2, "Prop Gain": 0.500, "Int Gain": 0.500, "Der Gain": 0.500, "Rev Out": "No"},
        {"DMX_512 Addr": 3, "Prop Gain": 0.500, "Int Gain": 0.500, "Der Gain": 0.500, "Rev Out": "No"},
    ]
    pid_df = pd.DataFrame(pid_table_data, index=["Axis 0", "Axis 1", "Axis 2", "Axis 3"])
    return pid_df

# Prop 0.500-10.000
# Int 0.500-1.500
# Der 0.500-1.500
# Rev Yes/No