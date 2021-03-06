from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from .. models import Department, Role

class DepartmentForm(FlaskForm):
    name = StringField("Department Name", validators=[DataRequired("Please enter a deparment name")])
    description = StringField("Description", validators=[DataRequired("Please enter a description")])
    submit = SubmitField("submit")


class RoleForm(FlaskForm):
    name = StringField("Role Name", validators=[DataRequired("Please enter a role")])
    description = StringField("Description", validators=[DataRequired("Please enter description")])
    submit = SubmitField("submit")

class EmployeeAssignmentForm(FlaskForm):
    department = QuerySelectField(query_factory=lambda: Department.query.all(),
                            get_label="name")
    role = QuerySelectField(query_factory=lambda: Role.query.all(),
                            get_label="name")
    submit = SubmitField("Submit")
    