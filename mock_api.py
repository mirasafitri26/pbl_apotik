from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Demo obat data
OBAT_DATA = [
    {
        "ID_OBAT": 1,
        "NAMA_OBAT": "Paracetamol",
        "JENIS_OBAT": "Analgesik",
        "STOK": 120,
        "EXPIRED_DATE": "2026-12-31",
        "HARGA_JUAL": 5000,
        "HARGA_BELI": 3000
    }
]

ANTRIAN_DATA = [
    {
        "ID_ANTRIAN": 1,
        "NOMOR_ANTRIAN": "A01",
        "NAMA_PASIEN": "Muhammad Khairi",
        "ID_RESEP": 101,
        "DAFTAR_OBAT": "Paracetamol 500mg",
        "STATUS": "MENUNGGU"
    },
    {
        "ID_ANTRIAN": 2,
        "NOMOR_ANTRIAN": "A02",
        "NAMA_PASIEN": "Ayu Ting Ting",
        "ID_RESEP": 102,
        "DAFTAR_OBAT": "Mylanta Cair 50ml",
        "STATUS": "DIPROSES"
    }
]

USERS = {
    "adminapotik@gmail.com": {"password": "uusganteng123", "role": "Admin"},
    "petugasapotik@gmail.com": {"password": "uusganteng123", "role": "Petugas"},
    "pasien@example.com": {"password": "pass123", "role": "Pasien"}
}

@app.route('/api/obat', methods=['GET'])
def get_obat():
    return jsonify({"data": OBAT_DATA}), 200

@app.route('/api/antrian-pengambilan-obat', methods=['GET'])
def get_antrian():
    return jsonify({"data": ANTRIAN_DATA}), 200

@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json() or {}
    email = data.get('email')
    password = data.get('password')
    role = data.get('role', '')

    user = USERS.get(email)
    if user and user['password'] == password:
        # simple role check
        token = f"demo-token-{email}"
        return jsonify({"success": True, "role": user['role'], "token": token}), 200

    return jsonify({"success": False, "message": "Email atau password salah"}), 401


# Alias compatible with /api/auth/login used by the real API docs
@app.route('/api/auth/login', methods=['POST'])
def auth_login():
    return login()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
