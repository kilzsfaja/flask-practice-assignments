from flask import Flask

app = Flask(__name__)

@app.route("/", methods=["GET"])
def hello_world():
    return "Hello World!"

@app.route("/dojo", methods=["GET"])
def dojo():
    return "DOJO!"

@app.route("/say/flask", methods=["GET"])
def say_flask():
    return f"<h1>Hi Flask!!</h1>"

@app.route("/say/<string:first_name>", methods=["GET"])
def greet_someone(first_name):
    return f"<h1>Wazzup {first_name}!</h1>"

@app.route("/say/john>", methods=["GET"])
def greet_john():
    return f"<h1>Wazzup John!</h1>"

@app.route("/repeat/<int:num>/<string:word>")
def repeater(num, word):
    # COULD ALSO DO:
    # return f"{word * num} >>> this will return all in a line
    output = ""

    for i in range(0, num):
        output += f"<h2>{word}</h2>"

    return output

# @app.route("/students", methods=["GET"])
# def display_list_of_students():
#     student_list = ["Alex", "M", "Roger", "Julie"]
#     result = ""

#     for student in student_list:
#         result += f"<p>{student}</p>"
#     return f"<h1>The students are: </h1> {result}"

if __name__ == "__main__":
    app.run(debug = True) # needed "boiler plate" *** SHOULD ALWAYS BE LAST STATEMENT ***