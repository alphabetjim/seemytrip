## Functional Testing


## Validator Testing
All pages were run through the [HTML Validator](https://validator.w3.org/#validate_by_input). This had to be done using the direct input method due to the presence of Django template tags within the html files, by pasting in the HTML shown by right-clicking and selecting "inspect source".

After resolving some simple unclosed script tag errors and fixing the approach used to implement trip comment update and delete functionality, which had initially used a button 'type' attribute, almost all pages passed showing no errors. 

The only exceptions to these were those used to edit instances of the Trip, Traveller and TripDay models. These failed due to the crispy forms package adding a 'type' attribute to textareas displayed in the form for models.CharField fields, and are outside of developer control.

![HTML Validator Pass](docs/testing/html%20validation%20home.png)
![HTML Validator fail on crispy-generated attribute](docs/testing/editprofile_crispyFailHtml.png)