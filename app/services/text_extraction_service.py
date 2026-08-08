from app.utils.pdf_utils import extract_pdf_text
from app.utils.excel_utils import extract_excel_text
from app.utils.csv_utils import extract_csv_text

def extract_text_from_file(uploaded_file):
    file_type = uploaded_file.type
    #---------------------------
    # Text Files
    #---------------------------
    if file_type == "text/plain":
        return uploaded_file.read().decode("utf-8")
    # -----------------------------
    # PDF
    # -----------------------------
    elif file_type == "application/pdf":
        return extract_pdf_text(uploaded_file)
    # -----------------------------
    # Excel 
    # -----------------------------
    elif file_type in [
        "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        "application/vnd.ms-excel"
    ]:
        return extract_excel_text(uploaded_file)
    # -----------------------------
    # CSV
    # -----------------------------
    elif file_type == "text/csv":
        return extract_csv_text(uploaded_file)
    
    return None