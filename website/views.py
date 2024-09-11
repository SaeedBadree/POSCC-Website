from flask import Blueprint, render_template, url_for, request, jsonify
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


@views.route('/contact')
def contact():
    return render_template('contact.html')



@views.route('/geospatial')
def geospatial():
    return render_template('geospatial.html')

@views.route('/procurement')
def procurement():
    pdf_url = url_for('static', filename='files/AnnualProcurement.pdf')
    return render_template('procurement.html', pdf_url=pdf_url)


@views.route('/projects')
def projects():
    current_projects = [
        {
            'id': '1',
            'title': 'Road Improvement Project',
            'image': 'images/road_improvement.jpg',
            'description': 'This project involves the improvement of major roads...'
        },
        {
            'id': '2',
            'title': 'New Community Center',
            'image': 'images/community_center.jpg',
            'description': 'A new community center is being built...'
        }
    ]

    completed_projects = [
        {
            'id': '3',
            'title': 'City Park Renovation',
            'image': 'images/city_park.jpg',
            'description': 'The city park renovation was completed...'
        },
        {
            'id': '4',
            'title': 'Downtown Cleanup',
            'image': 'images/downtown_cleanup.jpg',
            'description': 'A major cleanup initiative was successfully...'
        }
    ]

    return render_template('projects.html', current_projects=current_projects, completed_projects=completed_projects)


@views.route('/help')
def help():
    return render_template('help.html')


@views.route('/chatbot', methods=['POST'])
def chatbot():
    user_message = request.json.get('message')
    
    # Simple logic to respond to specific questions
    if "hours" in user_message.lower():
        response = "The Port of Spain City Corporation is open from 8am to 4pm, Monday to Friday."
    elif "building permit" in user_message.lower():
        response = "You can apply for a building permit through our online portal or by visiting the Building Inspectorate office."
    elif "property taxes" in user_message.lower():
        response = "Property taxes can be paid at the Finance Department or through our online payment system."
    else:
        response = "Thank you for your message. We will get back to you shortly."
    
    return jsonify({"response": response})


@views.route('/cityAdmin')
def cityAdmin():
    return render_template('cityAdmin.html')

@views.route('/cityEngineering')
def cityEngineering():
    return render_template('cityEngineering.html')

@views.route('/cityPolice')
def cityPolice():
    return render_template('cityPolice.html')

@views.route('/publicHealth')
def publicHealth():
    return render_template('publicHealth.html')

@views.route('/led')
def led():
    return render_template('led.html')

@views.route('/disasterManagement')
def disasterManagement():
    return render_template('disasterManagement.html')

@views.route('/cityAssessors')
def cityAssessors():
    return render_template('cityAssessors.html')

@views.route('/market')
def market():
    return render_template('market.html')