from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    template = {}
    return render_template('main.html', **template);


@app.route("/butler/", methods=['POST'])
def butler():
    print ("butler button: ", get_button(request))
    template = {}
    return render_template('main.html', **template);


def get_button(request):
    button = "none"
    for key in request.form.keys():
        button = key
    return button


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
