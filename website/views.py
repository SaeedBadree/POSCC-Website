from flask import Blueprint, render_template, url_for
from flask_login import login_required, current_user

views = Blueprint('views', __name__)

@views.route('/')
#@login_required
def home():
    return render_template('index.html', user=current_user)

@views.route('/about')
def about():
    return render_template('about.html')

@views.route('/services')
def services():
    return render_template('services.html')

@views.route('/departments')
def departments():
    return render_template('departments.html')

@views.route('/council')
def meet_the_council():
    councillors = [
        {
            'name': 'Neubun Clarke',
            'ward': 'Ward 1',
            'image': 'Neubun_Clarke.jpeg',
            'description': 'John Doe has been a dedicated councillor for Ward 1 since 2015. His work focuses on improving local infrastructure and community programs...'
        },
        {
            'name': 'Jane Smith',
            'ward': 'Ward 2',
            'image': 'jane_smith.jpg',
            'description': 'Jane Smith has been a strong advocate for environmental sustainability and public health in Ward 2...'
        },
        {
            'name': 'Robert Johnson',
            'ward': 'Ward 3',
            'image': 'robert_johnson.jpg',
            'description': 'Robert Johnson is known for his work on youth development and educational initiatives in Ward 3...'
        },
        # Add more sample councillors as needed
    ]
    return render_template('council.html', councillors=councillors)

@views.route('/projects')
def projects():
    return render_template('projects.html')

@views.route('/contact')
def contact():
    return render_template('contact.html')

@views.route('/help')
def help():
    return render_template('help.html')

@views.route('/geospatial')
def geospatial():
    return render_template('geospatial.html')

@views.route('/procurement')
def procurement():
    pdf_url = url_for('static', filename='files/AnnualProcurement.pdf')
    return render_template('procurement.html', pdf_url=pdf_url)
