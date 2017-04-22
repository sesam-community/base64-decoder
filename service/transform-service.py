from flask import Flask, request, Response
import json
import os
import base64

app = Flask(__name__)

source_prop = os.environ["SOURCE_PROPERTY"]
target_prop = os.environ["TARGET_PROPERTY"]
encoding = os.environ.get("ENCODING", "UTF-8")

@app.route('/transform', methods=['POST'])
def receiver():

    def generate(entities):
        yield "["
        for index, entity in enumerate(entities):
            if index > 0:
                yield ","
            entity[target_prop] = base64.b64decode(entity[source_prop]).decode(encoding)
            yield json.dumps(entity)
        yield "]"

    # get entities from request
    entities = request.get_json()

    # create the response
    return Response(generate(entities), mimetype='application/json')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)

