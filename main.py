import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
#Web表示は　streamlit run main.py
st.title('Streamlit 超入門')

st.write('DataFreame')

df = pd.DataFrame({
    '1列目':[1,2,3,4],
    '２列目':[10,20,30,40]
})

#st.write(df)
#datafreame は　write と違い、サイズ指定できる
#st.dataframe(df,width=100,height=100)

#ハイライト表示
#st.dataframe(df.style.highlight_max(axis=0))

#静的なテーブル　ただ表を表示に使用
#st.table(df.style.highlight_max(axis=0))

# 詳細は　https://docs.streamlit.io/develop/api-reference にある



# magic コマンド markdownが利用できる
"""
# 章
## 節
### 項

```python
import streamlit as st
import numpy as np
import pandas as pd
```

"""

df = pd.DataFrame(
    np.random.rand(20,3),
    columns=['a','b','c']
)
#折れ線グラフ
st.line_chart(df)

st.area_chart(df)

st.bar_chart(df)


#MAP plot
df_map = pd.DataFrame(
    np.random.rand(100,2)/[50,50] + [35.69,139.70],
    columns=['lat','lon']
)

st.map(df_map)

#画像を表示


st.write('Display Image')
img = Image.open('RUKA2.jpg')
st.image(img,caption='Ruka',use_column_width=True) #use_column_width= レイアウトの横幅に合わせる



