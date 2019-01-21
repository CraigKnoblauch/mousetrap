from flask import Flask
from flask import request
from flask import render_template


app = Flask("Verde Valley Volleyball")


@app.route("/")
def getAction():
    action = request.args.get("action")

    if not action:
        # Do nothing
        display = render_template("home.html", msg="")
        pass
    else: # Check that the user arg is a number
        try:
            action = int(action)
        except ValueError:
            display = render_template("home.html", msg="Error, you must input a number")
            return display # I'm only returning here because I don't know how to get out of this one

        if action > 5 or action < 1:
            display = render_template("home.html", msg="Error, invalid action number")
        else:
            # TODO, pass the action to the controller and figure out what to do.
            pass
        
    return display


if __name__ == "__main__":
    app.run(port=5000, debug=True)

