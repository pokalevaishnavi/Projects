import streamlit as st
import os

st.set_page_config(page_title="File Manager", layout="wide")
st.title("📁 File Manager")

# ---------- Helper Functions ----------

def list_files():
    return [f for f in os.listdir() if os.path.isfile(f)]


# ---------- Sidebar Navigation ----------
option = st.sidebar.radio("📌 Choose Action", [
    "📄 Create File",
    "📂 View Files",
    "📖 Read File",
    "✏️ Edit File",
    "❌ Delete File",
    "📤 Upload File",
])

# ---------- Create File ----------
if option == "📄 Create File":
    filename = st.text_input("Enter filename to create:")
    if st.button("Create File"):
        if filename:
            try:
                with open(filename, 'x'):
                    pass
                st.success(f"✅ File '{filename}' created!")
            except FileExistsError:
                st.warning(f"⚠️ File '{filename}' already exists.")
        else:
            st.error("❌ Please enter a valid filename.")

# ---------- View All Files ----------
elif option == "📂 View Files":
    st.subheader("📄 Files in Current Directory")
    files = list_files()
    if files:
        for file in files:           
            st.markdown(f"**{file}** ", unsafe_allow_html=True)
    else:
        st.info("No files found.")

# ---------- Read File ----------
elif option == "📖 Read File":
    files = list_files()
    if files:
        filename = st.selectbox("Choose a file to read:", files)
        if st.button("Read File"):
            try:
                with open(filename, 'r') as f:
                    content = f.read()
                st.text_area(f"📄 Content of {filename}", content, height=300)
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("No files to read.")

# ---------- Edit File ----------
elif option == "✏️ Edit File":
    files = list_files()
    if files:
        filename = st.selectbox("Choose a file to edit:", files)
        text_input = st.text_area("Enter content to append:")
        if st.button("Append Content"):
            try:
                with open(filename, 'a') as f:
                    f.write(text_input + '\n')
                st.success(f"Content added to '{filename}'")
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("No files to edit.")

# ---------- Delete File ----------
elif option == "❌ Delete File":
    files = list_files()
    if files:
        filename = st.selectbox("Select a file to delete:", files)
        if st.button("Delete File"):
            try:
                os.remove(filename)
                st.success(f"✅ '{filename}' deleted.")
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("No files to delete.")

# ---------- Upload File ----------
elif option == "📤 Upload File":
    uploaded_file = st.file_uploader("Choose a file to upload")
    if uploaded_file is not None:
        with open(uploaded_file.name, "wb") as f:
            f.write(uploaded_file.getbuffer())
        st.success(f"✅ Uploaded '{uploaded_file.name}' successfully!")

