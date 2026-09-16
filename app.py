import streamlit as st
import openai
import time

# ==========================================
# ⚙️ 【プロ選定・最終設定】アプリのタイトルとアイコン
# ==========================================
APP_TITLE = "NexusNote Pro"  # スマホのホーム画面に追加したときの名前
APP_ICON = "💎"               # プロ選定のダイヤモンド・アイコン

# ページ基本設定
st.set_page_config(page_title=APP_TITLE, page_icon=APP_ICON, layout="centered")

# エグゼクティブ版専用のプレミアムヘッダー
st.markdown(
    f"""
    <div style="background: linear-gradient(135deg, #0f2027 0%, #203a43 50%, #2c5364 100%); padding: 25px; border-radius: 12px; color: white; text-align: center; margin-bottom: 20px; box-shadow: 0 4px 15px rgba(0,0,0,0.2);">
        <h2 style="margin: 0; font-size: 26px; letter-spacing: 1px;">{APP_ICON} {APP_TITLE} Executive</h2>
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

# 入力セクション
api_key = st.text_input("OpenAI APIキー", type="password", placeholder="sk-...", help="ご自身のOpenAI APIキーを入力してください。空欄の場合はデモモードで動作します。")
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
    if not theme:
        st.warning("⚠️ 記事のテーマを入力してください。")
    else:
        generated_text = ""
        
        # APIキーが入力されている場合は本番APIコール
        if api_key and api_key.startswith("sk-"):
            try:
                with st.spinner("💎 OpenAI APIと連携し、最高品質の収益化記事を執筆中..."):
                    client = openai.OpenAI(api_key=api_key)
                    
                    prompt = f"""
                    あなたはプロのWEBマーケターおよび超一流のnoteライターです。
                    以下の条件に従って、有料noteで売上を最大化するための高品質な収益化記事を執筆してください。

                    - 記事のテーマ: {theme}
                    - ターゲット層: {target_layer}
                    - 採用する心理トリガー（誘導フック）: {monetize_angle}
                    - 目安文字数: 約 {output_length} 文字
                    
                    構成案：
                    1. プロローグ（読者の感情を揺さぶる導入と強いフック）
                    2. 第1章：現状の課題と放置するリスク
                    3. 第2章：門外不出の解決ロードマップ・ノウハウ本編
                    4. エピローグ＆有料noteへの自然な導線（CTA）
                    
                    読者が思わず「続きが読みたい、購入したい」と思うような熱量の高い文章をマークダウン形式で出力してください。
                    """
                    
                    response = client.chat.completions.create(
                        model="gpt-4o",
                        messages=[
                            {"role": "system", "content": "あなたはプロのマーケター兼トップライターです。"},
                            {"role": "user", "content": prompt}
                        ],
                        temperature=0.7,
                    )
                    generated_text = response.choices[0].message.content
                    st.success("✨ OpenAI APIによる本番記事の生成が完了しました！")
            except Exception as e:
                st.error(f"⚠️ API呼び出しエラーが発生しました: {e}")
                st.info("💡 APIキーが無効か残高不足の可能性があるため、デモモードの出力を表示します。")
                api_key = ""
                
        # APIキー未入力、またはエラー時のフォールバック（デモモード）
        if not api_key or not api_key.startswith("sk-"):
            with st.spinner("💎 プロ仕様のマーケティング構成と心理トリガーを構築中（デモモード）..."):
                time.sleep(1.5)
                st.success("✨ エグゼクティブ版の収益化記事の構築が完了しました！（デモ出力）")
                generated_text = f"""
### 【プロローグ：読者の感情を揺さぶる導入】
「本当にこのままで、毎月の収入やスキルに満足できていますか？」
あなたが入力したテーマ：**『{theme}』** に基づき、ターゲット層（{target_layer}）の心を鷲掴みにする強烈なフックを設置しました。

### 【第1章：現状の課題と損失回避の提示】
多くの人が勘違いしていますが、〇〇を怠っていると、年間で数十万円もの機会損失を生み出しています。今回は **{monetize_angle}** を軸に最適化した導線を組んでいます。

### 【第2章：門外不出の解決ロードマップ】
1. **初期フェーズ**: スマホ完結で環境を整える基礎固め
2. **中期フェーズ**: AIとマーケティングを掛け合わせた効率化
3. **マネタイズフェーズ**: 有料noteへ自然に着地させる心理トリガーの配置

*(※本番のOpenAI APIキーを入力すると、この部分が指定されたテーマ・文字数に合わせて毎回完全にオリジナルのリッチな長文記事として自動執筆されます)*
"""

        # マーケティングメタ情報
        st.markdown("### 📊 マーケティング・アナリティクス")
        st.info(f"**選定テーマ**: {theme}\n\n**ターゲット層**: {target_layer}\n\n**採用した心理トリガー**: {monetize_angle}\n\n**設計ボリューム**: *約 {output_length} 文字*")
        
        # 生成された記事の表示
        st.markdown("---")
        st.markdown("### 📝 【有料note対応】生成記事出力")
        st.markdown(generated_text)
