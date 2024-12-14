import time
import pandas as pd
import os
from rich.console import Console
from rich.table import Table
from rich.columns import Columns
from rich.panel import Panel
import axis_table, pid_table

console = Console()
pid_df = pid_table.pid_table()
axis_df = axis_table.axis_table()

def main():
    axis = None
    while True:
        while True: # Axis Loop
            display_table_and_options(df = 0, axis=axis)
            option = input("Select an option: ")
            if option == 'x':
                break
            if option == 's':
                while True:
                    axis = input("Select axis (Axis 1, Axis 2, Axis 3, Axis 4): ")
                    if axis in ["1", "2", "3", "4"]:
                        axis = str(int(axis) - 1)
                        break
                    print("Invalid axis")
            if option == '1':
                while True:
                    value = input("Enter minimum range (0-255): ")
                    if value.isdigit() and 0 <= int(value) <= 255:
                        set_min_range(axis_df, axis, value)
                        break
                    print("Invalid value")
            if option == '2':
                while True:
                    value = input("Enter maximum range (0-255): ")
                    if value.isdigit() and 0 <= int(value) <= 255:
                        set_max_range(axis_df, axis, value)
                        break
                    print("Invalid value")
            if option == '3':
                while True:
                    value = input("Enter force output to value (0-255): ")
                    if value.isdigit() and 0 <= int(value) <= 255:
                        force_output_to_value(axis_df,  axis, value)
                        break
                    print("Invalid value")
            if option == '4':
                while True:
                    value = input("Enter PowerOn Default (0-255): ")
                    if value.isdigit() and 0 <= int(value) <= 255:
                        set_poweron_default(axis_df, axis, value)
                        break
                    print("Invalid value")
            if option == '5':
                while True:
                    value = input("Enter velocity limit to value (0.00-10.00): ")
                    try:
                        value = float(value)    
                        if 0 <= value <= 10.00:
                            set_velocity_limit(axis_df, axis, value)
                            break
                        else:
                            raise ValueError
                    except ValueError:
                        print("Invalid value")
            if option == 'n':
                axis = str((int(axis) + 1) % 4)
            if option == 'l':
                axis = str((int(axis) - 1) % 4)
            if option == 'i':
                print("Made by Kaleb and Shawn :)")
                time.sleep (2)
            if option == 'k':
                break
        while True: # PID Loop
            display_table_and_options(df = 1, axis=axis)
            option = input("Select an option: ")
            if option == 'x':
                break
            if option == 's':
                while True:
                    axis = input("Select axis (Axis 1, Axis 2, Axis 3, Axis 4): ")
                    if axis in ["1", "2", "3", "4"]:
                        axis = str(int(axis) - 1)
                        break
                    print("Invalid axis")
            if option == '1':
                while True:
                    value = input(f"Enable/Disable Axis {0} (0 - Disable/1 - Enable): ")
                    if value.isdigit() and 0 <= int(value) <= 1:
                        # Add function to enable/disable axis
                        break
                    print("Invalid value")
            if option == '2':
                while True:
                    value = input("Enter proportional gain (0.500-10.000): ")
                    try:
                        value = float(value)
                        if 0.500 <= value <= 10.000:
                            # Add function to set prop gain
                            break
                        else:
                            raise ValueError
                    except ValueError:
                        print("Invalid value")
            if option == '3':
                while True:
                    value = input("Enter integral gain (0.500-1.500): ")
                    try:
                        value = float(value)
                        if 0.500 <= value <= 1.500:
                            # Add function to set integral gain
                            break
                        else:
                            raise ValueError
                    except ValueError:
                        print("Invalid value")
            if option == '4':
                while True:
                    value = input("Enter derivative gain (0.500-1.500): ")
                    try:
                        value = float(value)
                        if 0.500 <= value <= 1.500:
                            # Add function to set derivative gain
                            break
                        else:
                            raise ValueError
                    except ValueError:
                        print("Invalid value")
            if option == '5':
                while True:
                    value = input(f"Reverse Axis {axis}? (y/n): ")
                    if value in ["y", "n"]:
                        # Add function to reverse axis
                        break
                    print("Invalid value")
            if option == '6':
                # Add compliance settings
                pass
            if option == 'n':
                axis = str((int(axis) + 1) % 4)
            if option == 'l':
                axis = str((int(axis) - 1) % 4)
            if option == 'i':
                print("Made by Kaleb and Shawn :)")
                time.sleep (2)
            if option == 'k':
                break


# Function to display the table and options using rich
def display_table_and_options(df = 0, axis=None):
    os.system('cls' if os.name == 'nt' else 'clear')
    if df == 0:
        # Create the table
        table = Table(title="Axis Configuration Table")
        table.add_column("Axis", justify="right", style="cyan", no_wrap=True)
        table.add_column("DMX_512 Addr", style="magenta")
        table.add_column("Min Scale", style="green")
        table.add_column("Max Scale", style="green")
        table.add_column("Force Pos", style="green")
        table.add_column("Power Def", style="green")
        table.add_column("Vel Limit", style="green")

        for index, row in axis_df.iterrows():
            table.add_row(index, str(row["DMX_512 Addr"]), str(row["Min Scale"]), str(row["Max Scale"]),
                        str(row["Force Pos"]), str(row["Power Def"]), str(row["Vel Limit"]))

        # Create the options panel
        options = f"""
        s) axis to modify: {axis if axis else "#"}
        1) Set minimum range
        2) Set maximum range
        3) Force output to value
        4) Set PowerOn Default
        5) Set Velocity Limit
        6) Network Settings
        k) feedback Config
        n) next
        l) last
        i) info
        o) Def
        g) loop
        h) Halt
        x) eXit
        """
        options_panel = Panel(options, title="Options", border_style="blue")
    if df == 1: # PID Table
        # Create the table
        table = Table(title="PID Configuration Table")
        table.add_column("Axis", justify="right", style="cyan", no_wrap=True)
        table.add_column("DMX_512 Addr", style="magenta")
        table.add_column("Prop Gain", style="green")
        table.add_column("Int Gain", style="green")
        table.add_column("Der gain", style="green")
        table.add_column("Rev Out", style="green")


# Prop 0.500-10.000
# Int 0.500-1.500
# Der 0.500-1.500
# Rev Yes/No

        for index, row in pid_df.iterrows():
            table.add_row(index, str(row["DMX_512 Addr"]), str(row["Prop Gain"]), str(row["Int Gain"]),
                        str(row["Der Gain"]), str(row["Rev Out"]))

        # Create the options panel
        options = f"""
        s) axis to modify: {axis if axis else "#"}
        1) Axis {axis if axis else "#"}: Enabled
        2) Set proportional gain
        3) Set integral gain
        4) Set derivative gain
        5) Reverse axis output
        6) Compliance Settings
        7) More PID options
        k) main conf.
        n) next
        l) last
        i) info
        o) Def
        g) loop
        h) Halt
        x) eXit
        """
        options_panel = Panel(options, title="Options", border_style="blue")
    # Display side by side
    console.print(Columns([options_panel, table]))


# Functions to update the DataFrame
def set_min_range(df, axis, value):
    df.at[f"Axis {axis}", "Min Scale"] = value

def set_max_range(df, axis, value):
    df.at[f"Axis {axis}", "Max Scale"] = value

def force_output_to_value(df, axis, value):
    df.at[f"Axis {axis}", "Force Pos"] = value

def set_poweron_default(df, axis, value):
    df.at[f"Axis {axis}", "Power Def"] = value

def set_velocity_limit(df, axis, value):
    df.at[f"Axis {axis}", "Vel Limit"] = value
    


#

if __name__ == "__main__":
    main()