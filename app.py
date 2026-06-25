import streamlit as st

# Tiêu đề
st.title("🏠 TÍNH TIỀN PHÒNG TRỌ HÀNG THÁNG")

# Tiền phòng
A = st.number_input(
    "Nhập số tiền phòng (đồng)",
    min_value=0.0,
    value=2000000.0
)

# Điện
st.subheader("⚡ Tiền điện")

a = st.number_input(
    "Nhập số điện đầu tháng",
    min_value=0.0
)

b = st.number_input(
    "Nhập số điện cuối tháng",
    min_value=0.0
)

c = st.number_input(
    "Nhập đơn giá 1 số điện (đồng)",
    min_value=0.0,
    value=3500.0
)

# Nước
st.subheader("💧 Tiền nước")

x = st.number_input(
    "Nhập số nước đầu tháng",
    min_value=0.0
)

y = st.number_input(
    "Nhập số nước cuối tháng",
    min_value=0.0
)

z = st.number_input(
    "Nhập đơn giá 1 số nước (đồng)",
    min_value=0.0,
    value=12000.0
)

# Nút tính toán
if st.button("📊 Tính tiền phòng trọ"):

    B = (b - a) * c
    C = (y - x) * z
    D = A + B + C

    st.success(f"⚡ Tiền điện: {B:,.0f} đồng")
    st.success(f"💧 Tiền nước: {C:,.0f} đồng")
    st.success(f"🏠 Tổng tiền phòng trọ: {D:,.0f} đồng")
