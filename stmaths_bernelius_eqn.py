import streamlit as st

st.title("Bernoulli's Equation Calculator")

# Constants and Inputs
rho = st.number_input("Density (kg/m³)", value=1000.0)
g = 9.81

st.subheader("Point 1")
P1 = st.number_input("Pressure P₁ (Pa)", value=101325.0)
v1 = st.number_input("Velocity v₁ (m/s)", value=0.0)
h1 = st.number_input("Height h₁ (m)", value=0.0)

st.subheader("Point 2")
P2 = st.number_input("Pressure P₂ (Pa)", value=101325.0)
v2 = st.number_input("Velocity v₂ (m/s)", value=0.0)
h2 = st.number_input("Height h₂ (m)", value=0.0)

calc_mode = st.selectbox(
    "Which variable do you want to calculate at Point 2?",
    ["Pressure (P₂)", "Velocity (v₂)", "Height (h₂)"]
)

if st.button("Calculate"):
    # Bernoulli’s equation computations
    if calc_mode == "Pressure (P₂)":
        P2_calc = P1 + 0.5 * rho * (v1*2 - v2*2) + rho * g * (h1 - h2)
        st.write(f"Calculated Pressure at Point 2: {P2_calc:.2f} Pa")

    elif calc_mode == "Velocity (v₂)":
        v2_sq = v1**2 + (2 / rho) * (P1 - P2) + 2 * g * (h1 - h2)
        if v2_sq < 0:
            st.error("Unphysical result: Check your inputs.")
        else:
            v2_calc = v2_sq ** 0.5
            st.write(f"Calculated Velocity at Point 2: {v2_calc:.2f} m/s")

    elif calc_mode == "Height (h₂)":
        h2_calc = h1 + (P1 - P2) / (rho * g) + (0.5 / g) * (v1*2 - v2*2)
        st.write(f"Calculated Height at Point 2: {h2_calc:.2f} m")
st.markdown("[wikipedia](https://en.wikipedia.org/wiki/Bernoulli%27s_principle)")
st.text("by Subramanian Ramajayam")
