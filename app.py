mkdir -p note_ai_assistant
cd note_ai_assistant
cat > requirements.txt << EOF
streamlit
pandas
plotly
requests
pillow
EOF
cat > app.py << 'EOF'
import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

st.set_page_config(page_title="AI Note Studio", layout="wide")

st.title("🌌 AI Note Studio")
st.markdown("### 没入型 note 記事生成ツール")

page = st.sidebar.radio("ページを選択", ["記事生成", "作家分析"])

if page == "記事生成":
    topic = st.text_input("トピック", "現役大学生の副業")
    if st.button("記事生成", type="primary"):
        st.success("生成中...（サンプル）")
        st.write("ここに没入感のある記事が表示されます。")
        
elif page == "作家分析":
    username = st.text_input("noteユーザー名", "@example")
    if st.button("分析"):
        st.write("分析結果がここに表示されます。")
EOF
streamlit run app.py
