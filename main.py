import streamlit as st
import time

st.title('Streamlit First guide')
st.write('Interactive Widget')

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Interation {i+1}')
    bar.progress(i + 1)
    time.sleep(0.01)
    

"""
### mikuchan daisuki :) -------------------------------------------

### kyoumo kawaii
"""


text = st.text_input('Please tell me your favorite hobby')

'Your favorite hobby is', text, '!!'

condition = st.slider('How is your condition?', 0, 100, 50)
'Condition:', condition



left_column, right_column = st.columns(2)
button = left_column.button('desplay in right column')
if button:
    right_column.write('here is right column')

expander = st.expander('request')
expander.write('display request contents1')
expander.write('display request contents2')
expander.write('display request contents3')
expander.write('display request contents4')