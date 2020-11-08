from flask import Flask,request,render_template 

app=Flask(__name__)                             #Setting our flask name 

@app.route("/")
def introduce():                                
    from .data.about import bot                             #importing data from the about.py
    return render_template("index.html",data=bot)           #rendering index.html template as response


@app.route("/message",methods=['POST'])
def usermessage():
    if request.method == "POST":                            #If the request method is post we execute handle method from intents.py
        from .intents import handle
        return handle(request.form)
    else:
        return "INVALID"
    
if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.main(threaded=True, port=5000)
   