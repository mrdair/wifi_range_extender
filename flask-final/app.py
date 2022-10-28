from flask import Flask, render_template, request, redirect

app = Flask(__name__)


class Todo:
    def __init__(self, id, content, date_created):
        self.id = id
        self.content = content
        self.date_created = date_created


def get_tasks():
    config = open('/home/pi/flask/config').readlines()
    config = [config[0].strip(), config[1].strip(), config[2].strip(), config[3].strip()]
    return [Todo(1, str(config[0] + '@' + config[1]), 'Wifi'), Todo(2, str(config[2] + '@' + config[3]), 'Hotspot')]


def post_tasks(wifi, hotspot):
    wifi = str(wifi).split('@')
    hotspot = str(hotspot).split('@')
    file = open('/home/pi/flask/config', 'w')
    file.write(wifi[0])
    file.write('\n')
    file.write(wifi[1])
    file.write('\n')
    file.write(hotspot[0])
    file.write('\n')
    file.write(hotspot[1])
    file.close()


@app.route('/', methods=['POST', 'GET'])
def index():
    tasks = get_tasks()
    return render_template('index.html', tasks=tasks)


@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    tasks = get_tasks()
    if id==1:
        task = tasks[0]
    if id==2:
        task = tasks[1]
    if request.method == 'POST':
        task.content = request.form['content']
        if len(str(task.content).split('@'))!=2 or len(str(task.content).split('@')[1])<8:
            return redirect('/')
        try:
            if id == 1:
                post_tasks(task.content, tasks[1].content)
                return redirect('/')
            if id == 2:
                post_tasks(tasks[0].content, task.content)
                return redirect('/')
        except:
            return 'There was an issue updating'

    else:
        return render_template('update.html', task=task)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
    app.run(debug=True)
