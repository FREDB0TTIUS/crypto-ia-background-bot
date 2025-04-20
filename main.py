import openai
import os

# On récupère la clé depuis les variables d’environnement
openai.api_key = os.getenv("OPENAI_API_KEY")

def analyse_marche():
    print("🧠 Appel à GPT en cours...")

    # Prompt envoyé à GPT-4
    prompt = (
        "Tu es un expert en stratégie crypto. "
        "Analyse le marché aujourd'hui et réponds uniquement par un JSON avec 3 champs : "
        "{ 'decision': 'BUY/SELL/HOLD', 'token': 'le token concerné', 'amount': montant en USDT }"
    )

    # Appel GPT-4 via OpenAI API
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Tu es un conseiller de trading crypto très expérimenté."},
                {"role": "user", "content": prompt}
            ]
        )

        output = response['choices'][0]['message']['content']
        print("🔍 Réponse GPT brute :", output)

        # Conversion en dict (on suppose que la réponse est bien formatée)
        import json
        return json.loads(output)

    except Exception as e:
        print("❌ Erreur GPT :", e)
        return {"decision": "HOLD", "token": None, "amount": 0}
