import os
from flask import Flask, send_from_directory, request
from flask_restful import Resource, Api
from models import db, Image
from config import Config
import imghdr
import uuid
from werkzeug.utils import secure_filename


app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

app.json.compact = False

def validate_image(stream):
    header = stream.read(512)
    stream.seek(0)
    check_format = imghdr.what(stream, header)
    if not check_format:
        return None
    return "." + (check_format if check_format != "jpeg" else "jpg")

class ImageUpload(Resource):
    def post(self):
        image_name = request.form.get("image_name")
        image = request.files.get("image")

        if not image:
            return {"error": "No se mando ningun archivo"}, 400

        filename = secure_filename(image.filename)
        existing_files = [img.file_path for img in Image.query.all()]

        if filename in existing_files:
            unique_str = str(uuid.uuid4())[:8]
            filename = f"{unique_str}_{filename}"

        if filename:
            file_ext = os.path.splitext(filename)[1].lower()
            if file_ext not in app.config["UPLOAD_EXTENSIONS"] or file_ext != validate_image(image.stream):
                return {"error": "Archivo no soportado"}, 400

            image.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
            img = Image(name=image_name, file_path=filename)

            db.session.add(img)
            db.session.commit()
            return {"mensaje": "Imagen subida con exito", "file": filename}, 201

        return {"error": "Archivo no valido"}, 400

class ImageResource(Resource):
    def get(self, id):
        img = Image.query.filter_by(id=id).first()
        if not img:
            return {"error": "Imagen no encontrada"}, 404

        return send_from_directory(app.config["UPLOAD_FOLDER"], img.file_path)


api = Api(app)
api.add_resource(ImageUpload, "/upload")
api.add_resource(ImageResource, "/image/<id>")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
