from flask import Blueprint, render_template, redirect, url_for, flash
from app.forms import DesignRequestForm
from app.models import DesignSuggestion
from app import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/about')
def about():
    return render_template('about.html')

@main.route('/contact', methods=['GET', 'POST'])
def contact():
    form = DesignRequestForm()
    if form.validate_on_submit():
        suggestion = generate_suggestion(form.room_type.data, form.style_preference.data)
        new_suggestion = DesignSuggestion(customer_name=form.customer_name.data, customer_email=form.customer_email.data,
                                          room_type=form.room_type.data, style_preference=form.style_preference.data,
                                          suggestion=suggestion)
        db.session.add(new_suggestion)
        db.session.commit()
        flash('Your design suggestion has been created!', 'success')
        return redirect(url_for('main.contact'))
    return render_template('contact.html', form=form)

@main.route('/features')
def features():
    return render_template('features.html')

@main.route('/suggestions')
def suggestions():
    suggestions = DesignSuggestion.query.all()
    return render_template('suggestions.html', suggestions=suggestions)

def generate_suggestion(room_type, style_preference):
    # Placeholder function - replace with your logic for generating suggestions
    return f"Suggestion for a {style_preference} {room_type}"
