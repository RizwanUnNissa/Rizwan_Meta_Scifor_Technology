import streamlit as st
import pandas as pd

st.title("Simple Calculator :material/Calculate:")
st.markdown(''':green[Calculates simple functions.]''')

st.subheader("Enter two variables below.")


numberinput1 = st.text_input("Enter first number")
numberinput2 = st.text_input("Enter second number")


if numberinput1.lstrip('-').isdigit() and numberinput2.lstrip('-').isdigit():

	number1 = int(numberinput1)
	number2 = int(numberinput2)



col1,col2,col3,col4 = st.columns([1,1,1,1])

if col1.button("Add"):
	st.write(number1+number2)
	st.success('Addition complete!', icon='✅')


if col2.button("Sub"):
	st.write(number1-number2)
	st.success('Subtraction complete!', icon='✅')

if col3.button("Mul"):
	st.write(number1*number2)
	st.success('Multiplication complete!', icon='✅')

if col4.button("Div"):
	st.write(number1/number2)
	st.success('Division complete!', icon='✅')

