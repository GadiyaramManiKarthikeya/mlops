import streamlit as st

st.set_page_config(page_title="MLOps Project: Real-Time Recommendation System", layout="wide")

# -----------------------------
# Title & Intro
# -----------------------------
st.title("Real-Time Recommendation System (MLOps Project)")
st.markdown("""
This Streamlit app is a simplified version of our MLOps project workflow.
It demonstrates:
-  End-to-end MLOps stages  
-  Tools used  
-  Simple recommendation demo  
""")

st.divider()

# -----------------------------
# MLOps Workflow Section
# -----------------------------
st.header(" MLOps Workflow Stages")
st.markdown("""
1. **Data Ingestion** – Collect & clean data  
2. **Data Processing** – Validate schema and preprocess  
3. **Model Training** – ML model training + experiment tracking  
4. **Model Evaluation** – Compute metrics  
5. **Model Registry** – Save & version models  
6. **Deployment** – Expose model  
7. **Monitoring** – Drift, performance, alerts  
""")

st.divider()

# -----------------------------
# Tools Section
# -----------------------------
st.header(" MLOps Tools Used")
st.markdown("""
- **GitHub** – Version control  
- **MLFlow** – Experiment tracking & model registry  
- **Docker** – Environment packaging  
- **Kubernetes** – Deployment and scaling  
- **Prometheus + Grafana** – Monitoring  
- **FastAPI** – Model serving  
""")

st.divider()

# -----------------------------
# Simple Recommendation Demo
# -----------------------------
st.header("Simple Recommendation Demo")

st.write("Enter a user ID to generate sample recommendations:")

user_id = st.number_input("User ID", min_value=1, max_value=9999, value=1)

def recommend(user_id):
    # Dummy logic (replace with real model later)
    return [
        f"Recommended_Item_{user_id}_1",
        f"Recommended_Item_{user_id}_2",
        f"Recommended_Item_{user_id}_3"
    ]

if st.button("Generate Recommendations"):
    st.subheader("Your Recommendations:")
    for rec in recommend(user_id):
        st.write("", rec)

st.divider()

# -----------------------------
# Conclusion
# -----------------------------
st.header(" Summary")
st.markdown("""
This simple app shows:
- How MLOps workflow works  
- How real-time recommendations are generated  
- How to deploy a simple UI using **GitHub + Streamlit**  

This is a simplified frontend version of your PPT project.
""")
