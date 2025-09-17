from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv(override=True)
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

response = client.chat.completions.create(
    model="gpt-4o-mini",
    temperature=0.9,
    messages=[
        {"role": "system", 'content': "너는 배트맨에 나오는 조커야. 조커의 악당 캐릭터에 맞게 답변 해 줘."},
        {"role": "user", "content":"방금은 뭐라했어?"},
    ]
)

print(response.choices[0].message.content)