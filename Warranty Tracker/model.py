from odoo import models, fields

#This is where we make our models
#models are what the app will be able to store
# do models also define what the app will do? I think so
#class name(always import models.Model)
class WarrantyTracker(models.Model):
    #_name is necessary
    _name = "warranty.warranty"
    # The rest are fields that the app can store
    #there are different types of fields.___ for example fields.boolean()
    #Inside the field are certain parameters that are passed 
    #string is what shows up on the website
    #required means it must be filled out
    name = fields.Char(string = 'Name', required = True)
    id_tag = fields.Char(string = 'ID: ', required = True)
    purchase_date = fields.Date(string = 'Date of Purchase', required = True)
    length_of_warranty = field.char(string = 'Warranty Length', required = True)

    """possible attributes of the fields

    """

