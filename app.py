from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)

# Reference images (Using Flask's `url_for`)
image_paths = {
    "1": "reference_1.jpg",
    "2": "reference_2.jpg",
    "3": "reference_3.jpg",
    "4": "reference_4.jpg",
    "5": "reference_5.jpg",
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/view/<image_id>")
def view_image(image_id):
    if image_id not in image_paths:
        return redirect(url_for("home"))  # Prevent invalid image requests

    image_url = url_for('static', filename=image_paths[image_id])
    return render_template("view.html", image_src=image_url, countdown=5)  # 5 min countdown

if __name__ == "__main__":
    app.run(debug=True)
