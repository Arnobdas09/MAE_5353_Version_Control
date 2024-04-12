# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 23:54:30 2024

@author: arnob
"""

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Importing necessary libraries<<<<<<<<<<<<<<<<<<<<<<<<<<<<
import matplotlib.pyplot as plt
import pandas as pd

#=================== _________Reading the data _________========================
df = pd.read_excel('E:\\2nd_semester\\MAE_5353\\Arnob_HW\\HW_2\\PerformanceData_Unitxx_ArnobDas.xlsx', sheet_name='SteadyState', skiprows=[], header=0)
df1 = pd.read_excel('E:\\2nd_semester\\MAE_5353\\Arnob_HW\\HW_2\\PerformanceData_Unitxx_ArnobDas.xlsx', sheet_name='Uncertainties', skiprows=[], header=0)
df1.head()

x = 'Amb_Temp_F'
y = "COP_W/W"

fig, ax = plt.subplots(figsize=(10, 6))



# >>>>>>>>>>>>>>>>>>>>>>>>>>____Define functions for temperature conversion ____<<<<<<<<<<<<<<<<<<<<<<
def fahrenheit_to_celsius(x):
    return (x - 32) / 1.8  #Fahrenhite to celcius conversion formula

def celsius_to_fahrenheit(x):
    return x * 1.8 + 32 ## Celcius to Fahrenhite conversion formula 

def fahrenheit_to_kelvin(x):
    return (x-32)/1.8 + 273.15 ## Fahrenheit to Kelvin conversion formula 

def kelvin_to_fahrenheit(x):
    return (x-273.15) * 1.8 + 32 # Kelvin to Fahrenheit conversion formula

#==================== ____Secondary x-axis for Fahrenheit____ ========================
secax_x_celsius = ax.secondary_xaxis('top', functions=(fahrenheit_to_celsius, celsius_to_fahrenheit))
secax_x_celsius.set_xlabel(r'$Temperature\ [^oC]$',fontsize=14, fontweight='bold')

#==================== _____Tertiary x-axis for Kelvin _____==============================
secax_x_kelvin = ax.secondary_xaxis(1.2, functions=(fahrenheit_to_kelvin, kelvin_to_fahrenheit))
secax_x_kelvin.set_xlabel(r'$Temperature\ [K]$',fontsize=14, fontweight='bold')

#===================== _____Define functions for COP to EER and vice versa_____============================
def COPtoEER(x):
    y = 3.41 * x
    return y

def EERtoCOP(x):
    y = x / 3.41
    return y

# >>>>>>>>>>>>>>>>>____Secondary y-axis for EER____<<<<<<<<<<<<<<<<<<<<<<<<
secax_y_EER = ax.secondary_yaxis('right', functions=(COPtoEER, EERtoCOP))
secax_y_EER.set_ylabel(r'$EER\ [Btu/Wh]$',fontsize=13, fontweight='bold')

xerror = "Amb_Temp_F_err"
yerror = "COP_W/W_err"
xerror_1 = df1[xerror]
yerror_1 = df1[yerror]


#>>>>>>>>>>>>>>>>>>>>>>>____Plotting____<<<<<<<<<<<<<<<<<<<<<<<<<<<<
plt.scatter(df[x], df[y])
plt.errorbar(df[x], df[y], yerr=yerror_1, xerr=xerror_1, ecolor='red', fmt='o')
ax.set_xlabel(r'$Temperature\ [^oF]$',fontsize=14)
ax.set_ylabel(r'$COP\ [W/W]$', fontsize=14)
plt.grid(True)
plt.legend(['COP,EER'], loc="lower left",fontsize=16)
fig.suptitle('Temperature vs COP Plot', fontsize=18)
plt.tight_layout()
plt.show()
