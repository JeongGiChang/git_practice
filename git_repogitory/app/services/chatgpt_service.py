import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

class ChatGPTService:
    def __init__(self, api_key=None, model="gpt-4o-mini"):
        if api_key is None:
            api_key = os.getenv("OPENAI_API_KEY")
        self.client = OpenAI(api_key=api_key)
        self.model = model
    

    def generate_response(self, prompt):
        system_message = """
    너는 영양사 챗봇이야.
    사용자가 오늘 먹은 식단을 입력하면, 부족할 수 있는 영양소를 분석하고, 그에 맞는 영양제를 추천해줘.
    반드시 다음과 같은 형식을 지켜서 답변해줘:
    1. 식단 분석:
    - 어떤 영양소 위주의 식단을 했고 어떤 영양소가 부족함

    2. 추천:
    '영양소 :비타민 D'
    '효과 : 면역력 강화'
    '추천 영양제 : 나우푸드 비타민D 2000IU
    가격대 : 약 1만원
    """
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                   {"role": "system", "content": system_message},
                    {"role": "user", "content": prompt}
                ]
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            raise Exception(f"ChatGPT API 호출 중 오류: {e}")


