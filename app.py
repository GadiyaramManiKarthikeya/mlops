import streamlit as st
import pandas as pd
import random

st.title("Simple Recommendation System Demo")

# pretend dataset
items = ["Shoes", "T-shirt", "Watch", "Jeans", "Sunglasses", "Backpack"]

st.subheader("Enter User ID")
user_id = st.number_input("User ID", min_value=1, max_value=9999, value=1)

def generate_recommendations(uid):
    # dummy recommendations using random sampling
    recs = random.sample(items, 3)
    return recs

if st.button("Recommend Items"):
    st.subheader(f"Recommendations for User {user_id}")
    for r in generate_recommendations(user_id):
        st.write("✔", r)

