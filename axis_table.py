import time
import pandas as pd
import os
from rich.console import Console
from rich.table import Table
from rich.columns import Columns
from rich.panel import Panel
import axis_table, pid_table

def axis_table():
    axis_table_data = [
        {"DMX_512 Addr": 0, "Min Scale": 0, "Max Scale": 0, "Force Pos": 0, "Power Def": 0, "Vel Limit": 0},
        {"DMX_512 Addr": 1, "Min Scale": 0, "Max Scale": 0, "Force Pos": 0, "Power Def": 0, "Vel Limit": 0},
        {"DMX_512 Addr": 2, "Min Scale": 0, "Max Scale": 0, "Force Pos": 0, "Power Def": 0, "Vel Limit": 0},
        {"DMX_512 Addr": 3, "Min Scale": 0, "Max Scale": 0, "Force Pos": 0, "Power Def": 0, "Vel Limit": 0},
    ]
    axis_df = pd.DataFrame(axis_table_data, index=["Axis 0", "Axis 1", "Axis 2", "Axis 3"])
    return axis_df

