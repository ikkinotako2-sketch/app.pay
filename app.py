# 1. シンプルに現在のフォルダを使う
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

st.set_page_config(page_title="AI Note Studio", layout="wide")

st.title("🌌 AI Note Studio")
st.markdown("**3D没入感を追求した note 記事生成ツール**")

page = st.sidebar.radio("メニュー", ["記事生成", "作家分析", "人気傾向"])

if page == "記事生成":
    st.subheader("キーワードから記事を生成")
    topic = st.text_input("トピック", "現役大学生の副業")
    if st.button("🚀 生成する", type="primary"):
        with st.spinner("没入感のある文章を生成中..."):
            st.success("生成完了！")
            st.markdown(f"### {topic} - 生成例")
            st.write("視点がゆっくり動き、物語が深く展開するような記事がここに表示されます。")

elif page == "作家分析":
    st.subheader("note作家分析")
    username = st.text_input("ユーザー名", "@example_user")
    if st.button("分析開始"):
        df = pd.DataFrame({
            "記事": ["副業体験", "失敗談", "成功ノウハウ"],
            "スキ数": [450, 820, 1250]
        })
        fig = px.bar(df, x="記事", y="スキ数", title="人気記事ランキング")
        st.plotly_chart(fig, use_container_width=True)

else:
    st.subheader("note人気傾向")
    st.info("副業のリアル体験談が現在強いです。")

st.caption("Made with ❤️ for immersive note creation")
EOF
streamlit run app.py
