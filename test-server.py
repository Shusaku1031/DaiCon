from flask import Flask, request, abort, Markup
import subprocess
import os

app = Flask(__name__)

@app.route("/")
def home():
    html = """
    <form action="/controller">
        <label>Controll target: </label>
        <input type="text" name="query">
        <button type="submit" formmethod="post">Send signal</button>
    </form>
    <form action="/register">
        <label>Regist target: </label>
        <input type="text" name="query">
        <button type="submit" formmethod="post">Regist signal</button>
    </form>
    """
    
    return Markup(html)
    

@app.route("/controller",methods=["GET","POST"])
def controller():
    
    #if request.method == "GET":
    #    return request.args.get("query","")
    if request.method == "POST":
        if os.path.exists("irmcli/"+request.form["query"]+".json"):
            print(subprocess.run(["python","irmcli/irmcli.py","-p","-f","irmcli/"+request.form["query"]+".json"]))
            return """
                <h1>You sent {} signal.</h1>
                <form action="/controller">
                    <label>Controll target: </label>
                    <input type="text" name="query">
                    <button type="submit" formmethod="post">Send signal</button>
                </form>
                <button><a href="/">Return to main page</a></button>
                """.format(request.form["query"])
        else:
            return """
                    <h1>Failed...</h1>
                    <h2>You can retry to sent signal</h2>
                    <form action="/controller">
                        <label>Controll target: </label>
                        <input type="text" name="query">
                        <button type="submit" formmethod="post">Send signal</button>
                    </form>
                    <form action="/">
                        <button>Return to main page</button>
                    </form>
                    """
    else:
        abort(400)
    
    

@app.route("/register",methods=["GET","POST"])
def register():
    
    if request.method == "POST":
        
        result = subprocess.run(["python","irmcli/irmcli.py","-c","-f","irmcli/"+request.form["query"]+".json"])
        if result.returncode == 0 and os.path.exists("irmcli/"+request.form["query"]+".json") == True:
            print("success")
            return """
                <h1>Success({}.json)</h1>
                <form action="/">
                    <button>Return to main page</button>
                </form>
                """.format(request.form["query"])
        
        else:
             print("failed")
             return """
                <h1>Failed({}.json)</h1>
                <p>you can retry to register signal</p>
                <form action="/register">
                    <label>Regist target: </label>
                    <input type="text" name="query">
                    <button type="submit" formmethod="post">Regist signal</button>
                </form>
                <form action="/">
                    <button>Return to main page<
                    /button>
                </form>
                """.format(request.form["query"])
             
    else:
        return """
            <p>None</p>
            <form action="/">
                        <button>Return</button>
            </form>
            """


if __name__ == "__main__":
    app.run(debug=True)