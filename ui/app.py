import streamlit as st

def launch_ui(coordinator):
    st.title("📚 Agentic RAG Chatbot")
    
    uploaded_files = st.file_uploader("Upload your documents", accept_multiple_files=True, type=["pdf", "docx", "pptx", "csv", "txt", "md"])
    
    if uploaded_files:
        user_query = st.text_input("Ask a question about your documents")
        if st.button("Submit"):
            answer, sources = coordinator.process_query(user_query, uploaded_files)
            st.markdown(f"### 🧠 Answer:\n{answer}")
            st.markdown("### 📌 Sources:")
            for chunk in sources:
                st.write(f"- {chunk}")
