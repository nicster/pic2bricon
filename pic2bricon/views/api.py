import base64
import json
import re
from io import BytesIO

import flask
from PIL import Image

from pic2bricon import app


@app.route('/')
def hello_world():
    return "This is an awesome machine learning api"


@app.route('/bricon', methods=["POST"])
def get_bricon_for_pic():
    LUA_PATH = "/dinimuetter/minimuetter"
    result = flask.request.get_json()
    image_base64 = result["image"]

    image_data = re.sub(r'^data:image/.+;base64,', '', image_base64)

    img = Image.open(BytesIO(base64.b64decode(image_data)))
    img.save('out.jpg')
    return json.dumps({'result': 'success'}), 200, {'ContentType': 'application/json'}
