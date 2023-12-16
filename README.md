# Milestone Project Three - Macs Cookbook
# User Stories
## Site ownership goals
The site was created for a fictional owner who requires a cookbook app for users to log in and share recipes for a community culinary experience.
## Visitor/User Goals
### Logged in user goals
### Logged out user goals
### Logged in admin goals
# Features
## Site wide
The implementation of a global navbar and footer to make a uniform user experience has been completed site wide
## Pre Login
The user experience is limited to only 2 pages before logging in, from here they can navigate to the login page or sign up page
## Home Page
On the home page, users can take the opportunity to view both their own created recipes, and also the communities additions to the site, the CRUD functionality on the home page is read only by design to ensure that the recipes of other users are protected and cannot be edited or deleted.
## Account Page
In the account page the user is presented with a collapsible set of forms offering multiple functionalities
### Change Password
The user can opt to change the password in the database by supplying the app with the old password and the new request to take its place, the user is once again given a modal to confirm and guard against accidental changes.
### Change email
In the email section of the page the user is presented with the current email address linked to the account for reference, they are given the option to change to a new email via a form and presented with a modal to confirm the selection and submit to the database.
### Delete account
The user is provided with an option to remove the account from the database after supplying the form with the email associated to their own account, the function queries the email provided with the current session user to prevent and foul play and only allow for the deletion of the logged in account.
## Recipes Page
In the recipes page, the user is able to view all recipe submissions made by themselves with the option to update the recipes and also to delete them.

Upon clicking the edit button, the user is directed to a prefilled form referencing all of the recipes current values, allowing the user to change whatever is neccessary and resubmit the form back to the database to be updated.

To ensure no accidental deletions of the recipes, a modal has been implemented requiring the user to confirm the attempt before the recipe is removed from the database
## Admin Features
## Features left to implement
## Error Pages
## CRUD Functions
### Create
Sign In function

Create recipe function
### Read
Reads database to filter all recipes to home page

Reads database to filter current user recipe to recipes page

Reads database to filter first name to replace "Mac's Cookbook' in title

Reads database to supply email in account page

Verifies old email, password and current email before allowing changes on account page
### Update
User can update recipes that is associated with thier account

The user can change email addresses for the account if neccessary in the database

The user can update the account password via the account page

### Delete
The user has the option to remove/delete recipes from their account and the database

The user can delete the account from the website permanently

# Wireframes
## Login
## Sign Up
## Home
## Account

# Entity Relationship Diagram & Flow Chart
# Testing
## Wave testing
## Lighthouse Testing
## Functional Testing
### Bugs

# Technologies Utilised
## HTML
HTML5 Was used to create the front end skeleton of the website, semantic HTML in the form of Head, Nav, Main and Footer tags were used to create appropriate structure.
## CSS
Custom CSS styles were utilised to resize and reposition some elements on the site in order to maximise the user experience.
### Materialize Framework
The Materialize Framework was used in order to allow for easy to put together structures and fast styles to create a better user experience for the user.
## JavaScript/JQuery
### Materialize Framework
The Materialize Framework was also used in the form of JQuery to initialize some of the components used from the framework such as carousels and collapsible menus
## Python
### Flask Framework
The Flask Framework was used to create and initialise the app in order to run the server and to navigate through the site using routing and login functionality.
### Jinja Templating
Jinja Templating was used alongside Flask modules in order to create Python implementation in the html files rendered by the app
## External utility
### Font Awesome
Font Awesome was used to generate icons for the website and to style the links in a more reader friendly fashion
### Favicon
A Favicon was generated to display a recognisable icon in the browser tab in order to be more user friendly on the front end

# Deployment
## GitHub version control
## Deployment to Heroku

# Credits / Acknowledgements
## Books
During the creation of this site I used the book "Building Web Apps with Python and Flask" by Malhar Lathkar for help troubleshooting and general tips on creating the site

Site made for educational purposes only for assessment by Code Institute
