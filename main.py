import datetime

import  streamlit as st

import pandas as pd
import numpy as np

st.write("Hello world")
x = st.text_input("Favourite Cricketer?")
st.write(f"Your favourite cricketer is {x}")

is_clicked = st.button('Click Me')


st.write("# This is a H1 Title!")
st.write("## :rainbow[ This is a H2 Title!]")
st.code(''' // Java code to demonstrate the
// working of substring(int begIndex)
public class Substr1 {
    public static void main(String args[])
    {

        // Initializing String
        String Str = new String("Welcome to geeksforgeeks");

        // using substring() to extract substring
        // returns (whiteSpace)geeksforgeeks

        System.out.print("The extracted substring is : ");
        System.out.println(Str.substring(3));
    }
}''', language="java")



st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''')
st.divider()

df = pd.DataFrame(np.random.randn(50, 20), columns=("col %d" % i for i in range(20)))

st.dataframe(df.style.highlight_min(axis=0))  # Same as st.write(df)

df = pd.DataFrame(
    np.random.randn(10, 5), columns=("col %d" % i for i in range(5))
)

st.table(df)
chart_data = pd.DataFrame(np.random.randn(20, 2), columns=["a", "b"])

st.area_chart(chart_data)


chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.bar_chart(chart_data)

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.line_chart(chart_data)

st.feedback(options="thumbs")
st.feedback(options="stars")
st.feedback(options="faces")

st.radio("What's your favourite movie genre",
         ["Comedy","Action","Drama"])

st.toggle("Activated")
st.selectbox("Pick one", ("Cats", "Dags"))
st.date_input("Birthday", datetime.date(2000,2,19))


enable = st.checkbox("Enable camera")
picture = st.camera_input("Take a picture", disabled=not enable)

if picture:
    st.image(picture)

st.image("https://images.unsplash.com/photo-1720048171731-15b3d9d5473f?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDF8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", caption="Sunrise by the mountains")
st.video("https://youtu.be/oimbP-VyRSw?si=RXCtgRMiXNUKHMD7")


