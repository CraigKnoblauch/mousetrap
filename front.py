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
    should_go = False
    view.rosterSelected = False

    if not roster_id:
        # Do nothing
        display = render_template("home.html", rosterSelected=view.rosterSelected)
        pass
    else: # Get the number from the end of the value, convert to an int and send to the controller
        roster_id = int(roster_id[-1])
        controller.selectRoster(roster_id)
        view.rosterSelected = True
        display = render_template("home.html", rosterSelected=view.rosterSelected)

    if view.rosterSelected:
        while not should_go:
            should_go = request.args.get("go")

    if not should_go:
        # Do nothing
        pass

    else:
        # TODO, request from GO, if exists, then request from actionN
        action_id = request.args.get("actionN")

        # Use the action_id for the controller
        action_id = int(action_id[-1])
        msg = controller.goAction(action_id)
        display = render_template("home.html", rosterSelected=view.rosterSelected, msg=msg)

    return display

def getActionCode(): # AJAX request for this
    if view.rosterSelected:
        action_code = request.args.get("actionN")


if __name__ == "__main__":
    app.run(port=5000, debug=True)

