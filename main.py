
import time
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def analyse_marche():
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Tu es un assistant crypto expert."},
            {"role": "user", "content": "Analyse le marché crypto aujourd'hui et donne une stratégie à court terme."}
        ]
    )
    print("🔍 STRATÉGIE :", response['choices'][0]['message']['content'])

if __name__ == "__main__":
    while True:
        analyse_marche()
        print("⏳ Attente de 30 minutes avant la prochaine analyse...")
        time.sleep(1800)
