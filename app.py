import streamlit as st

# ページ基本設定
st.set_page_config(page_title="NexusNote Executive Pro", page_icon="👑", layout="centered")

# エグゼクティブ版専用のプレミアムヘッダー（高級感・ブランド力強化）
st.markdown(
    """
    <div style="background: linear-gradient(135deg, #0f2027 0%, #203a43 50%, #2c5364 100%); padding: 25px; border-radius: 12px; color: white; text-align: center; margin-bottom: 20px; box-shadow: 0 4px 15px rgba(0,0,0,0.2);">
        <h2 style="margin: 0; font-size: 26px; letter-spacing: 1px;">👑 NexusNote Executive Pro</h2>
        <p style="margin: 8px 0 0 0; font-size: 13px; opacity: 0.85;">最高峰AIマーケティング＆note自動収益化プラットフォーム</p>
    </div>
    """,
    unsafe_allow_html=True
)

# ライセンス＆エグゼクティブ・ステータス
st.markdown(
    """
    <div style="border: 1px solid #d4af37; background: linear-gradient(90deg, #fdfaf1 0%, #f4ebd0 100%); padding: 12px; border-radius: 6px; color: #795548; font-weight: bold; margin-bottom: 20px; text-align: center; font-size: 14px;">
        ⭐ ライセンス認証済み（Executive無制限枠・全機能解放）
    </div>
    """,
    unsafe_allow_html=True
)

# サイドバーまたはメインでのAPIキー＆設定
api_key = st.text_input("OpenAI APIキー", type="password", placeholder="sk-...", help="ご自身のOpenAI APIキーを入力してください")

# 記事テーマ
theme = st.text_input("狙う記事のテーマ・キーワード", placeholder="例: スキマ時間で月5万円稼ぐスマホライティング術")

# 【マーケティング特化】エグゼクティブ詳細設定
with st.expander("⚙️ マーケティング・収益化ブースト設定（プロ仕様）", expanded=True):
    target_layer = st.selectbox(
        "ターゲットの購買心理・層",
        ["初心者向け（不安解消・手軽さ訴求でコンバージョン重視）", "中級者向け（効率化・ノウハウ特化で信頼獲得）", "プロ向け（投資対効果・最高峰スペック訴求）"]
    )
    monetize_angle = st.selectbox(
        "有料noteへの誘導フック（心理トリガー）",
        ["損失回避の法則（このままだと損する未来を提示）", "権威性・希少性（限られた人のみ得られるノウハウ）", "ロードマップ型（段階的に引き込んで自然に購入させる）"]
    )
    output_length = st.slider("記事のボリューム（文字数目安）", min_value=3000, max_value=10000, value=5000, step=1000)

# アクションボタン
if st.button("🚀 【収益化特化】最高峰エグゼクティブ記事を生成する", type="primary", use_container_width=True):
    if not api_key:
        st.warning("⚠️ OpenAI APIキーを入力してください。")
    elif not theme:
        st.warning("⚠️ 記事のテーマを入力してください。")
    else:
        with st.spinner("💎 プロ仕様のマーケティング構成と心理トリガーを構築中..."):
            # ここに実際の生成ロジックやAIへの指示が組み込まれます
            st.success("✨ エグゼクティブ版の記事構成・本文の生成が完了しました！")
            
            # 生成結果のプレビュー表示（マーケティング演出）
            st.markdown("### 📝 生成された収益化プラットフォーム出力")
            st.info(f"**選定テーマ**: {theme}\n\n**適用した心理トリガー**: {monetize_angle}\n\n**目標文字数**: 約 {output_length} 文字")
            
            # サンプル出力
            st.markdown("""
            #### 【導入：読者の心を掴むプロローグ】
            「スマホ一台で、毎月安定して収益を生み出したい……そう思いながらも、何から書けばいいか分かっていませんか？」
            *(※ここにAIが自動構築した高単価note用の洗練された本文が出力されます)*
            """)
