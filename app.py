import streamlit as st
import pandas as pd
import os

st.set_page_config(
    page_title="StructGRIN-SCZ Prototype",
    page_icon="🧬",
    layout="wide"
)

st.title("🧬 StructGRIN-SCZ: Structural Vulnerability Index (SVI) Dashboard")
st.markdown("Interactive tool for analyzing structural vulnerability and clinical phenotypes of protein variants.")

# Load data safely
data_path = "final_svi_output.csv"
if os.path.exists(data_path):
    df = pd.read_csv(data_path)
    
    st.sidebar.header("Filter Options")
    selected_distance = st.sidebar.selectbox("Select Neighborhood Distance (Å):", [6, 8, 10])
    
    # Filter data
    filtered_df = df[df['distance_A'] == selected_distance]
    
    st.subheader(f"📊 Filtered Results (Distance: {selected_distance}Å)")
    st.dataframe(filtered_df[['residue', 'resname', 'region_domain', 'SASA_A2', 'RSA', 'svi_8A']])
    
    # Quick Metrics
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="Total Analyzed Residues", value=len(df))
    with col2:
        st.metric(label="Max SVI Score", value=f"{df['svi_8A'].max():.3f}")
    with col3:
        st.metric(label="Min SVI Score", value=f"{df['svi_8A'].min():.3f}")
        
    st.success("✅ Prototype loaded successfully with real project data!")
else:
    st.error(f"❌ Could not find data file at {data_path}. Please check your results folder.")
