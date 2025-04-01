import google.generativeai as genai

class GeminiService:
    def __init__(self, api_key="AIzaSyBJOYcSLxbx5cQdWmfYN4dOg8E0Bq33pYY", model="models/gemini-1.5-pro-latest"):
        genai.configure(api_key="AIzaSyBJOYcSLxbx5cQdWmfYN4dOg8E0Bq33pYY")
        self.model = genai.GenerativeModel(model)

    def generate_response(self, prompt):
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            raise Exception(f"Gemini API 호출 중 오류: {e}")

# 테스트용 실행
if __name__ == "__main__":
    API_KEY = "AIzaSyBJOYcSLxbx5cQdWmfYN4dOg8E0Bq33pYY"
    service = GeminiService(API_KEY)
    print(service.generate_response("안녕! 너는 누구야?"))
