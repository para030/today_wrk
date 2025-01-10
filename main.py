from flask import Flask ,render_template,request,redirect
from fun import*
app=Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def data1():
   if request.method=="POST":
      print(request.form["name"],request.form["age"],request.form["course"],request.form["address"])
      stud_reg(request.form["name"],request.form["age"],request.form["course"],request.form["address"])
      # data=read_json()
      # return render_template("new.html",stud_data=data["students"])
   data=read_json()
   return render_template("new.html",stud_data=data["students"])

@app.route("/delete/<id>")
def del_stud(id):
   delete_stud(id)
   return redirect("/")

@app.route("/update/<id>", methods=["POST", "GET"])
def up_stud(id):
   if request.method=="POST":
      update_stud(id,request.form["name"],request.form["age"],request.form["course"],request.form["address"])
   return redirect("/")
   
if __name__=="__main__":
    app.run(debug=True)


