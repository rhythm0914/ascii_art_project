from flask import Flask, render_template
from pyfiglet import Figlet

app = Flask(__name__)

@app.route('/')
def index():
    # Define colors (will be used for terminal, not for web)
    blue = '\033[34m'
    reset = '\033[0m'

    # Generate ASCII art
    figlet = Figlet(font='small')
    text = "RYAN JOSEPH"
    ascii_art = figlet.renderText(text)
    
    # Note: Colors won't be rendered in HTML; only ASCII art is passed to the template.
    ascii_art_html = f"<pre style='color: blue;'>{ascii_art}</pre>"

    return render_template('index.html', ascii_art=ascii_art_html)

if __name__ == "__main__":
    app.run(debug=True)
