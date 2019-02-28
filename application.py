from flask import Flask
from flask import request
from flask import render_template

from controller import Controller


class View:

    def __init__(self):
        self.rosterSelected = False

@app.route("/")
def getRosterId():
    roster_id = request.args.get("rosterN")
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
        attackers = controller.goAction(1)
        blockers = controller.goAction(2)
        teams = controller.goAction(3)
        display = render_template("home.html", rosterSelected=view.rosterSelected, top_attackers=attackers, top_blockers=blockers, teams=teams)

    return display

if __name__ == '__main__':
	view = View()
	controller = Controller()
	app = Flask("Verde Valley Volleyball")
    app.run(port=5000, debug=True)
