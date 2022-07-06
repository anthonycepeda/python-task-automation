import numpy as np
import pandas as pd
import seaborn as sns
import streamlit as st
from matplotlib.figure import Figure
from app.database import get_session
import app

st.set_page_config(
    page_title="Users Report", page_icon="📊", initial_sidebar_state="expanded"
)

st.title("Users Report WebApp")

DATE_COLUMN = "since"

data = pd.DataFrame(app.get_users_from_database(get_session()))
year_df = pd.DataFrame(data[DATE_COLUMN].dropna().value_counts()).reset_index()
year_df = year_df.sort_values(by="index")

if st.checkbox("Show Table"):
    st.subheader("Users")
    st.write(data)

if st.checkbox("Show Json"):
    st.subheader("Users")
    st.json(data.to_dict(orient="records"))


# bar
st.subheader("Users Added")
fig = Figure()
ax = fig.subplots()
sns.barplot(x=year_df["index"], y=year_df[DATE_COLUMN], ax=ax)
ax.set_xlabel("Year")
ax.set_ylabel("Users added")
st.pyplot(fig)


# cities
fig = Figure()
ax = fig.subplots()
sns.stripplot(x="city", y="profession", data=data, ax=ax)
ax.set_xlabel("Cities")
ax.set_ylabel("Professions")
st.pyplot(fig)


# sidebar
st.sidebar.subheader("Send Custom Report")
add_selectbox = st.sidebar.multiselect(
    "Please select users to be included in report", data["name"]
)

with st.sidebar:

    seleted_data = []
    for index, row in data.iterrows():
        if row["name"] in add_selectbox:
            seleted_data.append(row)

    if seleted_data:
        st.table(seleted_data)
        receiver_email = st.text_input("Your Email:")
        if st.button("Send Report"):
            content = {
                "message": str(seleted_data),
                "receiver_email": receiver_email,
                "subject": "[Test] Universidad Europea - webapp",
            }
            resp = app.send_report(content)
            st.warning(resp)
