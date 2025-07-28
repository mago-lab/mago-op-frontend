import streamlit as st

def apply_custom_style():
    """커스텀 스타일을 적용합니다."""
    st.markdown("""
    <style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }

    .sub-header {
        font-size: 1.5rem;
        font-weight: 600;
        color: #2c3e50;
        margin-bottom: 1rem;
    }

    .info-box {
        background-color: #e8f4fd;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #1f77b4;
        margin: 1rem 0;
    }

    .success-box {
        background-color: #d4edda;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #28a745;
        margin: 1rem 0;
    }

    .error-box {
        background-color: #f8d7da;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #dc3545;
        margin: 1rem 0;
    }

    .upload-area {
        border: 2px dashed #1f77b4;
        border-radius: 0.5rem;
        padding: 2rem;
        text-align: center;
        background-color: #f8f9fa;
        margin: 1rem 0;
    }

    .metric-card {
        background-color: #ffffff;
        padding: 1rem;
        border-radius: 0.5rem;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        margin: 0.5rem 0;
    }

    .sidebar .sidebar-content {
        background-color: #f8f9fa;
    }

    .stButton > button {
        background-color: #1f77b4;
        color: white;
        border: none;
        border-radius: 0.5rem;
        padding: 0.5rem 1rem;
        font-weight: 600;
    }

    .stButton > button:hover {
        background-color: #1565c0;
    }

    .stSelectbox > div > div > div {
        background-color: #ffffff;
        border: 1px solid #ced4da;
        border-radius: 0.5rem;
    }

    .stTextInput > div > div > input {
        border: 1px solid #ced4da;
        border-radius: 0.5rem;
    }
    </style>
    """, unsafe_allow_html=True)

def apply_button_style(style: str, key: str = "button"):
    """버튼 스타일을 적용합니다."""
    if style == "primary":
        st.markdown(f"""
        <style>
        .{key} > button {{
            background-color: #1f77b4;
            color: white;
            border: none;
            border-radius: 0.5rem;
            padding: 0.75rem 1.5rem;
            font-weight: 600;
            font-size: 1rem;
        }}
        .{key} > button:hover {{
            background-color: #1565c0;
        }}
        </style>
        """, unsafe_allow_html=True)
    elif style == "success":
        st.markdown(f"""
        <style>
        .{key} > button {{
            background-color: #28a745;
            color: white;
            border: none;
            border-radius: 0.5rem;
            padding: 0.75rem 1.5rem;
            font-weight: 600;
            font-size: 1rem;
        }}
        .{key} > button:hover {{
            background-color: #218838;
        }}
        </style>
        """, unsafe_allow_html=True)
    elif style == "warning":
        st.markdown(f"""
        <style>
        .{key} > button {{
            background-color: #ffc107;
            color: #212529;
            border: none;
            border-radius: 0.5rem;
            padding: 0.75rem 1.5rem;
            font-weight: 600;
            font-size: 1rem;
        }}
        .{key} > button:hover {{
            background-color: #e0a800;
        }}
        </style>
        """, unsafe_allow_html=True)
    elif style == "danger":
        st.markdown(f"""
        <style>
        .{key} > button {{
            background-color: #dc3545;
            color: white;
            border: none;
            border-radius: 0.5rem;
            padding: 0.75rem 1.5rem;
            font-weight: 600;
            font-size: 1rem;
        }}
        .{key} > button:hover {{
            background-color: #c82333;
        }}
        </style>
        """, unsafe_allow_html=True)