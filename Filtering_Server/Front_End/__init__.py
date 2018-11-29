from flask import Blueprint, request
from Filtering_Server.Front_End.Controllers import index_controller, filtering_controller
Front_End = Blueprint('front_end', __name__, static_folder='static', template_folder='Templates')

@Front_End.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        return index_controller.post_index()
    else:
        return index_controller.get_index()

@Front_End.route('/result', methods=['POST'])
def result():
    return filtering_controller.filter_view()
