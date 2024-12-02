from flask import Blueprint, render_template, url_for, request, jsonify
from flask_login import login_required, current_user
from .forms import ChangeOwnershipForm, RemoveOwnershipForm, IncludeOwnershipForm, TransferAllotmentForm
from .models import db, ChangeOwnershipFormModel  
from flask import flash, redirect, url_for, render_template, request

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


@views.route('/cityAdmin', methods=['GET', 'POST'])
def cityAdmin():
    change_ownership_form = ChangeOwnershipForm()
    remove_ownership_form = RemoveOwnershipForm()
    include_ownership_form = IncludeOwnershipForm()
    transfer_allotment_form = TransferAllotmentForm()

    return render_template(
        'cityAdmin.html',
        change_ownership_form=change_ownership_form,
        remove_ownership_form=remove_ownership_form,
        include_ownership_form=include_ownership_form,
        transfer_allotment_form=transfer_allotment_form,
    )
    
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

@views.route('/maintenance')
def maintenance():
    return render_template('maintenance.html')

@views.route('/news')
def news():
    return render_template('news.html')

@views.route('/treasurers')
def treasurers():
    return render_template('treasurers.html')

@views.route('/propertyManagement')
def propertyManagement():
    return render_template('propertyManagement.html')


@views.route('/submit_change_ownership', methods=['GET', 'POST'])
def submit_change_ownership():
    form = ChangeOwnershipForm()
    if form.validate_on_submit():  # This ensures the form is valid
        # Save data to the database
        new_entry = ChangeOwnershipFormModel(
            date=form.date.data,
            cemetery=form.cemetery.data,
            block_number=form.block_number.data,
            grave_space=form.grave_space.data,
            owner_details=form.owner_details.data,
            contact_number=form.contact_number.data,
            name_1=form.name_1.data,
            address_1=form.address_1.data,
            signature_1=form.signature_1.data,
            id_number_1=form.id_number_1.data,
        )
        db.session.add(new_entry)
        db.session.commit()

        flash('Form submitted successfully!', 'success')
        return redirect(url_for('views.cityAdmin'))

    return render_template('cityAdmin.html', form=form)



@views.route('/submit_remove_ownership', methods=['GET', 'POST'])
def submit_remove_ownership():
    form = RemoveOwnershipForm()
    if form.validate_on_submit():
        # Process form data here, e.g., save to the database
        flash('Remove Ownership form submitted successfully!', 'success')
        return redirect(url_for('views.cityAdmin'))
    return render_template('cityAdmin.html', remove_ownership_form=form)

@views.route('/submit_include_ownership', methods=['GET', 'POST'])
def submit_include_ownership():
    form = IncludeOwnershipForm()
    if form.validate_on_submit():
        # Process form data here, e.g., save to the database
        flash('Include Ownership form submitted successfully!', 'success')
        return redirect(url_for('views.cityAdmin'))
    return render_template('cityAdmin.html', include_ownership_form=form)

@views.route('/submit_transfer_allotment', methods=['GET', 'POST'])
def submit_transfer_allotment():
    form = TransferAllotmentForm()
    if form.validate_on_submit():
        # Process form data here, e.g., save to the database
        flash('Transfer Allotment form submitted successfully!', 'success')
        return redirect(url_for('views.cityAdmin'))
    return render_template('cityAdmin.html', transfer_allotment_form=form)


