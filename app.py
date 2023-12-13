import streamlit as st

def find_largest(num1, num2, num3):
  largest = max(num1, num2, num3)
  return largest

st.title("Find the Largest Number")
st.text("By 22f1000475")

num1 = st.number_input("Enter First Number")
num2 = st.number_input("Enter Second Number")
num3 = st.number_input("Enter Third Number")

if st.button("Find Largest"):
  largest_num = find_largest(num1, num2, num3)
  st.success(f"The largest number is: {largest_num}")
