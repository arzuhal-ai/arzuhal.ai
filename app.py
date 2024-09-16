from flask import Flask, request, jsonify, render_template
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

app = Flask(__name__)

# GPT-2 modelini ve tokenizer'ı yükleyin
model_name = "gpt2"
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate-dilekce', methods=['POST'])
def generate_dilekce():
    data = request.get_json()
    kisi_adi = data.get('kisiAdi', 'Yetkili Kişi/Makam')
    anahtar_kelime = data.get('anahtarKelime', 'Anahtar Kelime Girilmedi')

    # GPT-2'ye verilecek prompt
    prompt = f"Kime: {kisi_adi}\nKonu: {anahtar_kelime.capitalize()}\n\nSayın {kisi_adi},\n\n{anahtar_kelime.capitalize()} ile ilgili dilekçem aşağıdadır:\n"

    # GPT-2 modelini kullanarak metin oluşturma
    inputs = tokenizer.encode(prompt, return_tensors='pt')
    outputs = model.generate(inputs, max_length=200, num_return_sequences=1, no_repeat_ngram_size=2)
    generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

    dilekce = f"""Sayın {kisi_adi},\n\nKonu: {anahtar_kelime.capitalize()}\n\n{generated_text}\n\nGereğinin yapılmasını arz ederim.\n\nTarih: """
    
    return jsonify({'generated_text': dilekce})

if __name__ == '__main__':
    app.run(debug=True)
