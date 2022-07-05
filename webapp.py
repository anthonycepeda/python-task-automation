import streamlit as st
import pandas as pd
import numpy as np

import app

st.title("Active Users")

DATE_COLUMN = "seniority"

data = pd.DataFrame(app.load_a_file())
data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])

if st.checkbox("Show raw data"):
    st.subheader("Raw data")
    st.write(data)

st.subheader("User since")
hist_values = np.histogram(data[DATE_COLUMN].dt.month, bins=24, range=(0, 24))[0]
st.bar_chart(hist_values)


options = st.multiselect("Please select a user", data["name"])

st.write("You selected:", options)
seleted_data = []
for index, row in data.iterrows():
    if row["name"] in options:
        seleted_data.append(row)

if seleted_data:
    st.table(seleted_data)
    if st.button("Send Report"):
        content = {
            "message": str(seleted_data),
            "receiver_email": "acpytest@gmail.com",
            "subject": "[Test] Universidad Europea - webapp",
        }
        resp = app.send_report(content)
        st.write(resp)
