from flask import Flask
from utils import SCORES_FILE_NAME, BAD_RETURN_CODE
app = Flask(__name__)


@app.route('/')
def score_server():
    try:
        with open(SCORES_FILE_NAME, 'r+') as scores_file:
            score = scores_file.read()

        return f"""
        <html>
            <head>
                <title>Scores Game</title>
                <style>
                    body {{
                        font-family: Arial, sans-serif;
                        background-color: #f4f4f4;
                        display: flex;
                        flex-direction: column;
                        align-items: center;
                        justify-content: center;
                        height: 100vh;
                        margin: 0;
                    }}
                    h1 {{
                        color: #333;
                    }}
                    #score {{
                        font-size: 2em;
                        color: #4CAF50;
                        margin-top: 20px;
                        padding: 10px 20px;
                        border: 2px solid #4CAF50;
                        border-radius: 10px;
                        background-color: #e7f7e7;
                    }}
                    .container {{
                        text-align: center;
                        background: #fff;
                        padding: 20px;
                        border-radius: 10px;
                        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                    }}
                </style>
            </head>
            <body>
                <div class="container">
                    <h1>The score is:</h1>
                    <div id="score">{score}</div>
                </div>
            </body>
        </html>
        """
    except Exception as e:
        return f"""
        <html>
            <head>
                <title>Scores Game</title>
                <style>
                    body {{
                        font-family: Arial, sans-serif;
                        background-color: #f4f4f4;
                        display: flex;
                        flex-direction: column;
                        align-items: center;
                        justify-content: center;
                        height: 100vh;
                        margin: 0;
                    }}
                    h1 {{
                        color: #333;
                    }}
                    #score {{
                        font-size: 2em;
                        color: #FF6347;
                        margin-top: 20px;
                        padding: 10px 20px;
                        border: 2px solid #FF6347;
                        border-radius: 10px;
                        background-color: #ffecec;
                    }}
                    .container {{
                        text-align: center;
                        background: #fff;
                        padding: 20px;
                        border-radius: 10px;
                        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                    }}
                </style>
            </head>
            <body>
                <div class="container">
                    <h1>ERROR:</h1>
                    <div id="score">{BAD_RETURN_CODE}</div>
                </div>
            </body>
        </html>
        """


app.run(host='0.0.0.0')
