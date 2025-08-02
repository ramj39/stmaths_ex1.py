import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Quadratic Equation Solver")
st.latex(r"ax^2 + bx + c = 0")

# Input parameters
a = st.number_input("Enter a", value=1.0)
b = st.number_input("Enter b", value=-3.0)
c = st.number_input("Enter c", value=2.0)

# Calculate discriminant and roots
D = b**2 - 4*a*c
st.write(f"Discriminant: {D}")

if D >= 0:
    x1 = (-b + D**0.5) / (2*a)
    x2 = (-b - D**0.5) / (2*a)
    st.write(f"Roots: x₁ = {x1}, x₂ = {x2}")
else:
    st.write("No real roots")

# Plot the graph
x_vals = np.linspace(-10, 10, 400)
y_vals = a*x_vals**2 + b*x_vals + c
fig, ax = plt.subplots()
ax.plot(x_vals, y_vals)
ax.axhline(0, color='gray', linestyle='--')
st.pyplot(fig)
st.markdown("[wikipedia](https://en.wikipedia.org/wiki/Quadratic_formula)")
st.text("by subramanian ramajayam")
