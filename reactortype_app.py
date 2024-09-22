import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def cstr_volume(k, F, CA0, X):
    """Calculates the volume of a CSTR for a first-order reaction."""
    return F * X / (k * CA0 * (1 - X))

def pfr_volume(k, F, CA0, X):
    """Calculates the volume of a PFR for a first-order reaction."""
    return (F / (k * CA0)) * np.log(1 / (1 - X))

def pfr_conversion_profile(k, F, CA0, V):
    """Calculates the conversion profile along a PFR."""
    X = np.linspace(0, 1, 100)
    V_PFR = np.zeros_like(X)
    for i in range(len(X)):
        V_PFR[i] = pfr_volume(k, F, CA0, X[i])
    return X, V_PFR

def cstr_pfr_comparison(k, F, CA0, X):
    """Compares the volume required for CSTR and PFR."""
    VCSTR = cstr_volume(k, F, CA0, X)
    VPFR = pfr_volume(k, F, CA0, X)
    return VCSTR, VPFR

def main():
    st.title("CSTR and PFR Calculator")

    # User input parameters
    k = st.number_input("Rate constant (k)", value=1.0)
    F = st.number_input("Flow rate (F)", value=1.0)
    CA0 = st.number_input("Initial concentration (CA0)", value=1.0)
    X = st.number_input("Target conversion (X)", value=0.9)

    # Calculate reactor volumes
    VCSTR, VPFR = cstr_pfr_comparison(k, F, CA0, X)

    # Display results
    st.write("CSTR Volume:", VCSTR)
    st.write("PFR Volume:", VPFR)

    # Plot conversion profiles
    if st.button("Plot Conversion Profiles"):
        X, V_PFR = pfr_conversion_profile(k, F, CA0, VPFR)
        fig, ax = plt.subplots(2, 1, figsize=(10, 12))  # Adjust figure size
        ax[0].plot(V_PFR, X)
        ax[0].set_xlabel("Reactor Volume (V)")
        ax[0].set_ylabel("Conversion (X)")
        ax[0].set_title("PFR Conversion Profile")
        ax[1].plot(np.repeat(VCSTR, 100), X)
        ax[1].set_xlabel("Reactor Volume (V)")
        ax[1].set_ylabel("Conversion (X)")
        ax[1].set_title("CSTR Conversion")
        st.pyplot(fig)

if __name__ == "__main__":
    main()