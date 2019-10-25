class TodoService:

    def __init__(self):
        self.todos = []
        self.seq = 0

    def getnext(self):
        self.seq = self.seq + 1
        return self.seq

    def addTodo(self, todo):
        self.todos.append(todo)

    def getTodos(self):
        return self.todos
    
    def update(self, todo):
        for x in self.todos:
            if x.id == todo.id:
               self.todos.remove(x)

        self.todos.append(todo)

    def deleteTodo(self, id):
        for x in self.todos:
            if x.id == id:
                self.todos.remove(x)