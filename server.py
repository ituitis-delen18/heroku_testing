from bottle import Bottle, request, static_file
from pathlib import Path

listt = []

def index_page():
    for k in request.headers.get("X-Forwarded-For"):
        if k not in [listt[i][0] for i in range(0, len(listt))]:
            listt.append([k, 0])
        else:
            for i in listt:
                if i[0] == k:
                    i[1] += 1
                    break
    ipContent = ""
    for i in listt:
        current_ip_content = """
        <tr>
            <td>%(ipNumber)s</td>
            <td>%(count)s</td>
        </tr>
        """ % {
            "ipNumber": str(i[0]),
            "count": str(i[1])
        }
        ipContent = ipContent + current_ip_content
    return Path("index.html").read_text() % {"ipInformation": ipContent}

def mySkills_page():
    return Path("mySkills.html").read_text()

def contactWithMe_page():
    return Path("contactWithMe.html").read_text()

def myProjects_page():
    return Path("myProjects.html").read_text()

def aboutMe_page():
    return Path("aboutMe.html").read_text()

#for making static repo
def server_static(filename):
    return static_file(filename, root='./static_files')

def create_app():
    app = Bottle()
    app.route("/", "GET", index_page)
    app.route("/myskills", "GET", mySkills_page)
    app.route("/aboutMe", "GET", aboutMe_page)
    app.route("/myProjects", "GET", myProjects_page)
    app.route("/contactwithme", "GET", contactWithMe_page)
    app.route("/static/<filename>", "GET", server_static)
    return app



application = create_app()
application.run(debug = True)
