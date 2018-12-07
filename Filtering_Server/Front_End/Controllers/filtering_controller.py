from flask import url_for, request, current_app, send_from_directory
from Filtering_Server.Filtering import Filtering
import numpy as np
import os
import cv2
app = current_app

def filter_view():
    path = os.path.join(app.config['FOO'],request.form['image_file'])
    img = cv2.imread(path,0)
    name = request.form['filter']
    cutoff = np.int(request.form['cutoff_value'])
    implementation = request.form['fftImplemntation']
    f = Filtering(img, name, cutoff, implementation=implementation)
    f.apply_filter()
    filename = 'post_image_' + name + str(f.id) +  '.png'
    post_image = f.filter_image
    cv2.imwrite(os.path.join(app.config['UPLOAD_FOLDER'], filename), post_image)
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)
