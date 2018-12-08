from flask import url_for, request, current_app, send_from_directory, render_template
from Filtering_Server.Filtering import Filtering
import numpy as np
import os
import cv2
app = current_app

def filter_view():
    f = filter()
    filter_image = 'post_image_' + f.filter_name + str(f.id) +  '.png'
    cv2.imwrite(os.path.join(app.config['UPLOAD_FOLDER'], filter_image), f.filter_image)
    filter_image = 'Images/' + filter_image
    freq_image = 'freq_image_' + f.filter_name + str(f.id) + '.png'
    cv2.imwrite(os.path.join(app.config['UPLOAD_FOLDER'], freq_image), f.filter_freq_image)
    freq_image = 'Images/' + freq_image
    return render_template('filter_complete.html',
                            filter_name = f.filter_name,
                            filter_image = filter_image,
                            freq_image  = freq_image,
                            cutoff = f.cutoff,
                            a_value = f.a_value,
                            order = f.order,
                            width = f.width
                            )
def filter():
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
    return f
