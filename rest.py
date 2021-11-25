from flask import Flask,render_template,request

app=Flask(__name__)

github_user_name=['jai','deep','movva','chowdary']
@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/about', methods=["GET","POST"])
def about_page():
    query=request.form.get("query")
    return render_template('about.html',var=query)

@app.route('/about/zeel')
def norm_page():
    return "Excess document is processed"

@app.route('/<name>')
def user_page(name):
    # if name in github_user_name:
    #     return "hello {}".format(name)
    # else:
    #     return 'go away'
    return render_template('greet.html',var=name)
if __name__=='__main__':
    app.run(debug=True)