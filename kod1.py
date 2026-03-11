import streamlit as st

st.set_page_config(page_title="Professional Kalkulyator", page_icon="🧮")
st.title("🧮 Professional Kalkulyator")

# Giriş sahələri
num1 = st.number_input("Birinci rəqəmi daxil edin:", value=0.0)
num2 = st.number_input("İkinci rəqəmi daxil edin:", value=0.0)

operation = st.selectbox("Əməliyyatı seçin:", ["Toplama (+)", "Çıxma (-)", "Vurma (*)", "Bölmə (/)", "Faiz (%)"])

# Hesablama məntiqi
if st.button("Hesabla"):
    result = 0
    if operation == "Toplama (+)":
        result = num1 + num2
    elif operation == "Çıxma (-)":
        result = num1 - num2
    elif operation == "Vurma (*)":
        result = num1 * num2
    elif operation == "Bölmə (/)":
        if num2 != 0:
            result = num1 / num2
        else:
            st.error("Sıfıra bölmək olmaz!")
    elif operation == "Faiz (%)":
        result = (num1 * num2) / 100

    st.success(f"Nəticə: {result}")
    st.balloons()