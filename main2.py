import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('Streamlit 超入門')

st.write('Interactive Widgets')


#チェックにて画像表示有無
#checkbox はTrue　Falseのためif文にしてあげる

# if st.checkbox('Show Image'):
#     img = Image.open('RUKA2.jpg')
#     st.image(img,caption='Ruka',use_column_width=True) #use_column_width= レイアウトの横幅に合わせる

#セレクトボックス
# option=st.selectbox(
#     'あなたが好きな数字を教えてください、',
#     list(range(1,11))
# )
# 'あなたの好きな数字は、',option,'です！'

#テキストボックス
# text=st.text_input(
#      'あなたの趣味を教えてください。')
# 'あなたの趣味：',text

# #スライダー
# condition = st.slider('あなたの今の調子は？',0,100,50)
# 'コンディション：',condition

#サイドバー
# st.sidebar.write('Interactive Widgets')
# text=st.sidebar.text_input(
#      'あなたの趣味を教えてください。')
# condition = st.sidebar.slider('あなたの今の調子は？',0,100,50)

# 'あなたの趣味：',text
# 'コンディション：',condition

#プレグレスバーの表示
import time
st.write('プレグレスバーの表示')
'Start!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration  {i+1}')
    bar.progress(i+1)
    time.sleep(0.01)

'Done!!!'

#2カラム
#st.write('Interactive Widgets')

left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

expander1 = st.expander('問い合わせ1')
expander1.write('問い合わせ1の回答')
expander2 = st.expander('問い合わせ2')
expander2.write('問い合わせ2の回答')


# git入門　https://backlog.com/ja/git-tutorial/




# text=st.text_input(
#      'あなたの趣味を教えてください。')
# condition = st.slider('あなたの今の調子は？',0,100,50)

# 'あなたの趣味：',text
# 'コンディション：',condition
