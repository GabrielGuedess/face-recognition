from flask import Flask, request
import json
from app import compare_faces

app = Flask(__name__)


@app.route("/face_match", methods=["POST"])
def face_match():
    if request.method == "POST":
        if ("file1" in request.files) and ("file2" in request.files):
            file1 = request.files.get("file1")
            file2 = request.files.get("file2")

            ret = compare_faces(file1, file2)

            resp_data = {"match": bool(ret)}

            return json.dumps(resp_data)


app.run(host="0.0.0.0", port="5001", debug=True)
