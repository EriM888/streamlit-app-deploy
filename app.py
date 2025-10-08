import streamlit as st

st.title("Hello Streamlit!")
st.write("Streamlitアプリケーションへようこそ！")

# サンプルコンテンツを追加
st.header("基本的なStreamlit機能のデモ")

# テキスト入力
name = st.text_input("あなたの名前を入力してください:")
if name:
    st.write(f"こんにちは、{name}さん！")

# ボタン
if st.button("クリックしてください"):
    st.write("ボタンがクリックされました！")

# スライダー
age = st.slider("年齢を選択してください", 0, 100, 25)
st.write(f"選択された年齢: {age}歳")
import streamlit as st

st.title("Hello Streamlit!")

import streamlit as st

st.title("Hello Streamlit!")

import streamlit as st

st.title("サンプルアプリ①: 簡単なWebアプリ")

input_message = st.text_input(label="文字数のカウント対象となるテキストを入力してください。")

text_count = len(input_message)

if st.button("実行"):
    st.write(f"入力されたテキストの文字数: {text_count}文字")