import streamlit as st
import pandas as pd
import plotly.express as px
import mysql.connector
from datetime import datetime

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="Pharmacy Inventory Dashboard",
    page_icon="💊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =====================================================
# CUSTOM CSS
# =====================================================
st.markdown("""
<style>

.stTabs [data-baseweb="tab"]{
    background-color:#158BDA;
    color:white;
    border-radius:10px;
    padding:10px 20px;
    font-weight:bold;
}

.stTabs [aria-selected="true"]{
    background-color:#CC2411 !important;
    color:white !important;
}

</style>
""", unsafe_allow_html=True)
st.markdown("""
<style>

/* ================================================= */
/* MAIN BACKGROUND */
/* ================================================= */

.stApp {

    background-image:
    linear-gradient(
        rgba(0, 18, 25, 0.88),
        rgba(0, 48, 73, 0.92)
    ),

    url("https://images.unsplash.com/photo-1576091160399-112ba8d25d1d");

    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}
            
/* ================================================= */
/* HEADINGS */
/* ================================================= */

h1,h2,h3,h4 {

    color: white;

    # font-family: 
    <h2 style='
font-size:42px;
font-weight:800;
font-family:Garamond;
text-shadow:0 0 10px rgba(255,255,255,0.2);
'>
50
</h2>
}

/* ================================================= */
/* KPI CARDS */
/* ================================================= */

[data-testid="stMetric"] {

    /* Glass Blue Gradient */
    background: linear-gradient(
        135deg,
        rgba(0,119,182,0.75),
        rgba(0,180,216,0.45)
    );

    /* Glass Effect */
    backdrop-filter: blur(18px);
    -webkit-backdrop-filter: blur(18px);

    /* Soft Border */
    border: 1px solid rgba(255,255,255,0.18);

    /* Layout */
    padding: 28px 20px;
    border-radius: 30px;

    /* Professional Shadow */
    box-shadow:
        0 8px 32px rgba(0, 119, 182, 0.18),
        0 2px 8px rgba(255,255,255,0.08) inset;

    /* Smooth Animation */
    transition:
        transform 0.35s ease,
        box-shadow 0.35s ease,
        background 0.35s ease;

    position: relative;
    overflow: hidden;
}

/* Elegant Glow Layer */
[data-testid="stMetric"]::before {
    content: "";

    position: absolute;
    top: 0;
    left: -120%;

    width: 120%;
    height: 100%;

    background: linear-gradient(
        90deg,
        transparent,
        rgba(255,255,255,0.18),
        transparent
    );

    transition: 0.8s;
}

/* Hover Animation */
[data-testid="stMetric"]:hover {

    # transform: translateY(-6px) scale(1.02);
    transform: translateY(-8px) scale(1.04);

    box-shadow:
        0 14px 40px rgba(0,119,182,0.28),
        0 4px 12px rgba(255,255,255,0.12) inset;

    background: linear-gradient(
        135deg,
        rgba(0,119,182,0.82),
        rgba(0,180,216,0.58)
    );
}

/* Shine Effect Movement */
[data-testid="stMetric"]:hover::before {
    left: 130%;
}

/* KPI LABEL */
[data-testid="stMetricLabel"] {
    color: rgba(255,255,255,0.88);
    font-size: 17px;
    font-weight: 700;
    letter-spacing: 0.5px;
    
}

/* KPI VALUE */
[data-testid="stMetricValue"] {
    color: white;
    font-size: 37px;
    font-weight: 700;
}

/* Delta Value */
[data-testid="stMetricDelta"] {
    color: #DFF6FF;
    font-weight: 800;
}

/* Remove default ugly borders */
div[data-testid="metric-container"] {
    border: none !important;
}
 box-shadow:0 8px 20px rgba(0,0,0,0.25);
border:1px solid rgba(255,255,255,0.1);
backdrop-filter: blur(8px);   

[data-testid="stMetric"] {

border-left: 5px solid #00D1FF;

}
            
                           
/* ================================================= */
/* SIDEBAR */
/* ================================================= */

section[data-testid="stSidebar"] {

    background:
    linear-gradient(
        180deg,
        #001219,
        #005F73
    );
}

section[data-testid="stSidebar"] * {

    color: white;
}

/* ================================================= */
/* DROPDOWNS */
/* ================================================= */

div[data-baseweb="select"] {

    background-color:
    rgba(255,255,255,0.08);

    border-radius: 12px;
}

/* ================================================= */
/* BUTTONS */
/* ================================================= */

# .stButton>button {

    width: 100%;

    height: 52px;

    background:
    linear-gradient(
        135deg,
        #0096C7,
        #00B4D8
    );

    color: white;

    border-radius: 14px;

    border: none;

    font-size: 16px;

    font-weight: 800;

    transition: all 0.3s ease;

    box-shadow:
    0px 6px 20px rgba(0,0,0,0.5);
}

.stButton>button:hover {

    transform: translateY(-3px);

    background:
    linear-gradient(
        135deg,
        #EE9B00,
        #CA6702
    );

    box-shadow:
    0px 10px 25px rgba(0,0,0,0.45);
}
/* ================================================= */
/* DOWNLOAD BUTTON */
/* ================================================= */

.stDownloadButton>button {

    background:
    linear-gradient(
        135deg,
        #AE2012,
        #BB3E03
    );

    color: white;

    border-radius: 12px;

    height: 50px;

    border: none;

    font-size: 16px;

    font-weight: bold;
}
            
/* ================================================= */
/* GLASS EFFECT CONTAINERS */
/* ================================================= */

[data-testid="stPlotlyChart"] {

    background: rgba(255,255,255,0.08);

    border: 1px solid rgba(255,255,255,0.18);

    backdrop-filter: blur(14px);

    border-radius: 20px;

    padding: 10px;

    box-shadow:
    0px 8px 32px rgba(0,0,0,0.35);

    margin-bottom: 20px;
}

/* ================================================= */
/* DATAFRAME GLASS EFFECT */
/* ================================================= */

[data-testid="stDataFrame"] {

    background: rgba(255,255,255,0.08);

    backdrop-filter: blur(14px);

    border-radius: 20px;

    border: 1px solid rgba(255,255,255,0.2);

    padding: 10px;

    box-shadow:
    0px 8px 32px rgba(0,0,0,0.3);
}

/* ================================================= */
/* SIDEBAR GLASS */
/* ================================================= */

section[data-testid="stSidebar"] {

    background:
     linear-gradient(
     180deg,
        rgba(0,18,25,0.95),
        rgba(0,95,115,0.92)
    );
    


    backdrop-filter: blur(18px);
}

/* ================================================= */
/* CHART HOVER EFFECT */
/* ================================================= */

[data-testid="stPlotlyChart"]:hover {

    transform: scale(1.01);

    transition: 0.3s ease-in-out;
}     
                        
/* ================================================= */
/* TABLES */
/* ================================================= */

[data-testid="stDataFrame"] {

    border-radius: 15px;

    overflow: hidden;

    background-color: white;
}

/* ================================================= */
/* HR */
/* ================================================= */

hr {

    border: 1px solid rgba(255,255,255,0.2);
}

</style>
""", unsafe_allow_html=True)

# =====================================================
# MYSQL CONNECTION
# =====================================================

import os
from dotenv import load_dotenv
import mysql.connector

# Load environment variables
load_dotenv()

username = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
host = os.getenv("DB_HOST")
database = os.getenv("DB_NAME")

# Connect to MySQL
conn = mysql.connector.connect(
    host=host,
    user=username,
    password=password,
    database=database
)

print("MySQL connected successfully!")

conn.close()
query = "SELECT * FROM medicine_inventory"

df = pd.read_sql(query, conn)

# =====================================================
# DATE PROCESSING
# =====================================================

df["Expiry_Date"] = pd.to_datetime(df["Expiry_Date"])

today = datetime.today()

df["Days_To_Expire"] = (
    df["Expiry_Date"] - today
).dt.days

# =====================================================
# EXPIRY STATUS
# =====================================================

df["Expiry_Status"] = df["Days_To_Expire"].apply(
    lambda x:
    "Expired" if x < 0 else
    "Expiring Soon" if x <= 30 else
    "Safe"
)

#Styled Title with Blue Accent

st.markdown("""
<div style='
background:rgba(255,255,255,0.08);
padding:30px;
border-radius:25px;
backdrop-filter:blur(15px);
text-align:center;
margin-bottom:20px;
'>

<h1 style='
color:#00D1FF;
font-size:55px;
font-weight:800;
'>
🛡️ MediGuard
</h1>

<h2 style='
color:white;
font-size:42px;
'>
💊 Medicine Inventory & Expiry Tracking Dashboard
</h2>

<p style='
color:#E0E0E0;
font-size:20px;
'>
📦 Smart Inventory Monitoring |
📅 Expiry Alerts |
🏥 Supplier Analytics
</p>

</div>
""", unsafe_allow_html=True)

st.markdown("---")

from datetime import datetime

st.markdown(
f"""
<div style='text-align:right;
color:white;
font-size:18px;
font-weight:bold;'>

🕒 {datetime.now().strftime("%d-%m-%Y %H:%M:%S")}

</div>
""",
unsafe_allow_html=True
)


import streamlit as st

# ==========================================
# 1. SIDEBAR LOGO & BRANDING
# ==========================================

# This places your new "Medicine Inventory & Expiry" logo at the very top
try:
    # st.sidebar.image("sidebar7.png", use_container_width=True)
    st.sidebar.image("sidebar7.png", width=190)
except Exception:
    # If the image file is missing, show a clean text title instead
    st.sidebar.title("💊 Pharmacy Management")


# TITLE

st.sidebar.markdown("""
<h1 style='text-align:center;color:white;'>
🏥 StockMedic
</h1>
""", unsafe_allow_html=True)

st.sidebar.markdown("---")

filtered_df = df

# 1. Initialize the page state so the dashboard doesn't disappear on refresh
if 'page' not in st.session_state:
    st.session_state.page = "Dashboard"

# --- QUICK NAVIGATION SIDEBAR ---
st.sidebar.markdown("""
<h3 style='
background: linear-gradient(90deg,#00c6ff,#00ffcc);
-webkit-background-clip:text;
-webkit-text-fill-color: transparent;
font-weight:700;
font-size:26px;
'>
⚡ Quick Navigation
</h3>
""", unsafe_allow_html=True)


# Update the session state when a button is clicked
if st.sidebar.button("📊 Dashboard Overview"):
    st.session_state.page = "Dashboard"

if st.sidebar.button("💊 Inventory Status"):
    st.session_state.page = "Inventory"

if st.sidebar.button("📅 Expiry Monitoring"):
    st.session_state.page = "Expiry"

if st.sidebar.button("🏢 Supplier Analysis"):
    st.session_state.page = "Supplier"

if st.sidebar.button("📁 Download Reports"):
    st.session_state.page = "Reports"

st.sidebar.markdown("---")

# 2. MAIN PAGE LOGIC - This shows the actual data changes
if st.session_state.page == "Dashboard":

    
    st.write("Welcome to the main dashboard.")

elif st.session_state.page == "Inventory":
    st.title("💊 Inventory Status")
    
    
    st.dataframe(filtered_df) 

elif st.session_state.page == "Expiry":
    st.title("📅 Expiry Monitoring")
    

elif st.session_state.page == "Supplier":
    st.title("🏢 Supplier Analysis")
    
elif st.session_state.page == "Reports":
    st.title("📁 Download Reports")


search = st.sidebar.text_input(
    "🔍 Search Medicine Name"
)

if search:

    df = df[
        df["Medicine_Name"]
        .str.contains(search, case=False)
    ]

# =====================================================
# DROPDOWN FILTERS
# =====================================================

st.sidebar.markdown("""
### 💠 Smart Filters
""")

# CATEGORY FILTER

category = st.sidebar.selectbox(
    "💊 Select Medicine Category",
    options=["All"] + list(df["Category_Name"].unique())
)

# SUPPLIER FILTER

supplier = st.sidebar.selectbox(
    "🏢 Select Supplier Company",
    options=["All"] + list(df["Supplier_Name"].unique())
)

# WAREHOUSE FILTER

warehouse = st.sidebar.selectbox(
    "🏬 Select Warehouse",
    options=["All"] + list(df["Warehouse_Name"].unique())
)

# EXPIRY STATUS FILTER

expiry_status = st.sidebar.selectbox(
    "📅 Select Expiry Status",
    options=["All"] + list(df["Expiry_Status"].unique())
)

st.sidebar.markdown("---")

# =====================================================
# FILTER LOGIC
# =====================================================

filtered_df = df.copy()

if category != "All":

    filtered_df = filtered_df[
        filtered_df["Category_Name"] == category
    ]

if supplier != "All":

    filtered_df = filtered_df[
        filtered_df["Supplier_Name"] == supplier
    ]

if warehouse != "All":

    filtered_df = filtered_df[
        filtered_df["Warehouse_Name"] == warehouse
    ]

if expiry_status != "All":

    filtered_df = filtered_df[
        filtered_df["Expiry_Status"] == expiry_status
    ]

# =====================================================
# SIDEBAR STATS
# =====================================================

st.sidebar.markdown("""
### 📌 Quick Statistics
""")

st.sidebar.success(
    f"💊 Total Medicines: {filtered_df.shape[0]}"
)

st.sidebar.warning(
    f"⚠️ Low Stock: {filtered_df[filtered_df['Stock_Quantity'] <= filtered_df['Reorder_Level']].shape[0]}"
)

st.sidebar.error(
    f"🗑️ Expired: {filtered_df[filtered_df['Expiry_Status'] == 'Expired'].shape[0]}"
)

st.sidebar.info(
    f"⏳ Expiring Soon: {filtered_df[filtered_df['Expiry_Status'] == 'Expiring Soon'].shape[0]}"
)

st.sidebar.markdown("---")

# =====================================================
# EXTRA ACTION BUTTONS
# =====================================================

st.sidebar.markdown("""
### 🚨 Quick Actions
""")

refresh_btn = st.sidebar.button("🔄 Refresh Data")

download_btn = st.sidebar.button("⬇️ Export Inventory")

alert_btn = st.sidebar.button("🚨 Generate Alerts")

email_btn = st.sidebar.button("📧 Send Notifications")

backup_btn = st.sidebar.button("💾 Backup Database")


# =====================================================
# KPI SECTION
# =====================================================

total_medicines = filtered_df["Medicine_ID"].nunique()

low_stock = filtered_df[
    filtered_df["Stock_Quantity"] <=
    filtered_df["Reorder_Level"]
].shape[0]

expiring_soon = filtered_df[
    filtered_df["Expiry_Status"] == "Expiring Soon"
].shape[0]

expired = filtered_df[
    filtered_df["Expiry_Status"] == "Expired"
].shape[0]

safe = filtered_df[
    filtered_df["Expiry_Status"] == "Safe"
].shape[0]

col1, col2, col3, col4, col5 = st.columns(5)

col1.metric("💊 Total Medicines", total_medicines)

col2.metric("📦 Low Stock", low_stock)

col3.metric("⏳ Expiring Soon", expiring_soon)

col4.metric("🚫 Expired", expired)

col5.metric("✅ Safe Stock", safe)

st.markdown("---")

if expired > 0:

    st.error(
        f"🚨 Alert! {expired} medicines have expired and require immediate attention."
    )

elif expiring_soon > 0:

    st.warning(
        f"⚠️ {expiring_soon} medicines are expiring within 30 days."
    )

else:

    st.success(
        "✅ All medicines are safe."
    )

# =====================================================
# MODERN CHART LAYOUT FUNCTION
# =====================================================

def modern_layout(fig):

    fig.update_layout(

        height=520,

        margin=dict(
            l=20,
            r=150,
            t=60,
            b=120
        ),

        legend=dict(

            orientation="v",

            y=0.9,

            x=1.05,

            xanchor="left",

            yanchor="top",

            bgcolor="rgba(0,0,0,0)",

            font=dict(
                size=12,
                color="white"
            )
        ),

        template="plotly_dark",

        paper_bgcolor='rgba(0,0,0,0)',

        plot_bgcolor='rgba(0,0,0,0)',

        font=dict(
            color="white",
            size=14
        ),

        title_font=dict(
            size=20
        )
    )

    return fig

# =====================================================
# COLOR THEME
# =====================================================

color_scale = ["#158BDA", "#0A5E2D", "#CC2411", "#CCAE36"]

# =====================================================
# CHART 1 — CATEGORY STOCK
# =====================================================

category_stock = filtered_df.groupby(
     "Category_Name"
 )["Stock_Quantity"].sum().reset_index()

fig1 = px.bar(

    category_stock,

    x="Category_Name",

    y="Stock_Quantity",

    color="Category_Name",

    text_auto=True,

    title="📦 Category Wise Inventory",

    color_discrete_sequence=color_scale,

)
fig1 = modern_layout(fig1)

# =====================================================
# CHART 2 — SUPPLIER DISTRIBUTION
# =====================================================

supplier_data = filtered_df.groupby(
    "Supplier_Name"
)["Medicine_ID"].count().reset_index()

fig2 = px.pie(

    supplier_data,

    names="Supplier_Name",

    values="Medicine_ID",

    hole=0.5,

    title="🏢 Supplier Distribution",

    color_discrete_sequence=color_scale
)

fig2 = modern_layout(fig2)

# =====================================================
# CHART 3 — EXPIRY STATUS
# =====================================================

expiry_data = filtered_df.groupby(
    "Expiry_Status"
)["Medicine_ID"].count().reset_index()

fig3 = px.pie(

    expiry_data,

    names="Expiry_Status",

    values="Medicine_ID",

    hole=0.45,

    title="📅 Inventory Expiry Status",

    color_discrete_sequence=color_scale
)

fig3 = modern_layout(fig3)

# =====================================================
# CHART 4 — MEDICINE EXPIRY TIMELINE
# =====================================================

timeline = filtered_df.groupby(
    filtered_df["Expiry_Date"].dt.strftime("%Y-%m")
)["Medicine_ID"].count().reset_index()

timeline.columns = [
    "Expiry_Month",
    "Total_Medicines"
]

# Create colors based on medicine count
colors = [
    "#00E676" if x < 300 else
    "#FFD54F" if x < 700 else
    "#FF4081"
    for x in timeline["Total_Medicines"]
]

fig4 = px.line(
    timeline,
    x="Expiry_Month",
    y="Total_Medicines",
    markers=True,
    title="📈 Medicine Expiry Timeline",
    line_shape="spline",
    color_discrete_sequence=["#22D3EE"]
)

fig4.update_traces(
    line=dict(
        width=5,
        color="#22D3EE"
    ),
    marker=dict(
        size=12,
        color=colors,
        line=dict(
            width=2,
            color="white"
        )
    )
)

fig4.update_layout(
    hovermode="x unified"
)

fig4 = modern_layout(fig4)
fig4.update_traces(
    fill="tozeroy",
    fillcolor="rgba(34,211,238,0.12)"
)
# =====================================================
# CHART 5 — STOCK DISTRIBUTION
# =====================================================

fig5 = px.histogram(

    filtered_df,

    x="Stock_Quantity",
    

    nbins=10,

    title="📊 Medicine Stock Distribution",
    
    color_discrete_sequence=["#38BDF8"]
)

fig5 = modern_layout(fig5)
fig5.update_layout(
    bargap=0.40,
    xaxis_title="Stock Quantity",
    yaxis_title="Medicine Count"
)

fig5.update_traces(
    textposition='outside', 
    textfont_size=10,
    cliponaxis=False
)

# =====================================================
# CHART 5 — STOCK DISTRIBUTION
# =====================================================

fig5 = px.histogram(
    filtered_df,
    x="Stock_Quantity",
    nbins=10,
    title="📊 Medicine Stock Distribution",
    color_discrete_sequence=["#38BDF8"]
    
)

fig5 = modern_layout(fig5)

fig5.update_layout(
    bargap=0.25,
    xaxis_title="Stock Quantity",
    yaxis_title="Medicine Count",
    title_x=0.5,
    font=dict(
        family="Segoe UI",
        size=14,
        color="white"
    ),
    plot_bgcolor="rgba(0,0,0,0)",
    paper_bgcolor="rgba(0,0,0,0)"
)

fig5.update_traces(
    texttemplate="%{y}",
    textposition="outside",
    marker=dict(
        line=dict(
            color="#FFFFFF",
            width=1
        )
    ),
    opacity=0.9
)  
mean_stock = filtered_df["Stock_Quantity"].mean()

fig5.add_vline(
    x=mean_stock,
    line_width=3,
    line_dash="dash",
    line_color="#FF4D6D",
    annotation_text="Average Stock",
    annotation_position="top"
)

fig5.update_traces(
    hovertemplate=
    "<b>Stock Range</b><br>" +
    "Count: %{y}<extra></extra>"
)

# =====================================================
# TABS
# =====================================================

tab_charts, tab_inventory, tab_search = st.tabs([

    "📊 Analytics",

    "📋 Inventory List",

    "🔍 Quick Search"
])


# =====================================================
# ANALYTICS TAB
# =====================================================

with tab_charts:

    c1, c2 = st.columns([1.2,1.2])

    with c1:

        st.plotly_chart(
            fig1,
            use_container_width=True
        )

    with c2:

        st.plotly_chart(
            fig2,
            use_container_width=True
        )

    c3, c4 = st.columns([1.2,1.2])

    with c3:

        st.plotly_chart(
            fig3,
            use_container_width=True
        )

    with c4:

        st.plotly_chart(
            fig4,
            use_container_width=True
        )

    st.plotly_chart(
        fig5,
        use_container_width=True
    )


# =====================================================
# INVENTORY TAB
# =====================================================

with tab_inventory:

    st.subheader("📋 Complete Inventory")

    st.dataframe(
        filtered_df,
        use_container_width=True
    )


# =====================================================
# SEARCH TAB
# =====================================================

with tab_search:

    medicine_search = st.text_input(
        "🔍 Search Medicine Name"
    )

    if medicine_search:

        result = filtered_df[
            filtered_df["Medicine_Name"]
            .str.contains(
                medicine_search,
                case=False
            )
        ]

        st.dataframe(
            result,
            use_container_width=True
        )


# =====================================================
# LOW STOCK TABLE
# =====================================================

st.subheader("📥 Low Stock Medicines")

low_stock_table = filtered_df[
    filtered_df["Stock_Quantity"] <=
    filtered_df["Reorder_Level"]
]

st.dataframe(

    low_stock_table[
        [
            "Medicine_Name",
            "Category_Name",
            "Supplier_Name",
            "Stock_Quantity",
            "Reorder_Level",
            "Expiry_Status"
        ]
    ],

    use_container_width=True
)


# =====================================================
# DOWNLOAD BUTTON
# =====================================================

csv = filtered_df.to_csv(
    index=False
).encode("utf-8")

st.download_button(

    label="⬇️ Download Inventory Data",

    data=csv,

    file_name="final_pharmacy_data.csv",

    mime="text/csv"
)


# =====================================================
# FOOTER
# =====================================================

st.markdown("---")


st.markdown("""

<center style='color:white;font-size:18px;'>

🏥 Pharmacy Inventory & Expiry Tracking System

💻 Developed By Gauri Malpe 

📊 Streamlit • MySQL • Plotly • Pandas

</center>
""", unsafe_allow_html=True)