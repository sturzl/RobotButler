from flask import Flask, render_template, request
from butler.Arm import Arm
import sys


app = Flask(__name__)
valid_selections = {'1','2','3','4','5'}
arm = None


@app.route("/")
def home():
    template = {}
    return render_template('main.html', **template)

@app.route("/butler/", methods=['POST'])
def butler():
    selection = parse_request(request)
    if selection in valid_selections:
        serve_customer(selection)
    else:
        print('Invalid selection: ', selection)
    template = {}
    return render_template('main.html', **template)

def serve_customer(selection):
    arm.aim_arm()
    arm.set_blink_speed(selection)
    arm.reset_arm()

def parse_request(request):
    button = "none"
    for key in request.form.keys():
        button = key
    print("Selection from website parsing: ", button)
    return button

if __name__ == "__main__":
    port = None
    if len(sys.argv) == 2:
        port = sys.argv[1]
    else:
        print('Incorrect parameters. Please enter arduino port as only parameter.')
        exit()

    arm = Arm(port)

    app.run(host='0.0.0.0', port=80)