from flask import render_template, request, redirect, url_for
from Filtering_Server.Front_End.Controllers import upload_controller

def get_index():
    return render_template('index.html')

def post_index():
    img_name = str(upload_controller.upload_file())
    filter = str(request.form['filter'])
    implementation = str(request.form['fftImplemntation'])
    return redirect(url_for('front_end.confirm',
                    img_name = img_name,
                    filter = filter,
                    implementation = implementation))
