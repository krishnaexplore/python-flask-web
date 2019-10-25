from app.controller import getTodos

def test_getTodos(app):
    with app.app_context():
        list1 = getTodos()