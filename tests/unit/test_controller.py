from app.controller import getTodos, app
from unittest.mock import patch



@patch('app.service.TodoService')
def test_getTodos(self):
    with app.app_context():
        list1 = getTodos()
    print(list1)
