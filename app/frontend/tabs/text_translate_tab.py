import streamlit as st

def render():
    #widget_key = st.session_state.translate_input_widget_key

    text = st.text_area(
        "Enter text you wish to translate",
        value=st.session_state.get("text_input_data", ""),
        height=200,
        key=st.session_state.translate_input_widget_key
    )

    st.session_state.text_input_data = text
    return text

    
    
    
    
    
    
      

  
  
    
    
