# Milestone Project Three - Macs Cookbook
# User Stories
## Site ownership goals
The site was created for a fictional owner who requires a cookbook app for users to log in and share recipes for a community culinary experience.
## Visitor/User Goals
### Logged in user goals

As a logged in user, I would like to be able to contribute my own recipes to the site

As a logged in user, I would like to be able to adjust and delete the recipes I have submitted on the website at my own leisure

As a logged in user, I would like the flexibility to change my email and password when I need to

As a logged in user I would like to be able to navigate around the site structure easily and understand the layout of the site instictively

As a logged user, I would like to be able to delete my account if I decide to leave the site at a later date

### Logged out user goals

As a logged out user, I would like to be able to access the register page to create an account and get feedback based on a successful registration

As a logged out user, I would like to be able to sign in and access the site

### Logged in admin goals

As an admin, I would like to be able to grant/remove admin access to trusted users on the site

As an admin, I would like to see which users currently have admin privileges on the site for a clear picture of who has access

# Features
## Site wide
The implementation of a global navbar and footer to make a uniform user experience has been completed site wide
- As a logged in user I would like to be able to navigate around the site structure easily and understand the layout of the site instinctively
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
On the admin page, an admin can add or remove access to admin features using the user email of the account needing the access using a simple form with a checkbox to add/remove privilege

The admin page also allows admins to view other admins on the site for clarity to protect against unwanted or unneccesary access of the privileges.

## Features left to implement
### Forgot Password Form
A feature that can be implemented in the future would be the forgot password form, I would place this at the bottom of the login page and use the following steps to implement the feature.

- Fill email form
- Query database for email
- If it exists, connect to an API to send email and allow the user to change password using the change password function.
## Error Pages
## CRUD Functions
### Create
Sign In function
- As a logged out user, I would like to be able to sign in and access the site
- As a logged out user, I would like to be able to access the register page to create an account and get feedback based on a successful registration

Create recipe function
- As a logged in user, I would like to be able to contribute my own recipes to the site

### Read
Reads database to filter all recipes to home page

Reads database to filter current user recipe to recipes page

Reads database to filter first name to replace "Mac's Cookbook' in title

Reads database to supply email in account page

Verifies old email, password and current email before allowing changes on account page

Admins can view other admin users via the admin page
### Update
User can update recipes that is associated with their account
- As a logged in user, I would like to be able to adjust and delete the recipes I have submitted on the website at my own leisure

The user can change email addresses for the account if neccessary in the database
- As a logged in user, I would like the flexibility to change my email and password when I need t

The user can update the account password via the account page
- As a logged in user, I would like the flexibility to change my email and password when I need to

Toggle admin function
- As an admin, I would like to be able to grant/remove admin access to trusted users on the site

### Delete
The user has the option to remove/delete recipes from their account and the database

The user can delete the account from the website permanently
- As a logged user, I would like to be able to delete my account if I decide to leave the site at a later date

# Wireframes
## Login
Wire frames of the login page were created to provide a positive user experience, offering clear contrasts and large font sizes with minimal clutter

![Login Desktop Wireframe](/cookbook/docs/Wireframes/Desktop/signin-desktop.png "Login Desktop Wireframe")

## Sign Up
The sign up page wireframe was created with the idea of keeping the screen clutter free and easy to read.

![Register Desktop Wireframe](/cookbook/docs/Wireframes/Desktop/signup-desktop.png "Register Desktop Wireframe")

## Home
The home wireframe was designed to allow for a display of community recipes and allow the user to browse freely for inspiration

![Home Desktop Wireframe](/cookbook/docs/Wireframes/Desktop/home-desktop.png "Home Desktop Wireframe")

## Recipes
The recipes page wireframe was designed to show the users recipes in a clear and uncluttered manner offering good contrast ratios and easy to read buttons

![Recipes Desktop Wireframe](/cookbook/docs/Wireframes/Desktop/recipes-desktop.png "Recipes Desktop Wireframe")

## Add a recipe
The add a recipe form was created with the intention of allowing the user to upload recipes in a simple manner providing the necessary information alongside verification of the submission

![Add recipes Desktop Wireframe](/cookbook/docs/Wireframes/Desktop/add-recipe-desktop.png "Add recipes Desktop Wireframe")

## Edit a recipe
The edit page was designed to be clear and concise with one form only. allowing the user to focus on the editing with minimal distractions

![Edit recipes Desktop Wireframe](/cookbook/docs/Wireframes/Desktop/edit-recipe-desktop.png "Edit recipes Desktop Wireframe")

## Account
The account page was designed to be collapsible to allow for minimal screen clutter when filling out forms in the page

![Account Desktop Wireframe](/cookbook/docs/Wireframes/Desktop/account-desktop.png "Account Desktop Wireframe")

## Admin


## Expand Recipe 


# Entity Relationship Diagram & Flow Chart
## ERD Diagram
![ERD Diagram](/cookbook/docs/Diagrams/erd-diagram.png/ "ERD Diagram")

## Flow charts
### Login/Register
![Login flow chart](/cookbook/docs/Diagrams/login-chart.png "Login flow chart")

The login functionality of the site is presented to the user on page load alongside the sign up page in the navigation. The user is restricted to these pages until they are authenticated. If a user signs up to the site they are redirected on successful registration to the login page to continue the use of the site. 

### Delete Account
![Delete account flow chart](/cookbook/docs/Diagrams/delete-account-chart.png "Delete account flow chart")

The functionality regarding deleting an account begins at the account page once the user has logged in, the user must click the collapsible to show the delete account portion of the page and also confirm their intentions to delete by entering the email associated with that account. On form submission the backend queries the database using the current user ID and if the email written in the input field matched the current user email, the account is deleted.

### Email Changed
![Email changed flow chart](/cookbook/docs/Diagrams/email-changed-chart.png "Email changed flow chart")

The email change section of the site starts with displaying the users currently associated email with the site account, it then offers an input field for the user to submit a new email validated by the HTML before offering a modal to confirm the user choice. If the user clicks the modal the database will be queried and if no account is linked with the new email already, it will be assigned to the account. Otherwise feedback will be given to the user regarding the email being used.

### Password Change
![Password change flow chart](/cookbook/docs/Diagrams/password-change-chart.png "Password change flow chart")

The account page offers functionality for a password change to the user, the form required the user to confirm the current account password as verification of the intention to change the account, and also a new password to replace it. The database is then queried and if the current password matches the one in the database storage, it will be replaced by the new password.

### Add Recipe
![Add recipe flow chart](/cookbook/docs/Diagrams/add-recipe-chart.png "Add recipe flow chart")

The add recipe function is a simple form validated by HTML for the user to fill out. On submission of the form the database will commit the recipe to storage and reload the recipes page to show the new recipe as a card with the option to edit and delete.

### Edit Recipe
![Edit recipe flow chart](/cookbook/docs/Diagrams/edit-recipe-chart.png "Edit recipe flow chart")

Similar to the add recipe function the edit recipe uses the same form however targets the recipe ID passed to the function when clicking edit on a recipe card that the user owns. Users can only edit their own recipes.

### Delete Recipe
![Delete recipe flow chart](/cookbook/docs/Diagrams/delete-recipe-chart.png "Delete recipe flow chart")

The delete recipe function, much like the edit recipe is only available via the your recipes page and can only be used on a recipe that is owned by the current user, the function also has a modal to confirm deletion to prevent accidental deletes.

### Admin Toggle

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

The site was created using the template provided by code institute regarding milestone project 3. The code was written in gitpod and pushed using the gitpod source control option on the side bar of the application.

### Github Pages
- Adding it to Github Pages
- To create the live link for the site, github pages was used in the following way.
- Navigate to settings
- Click on the Pages tab
- Select the branch "main"
- This will generate the link to the live site when created.
- Click Save

### Cloning
- Select the github repository to clone.
- Click on the code button to access the dropdown menu.
- Download the file then open with IDE or copy Git URL from the HTTPS dialogue box.
- Open the console window in the IDE of your choice.
- Use the 'git clone' command inside the terminal and follow the command with the url you wish to clone.
- A clone of the project will be created locally on your machine.

## Deployment to Heroku

# Credits / Acknowledgements
## Books
During the creation of this site I used the book "Building Web Apps with Python and Flask" by Malhar Lathkar for help troubleshooting and general tips on creating the site

Site made for educational purposes only for assessment by Code Institute
