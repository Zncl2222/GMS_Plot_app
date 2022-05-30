import os
from flask import Flask, request, redirect, url_for, render_template, send_file
from werkzeug.utils import secure_filename
from flask import send_from_directory
from model.markovchain_plot import GMS_Plot

UPLOAD_FOLDER = './static/data'
ALLOWED_DATATYPE = set(['txt'])
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_SIZE'] = 1024 * 1024


def allowed_file(filename):
    return '.' in filename and filename.split('.', 1)[1] in ALLOWED_DATATYPE

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/upload', methods=['GET','POST'])
def upload_file():
    
    origin_file = os.listdir('./static/data')
    for item in origin_file:
        os.remove('./static/data/'+item)

    if request.method == 'POST':
        uploaded_files = request.files.getlist("files")
        filenames=[]
    
    for item in uploaded_files:

        if item and allowed_file(item.filename):
            filename = secure_filename(item.filename)
            item.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
            filenames.append(filename)

    return render_template("home.html")

@app.route('/plot', methods=['GET','POST'])
def Plot():
    a = os.listdir('./static/data/')
    gms_plot = GMS_Plot()
    param_dict = request.form.to_dict()
    x_ratio = int(param_dict['x_ratio'])
    
    if len(a) == 4:
    
        x = gms_plot.ReadData2()

        gms_plot.Subplot2(x, x_ratio)

    elif len(a) == 9:

        x = gms_plot.ReadData2()

        gms_plot.Subplot3(x, x_ratio)
        
    elif len(a) == 16:
        print("len16")
        x = gms_plot.ReadData2()

        gms_plot.Subplot4(x, x_ratio)

    return render_template("home.html", img = a)

@app.route('/download')
def download():
    path = './static/images/GMSPlot.png'
    return send_file(path, as_attachment=True)

@app.route('/upload/<filename>')
def uploaded_file(filename):
    return send_from_directory('./static/data',filename)


if __name__ == '__main__':
    app.run(debug=True)