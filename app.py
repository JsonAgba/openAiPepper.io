from flask import Flask, request, render_template
import subprocess


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        ip = request.form.get('ip')
        run_scripts(ip)
    return render_template('index.html')


def run_scripts(ip):
    commands = [
        ['python', 'startDialogueServer.py'],
        ['python2.7', 'module-SpeechRecongnition.py', '--pip', ip],
        ['python2.7', 'module-startDialogue.py', '--pip', ip]
    ]
    for command in commands:
        subprocess.call(command)


if __name__ == '__main__':
    app.run(debug=True)
