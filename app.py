import psutil
from flask import Flask,render_template

app= Flask(__name__,template_folder="Templates")





@app.route("/")
def index():
    cpu_memory=psutil.cpu_percent()
    memory_percent=psutil.virtual_memory().percent
    Message=None
    if cpu_memory>80 or memory_percent>80:
        Message="CPU or Memory Ussage is more"
        
    return render_template("index.html",cpu_metric=cpu_memory,mem_metric=memory_percent,message=Message)
if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0')