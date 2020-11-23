from flask import render_template, abort
from flask_login import login_required

from . import home
from . checkAdmin import check_admin

@home.route("/")
def homepage():
    return render_template('home/index.html', title="Welcome")
    
@home.route("/dashboard")
@login_required
def dashboard():
    return render_template('home/dashboard.html', title="Dashboard")


from flask import render_template, abort
from flask_login import current_user, login_required


@home.route('/admin/dasboard')
#@login_required
def admin_dashboard():
    check_admin()
    return render_template('home/admin_dashboard.html', title="Dashboard")