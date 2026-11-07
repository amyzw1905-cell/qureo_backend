from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/solve', methods=['POST'])
def solve_task():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    grade = data.get('grade')
    section = data.get('section')

    if not username or not password:
        return jsonify({"error": "البيانات ناقصة"}), 400

    simulated_steps = [
        f"تم تسجيل الدخول بنجاح للحساب: {username}",
        f"تم تحديد الصف: {grade} والقسم: {section}",
        "جاري تخطي الحصص وحل المهام تلقائياً...",
        "تم الانتهاء بنجاح!"
    ]

    return jsonify({"status": "success", "steps": simulated_steps})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
