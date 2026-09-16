import streamlit as st

# ページ基本設定
st.set_page_config(page_title="NexusNote Executive Pro", page_icon="👑", layout="centered")

# エグゼクティブ版専用のプレミアムヘッダー
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

# 入力セクション
api_key = st.text_input("OpenAI APIキー（※未所持の場合は空欄でOK）", type="password", placeholder="sk-...", help="APIキーがない場合はデモモードで動作します")
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
        with st.spinner("💎 プロ仕様のマーケティング構成と心理トリガーを構築中..."):
            # デモ用の演出（数秒待つような挙動）
            import time
            time.sleep(1)
            
            st.success("✨ エグゼクティブ版の収益化記事の構築が完了しました！")
            
            # マーケティングメタ情報
            st.markdown("### 📊 マーケティング・アナリティクス")
            st.info(f"**選定テーマ**: {theme}\n\n**ターゲット層**: {target_layer}\n\n**採用した心理トリガー**: {monetize_angle}\n\n**設計ボリューム**: 約 {output_length} 文字")
            
            # 生成されたプレビュー記事
            st.markdown("---")
            st.markdown("### 📝 【有料note対応】生成プレビュー出力")
            st.markdown(f"""
            #### 【プロローグ：読者の感情を揺さぶる導入】
            「本当にこのままで、毎月の収入やスキルに満足できていますか？」
            あなたが今入力したテーマ：**『{theme}』** に基づき、読者が思わず手を止めてしまう強烈なフックを設置しました。
            
            #### 【第1章：現状の課題と損失回避の提示】
            多くの人が勘違いしていますが、〇〇を怠っていると、年間で数十万円もの機会損失を生み出しています。今回、{target_layer}に向けて最適化した導線を組んでいます。
            
            #### 【第2章：門外不出の解決ロードマップ】
            1. 初期フェーズ：スマホ完結で環境を整える
            2. 中期フェーズ：AIとマーケティングを掛け合わせた自動化
            3. マネタイズフェーズ：有料noteへ自然に着地させる心理トリガーの配置
            
            *(※実際のAPIが連携された環境では、ここからさらに数千文字の濃密な執筆・推敲が行われます)*
            """)
            
            # コピー用ボタンの模倣（UIの高級感アップ）
            st.button("📋 記事全体をクリップボードにコピーする", use_container_width=True)
