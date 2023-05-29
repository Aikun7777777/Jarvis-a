
import openai
from flask import Flask, request, render_template


openai.api_key = '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'



import json

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        user_prompt = request.form['prompt']
        with open('personal_info.json', 'r') as json_file:
            loaded_info = json.load(json_file)
        fixed_prompt = "Given the personal information {}, "
        full_prompt = fixed_prompt.format(loaded_info) + user_prompt
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=full_prompt,
            max_tokens=1000
        )
        return render_template('index.html', gpt_response=response.choices[0].text.strip())
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port=5001, debug=True)


# # 从 'personal_info.json' 文件中加载个人信息
# with open('personal_info.json', 'r') as json_file:
#     loaded_info = json.load(json_file)

# # 设置你的OpenAI API密钥
# # openai.api_key = 'your-api-key'

# # 创建一个提示，用你的个人信息作为输入
# # prompt = f"Given the personal information {loaded_info},用中文回答应这样的人该找一个什么样的女朋友"

# # 创建一个固定的提示
# fixed_prompt = "Given the personal information {}, 假设我是John Doe，请根据这些信息在作出以下的回答，回答全部用中文，想我这样的人"

# # 创建一个动态的提示，这可以根据你的需要在运行时改变
# user_prompt = input("Please enter your prompt: ")

# # 将固定的提示、用户的提示和个人信息组合起来
# full_prompt = fixed_prompt.format(loaded_info) + user_prompt

# # 调用GPT API生成描述
# response = openai.Completion.create(
#   engine="text-davinci-003",
#   prompt=full_prompt,
#   max_tokens=1000
# )

# # 打印出GPT的响应
# print(response.choices[0].text.strip())


