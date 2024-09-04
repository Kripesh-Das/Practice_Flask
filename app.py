from flask import Flask,render_template,request,redirect,url_for,jsonify

app = Flask(__name__)

@app.route('/', methods=["GET"])
def Welcome():
    return "<h1>Hello! It's me Kripesh Das</h1>"

@app.route('/index', methods=["GET"])
def Index():
    return "<h2>Hello! Welcome to page 2</h2>"

## VARIABLE METHOD

@app.route('/success/<int:score>', methods=["GET"])
def Success(score):
    return "<h3>Success! Your score is</h3>" + str(score)

@app.route('/fail/<int:score>', methods=["GET"])
def Fail(score):
    return "<h4>Failure! Your score is</h4>" + str(score)

## DIFFERENT TYPES OF METHOD

@app.route('/form', methods=["GET","POST"])
def Form():
    if request.method == "GET":
        return render_template("form.html") # BASIC HTML FILE WITH ONE SENTENCE 
    else:
        maths = float(request.form["maths"])
        science = float(request.form["science"])
        history = float(request.form["history"])
        avg = (maths+science+history)/3
        
        result = ""
        if avg>=50:
            result = "Success"
        else:
            result = "Fail"
        
        return redirect(url_for(result,score=avg))
        ## return render_template("form.html", score = avg) #jinja2 technique

### P O S T M A N    A P I

@app.route("/api", methods = ["POST"])
def calc_sum():
    data = request.get_json()
    a_val = float(dict(data)["a"])
    b_val = float(dict(data)["b"])
    return jsonify(a_val+b_val)
    

if __name__ == '__main__':
    app.run(debug=True)
    
    
# USE KRISH NAIK VIDEO TO WRITE THE HTML SCRIPT FOR GET AND POST METHODS