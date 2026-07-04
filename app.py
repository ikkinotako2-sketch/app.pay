rm -f app.py
cat > app.py << 'EOF'
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="AI Note Studio", layout="wide", initial_sidebar_state="expanded")

st.title("🌌 AI Note Studio")
st.markdown("**3Dのような没入感を追求した note 支援ツール**")

page = st.sidebar.radio("メニューを選択", ["記事生成", "作家分析", "人気傾向"])

if page == "記事生成":
    st.subheader("✍️ 記事生成")
    topic = st.text_input("トピックを入力してください", "現役大学生の副業")
    if st.button("🚀 記事を生成", type="primary"):
        with st.spinner("深みのある物語を生成中..."):
            st.success("生成完了！")
            st.markdown(f"### {topic}")
            st.write("ここに視点移動を意識した美しい文章が表示されます。体験談や失敗談も自動で入ります。")

elif page == "作家分析":
    st.subheader("📊 note作家分析")
    username = st.text_input("noteユーザー名を入力", "@example")
    if st.button("分析する"):
        st.info("サンプル分析結果")
        df = pd.DataFrame({
            "記事": ["副業1", "副業2", "失敗談"],
            "スキ": [320, 980, 450]
        })
        fig = px.bar(df, x="記事", y="スキ", title="記事別スキ数")
        st.plotly_chart(fig, use_container_width=True)

elif page == "人気傾向":
    st.subheader("🔥 note人気傾向")
    st.write("現在、副業のリアル体験談が人気です。")

st.caption("AI Note Studio - シンプルかつ没入感のある体験を目指して")
EOF
streamlit run app.py
