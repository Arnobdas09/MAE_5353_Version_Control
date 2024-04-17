# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 13:34:30 2024

@author: arnob
"""

import matplotlib.pyplot as plt
import pandas as pd

# Define input and output file paths
input_file_path = 'E:\\2nd_semester\\MAE_5353\\Arnob_HW\\HW_2\\PerformanceData_Unitxx_ArnobDas.xlsx'
output_file_path = 'E:\\2nd_semester\\MAE_5353\\Arnob_HW\\HW_2\\Output.xlsx'

#=================== _________Reading the data _________========================
df = pd.read_excel(input_file_path, sheet_name='SteadyState', skiprows=[], header=0)
df1 = pd.read_excel(input_file_path, sheet_name='Uncertainties', skiprows=[], header=0)
df1.head()

x, y = 'Amb_Temp_F', 'COP_W/W'

fig, ax = plt.subplots(figsize=(10, 6))

# Temperature conversion functions
def f2c(x): return (x - 32) / 1.8
def f2k(x): return (x - 32) / 1.8 + 273.15
def c2f(x): return x * 1.8 + 32
def k2f(x): return (x - 273.15) * 1.8 + 32

# Secondary axes
secax_x_c, secax_x_k = ax.secondary_xaxis('top', functions=(f2c, c2f)), ax.secondary_xaxis(1.2, functions=(f2k, k2f))
secax_x_c.set_xlabel(r'$Temperature\ [^oC]$', fontsize=14, fontweight='bold')
secax_x_k.set_xlabel(r'$Temperature\ [K]$', fontsize=14, fontweight='bold')

# COP-EER conversion functions
def COP2EER(x): return 3.41 * x
def EER2COP(x): return x / 3.41

secax_y_EER = ax.secondary_yaxis('right', functions=(COP2EER, EER2COP))
secax_y_EER.set_ylabel(r'$EER\ [Btu/Wh]$', fontsize=13, fontweight='bold')

xerr, yerr = "Amb_Temp_F_err", "COP_W/W_err"
xerr_1, yerr_1 = df1[xerr], df1[yerr]

plt.scatter(df[x], df[y])
plt.errorbar(df[x], df[y], yerr=yerr_1, xerr=xerr_1, ecolor='red', fmt='o')

# Aligning tick markers
ax.set_xlabel(r'$Temperature\ [^oF]$', fontsize=14)
ax.set_ylabel(r'$COP\ [W/W]$', fontsize=14)
plt.grid(True)
plt.legend(['COP,EER'], loc="lower left", fontsize=16)
fig.suptitle('Temperature vs COP Plot', fontsize=18)

# Adjusting tick locations and labels
secax_x_c.set_xticks([f2c(tick) for tick in ax.get_xticks()])
secax_x_k.set_xticks([f2k(tick) for tick in ax.get_xticks()])
secax_y_EER.set_yticks([COP2EER(tick) for tick in ax.get_yticks()])

plt.tight_layout()
# Save the plot as PNG file with 300 DPI resolution
plt.savefig('output_plot.png', dpi=300)

# Save the plot as SVG file
plt.savefig('output_plot.svg')
plt.show()
