# First we bring in Flask.
# Flask is what lets us create a website using Python.
from flask import Flask, render_template, request

# This line creates our app.
# __name__ just tells Flask where this file is located.
app = Flask(__name__)


# HOME PAGE
@app.route("/")
def home():
    return render_template("home.html")


# LESSON PAGES
@app.route("/lessons")
def lessons():
    return render_template("lessons.html")

@app.route("/basicpython")
def basicpython():
    return render_template("basicpython.html")

@app.route("/strings")
def strings():
    return render_template("strings.html")

@app.route("/variables")
def variables():
    return render_template("variables.html")

@app.route("/basic_arithmetic_operations")
def basic_arithmetic_operations():
    return render_template("basic_arithmetic_operations.html")

@app.route("/booleans")
def booleans():
    return render_template("booleans.html")

@app.route("/loops")
def loops():
    return render_template("loops.html")

@app.route("/function_global_variables")
def function_global_variables():
    return render_template("function_global_variables.html")

@app.route("/arrays")
def arrays():
    return render_template("arrays.html")

@app.route("/lists_tuples_sets")
def lists_tuples_sets():
    return render_template("lists_tuples_sets.html")

@app.route("/range")
def range():
    return render_template("range.html")



# QUIZ PAGEs


# If someone types /quiz,
# it will open the quiz page.
@app.route("/quiz")
def quiz():
    return render_template("quiz.html")

@app.route("/quiz_basic", methods=["GET", "POST"]) # allows the page to load (GET) and recieve the form (POST)
def quiz_basic():
    score = None  # This sets the score to start as None
    if request.method == "POST": # check to see if the submit button was pressed
        score = 0 # will reset the score back to 0 before checking
        if request.form.get("q1") == "c":  # correct answer
            score += 1
        if request.form.get("q2") == "b":
            score += 1
        if request.form.get("q3") == "c":
            score += 1
        if request.form.get("q4") == "b":
            score += 1
        if request.form.get("q5") == "c":
            score += 1
        if request.form.get("q6") == "true":
            score += 1
    return render_template("quiz_basic.html", score=score)


@app.route("/quiz_strings", methods=["GET", "POST"])
def quiz_strings():
    score = None

    if request.method == "POST":
        score = 0

        if request.form.get("q1") == "b":
            score += 1
        if request.form.get("q2") == "b":
            score += 1
        if request.form.get("q3") == "b":
            score += 1
        if request.form.get("q4") == "false":
            score += 1
        if request.form.get("q5") == "d":
            score += 1
        if request.form.get("q6") == "b":
            score += 1
        if request.form.get("q7") == "c":
            score += 1
    return render_template("quiz_strings.html", score=score)



@app.route("/quiz_variables", methods=["GET", "POST"])
def quiz_variables():
    score = None

    if request.method == "POST":
        score = 0

        if request.form.get("q1") == "c":
            score += 1
        if request.form.get("q2") == "true":
            score += 1
        if request.form.get("q3") == "b":
            score += 1
        if request.form.get("q4") == "c":
            score += 1
        if request.form.get("q5") == "b":
            score += 1
        if request.form.get("q6") == "b":
            score += 1
    return render_template("quiz_variables.html", score=score)



@app.route("/quiz_basic_arithmetic", methods=["GET", "POST"])
def quiz_basic_arithmetic():
    score = None

    if request.method == "POST":
        score = 0

        if request.form.get("q1") == "b":
            score += 1
        if request.form.get("q2") == "b":
            score += 1
        if request.form.get("q3") == "true":
            score += 1
        if request.form.get("q4") == "c":
            score += 1
        if request.form.get("q5") == "b":
            score += 1
        if request.form.get("q6") == "b":
            score += 1
        if request.form.get("q7") == "b":
            score += 1

    return render_template("quiz_basic_arithmetic.html",  score=score)


@app.route("/quiz_boolean", methods=["GET", "POST"])
def quiz_boolean():
    score = None

    if request.method == "POST":
        score = 0

        if request.form.get("q1") == "b":
            score += 1
        if request.form.get("q2") == "b":
            score += 1
        if request.form.get("q3") == "true":
            score += 1
        if request.form.get("q4") == "b":
            score += 1
        if request.form.get("q5") == "b":
            score += 1
        if request.form.get("q6") == "b":
            score += 1


    return render_template("quiz_boolean.html",  score=score)

@app.route("/quiz_loops", methods=["GET", "POST"])
def quiz_loops():
    score = None

    if request.method == "POST":
        score = 0

        if request.form.get("q1") == "b":
            score += 1
        if request.form.get("q2") == "a":
            score += 1
        if request.form.get("q3") == "b":
            score += 1
        if request.form.get("q4") == "b":
            score += 1
        if request.form.get("q5") == "b":
            score += 1
        if request.form.get("q6") == "a":
            score += 1
        if request.form.get("q7") == "b":
            score += 1

    return render_template("quiz_loops.html", score=score)



@app.route("/quiz_function", methods=["GET", "POST"])
def quiz_function():
    score = None

    if request.method == "POST":
        score = 0

        if request.form.get("q1") == "b":
            score += 1
        if request.form.get("q2") == "b":
            score += 1
        if request.form.get("q3") == "b":
            score += 1
        if request.form.get("q4") == "b":
            score += 1
        if request.form.get("q5") == "false":
            score += 1
        if request.form.get("q6") == "c":
            score += 1
        if request.form.get("q7") == "b":
            score += 1

    return render_template("quiz_function.html",  score=score)


@app.route("/quiz_lists", methods=["GET", "POST"])
def quiz_lists():
    score = None

    if request.method == "POST":
        score = 0

        if request.form.get("q1") == "d":
            score += 1
        if request.form.get("q2") == "b":
            score += 1
        if request.form.get("q3") == "c":
            score += 1
        if request.form.get("q4") == "b":
            score += 1
        if request.form.get("q5") == "false":
            score += 1
        if request.form.get("q6") == "c":
            score += 1

    return render_template("quiz_lists.html",  score=score)



@app.route("/quiz_range", methods=["GET", "POST"])
def quiz_range():
    score = None

    if request.method == "POST":
        score = 0

        if request.form.get("q1") == "a":
            score += 1
        if request.form.get("q2") == "b":
            score += 1
        if request.form.get("q3") == "false":
            score += 1
        if request.form.get("q4") == "b":
            score += 1
        if request.form.get("q5") == "a":
            score += 1


    return render_template("quiz_range.html",  score=score)



@app.route("/quiz_arrays", methods=["GET", "POST"])
def quiz_arrays():
    score = None

    if request.method == "POST":
        score = 0

        if request.form.get("q1") == "b":
            score += 1
        if request.form.get("q2") == "b":
            score += 1
        if request.form.get("q3") == "c":
            score += 1
        if request.form.get("q4") == "a":
            score += 1
        if request.form.get("q5") == "false":
            score += 1
        if request.form.get("q6") == "b":
            score += 1


    return render_template("quiz_arrays.html",  score=score)



#Python practice page
@app.route("/python_tester")
def python_tester():
    return render_template("python_tester.html")





# RUN THE WEBSITE


# This part makes the app actually run.
# Without this, nothing would show up.
# RUN THE WEBSITE
if __name__ == "__main__":
    app.run(debug=True)

#Flask = what lets us build the website
#@app.route() = tells the app what page to show
#render_template() = loads the HTML file
#debug=True = helps us when we mess up
#It runs locally on my computer.
#to run it with app.py in the terminal to create small server on your computer
