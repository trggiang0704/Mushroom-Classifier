from flask import Flask, render_template, request
import pickle

# ------------------------
# Load model
# ------------------------
MODEL_PATH = "mushroom_model.pkl"  # đổi thành "mushroom_model_3features.pkl" nếu bạn lưu tên này
with open(MODEL_PATH, "rb") as f:
    tree = pickle.load(f)

# ------------------------
# Hàm dự đoán trên cây ID3
# ------------------------
def predict(tree, sample):
    if not isinstance(tree, dict):
        return tree
    feature = next(iter(tree))
    value = sample.get(feature, None)
    if value in tree[feature]:
        return predict(tree[feature][value], sample)
    else:
        # Giữ nguyên hành vi như bản Tkinter của bạn
        return "Không xác định"

# ------------------------
# Từ điển giá trị (song ngữ)
# ------------------------
odor_values = {
    "a": "a - hạnh nhân (almond)",
    "l": "l - hồi (anise)",
    "c": "c - creosote (nhựa gỗ)",
    "y": "y - cá (fishy)",
    "f": "f - hôi (foul)",
    "m": "m - mốc (musty)",
    "n": "n - không mùi (none)",
    "p": "p - cay (pungent)",
    "s": "s - cay nồng (spicy)"
}

cap_color_values = {
    "n": "n - nâu (brown)",
    "b": "b - be (buff)",
    "c": "c - quế (cinnamon)",
    "g": "g - xám (gray)",
    "r": "r - xanh lục (green)",
    "p": "p - hồng (pink)",
    "u": "u - tím (purple)",
    "e": "e - đỏ (red)",
    "w": "w - trắng (white)",
    "y": "y - vàng (yellow)"
}

gill_color_values = {
    "k": "k - đen (black)",
    "n": "n - nâu (brown)",
    "b": "b - be (buff)",
    "h": "h - chocolate",
    "g": "g - xám (gray)",
    "r": "r - xanh lục (green)",
    "o": "o - cam (orange)",
    "p": "p - hồng (pink)",
    "u": "u - tím (purple)",
    "e": "e - đỏ (red)",
    "w": "w - trắng (white)",
    "y": "y - vàng (yellow)"
}

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    pred_code = None

    if request.method == "POST":
        odor_sel = request.form.get("odor")
        cap_color_sel = request.form.get("cap_color")
        gill_color_sel = request.form.get("gill_color")

        if not odor_sel or not cap_color_sel or not gill_color_sel:
            result = "⚠️ Vui lòng chọn đầy đủ thông tin!"
        else:
            sample = {
                "odor": odor_sel,
                "cap-color": cap_color_sel,
                "gill-color": gill_color_sel
            }
            pred_code = predict(tree, sample)
            if pred_code == "e":
                result = "🍄 Nấm ăn được (Edible)"
            elif pred_code == "p":
                result = "☠️ Nấm độc (Poisonous)"
            else:
                result = "⚠️ Không xác định được"

    return render_template(
        "index.html",
        odor_values=odor_values,
        cap_color_values=cap_color_values,
        gill_color_values=gill_color_values,
        result=result,
        pred_code=pred_code
    )

if __name__ == "__main__":
    # Chạy dev server
    app.run(host="0.0.0.0", port=5000, debug=True)
