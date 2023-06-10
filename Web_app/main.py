from flask import Flask,render_template,redirect,url_for,request
from Search_Engine.driver import search_execute

app = Flask(__name__,static_folder = "static", static_url_path='')



@app.route('/')
def home():
    return render_template('index.html')


@app.route('/query_result', methods =["GET", "POST"])
def query_result():
    if request.method == "POST":
       question = request.form.get("search")
       api_key = request.form.get("API_KEY")
       res = search_execute(api_key=api_key,question=question)
       
       return render_template('output.html',res=res,question=question)
    return render_template("index.html")




if __name__ == '__main__':
    app.run()
