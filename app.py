rm -f app.py && cat > app.py << 'EOF'
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="AI Note Studio", layout="wide")

st.title("🌌 AI Note Studio")
st.markdown("**没入感を重視した note 自動記事生成ツール**")

page = st.sidebar.radio("メニュー", ["記事生成", "作家分析"])

if page == "記事生成":
    st.subheader("記事生成")
    topic = st.text_input("トピック", "現役大学生の副業")
    if st.button("生成", type="primary"):
        st.success("生成完了！（サンプル）")
        st.markdown(f"**{topic}** の記事がここに表示されます。")

elif page == "作家分析":
    st.subheader("作家分析")
    username = st.text_input("ユーザー名", "@example")
    if st.button("分析"):
        df = pd.DataFrame({"記事": ["A", "B"], "スキ": [500, 1200]})
        fig = px.bar(df, x="記事", y="スキ")
        st.plotly_chart(fig)

st.caption("3D没入感UIを目指したアプリ")
EOF
streamlit run app.py
