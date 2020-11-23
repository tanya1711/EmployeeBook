from flask_login import login_required, current_user
from flask import abort
from app import db
from .. models import Department, Employee, Role


def check_admin():
    """
    user = Employee.query.filter_by(id = current_user.id).first()
    admin_email = 'admin@admin.com' 
    if user['email'] is not admin_email:
        abort(403)
        print('Not Admin')
    print('Admin')
    """
    if not current_user.is_admin:
        abort(403)