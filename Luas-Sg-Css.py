from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def hitung_luas_segitiga(alas, tinggi):
    if alas <= 0 or tinggi <= 0:
        return "Alas dan tinggi harus lebih besar dari 0."
    luas = 0.5 * alas * tinggi
    return luas

@app.route('/')
def index():
    return render_template('Hit_Luas.html')

@app.route('/hitung_luas', methods=['POST'])
def hitung_luas():
    alas = float(request.json['alas'])
    tinggi = float(request.json['tinggi'])
    hasil = hitung_luas_segitiga(alas,tinggi)
    return jsonify({'hasil':hasil})

if __name__ == '__main__':
    app.run()