# import streamlit as st
# import pandas as pd
# from io import BytesIO

# st.set_page_config(page_title="📁 File Convertor & Cleaner", layout="wide")

# st.title("📁 File Convertor and Cleaner.")
# st.write("### Upload your CSV and Excel Files to clean the data and convert formats effortlessly 🚀")

# files = st.file_uploader("Upload CSV or Excel Files", type=["csv", "xlsx"], accept_multiple_files=True)

# if files:
#     for file in files:
#         ext = file.name.split(".")[-1]

#         df = pd.read_csv(file) if ext == "csv" else pd.read_excel(file)

#         st.subheader(f"🔍 {file.name} - Preview")
#         st.dataframe(df.head())

#         if st.checkbox(f"Fill Missing Values - {file.name}"):
#             df.fillna(df.select_dtypes(include="number").mean(), inplace=True)
#             st.success("Missing values filled successfully")
#             st.dataframe(df.head())

#         selectedColumns = st.multiselect(f"Select Columns - {file.name}", df.columns, default=df.columns)

#         df = df[selectedColumns]
#         st.dataframe(df.head())

#         if st.checkbox(f"📊Show Chart - {file.name}") and not df.select_dtypes(include="number").empty:
#             st.bar_chart(df.select_dtypes(include="number").iloc[:, :2])

#         formatChoice = st.radio(f"Convert {file.name} To:", ["CSV", "Excel"], key=file.name)

#         if st.button(f"Download {file.name} as {formatChoice}"):
#             output = BytesIO()
#             if formatChoice == "CSV":
#                 df.to_csv(output, index=False)
#                 mime = "text/csv"
#                 newName = file.name.replace(ext, "csv")

#             else:
#                 df.to_excel(output, index=False)
#                 mime = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
#                 newName = file.name.replace(ext, "xlsx")

#             output.seek(0)
#             st.download_button("Download File", file_name=newName, data=output, mime= mime)
#         st.success("Processing Complete 🙌🏻")

import streamlit as st
import pandas as pd
import os
from io import BytesIO

st.set_page_config(page_title="📁 File Converter & Cleaner", layout="wide")

st.title("📁 File Converter and Cleaner")
st.write("### Upload your CSV and Excel files to clean data and convert formats effortlessly 🚀")

files = st.file_uploader("Upload CSV or Excel Files", type=["csv", "xlsx"], accept_multiple_files=True)

if files:
    for file in files:
        ext = file.name.split(".")[-1].lower()
        df = pd.read_csv(file) if ext == "csv" else pd.read_excel(file)

        st.subheader(f"🔍 {file.name} - Preview")
        st.dataframe(df.head())

        if st.checkbox(f"🧼 Fill Missing Values - {file.name}"):
            st.write(f"🔎 Missing values before fill: {df.isnull().sum().sum()}")
            df.fillna(df.select_dtypes(include="number").mean(), inplace=True)
            st.success("✅ Missing values filled successfully")
            st.dataframe(df.head())

        selected_columns = st.multiselect(f"🧠 Select Columns - {file.name}", df.columns, default=df.columns)
        df = df[selected_columns]
        st.dataframe(df.head())

        if st.checkbox(f"📊 Show Chart - {file.name}"):
            numeric_data = df.select_dtypes(include="number")
            if not numeric_data.empty:
                st.bar_chart(numeric_data.iloc[:, :2])
            else:
                st.warning("⚠️ No numeric columns found to display the chart.")

        format_choice = st.radio(f"💾 Convert {file.name} To:", ["CSV", "Excel"], key=file.name)

        if st.button(f"⬇️ Download {file.name} as {format_choice}"):
            output = BytesIO()
            filename_wo_ext = os.path.splitext(file.name)[0]
            new_name = f"{filename_wo_ext}.csv" if format_choice == "CSV" else f"{filename_wo_ext}.xlsx"

            if format_choice == "CSV":
                df.to_csv(output, index=False)
                mime = "text/csv"
            else:
                df.to_excel(output, index=False, engine='openpyxl')
                mime = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"

            output.seek(0)
            st.download_button("⬇️ Download File", file_name=new_name, data=output, mime=mime)

        st.success("✅ Processing Complete 🙌🏻")
