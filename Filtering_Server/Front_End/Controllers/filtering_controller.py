from flask import url_for, request, current_app, send_from_directory
from Filtering_Server.Filtering import Filtering
import numpy as np
import os
import cv2
app = current_app

def filter_view():
    path = os.path.join(app.config['FOO'],request.form.get('image_file'))
    image = cv2.imread(path,0)
    filter_name = request.form.get('filter', 'laplacian_filter')
    cutoff = np.int(request.form.get('cutoff', "0"))
    a_value = np.int(request.form.get('a_value', "0"))
    order = np.int(request.form.get('order', "0"))
    width = np.int(request.form.get('width', "0"))
    implementation = request.form['fftImplemntation']
    f = Filtering(image, filter_name, cutoff, a_value, order, width, implementation)
    f.apply_filter()
    filename = 'post_image_' + filter_name + str(f.id) +  '.png'
    post_image = f.filter_image
    cv2.imwrite(os.path.join(app.config['UPLOAD_FOLDER'], filename), post_image)
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)
