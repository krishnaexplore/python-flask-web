from flask import Flask, jsonify, request

from app.service import TodoService
from app.model import Todo
import jsons

app = Flask(__name__)


todoservice = TodoService()

@app.route('/todos', methods=['GET'])
def getTodos():
    
    values = todoservice.getTodos()
    jsonValues = jsons.dump(values)
    return jsonify({ 'items': jsonValues})

@app.route('/todos/', methods=['POST'])
def todos():
    todoId = todoservice.getnext()
    todo = Todo(todoId, request.json.get('title'), request.json.get('done'))
    todoservice.addTodo(todo)
    todoMap = {'id':todo.id,'title':todo.titile,'done':todo.done}
    response = jsonify(todoMap)
    return response

@app.route('/todos/<int:id>', methods=['PUT'])
def updateTodo(id):
    
    todo = Todo(id, request.json.get('title'), request.json.get('done'))
    todoservice.update(todo)
    jsonTodo = jsons.dump(todo)
    response = jsonify(jsonTodo)
    return response

@app.route('/todos/<int:id>', methods=['DELETE'])
def deleteTodo(id):
    
    todoservice.deleteTodo(id)
    return 'no content'