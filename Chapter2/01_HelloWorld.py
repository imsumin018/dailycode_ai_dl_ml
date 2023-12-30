#2.4.2 'Hello World' 예제

from openai import OpenAI
client = OpenAI(api_key='OpenAI_API_KEY') #OpenAI 사이트에서 획득한 사용자의 API키를 입력합니다. ChatGPT Plus 요금제와 별도로 크레딧이 충전되어 있어야 합니다
  
# 오픈AI 채팅 완성 엔드포인트 호출
response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[{"role": "user", "content": "Hello World!"}]
)
  
# 응답 추출
print(response.choices[0].message.content)
