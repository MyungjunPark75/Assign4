# Import necessary packages (Make sure to also include in "requirements.txt" in this repository.)
import streamlit as st
import pandas as pd

# Print Title for the App
st.title("Microsoft Stock Data Dashboard by Myungjun_Park")

# Read CSV file with stock data (CSV file must be in 'main' folder for your assignment 4 repository) 
df = pd.read_csv("msft.csv")

# Set up the 4 tabs on the Dashboard
tabs = st.tabs(["📋 Raw Data", "📈 Price Chart", "📊 Volume Chart","Fun Tab"])

# Tab 1: Raw Data
with tabs[0]:
    st.subheader(f"Raw Data for MSFT")
    st.dataframe(df, use_container_width=True)

# Tab 2: Closing Price Chart
with tabs[1]:
    st.subheader(f"Closing Price for MSFT")
    st.line_chart(df['Close'])

# Tab 3: Volume Chart
with tabs[2]:
    st.subheader(f"Volume for MSFT")
    st.bar_chart(df['Volume'])

# Tab 4: Volume Chart
with tabs[3]:
    st.subheader(f"🔴 Basic Circle Drawing App")

# Add a slider to let the user control the radius of the circle
radius = st.slider("Select the radius:", min_value=0.1, max_value=10.0, value=5.0, step=0.1)

# Create a matplotlib figure and axis
fig, ax = plt.subplots()

# Draw the circle centered at (0,0)
circle = plt.Circle((0, 0), radius, color='blue', fill=False, linewidth=2)
ax.add_patch(circle)

# Set equal scaling and limits so the circle doesn't look stretched (like an ellipse)
ax.set_aspect('equal', adjustable='datalim')
ax.set_xlim(-11, 11)
ax.set_ylim(-11, 11)

# Add grid lines and a center marker for reference
ax.grid(True, which='both', linestyle='--', linewidth=0.5)
ax.axhline(y=0, color='k', linewidth=0.5)
ax.axvline(x=0, color='k', linewidth=0.5)

# Display the plot in the Streamlit app
st.pyplot(fig)
