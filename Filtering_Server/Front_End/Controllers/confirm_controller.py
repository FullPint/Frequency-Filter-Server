from flask import render_template

def get_confirm(image, filter, implementation):
        return render_template('filter_confirm.html',
                                image = image,
                                implementation=implementation,
                                filter=filter)
