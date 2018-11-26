from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                float: left;
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
        <form class= "caesar-form" action = "/" method="POST">
        Rotate by: <input type="text" name="rot" id="rot" value="0" /> <br>
        <textarea name="text" id="text" />{0}
        </textarea><br> 
        <input type = "Submit" value="Submit Query" />
        </form>
    </body>
</html>
"""

@app.route("/")


def index():
    return form.format("")

@app.route("/", methods=['POST'])
def encrypt():
    rot=int(request.form['rot'])
    text=str(request.form['text'])
    encrypted_text = rotate_string(text, rot)

    return form.format(encrypted_text)

app.run()