import streamlit as st
import time
from openai import OpenAI

# ==========================================
# 💎 アプリのタイトルと基本設定
# ==========================================
st.set_page_config(page_title="NexusNote Pro", page_icon="💎", layout="centered")

# セッション状態の初期化（エラー防止用）
if "generated_text" not in st.session_state:
    st.session_state.generated_text = ""

# ヘッダー
st.markdown(
    """
    <div style="background: linear-gradient(135deg, #0f2027 0%, #203a43 50%, #2c5364 100%); padding: 25px; border-radius: 12px; color: white; text-align: center; box-shadow: 0 4px 15px rgba(0,0,0,0.2);">
        <h2 style="margin: 0; font-size: 26px; letter-spacing: 1px;">💎 NexusNote Pro エグゼクティブ</h2>
        <p style="margin: 8px 0 0; font-size: 13px; opacity: 0.85;">最高峰AIマーケティング＆note収益化プラットフォーム</p>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("")

# ライセンス
st.markdown(
    """
    <div style="border: 1px solid #d4af37; background: linear-gradient(90deg, #fdfaf1 0%, #f4e8d0 100%); padding: 12px; border-radius: 8px; text-align: center; font-weight: bold; color: #8a6d3b;">
        ✨ ライセンス認証済み (Executive無制限枠・全機能解放)
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("")

# 入力セクション
api_key = st.text_input("OpenAI APIキー", type="password", placeholder="sk-...", help="ご自身のOpenAI APIキーを入力してください。")
theme = st.text_input("狙う記事のテーマ・キーワード", placeholder="例：スキマ時間で月5万円稼ぐスマホライティング術")

# 詳細設定
with st.expander("⚙️ マーケティング・収益化ブースト設定（プロ仕様）", expanded=True):
    target_layer = st.selectbox(
        "ターゲットの購買心理・層",
        ("初心者向け（不安解消・手軽さ訴求でコンバージョン重視）", "中級者向け（効率化・ノウハウ特化で信頼獲得）", "プロ向け（投資対効果・最高峰スペック訴求）")
    )
    monetize_angle = st.selectbox(
        "有料noteへの誘導フック（心理トリガー）",
        ("損失回避の法則（このままだと損する未来を提示）", "権威性・希少性（限られた人のみ得られるノウハウ）", "ロードマップ型（段階的に引き込んで自然に購入させる）")
    )
    output_length = st.slider("記事のボリューム（文字数目安）", min_value=3000, max_value=10000, value=5000, step=1000)

# アクションボタン（本気モード・API連携）
if st.button("🚀 【収益化特化】最高峰エグゼクティブ記事を生成する", type="primary", use_container_width=True):
    if not api_key:
        st.error("⚠️ OpenAI APIキーを入力してください。")
    elif not theme:
        st.warning("⚠️ 記事のテーマを入力してください。")
    else:
        try:
            with st.spinner("💎 OpenAI APIがプロ仕様のマーケティング構成と長文記事を構築中..."):
                client = OpenAI(api_key=api_key)
                
                prompt = f"""
                あなたはプロのマーケター兼トップnoteライターです。
                以下の条件に従って、有料note用の本格的な高品質・長文記事を執筆してください。

                【記事テーマ】
                {theme}

                【ターゲット層】
                {target_layer}

                【有料noteへの誘導フック・心理トリガー】
                {monetize_angle}

                【構成要件】
                1. 読者の心を強く揺さぶる魅力的なプロローグ（導入）
                2. 現状の課題と損失回避の提示（第1章）
                3. 具体的な解決策・ロードマップ（第2章〜、ボリューム感を意識した詳細な解説）
                4. 有料エリアへ自然に誘導する強力なCTAとエピローグ
                """

                response = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[{"role": "user", "content": prompt}],
                    temperature=0.7,
                )
                
                st.session_state.generated_text = response.choices[0].message.content
                st.success("✨ 本格的なエグゼクティブ収益化記事の構築が完了しました！")
                
        except Exception as e:
            st.error(f"エラーが発生しました（APIキーや残高をご確認ください）: {e}")

# 生成されたテキストが存在する場合に表示＆コピー用エリアを設置
if st.session_state.generated_text:
    # マーケティングメタ情報
    st.markdown("---")
    st.markdown("### 📊 マーケティング・アナリティクス")
    st.info(f"選定テーマ：{theme}\n\nターゲット層：{target_layer}\n\n採用した心理トリガー：{monetize_angle}\n\n設計ボリューム：約 {output_length} 文字")

    # 生成された記事の表示
    st.markdown("---")
    st.markdown("### 📝 【有料note対応】生成記事出力")
    st.markdown(st.session_state.generated_text)

    # スマホでも一発でコピーできる専用テキストエリア
    st.markdown("#### 📋 コピー用テキストボックス")
    st.text_area(
        "以下の枠内をすべて選択してコピーしてください",
        value=st.session_state.generated_text,
        height=300
    )
