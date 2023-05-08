import openai
import openai_secret_manager
import requests

secrets = {
    "api_key": "********************************************"
}
#openai_secret_manager.set_secret("openai", secrets)

def ask_gpt(prompt, model, max_tokens=16, temperature=0.5):
	# OpenAI APIキーを取得
	#secrets = openai_secret_manager.get_secret("openai")
	#api_key = secrets["api_key"]
	api_key = secrets["api_key"]
	
	# APIリクエストのヘッダー情報を設定
	headers = {
		"Content-Type": "application/json",
		"Authorization": f"Bearer {api_key}"
	}
	
	# APIリクエストのボディを設定
	data = {
		"prompt": prompt,
		"model": model,
		"max_tokens": max_tokens,
		"temperature": temperature
	}
	
	# APIリクエストを送信
	#response = requests.post("https://api.openai.com/v1/engine/completion", headers=headers, json=data)
	response = requests.post("https://api.openai.com/v1/engine/babbage/completions", headers=headers, json=data)
	print(response)

	# APIレスポンスのテキストを返す
	#return response.json()["choices"][0]["text"].strip()


# ChatGPTに対してAPIリクエストを送信し、応答を受け取る
prompt = "Hello, how are you?"
#model = "gpt-3.5-turbo"
model = "aba"
response = ask_gpt(prompt, model)

# ChatGPTの応答を表示する
print(response)
