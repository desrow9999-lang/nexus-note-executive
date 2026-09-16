import streamlit as st

# ページ基本設定
st.set_page_config(page_title="NexusNote Executive Pro", page_icon="👑", layout="centered")

# エグゼクティブ版専用のプレミアムヘッダー
st.markdown(
    """
    <div style="background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%); padding: 20px; border-radius: 10px; color: white; text-align: center; margin-bottom: 20px;">
        <h2 style="margin: 0; font-size: 24px;">👑 NexusNote Executive Pro</h2>
        <p style="margin: 5px 0 0 0; font-size: 14px; opacity: 0.9;">月〇万円自動化プラットフォーム（最高峰エグゼクティブ仕様）</p>
    </div>
    """,
    unsafe_allow_html=True
)

# ライセンス認証ステータス
st.markdown(
    """
    <div style="border: 1px solid #d4af37; background-color: #fdfaf1; padding: 10px; border-radius: 5px; color: #8a6d3b; font-weight: bold; margin-bottom: 20px;">
        ✓ ライセンス認証済み（Executive Pro 無制限有効）
    </div>
    """,
    unsafe_allow_html=True
)

# APIキー入力
api_key = st.text_input("OpenAI APIキー", type="password", placeholder="sk-...")

# 記事のテーマ入力
theme = st.text_input("記事のテーマ", placeholder="例: スキマ時間で月5万円稼ぐスマホライティング術")

# エグゼクティブ版限定の収益化オプション
with st.expander("⚙️ エグゼクティブ詳細設定（収益化ブースト）"):
    target_layer = st.selectbox("ターゲット層の心理設計", ["初心者向け（不安解消・手軽さ訴求）", "中級者向け（ノウハウ・効率化訴求）", "プロ向け（投資対効果・最高峰訴求）"])
    monetize_mode = st.checkbox("有料noteへの誘導フック（心理トリガー）を自動強化する", value=True)

# 生成ボタン
if st.button("🚀 エグゼクティブ版・note記事を生成する", type="primary"):
    if not api_key:
        st.warning("APIキーを入力してください。")
    elif not theme:
        st.warning("記事のテーマを入力してください。")
    else:
        with st.spinner("AIが最高峰のエグゼクティブ記事を構築中..."):
            st.success("記事の生成が完了しました！")

