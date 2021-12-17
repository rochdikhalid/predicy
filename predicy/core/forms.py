from flask_wtf import FlaskForm
from wtforms import FloatField, SelectField, SubmitField
from wtforms.validators import DataRequired
from core.config import getNumOfBathrooms, getNumOfBedrooms, getLocations



# Set entries variables
furnitureChoices = ['Furnished', 'Semi-furnished', 'Unfurnished']
transactionChoices = ['New property','Resale']
numOfBedrooms = getNumOfBedrooms()
numOfBathrooms = getNumOfBathrooms()
locality_choices = getLocations()

# Creating multiple forms to add entries
class FillToPredictForm(FlaskForm):
    # Area form
    area = FloatField('Define Area (Sf)', validators = [DataRequired()], description = 'Area (sf)')
    # Bedroom form
    bedroom = SelectField('Number of Bedrooms', validators = [DataRequired()], description = 'Bedroom', choices = numOfBedrooms)
    # Bathroom form
    bathroom = SelectField('Number of Bathroom', validators = [DataRequired()], description = 'Bathroom', choices = numOfBathrooms)
    # Furnishing form
    furnishing = SelectField('Select Furnishing', validators = [DataRequired()], choices = furnitureChoices, description = 'Furnishing')
    # Transaction form
    transaction = SelectField('Transaction Type', validators = [DataRequired()], choices = transactionChoices, description = 'Transaction')
    # Locality form
    locality = SelectField('Choose Locality', validators = [DataRequired()], choices = locality_choices, description = 'Locality')
    # Predict form
    predict = SubmitField('Predict Price')
    # Predict form
    v_predicted = SubmitField('Predict Price')

    