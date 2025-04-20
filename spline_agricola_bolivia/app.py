import streamlit as st
import numpy as np
from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt

st.title("Interpolación por Spline Cúbico")
st.write("Producción Agrícola de Bolivia (2010–2016)")

# Datos reales proporcionados
anios = np.array([2010, 2011, 2012, 2013, 2014, 2015, 2016])
produccion = np.array([1969567, 2229608, 2273072, 2449393, 2934920, 2660494, 2279134])

# Crear spline cúbico natural
spline = CubicSpline(anios, produccion, bc_type='natural')

# Input de usuario
x_interp = st.slider("Selecciona el año a interpolar", 2010.0, 2016.0, 2012.5, 0.1)
y_interp = spline(x_interp)

st.write(f"📍 Producción interpolada en {x_interp}: **{y_interp:,.2f}**")

# Graficar
x_vals = np.linspace(2010, 2016, 500)
y_vals = spline(x_vals)

fig, ax = plt.subplots()
ax.plot(anios, produccion, 'o', label='Datos originales')
ax.plot(x_vals, y_vals, '-', label='Spline Cúbico')
ax.plot(x_interp, y_interp, 'r*', markersize=10, label='Interpolado')
ax.set_xlabel('Año')
ax.set_ylabel('Producción')
ax.set_title('Spline Cúbico de Producción Agrícola')
ax.legend()
ax.grid(True)
st.pyplot(fig)