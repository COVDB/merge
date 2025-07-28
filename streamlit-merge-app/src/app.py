import streamlit as st
import pandas as pd
from utils.merge import merge_data

def main():
    st.title("Excel Data Merger")
    
    st.write("Upload three Excel files to merge their data.")
    
    file1 = st.file_uploader("AM LOG", type=["xlsx"])
    file2 = st.file_uploader("ZSD_PO_PER_SO ", type=["xlsx"])
    file3 = st.file_uploader("ZSTATUS", type=["xlsx"])
    
    if st.button("Merge"):
        if file1 and file2 and file3:
            # Read the uploaded files
            df1 = pd.read_excel(file1)
            df2 = pd.read_excel(file2)
            df3 = pd.read_excel(file3)

            # Select relevant columns from AM LOG
            am_log_columns = ["Delivery Date", "Customer Reference", "Material Number", "Serial number", "Year of construction", "Month of construction"]
            df1 = df1[am_log_columns]

            # Merge the data
            merged_df = merge_data(df1, df2, df3)

            st.write("Merged Data:")
            st.dataframe(merged_df)
        else:
            st.error("Please upload all three Excel files.")

if __name__ == "__main__":
    main()
