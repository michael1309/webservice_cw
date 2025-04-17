from flask import Flask, send_file
from io import BytesIO
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont

app = Flask(__name__)

@app.route("/")
def index():
    return "Try /kw.png"

@app.route("/kw.png")
def calendar_week_image():
    now = datetime.now()
    week = now.isocalendar()[1]
    date_str = now.strftime("%d.%m.%Y")
    text = f"KW{week} – {date_str}"

    img = Image.new('RGB', (300, 60), color='white')
    draw = ImageDraw.Draw(img)
    font = ImageFont.load_default()
    draw.text((10, 20), text, fill='black', font=font)

    img_bytes = BytesIO()
    img.save(img_bytes, format='PNG')
    img_bytes.seek(0)

    return send_file(img_bytes, mimetype='image/png')
