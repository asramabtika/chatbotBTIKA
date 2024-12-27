from flask import Flask, request, jsonify

app = Flask(__name__)

# Contoh jawaban chatbot
responses = {
    "alamat asrama": "Asrama Bhinneka Tunggal Ika terletak di Jalan Dharmawangsa No. 10, Surabaya.",
    "fasilitas": "Asrama menyediakan fasilitas seperti kamar tidur, dapur, ruang belajar, dan koneksi Wi-Fi.",
    "aturan asrama": "Aturan utama adalah menjaga kebersihan, tidak membawa barang terlarang, dan mematuhi jam malam pukul 22:00.",
    "kontak": "Untuk informasi lebih lanjut, hubungi 0812-3456-7890.",
    "kegiatan asrama": "Kegiatan meliputi senam pagi, diskusi mingguan, dan kegiatan kebersamaan lainnya.",
    "pendaftaran": "Pendaftaran dilakukan secara online melalui website resmi asrama atau datang langsung ke kantor administrasi.",
    "default": "Maaf, saya tidak mengerti pertanyaan Anda. Silakan coba lagi dengan kata kunci yang lebih jelas."
}

@app.route('/chat', methods=['GET'])
def chat():
    user_input = request.args.get('q', '').lower()
    response = responses.get(user_input, responses["default"])
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
