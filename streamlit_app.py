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

    # Create a figure and axis
    fig, ax = plt.subplots()

    # Draw a circle at center (0.5, 0.5) with radius 0.3
    circle = plt.Circle((0.5, 0.5), 0.3, color="red")
    ax.add_patch(circle)

    # Adjust plot limits and keep aspect ratio perfectly equal
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect("equal")

    # Hide the grid axes lines for a clean look
    ax.axis("off")
    
    # Display the drawing inside Streamlit
    st.pyplot(fig)

# Display the plot in the Streamlit app
st.pyplot(fig)
