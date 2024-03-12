import streamlit as st
from factorial import fact

def main():
    st.title("Chuong trinh tinh giai thua")
    number = st.number_input("Nhập vào số cần tính: ",
                             min_value=0,
                             max_value=900)
    if st.button("Tính"):
        result = fact(number)
        st.write(f"Kết quả giai thừa của {number} là {result}")

if __name__ == "__main__":
    main()
