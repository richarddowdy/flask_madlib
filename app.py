from flask import Flask, request
from stories import story

app = Flask(__name__)

@app.route("/")
def root():
    """Show Homepage"""
    input_form = ""
    for prompt in story.prompts:
        input_form += f'<label style="display:block">{prompt} : <input  name="{prompt}""></input></label>'

    return f"""
        <html>
            <head>
                <title>Madlibs</title>
            </head>
            <body>
                <h1>Madlibs</h1>
                <form action="/story" method="POST">
                    {input_form}
                    <button>SUBMIT</button>
                </form>
            </body>
        </html>
    """

@app.route("/story", methods=["POST"])
def madlib_story():
    """Show the story generated"""

    answers = request.form

    return f"<h1>{story.generate(answers)}</h1>"

    

