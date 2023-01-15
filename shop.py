from app import app, db, User


if __name__ == '__main__':
    app.run()

# @app.shell_context_processor
# def make_context_processor():
#     return {'db': db, 'Udbser': User}