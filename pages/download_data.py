import streamlit as st, os

# Sidebar name
with st.sidebar:
    st.title('Download Data')

st.title('Download Data')

# Load links for csv files
data_output_dir = 'data/output/'
if os.path.exists(data_output_dir):
    files = sorted([f for f in os.listdir('data/output/') if f.endswith('.csv')])
    fpaths = [os.path.join(data_output_dir, f) for f in files]
    for f, fp in zip(files, fpaths):
        with open(fp, 'rb') as file:
            st.download_button(label=f, data=file, file_name=f, mime='text/csv')