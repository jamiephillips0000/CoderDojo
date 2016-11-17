import os
from flask import Flask, render_template, make_response
app = Flask(__name__)


def make_tree(path):

    tree = dict(name=os.path.basename(path), children=[])
    try: lst = os.listdir(path)
    except OSError:
        pass #ignore errors
    else:
        for name in lst:
            fn = os.path.join(path, name)
            if os.path.isdir(fn):
                tree['children'].append(make_tree(fn))
            else:
                tree['children'].append(dict(name=name))
    return tree



@app.route('/')
def dirtree():
    # path = os.path.expanduser('/home/jamie/')
    path = __file__#'/home/jamie/'
    idx = path.rindex("/")
    path = path[0:idx] + "/files"
    return render_template('dirtree.html', tree=make_tree(path))

@app.route('/files/<path:path>')
def static_file(path):
    pwd = "/home/jamie/git/CODE/PYTHON/FlaskCoderDojo/files/"
    with open(pwd + path , mode="r,b") as file:
        filecontent = file.read()
    response = make_response(filecontent)

    mime = ""

    if path.find("jpg"):
        mime = 'image/jpg'
    elif path.find("mp4"):
        mime = 'video/mp4'
    response.mimetype = mime
    return response
    # return app.send_static_file("jamie.html")



if __name__=="__main__":
    app.run(host='localhost', port=8888, debug=True,  template_folder='templates', static_url_path='/home/jamie/')

# @app.route("/")
# def hello():
#     return "Hello World!"
#
# if __name__ == "__main__":
#     app.run()
