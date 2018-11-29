from flask import render_template, request
from Filtering_Server.Front_End.Controllers import upload_controller

def get_index():
    return render_template('index.html')

def post_index():
    img_url = "Images/" + upload_controller.upload_file()
    implementation = str(request.form['fftImplemntation'])
    filter = str(request.form['filter'])
    return render_template('filter_confirm.html',
    image = img_url, implementation=implementation, filter=filter)
