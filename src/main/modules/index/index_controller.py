from flask import Blueprint, render_template, g, current_app, request, jsonify, flash
from flask_login import current_user

# defining controller
# the static_url_path='home/static' means: this route has registered with url_prefix='/',
# so we need to add an alias name (will be displayed on the Browser's url bar)
# the alias 'home' here to prevent conflicting resource between the main app vs this route
indx = Blueprint('index', __name__, template_folder='templates', static_folder='static', static_url_path='home/static')


@indx.route("/", methods=["GET"])
def index():
    tasks = []

    if current_user.is_authenticated:
        from src.main.modules.task.task_model import Task
        print(current_user)
        tasks = Task.query.filter_by(user_id=current_user.email)
        print(tasks)

    return render_template('index.html', tasks=tasks)
