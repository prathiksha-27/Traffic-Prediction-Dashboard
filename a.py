import streamlit as st
import pandas as pd

st.title("🚦 Traffic Prediction System")

# Location selection
location = st.selectbox(
    "Select Location",
    ["T Nagar", "Anna Nagar", "Velachery", "Tambaram", "Guindy"]
)

# Time input
hour = st.slider("Select Time (Hour)", 0, 23, 8)

# Traffic prediction logic
def predict_traffic(hour):
    if 7 <= hour <= 10:
        return "High Traffic"
    elif 17 <= hour <= 21:
        return "High Traffic"
    elif 11 <= hour <= 16:
        return "Medium Traffic"
    else:
        return "Low Traffic"

traffic = predict_traffic(hour)

# Show result
st.subheader("Prediction Result")
st.write("Location:", location)
st.write("Time:", hour)
st.write("Traffic Level:", traffic)

# Create graph data
hours = list(range(24))
traffic_values = []

for h in hours:
    if 7 <= h <= 10 or 17 <= h <= 21:
        traffic_values.append(80)
    elif 11 <= h <= 16:
        traffic_values.append(50)
    else:
        traffic_values.append(20)

df = pd.DataFrame({
    "Hour": hours,
    "Traffic": traffic_values
})

# Show graph
st.subheader("Traffic Graph")
st.line_chart(df.set_index("Hour"))