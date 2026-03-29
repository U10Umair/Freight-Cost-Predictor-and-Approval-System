# import pandas as pd
# import numpy as np
# import streamlit as st

# from inference.predict_freight import predict_freight_cost
# from inference.predict_invoice_flag import predict_invoice_flag


# # --------------------------------------------------
# # Page Configuration
# # --------------------------------------------------

# st.set_page_config(
#     page_title="📦 Vendor Invoice Intelligence Portal",
#     page_icon="📦",
#     layout="wide"
# )


# # --------------------------------------------------
# # Header Section
# # --------------------------------------------------

# st.markdown("""
# # 📦 Vendor Invoice Intelligence Portal
# ### AI-Driven Freight Cost Prediction & Invoice Risk Flagging

# This internal analytics portal leverages machine learning to
# - **Forecast freight costs accurately**
# - **Detect risky or abnormal vendor invoices**
# - **Reduce financial leakage and manual workload**
# """)

# st.divider()


# # --------------------------------------------------
# # Sidebar
# # --------------------------------------------------

# st.sidebar.title("🔍 Model Selection")

# selected_model = st.sidebar.radio(
#     "Choose Prediction Module",
#     [
#         "Freight Cost Prediction",
#         "Invoice Manual Approval Flag"
#     ]
# )

# st.sidebar.markdown("""
# ---
# **Business Impact**
# - 📈 Improved cost forecasting
# - 🚨 Reduced invoice fraud & anomalies
# - ⚙️ Faster finance operations
# """)


# # --------------------------------------------------
# # Freight Cost Prediction
# # --------------------------------------------------


# if selected_model == "Freight Cost Prediction":
#     st.subheader("🚚 Freight Cost Prediction")

#     st.markdown("""
#     **Objective:**
#     Predict freight cost for a vendor invoice using **Quantity** and **Invoice Dollars**
#     to support budgeting, forecasting, and vendor negotiations.
#     """)

#     with st.form("freight_form"):
#         # col1, col2 = st.columns(2)

#         # with col1:
#         #     quantity = st.number_input(
#         #         "📦 Quantity",
#         #         min_value=1,
#         #         value=1200
#         #     )

        
#         dollars = st.number_input(
#                 "💲 Invoice Dollars",
#                 min_value=1.0,
#                 value=18500.0
#             )

#         submit_freight = st.form_submit_button("🔮 Predict Freight Cost")

#         if submit_freight:
#             input_data = {
#                 # "Quantity": [quantity],
#                 "Dollars": [dollars]
#             }

#             prediction = predict_freight_cost(input_data)['Predicted_Freight']

#             st.success("Prediction completed successfully.")

#             st.metric(
#                 label="📊 Estimated Freight Cost",
#                 value=f"${prediction[0]:,.2f}"
#             )
            
            
# # --------------------------------------------------------------
# # Invoice Flag Prediction
# # --------------------------------------------------------------
# else:
#     st.subheader("🚨 Invoice Manual Approval Prediction")

#     st.markdown("""
#     **Objective:**
#     Predict whether a vendor invoice should be **flagged for manual approval**
#     based on abnormal cost, freight, or delivery patterns.
#     """)

#     with st.form("invoice_flag_form"):
#         col1, col2, col3 = st.columns(3)

#         with col1:
#             invoice_quantity = st.number_input(
#                 "Invoice Quantity",
#                 min_value=1,
#                 value=50
#             )

#             freight = st.number_input(
#                 "Freight Cost",
#                 min_value=0.0,
#                 value=1.73
#             )

#         with col2:
#             invoice_dollars = st.number_input(
#                 "Invoice Dollars",
#                 min_value=1.0,
#                 value=352.95
#             )

#             total_item_quantity = st.number_input(
#                 "Total Item Quantity",
#                 min_value=1,
#                 value=162
#             )

#         with col3:
#             total_item_dollars = st.number_input(
#                 "Total Item Dollars",
#                 min_value=1.0,
#                 value=2476.0
#             )

#         submit_flag = st.form_submit_button("🧠 Evaluate Invoice Risk")

#     if submit_flag:
#         input_data = {
#             "invoice_quantity": [invoice_quantity],
#             "freight": [freight],
#             "invoice_dollars": [invoice_dollars],
#             "total_item_quantity": [total_item_quantity],
#             "total_item_dollars": [total_item_dollars]
#         }
        
#         flag_prediction = predict_invoice_flag(input_data)['Predicted_Flag']

#         is_flagged = bool(flag_prediction[0])

#         if is_flagged:
#                 st.error("🚨 Invoice requires **MANUAL APPROVAL**")
#         else:
#              st.success("✅ Invoice is **SAFE for Auto-Approval**")


"""
refined code with some changes
"""



import pandas as pd
import numpy as np
import streamlit as st
from inference.predict_freight import predict_freight_cost
from inference.predict_invoice_flag import predict_invoice_flag

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------
st.set_page_config(
    page_title="📦 Vendor Invoice Intelligence Portal",
    page_icon="📦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --------------------------------------------------
# Custom CSS 
# --------------------------------------------------
st.markdown("""
<style>
    /* Ensure text is always readable */
    .stApp {
        background-color: #f8f9fa;
    }
    
    /* Dark mode detection and styling */
    @media (prefers-color-scheme: dark) {
        .stApp {
            background-color: #1a1a2e;
        }
        
        .main-header {
            background: linear-gradient(135deg, #0f3460 0%, #16213e 100%);
        }
        
        .metric-card {
            background: linear-gradient(135deg, #0f3460 0%, #16213e 100%);
        }
        
        .stForm {
            background: #16213e;
            color: #ffffff;
        }
        
        .result-card {
            background: linear-gradient(135deg, #0f3460 0%, #16213e 100%);
        }
        
        .business-impact {
            background: linear-gradient(135deg, #0f3460 0%, #16213e 100%);
        }
        
        p, label, .stMarkdown {
            color: #e0e0e0 !important;
        }
        
        h1, h2, h3, h4 {
            color: #ffffff !important;
        }
    }
    
    /* Card styling for both modes */
    .css-1r6slb0, .css-1v3fvcr {
        background: rgba(255, 255, 255, 0.95);
        border-radius: 20px;
        padding: 25px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        border: 1px solid rgba(0,0,0,0.1);
    }
    
    @media (prefers-color-scheme: dark) {
        .css-1r6slb0, .css-1v3fvcr {
            background: #16213e;
            border: 1px solid rgba(255,255,255,0.1);
        }
    }
    
    /* Header styling */
    .main-header {
        background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
        padding: 2rem;
        border-radius: 20px;
        margin-bottom: 2rem;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
    
    .main-header h1 {
        color: #ffffff;
        font-size: 2.5rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }
    
    .main-header h3 {
        color: #f0f0f0;
        font-size: 1.2rem;
        font-weight: 500;
    }
    
    .main-header p {
        color: #e0e0e0;
        margin-top: 1rem;
    }
    
    /* Metric card styling */
    .metric-card {
        background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        color: #ffffff;
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        transition: transform 0.3s ease;
    }
    
    .metric-card:hover {
        transform: translateY(-5px);
    }
    
    .metric-value {
        font-size: 2rem;
        font-weight: bold;
        margin: 10px 0;
        color: #ffffff;
    }
    
    .metric-label {
        font-size: 1rem;
        color: #f0f0f0;
    }
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
        color: white;
        border: none;
        padding: 12px 30px;
        border-radius: 25px;
        font-weight: 600;
        transition: all 0.3s ease;
        width: 100%;
        cursor: pointer;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 20px rgba(30,60,114,0.4);
        background: linear-gradient(135deg, #2a5298 0%, #1e3c72 100%);
    }
    
    /* Form styling */
    .stForm {
        background: #ffffff;
        border-radius: 20px;
        padding: 20px;
        box-shadow: 0 5px 20px rgba(0,0,0,0.08);
    }
    
    @media (prefers-color-scheme: dark) {
        .stForm {
            background: #16213e;
        }
    }
    
    /* Input field styling */
    .stNumberInput > div > div > input {
        border-radius: 10px;
        border: 2px solid #d1d5db;
        transition: all 0.3s ease;
        background: white;
        color: #1f2937;
    }
    
    @media (prefers-color-scheme: dark) {
        .stNumberInput > div > div > input {
            background: #0f3460;
            border-color: #2a5298;
            color: #ffffff;
        }
    }
    
    .stNumberInput > div > div > input:focus {
        border-color: #1e3c72;
        box-shadow: 0 0 0 3px rgba(30,60,114,0.2);
        outline: none;
    }
    
    /* Label styling */
    .stNumberInput label, .stRadio label {
        font-weight: 600;
        color: #1f2937;
        margin-bottom: 0.5rem;
    }
    
    @media (prefers-color-scheme: dark) {
        .stNumberInput label, .stRadio label {
            color: #e0e0e0;
        }
    }
    
    /* Success and error message styling */
    .stAlert {
        border-radius: 15px;
        border-left: 5px solid;
        padding: 15px;
        margin: 10px 0;
    }
    
    /* Sidebar styling */
    .css-1d391kg {
        background: #ffffff;
        border-right: 1px solid #e5e7eb;
    }
    
    @media (prefers-color-scheme: dark) {
        .css-1d391kg {
            background: #16213e;
            border-right: 1px solid #2a5298;
        }
    }
    
    /* Tab styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background-color: #f3f4f6;
        border-radius: 10px;
        padding: 5px;
    }
    
    @media (prefers-color-scheme: dark) {
        .stTabs [data-baseweb="tab-list"] {
            background-color: #0f3460;
        }
    }
    
    .stTabs [data-baseweb="tab"] {
        border-radius: 8px;
        padding: 10px 20px;
        font-weight: 600;
        color: #1f2937;
    }
    
    @media (prefers-color-scheme: dark) {
        .stTabs [data-baseweb="tab"] {
            color: #e0e0e0;
        }
    }
    
    /* Divider styling */
    hr {
        margin: 2rem 0;
        border: none;
        height: 2px;
        background: linear-gradient(90deg, transparent, #1e3c72, transparent);
    }
    
    /* Animation for metrics */
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    .stMetric {
        animation: fadeInUp 0.6s ease-out;
    }
    
    /* Result card styling */
    .result-card {
        background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
        padding: 30px;
        border-radius: 20px;
        text-align: center;
        margin-top: 20px;
        animation: fadeInUp 0.6s ease-out;
    }
    
    .result-card-success {
        background: linear-gradient(135deg, #059669 0%, #10b981 100%);
    }
    
    .result-card-error {
        background: linear-gradient(135deg, #dc2626 0%, #ef4444 100%);
    }
    
    .result-card h3 {
        color: white;
        font-size: 1.8rem;
        margin: 15px 0;
    }
    
    .result-card p {
        color: rgba(255,255,255,0.9);
        font-size: 1rem;
    }
    
    /* Business impact card */
    .business-impact {
        background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
        padding: 20px;
        border-radius: 15px;
        margin-top: 20px;
    }
    
    .business-impact h4 {
        color: white;
        margin-bottom: 15px;
    }
    
    .business-impact p {
        color: #f0f0f0;
        margin: 8px 0;
    }
    
    /* Tooltip styling */
    .tooltip-icon {
        cursor: help;
        margin-left: 5px;
        color: #6b7280;
    }
    
    /* Footer styling */
    .footer {
        text-align: center;
        padding: 20px;
        color: #6b7280;
        margin-top: 40px;
    }
    
    @media (prefers-color-scheme: dark) {
        .footer {
            color: #9ca3af;
        }
    }
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# Header Section
# --------------------------------------------------
st.markdown("""
<div class="main-header">
    <h1>📦 Vendor Invoice Intelligence Portal</h1>
    <h3>AI-Driven Freight Cost Prediction & Invoice Risk Flagging</h3>
    <p>This internal analytics portal leverages machine learning to:
    <br>• <strong>Forecast freight costs accurately</strong>
    <br>• <strong>Detect risky or abnormal vendor invoices</strong>
    <br>• <strong>Reduce financial leakage and manual workload</strong></p>
</div>
""", unsafe_allow_html=True)

# --------------------------------------------------
# Sidebar
# --------------------------------------------------
with st.sidebar:
    st.markdown("""
    <div style="text-align: center; padding: 20px 0;">
        <div style="font-size: 3rem;">🔍</div>
        <h2 style="color: #1e3c72;">Model Selection</h2>
    </div>
    """, unsafe_allow_html=True)
    
    selected_model = st.radio(
        "Choose Prediction Module",
        [
            "Freight Cost Prediction",
            "Invoice Manual Approval Flag"
        ],
        label_visibility="collapsed"
    )
    
    st.markdown("""
    <div class="business-impact">
        <h4 style="color: white; margin-bottom: 15px;">💡 Business Impact</h4>
        <p>📈 Improved cost forecasting</p>
        <p>🚨 Reduced invoice fraud & anomalies</p>
        <p>⚙️ Faster finance operations</p>
    </div>
    """, unsafe_allow_html=True)

# --------------------------------------------------
# Freight Cost Prediction
# --------------------------------------------------
if selected_model == "Freight Cost Prediction":
    st.markdown("""
    <div style="margin-bottom: 20px;">
        <h2 style="color: #1e3c72;">🚚 Freight Cost Prediction</h2>
        <p style="color: #4b5563;"><strong>Objective:</strong>
        Predict freight cost for a vendor invoice using <strong>Quantity</strong> and <strong>Invoice Dollars</strong>
        to support budgeting, forecasting, and vendor negotiations.</p>
    </div>
    """, unsafe_allow_html=True)
    
    with st.form("freight_form"):
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            dollars = st.number_input(
                "💲 Invoice Dollars",
                min_value=1.0,
                value=18500.0,
                help="Enter the invoice amount to predict freight cost"
            )
            
            submit_freight = st.form_submit_button("🔮 Predict Freight Cost", use_container_width=True)
        
        if submit_freight:
            input_data = {
                "Dollars": [dollars]
            }
            
            with st.spinner("🔄 Calculating freight prediction..."):
                prediction = predict_freight_cost(input_data)['Predicted_Freight']
            
            st.markdown(f"""
            <div class="result-card">
                <div style="font-size: 2rem;">📊</div>
                <h3>Estimated Freight Cost</h3>
                <div style="font-size: 3rem; font-weight: bold; color: white; margin: 20px 0;">${prediction[0]:,.2f}</div>
                <p>✅ Prediction completed successfully</p>
            </div>
            """, unsafe_allow_html=True)
            
# --------------------------------------------------------------
# Invoice Flag Prediction
# --------------------------------------------------------------
else:
    st.markdown("""
    <div style="margin-bottom: 20px;">
        <h2 style="color: #1e3c72;">🚨 Invoice Manual Approval Prediction</h2>
        <p style="color: #4b5563;"><strong>Objective:</strong>
        Predict whether a vendor invoice should be <strong>flagged for manual approval</strong>
        based on abnormal cost, freight, or delivery patterns.</p>
    </div>
    """, unsafe_allow_html=True)
    
    with st.form("invoice_flag_form"):
        col1, col2, col3 = st.columns(3)
        
        with col1:
            invoice_quantity = st.number_input(
                "📦 Invoice Quantity",
                min_value=1,
                value=50,
                help="Number of items in this invoice"
            )
            
            freight = st.number_input(
                "🚚 Freight Cost",
                min_value=0.0,
                value=1.73,
                help="Shipping cost for this invoice"
            )
        
        with col2:
            invoice_dollars = st.number_input(
                "💰 Invoice Dollars",
                min_value=1.0,
                value=352.95,
                help="Total amount of this invoice"
            )
            
            total_item_quantity = st.number_input(
                "📊 Total Item Quantity",
                min_value=1,
                value=162,
                help="Total quantity across all items"
            )
        
        with col3:
            total_item_dollars = st.number_input(
                "💵 Total Item Dollars",
                min_value=1.0,
                value=2476.0,
                help="Total value across all items"
            )
        
        submit_flag = st.form_submit_button("🧠 Evaluate Invoice Risk", use_container_width=True)
    
    if submit_flag:
        input_data = {
            "invoice_quantity": [invoice_quantity],
            "freight": [freight],
            "invoice_dollars": [invoice_dollars],
            "total_item_quantity": [total_item_quantity],
            "total_item_dollars": [total_item_dollars]
        }
        
        with st.spinner("🔍 Analyzing invoice patterns..."):
            flag_prediction = predict_invoice_flag(input_data)['Predicted_Flag']
        
        is_flagged = bool(flag_prediction[0])
        
        if is_flagged:
            st.markdown("""
            <div class="result-card result-card-error">
                <div style="font-size: 3rem;">🚨</div>
                <h3>Invoice requires MANUAL APPROVAL</h3>
                <p>High-risk pattern detected. Please review this invoice carefully.</p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="result-card result-card-success">
                <div style="font-size: 3rem;">✅</div>
                <h3>Invoice is SAFE for Auto-Approval</h3>
                <p>No risk indicators detected. Invoice can be processed automatically.</p>
            </div>
            """, unsafe_allow_html=True)

# --------------------------------------------------
# Footer
# --------------------------------------------------
st.markdown("""
<div class="footer">
    <p>Powered by AI & Machine Learning | Vendor Invoice Intelligence Portal v2.0</p>
</div>
""", unsafe_allow_html=True)