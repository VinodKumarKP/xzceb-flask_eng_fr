from machinetranslation import translator
from flask import Flask, render_template, request
import json
from machinetranslation.translator import french_to_english, english_to_french

app = Flask("Web Translator")


@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    french_text = english_to_french(textToTranslate)
    return french_text


@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    english_text = french_to_english(textToTranslate)
    return english_text


@app.route("/")
def renderIndexPage():
    # Write the code to render template
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
