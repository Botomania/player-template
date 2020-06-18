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
        action = self.sol(state)

        return action

    def runner_exec(self, state):
        state = str(state)

        p = subprocess.Popen(self.sol, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        action = p.communicate(input=state.encode())[0].decode("utf-8")

        return action.strip()


@app.route("/", methods=["POST"])
def handle():
    """
    Pass state to function and return
    """
    state = request.json["state"]
    action = r.run(state)

    return jsonify({"action": action})


@app.route("/end", methods=["POST"])
def quit():
    """
    Closes everything and shuts down
    """
    request.environ.get("werkzeug.server.shutdown")()
    return "Shutting down..."


def run(format, solution):
    global r
    r = Runner(format, solution)

    app.run("0.0.0.0", 5000)
