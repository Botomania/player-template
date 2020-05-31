import sys
import subprocess

from flask import Flask, request, jsonify

app = Flask(__name__)
r = None


class Runner:
    """
    Manages running of all submissions
    """

    def __init__(self, format, solution):
        self.fmt = format
        self.sol = solution

        self.runners = {
            "python": self.runner_py,
            "executable": self.runner_exec,
        }

    def run(self, state):
        return self.runners[self.fmt](state)

    def runner_py(self, state):
        new_state = self.sol(state)

        return new_state

    def runner_exec(self, state):
        state = str(state)

        p = subprocess.Popen(self.sol, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        new_state = p.communicate(input=state.encode())[0].decode("utf-8")

        return new_state.strip()


@app.route("/", methods=["POST"])
def handle():
    """
    Pass state to function and return
    """
    state = request.json["state"]
    new_state = r.run(state)

    return jsonify({"state": new_state})


@app.route("/end", methods=["POST"])
def quit():
    """
    Closes everything and shuts down
    """
    print("Quitting...")
    sys.exit(0)


def run(format, solution):
    global r
    r = Runner(format, solution)

    app.run("0.0.0.0", 5000)
