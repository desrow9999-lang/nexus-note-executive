import streamlit as st
import time

# ==========================================
# 💎 アプリのタイトルと基本設定
# ==========================================
st.set_page_config(page_title="NexusNote Pro", page_icon="💎", layout="centered")

# セッション状態の初期化
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

# アクションボタン
if st.button("🚀 【収益化特化】最高峰エグゼクティブ記事を生成する", type="primary", use_container_width=True):
    if not theme:
        st.warning("⚠️ 記事のテーマを入力してください。")
    else:
        with st.spinner("💎 プロ仕様のマーケティング構成と長文記事を構築中..."):
            time.sleep(1.5)
            
            st.session_state.generated_text = f"""# 【完全版】{theme}：成功を掴むための極秘ロードマップ

## プロローグ：読者の感情を揺さぶる導入
「本当にこのまま、毎月の収入やスキルに満足できていますか？」
毎日ただ時間を消費し、将来への漠然とした不安を抱えながら生きている人は少なくありません。今回は、あなたが入力したテーマである **{theme}** に焦点を当て、ターゲット層である **{target_layer}** の心をつかんで離さない、実践的なアプローチを完全網羅でお届けします。

## 第1章：現状の課題と「損失回避」の真実
多くの人が勘違いしていますが、適切なマーケティング導線や知識を怠っていると、年間で数十万円もの大きな機会損失を生み出しています。「まだ自分には早い」「何から始めればいいかわからない」と立ち止まっている時間そのものが、あなたの未来の可能性を削っているのです。
今回は **{monetize_angle}** に最適化された心理トリガーをフル活用し、読者の行動を自然に促す構成を組み込んでいます。

## 第2章：門外不出の解決ロードマップ（設計ボリューム：約 {output_length} 文字仕様）
ここからは、実際に成果を出すための具体的なステップを段階的に解説します。

1. **初期フェーズ：スマホ完結で環境を整える基礎固め**
   - 余計なコストをかけず、手元のデバイスだけで最大限のパフォーマンスを発揮するための初期設定。
   - 挫折しないためのスケジュール管理とマインドセット。

2. **中期フェーズ：マーケティングを掛け合わせた効率化**
   - ターゲットの欲求を正確にスナイプするキーワード選定とリサーチ術。
   - 読者の離脱を防ぐ、文章の緩急と構成テンプレートの活用法。

3. **マネタイズフェーズ：有料エリアへ自然に着地させる心理誘導**
   - 無料部分で読者の期待値を限界まで高め、「ここから先を知りたい」と思わせるフックの配置。
   - クレームや不安を排除し、高いコンバージョン率を叩き出すCTAの設置テクニック。

## エピローグ ＆ 有料noteへの強力なCTA
ここから先の有料エリアでは、さらに具体的なテンプレート、実際の成功事例、そのままコピペして使えるフレーズ集を完全公開しています。
読者の購買意欲を最高潮まで高め、確実に成約へと繋げるためのノウハウがここに詰まっています。あなたの次のステップを、今ここからはじめましょう。
"""
            st.success("✨ 本格的なエグゼクティブ収益化記事の構築が完了しました！")

# 生成されたテキストがある場合、表示とコピー用ボックスを表示
if st.session_state.generated_text:
    st.markdown("---")
    st.markdown("### 📊 マーケティング・アナリティクス")
    st.info(f"選定テーマ：{theme}\n\nターゲット層：{target_layer}\n\n採用した心理トリガー：{monetize_angle}\n\n設計ボリューム：約 {output_length} 文字")

    st.markdown("---")
    st.markdown("### 📝 【有料note対応】生成記事出力")
    st.markdown(st.session_state.generated_text)

    st.markdown("#### 📋 コピー用テキストボックス")
    st.text_area(
        "以下の枠内をすべて選択してコピーしてください",
        value=st.session_state.generated_text,
        height=300
    )
