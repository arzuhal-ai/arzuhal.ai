from flask import Flask, request, jsonify
import openai  # Veya ilgili GPT-2/3 kütüphanesi

app = Flask(__name__)

@app.route('/generate-dilekce', methods=['POST'])
def generate_dilekce():
    data = request.get_json()
    kisi_adi = data.get('kisiAdi')
    anahtar_kelime = data.get('anahtarKelime')
    
    # GPT modelini kullanarak dilekçeyi oluşturun
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",  # veya uygun model
            prompt=f"Dilekçe talebi:\nKişi Adı: {kisi_adi}\nAnahtar Kelime: {anahtar_kelime}",
            max_tokens=150
        )
        generated_text = response.choices[0].text.strip()
        return jsonify({'generated_text': generated_text})
    except Exception as e:
        print(f'API hatası: {e}')
        return jsonify({'error': 'Dilekçe oluşturulamadı.'}), 500

if __name__ == '__main__':
    app.run(debug=True)
