import streamlit as st 
import pandas as pd 
from st_aggrid import AgGrid

# baca dataframe dari file csv 
house = pd.read_csv('house_clean.csv')

house_chart = pd.read_csv('house_clean.csv', usecols=['id','price'])

def main() : 
  
# membuat text
  st.header('Belajar Streamlit di Pusdiklat KU')
  st.write('Minimal Example')
  
# membuat header, subheader, markdown
  st.header('Halaman Streamlit Adrianta Ras Sembiring')
  st.subheader('This is SubHeader')
  st.markdown('# Rendering Markdown ')
  st.write('Some Phytagorean Equation : ')
  st.latex('c^2 = a^2+b^2')
  
# menampilkan dataframe
  st.write('CONTOH DATA FRAME')
  st.dataframe(house)
  
# menampilkan metrics
  st.write('MENAMPILKAN METRICS')
  st.write('Metrics')
  st.metric(label="Temperature", value="70 °F", delta="1.2 °F")
  
# menampilkan buttons
  st.write('MENAMPILKAN BUTTONS')
  click_me_btn = st.button('Click Me')
  st.write(click_me_btn) #Return True kalo di Click 
  check_btn = st.checkbox('Klik Jika Setuju')
  if check_btn :
      st.write('Anda Setuju')
  
  st.write('MENAMPILKAN RADIO BUTTONS')
  radio_button= st.radio('Choose below',[x for x in range(1,3)])
  st.write('Anda Memilih',radio_button)
  
# menampilkan slider
  st.write('MENAMPILKAN SLIDER')
  age_slider = st.slider('Berapa Usia Anda',0,100)
  st.write('Usia Anda',age_slider)
  
# menampilkan input typing
  st.write('MENAMPILKAN INPUT TYPING')
  num_input = st.number_input('Input Berapapun')
  st.write('Kuadrat dari {} adalah {}'.format(num_input,num_input**2))
  
# menampilkan sidebar
  st.sidebar.write('MENAMPILKAN SIDEBAR')
  sidebar_checkbox = st.sidebar.checkbox('Checkbox di Sidebar')
  sidebar_radio_button = st.sidebar.radio('Pilih Menu',options=['A','B','C'])

# menampilkan columns
  st.write('MENAMPILKAN KOLOM')
  col1, col2, col3 = st.columns(3)
  with col1:
      st.header("A cat")
      st.image("https://static.streamlit.io/examples/cat.jpg")
    
#atau dengan assignment 
  image_col1 = col1.image("https://static.streamlit.io/examples/cat.jpg")
  with col2:
      st.header("A dog")
      st.image("https://static.streamlit.io/examples/dog.jpg")
  with col3:
      st.header("An owl")
      st.image("https://static.streamlit.io/examples/owl.jpg")
    
# menampilkan expander 
# dengan with atau dengan assignment 
  st.write('MENAMPILKAN EXPANDER') 
  expander = st.expander("Klik Untuk Detail ")
  expander.write('Anda Telah Membuka Detail')
  
#sidebar 
  with st.form("Data Diri"):
      st.write("Inside the form")
      slider_val = st.slider("Form slider")
      checkbox_val = st.checkbox("Form checkbox")
# Every form must have a submit button.
      submitted = st.form_submit_button("Submit")
      if submitted:
          st.write("slider", slider_val, "checkbox", checkbox_val)
  st.write("Outside the form")
  
# menampilkan line chart
  st.write('MENAMPILKAN LINE CHART') 
  st.line_chart(house_chart)

# Insert containers separated into tabs:
tab1, tab2 = st.tabs(["Tab 1", "Tab2"])
tab1.write("Ini adalah Tab 1")
tab2.write("Ini adalah Tab 2")

if __name__ == '__main__' : 
  main()
