from app import app



if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT=int(os.environ.get('SERVER_PORT', '5000'))
    except ValueError:
        PORT=5000   
    app.run(HOST, PORT, debug=True)