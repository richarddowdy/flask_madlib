from flask import Flask, request, render_template
from stories import story

app = Flask(__name__)

@app.route("/story")
def root():
    """Show Homepage"""

    return render_template("madLibPrompt.html", prompts=story.prompts)

    # input_form = ""
    # for prompt in story.prompts:
    #     input_form += f'<label style="display:block">{prompt} : <input  name="{prompt}""></input></label>'

    # return f"""
    #     <html>
    #         <head>
    #             <title>Madlibs</title>
    #         </head>
    #         <body>
    #             <h1>Madlibs</h1>
    #             <form action="/story" method="POST">
    #                 {input_form}
    #                 <button>SUBMIT</button>
    #             </form>
    #         </body>
    #     </html>
    # """

@app.route("/story", methods=["POST"])
def madlib_story():
    """Show the story generated"""

    answers = request.form

    return render_template("madLibStory.html", your_story=story.generate(answers))
