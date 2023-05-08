import os
import openai
import sys
#openai.organization = "org-*******************************"

# APIキー
## set-hack-note
#openai.api_key = "sk-***************************************"
## test-hack-note
openai.api_key = "sk-***************************************"

# 疎通確認のために、エンジン一覧を取得する
engines = openai.Engine.list()
#print(engines)%exit()

#---
# 標準入力からテキストを受け取る
txt = sys.stdin.read()

# テキストを加工する（ここでは、テキストを大文字に変換してから表示する）
txt_up = txt.upper()
#print(text_uppercase)%exit()
#---

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  #model="curie",
  messages=[
    {"role": "user", "content": txt_up}
  ]
)

message = completion.choices[0].message
text = message.content
print(text)%exit()
decoded_text = text.encode('utf-8').decode('unicode_escape')
print(decoded_text)
