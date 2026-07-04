# 1. プロジェクトフォルダを作成
mkdir -p note_ai_assistant
cd note_ai_assistant

# 2. requirements.txt を作成
cat > requirements.txt << EOF
streamlit
pandas
plotly
requests
pillow
EOF

# 3. app.py を作成（ここにコードを貼り付ける）
cat > app.py << 'EOF'
import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

st.set_page_config(page_title="AI Note Studio", layout="wide", initial_sidebar_state="expanded")

st.sidebar.title("🌌 AI Note Studio")
st.sidebar.markdown("**没入型 note 記事生成 & 分析**")
page = st.sidebar.radio("メニュー", ["記事生成", "作家分析", "人気傾向", "設定"])

if page == "記事生成":
    st.title("✍️ 没入型 note 記事生成")
    topic = st.text_input("トピックを入力してください", "現役大学生の副業")
    if st.button("🚀 記事を生成", type="primary"):
        with st.spinner("深みのある物語を生成中..."):
            st.success("生成完了！")
            st.markdown("### 生成例")
            st.markdown(f"**{topic}** についての没入型記事がここに表示されます。")
            
elif page == "作家分析":
    st.title("📊 note 作家分析")
    username = st.text_input("ユーザー名 (@example)", "@example")
    if st.button("分析する"):
        st.info("分析結果（サンプル）")
        data = {"記事": ["副業1", "副業2"], "スキ": [300, 850]}
        df = pd.DataFrame(data)
        fig = px.bar(df, x="記事", y="スキ")
        st.plotly_chart(fig)

else:
    st.title("Coming Soon...")
EOF
streamlit run app.py
