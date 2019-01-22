from flask import Flask
from flask import request
from flask import render_template

from controller import Controller


class View:

    def __init__(self):
        self.rosterSelected = False


view = View()
controller = Controller()
app = Flask("Verde Valley Volleyball")


@app.route("/")
def getRosterId():
    roster_id = request.args.get("rosterN")

    if not roster_id:
        # Do nothing
        display = render_template("home.html", rosterSelected=view.rosterSelected)
        pass
    else: # Get the number from the end of the value, convert to an int and send to the controller
        roster_id = int(roster_id[-1])
        controller.selectRoster(roster_id)
        view.rosterSelected = True
        display = render_template("home.html", rosterSelected=view.rosterSelected)

    return display

def getActionCode():
    if view.rosterSelected:
        action_code = request.args.get("actionN")


if __name__ == "__main__":
    app.run(port=5000, debug=True)

