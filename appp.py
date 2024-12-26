import streamlit as st

st.set_page_config(
    page_title="Hotel Booking Cancellation Predictor",
    page_icon="🏨",
    layout="centered"
)

# Streamlit UI
st.sidebar.title(" **Prediksi Pembatalan Hotel**")

# Add a logo or image to the sidebar with round shape
st.sidebar.markdown(
    """
    <style>
    .round-image {
        border-radius: 50%;
        width: 150px;
        height: 150px;
        object-fit: cover;
    }
    .image-container {
        display: flex;
        justify-content: space-around;
        margin-top: 20px;
    }
    .image-container div {
        text-align: center;
    }
    .image-container img {
        width: 150px;
        height: 150px;
        border-radius: 50%;
        object-fit: cover;
    }
    </style>
    """, unsafe_allow_html=True
)

# Display three images of the creators
st.markdown("""
    <div class="image-container">
        <div>
            <img src="logoai.png" class="round-image" />
            <p>Creator 1</p>
        </div>
        <div>
            <img src="creator2.jpg" class="round-image" />
            <p>Creator 2</p>
        </div>
        <div>
            <img src="creator3.jpg" class="round-image" />
            <p>Creator 3</p>
        </div>
    </div>
""", unsafe_allow_html=True)

# Add description to sidebar
st.sidebar.markdown("""
    Di sini, Anda dapat mengeksplorasi data, memprediksi kemungkinan pembatalan, 
    dan mengoptimalkan tingkat hunian hotel Anda.
""")

# Sidebar navigation options with selectbox
page = st.sidebar.selectbox(
    "Pilih Halaman", 
    ("Latar Belakang", "Tujuan Proyek", "Prediksi Pembatalan", "Evaluasi Model", "Prediksi dengan Dataset"),
    index=0  # Default to "Latar Belakang"
)

if page == "Latar Belakang":
    # Judul Halaman
    st.title("🏨 Prediksi Pembatalan Pemesanan Hotel")
    st.markdown("### **Mengoptimalkan Tingkat Hunian Hotel Anda**")
    st.markdown("---")

    st.write("""
        Industri perhotelan menghadapi tantangan besar dalam mengatasi pembatalan pemesanan, yang sering kali 
        berdampak pada pendapatan dan perencanaan operasional. Dengan menggunakan pendekatan berbasis data, 
        hotel dapat memprediksi kemungkinan pembatalan pemesanan sehingga keputusan strategis dapat diambil untuk 
        meminimalkan kerugian dan meningkatkan efisiensi.
    """)
    
    
    # Membuat dua tab: Tips dan Call to Action
    tab1, tab2 = st.tabs(["💡 Tips", "🚀 Call to Action"])

    # Tab 1: Tips untuk Mengurangi Risiko Pembatalan
    with tab1:
        st.markdown("### **Tips untuk Mengurangi Risiko Pembatalan**")
        st.success(""" 
            - **Optimalkan Waktu Pemesanan**: Pemesanan yang lebih dekat dengan tanggal menginap cenderung memiliki risiko pembatalan lebih rendah.
            - **Tawarkan Deposit Penuh**: Deposit penuh membantu meningkatkan komitmen pelanggan terhadap pemesanan mereka.
            - **Kelola Permintaan Khusus**: Hindari menerima terlalu banyak permintaan khusus, karena hal ini dapat meningkatkan risiko pembatalan.
        """)

    # Tab 2: Call to Action
    with tab2:
        st.write(""" 
            Dengan solusi ini, Anda tidak hanya dapat meningkatkan pendapatan, tetapi juga menciptakan pengalaman tamu yang lebih baik.
            **Mulai prediksi pembatalan sekarang!**
        """)
