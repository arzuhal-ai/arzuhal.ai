document.getElementById('dilekce-form').addEventListener('submit', async (event) => {
    event.preventDefault();
    
    const kisiAdi = document.getElementById('kisiAdi').value;
    const anahtarKelime = document.getElementById('anahtarKelime').value;
    
    try {
        const response = await fetch('/generate-dilekce', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ kisiAdi, anahtarKelime })
        });
        
        if (!response.ok) {
            throw new Error('Ağ hatası');
        }
        
        const data = await response.json();
        document.getElementById('output').innerText = data.generated_text;
    } catch (error) {
        console.error('Bir hata oluştu:', error);
        document.getElementById('output').innerText = 'Dilekçe oluşturulamadı. Lütfen tekrar deneyin.';
    }
});
