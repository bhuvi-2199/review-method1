from flask import Flask, render_template, request

app = Flask(__name__)
@app.route('/', methods=["GET","POST"])
def main():
    if request.method == "POST": 
        a=int(request.form.get("a"))
        b=int(request.form.get("b"))
        if (request.form.get("add")):
            x = a+b 
        elif (request.form.get("sub")):
            x = a-b
        elif (request.form.get("mult")):
            x = a*b
        elif (request.form.get("div")):
            x = a/b
        elif (request.form.get("mod")):
            x = a%b
        else:
            x = 'Invalid operation'
        return render_template("index.html",ans=x,a=a,b=b)
    else:
        return render_template("index.html",ans='')
if __name__ == '__main__':
   app.run(debug = True)
   