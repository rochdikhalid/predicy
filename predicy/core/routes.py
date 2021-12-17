# Dependencies
from core import app
from flask import render_template, request, flash
from core.forms import FillToPredictForm, furnitureChoices, transactionChoices, locality_choices
import pickle



# Home route
@app.route('/', methods = ['GET', 'POST'])
@app.route('/home', methods = ['GET', 'POST'])
def home():
    form = FillToPredictForm()
    # To submit the form
    if form.is_submitted():
        # Open pickle model
        with open("../models/model_0.h5", "rb") as file:
            model = pickle.load(file)
        # Set the trained model
        predicted = model.predict([[
            form.area.data,
            int(form.bedroom.data),
            int(form.bathroom.data),
            furnitureChoices.index(form.furnishing.data),
            locality_choices.index(form.locality.data),
            transactionChoices.index(form.transaction.data)
        ]])
        # Convert the result to string, and round it to two decimals after comma
        value = str(round(predicted[0], 2))
        # To show the result
        if value:
            # Display the predicted price
            flash(f'Predicy predicted this price: {value}$', 'info')
    return render_template('home.html', title = 'Home', form = form)


