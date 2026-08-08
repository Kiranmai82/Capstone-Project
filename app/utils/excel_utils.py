import pandas as pd

def extract_excel_text(uploaded_file):
    
    # Read the Excel file into a DataFrame
    df = pd.read_excel(uploaded_file)
    # return the DataFrame as a string representation    
    return df.to_string()