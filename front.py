from flask import Flask
from flask import request
from flask import render_template

from controller import Controller

controller = Controller()
app = Flask("Verde Valley Volleyball")


@app.route("/")
def getAction():
    roster_id = request.args.get("rosterN")

    if not roster_id:
        # Do nothing
        display = render_template("home.html", msg="")
        pass
    else: # Get the number from the end of the value, convert to an int and send to the controller
        roster_id = int(roster_id[-1])
        display = render_template("home.html", msg="You selected {}".format(roster_id))

    return display


if __name__ == "__main__":
    app.run(port=5000, debug=True)

