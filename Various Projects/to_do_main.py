from flask import request, jsonify, Flask, abort
import json

app = Flask(__name__)

FILE_PATH = "C:/Users/Asus/PycharmProjects/pythonProject3/todolist.json"

def get_todo_repo_from_file():
    with open(FILE_PATH, mode="r", encoding="UTF-8") as file:
        todo_repo = json.load(file)
        return todo_repo


def write_todo_repo_to_file(todo_repo):
    with open(FILE_PATH, mode="w", encoding="UTF-8") as file:
        json.dump(todo_repo, file)

@app.route('/', methods=['GET'])
def home():
    return "Hello world"

@app.route('/lists', methods=['GET'])
def get_lists():
    return str(get_todo_repo_from_file()["lists"])

@app.route('/create_list/<name>', methods=['POST'])
def create_list(name):
    todo_repo = get_todo_repo_from_file()
    new_list = {"name": name, "todos": []}
    todo_repo["lists"].append(new_list)
    write_todo_repo_to_file(todo_repo)
    return str([list["name"] for list in todo_repo["lists"]])

@app.route('/<list_name>/add_todos/', methods=['POST'])
def add_todo_to_list(list_name):
    request_body = request.json
    new_todos = request_body["todos"]
    todo_repo = get_todo_repo_from_file()
    lists = todo_repo["lists"]
    for list in lists:
        if list["name"] == list_name:
            list["todos"] += new_todos
    write_todo_repo_to_file(todo_repo)
    return "OK"

@app.route('/<list_name>/get_todos/', methods=['GET'])
def get_todos_in_list_name(list_name):
    todo_repo = get_todo_repo_from_file()
    lists = todo_repo["lists"]
    for list in lists:
        if list["name"].upper() == list_name.upper():
            return {"todos": list["todos"]}
    abort(404)

#Delete method


app.run()