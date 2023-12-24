# Milestone Project Three - Macs Cookbook
# Contents
<details>
<summary><b>User Stories<b></summary>

## Site ownership goals
The site was created for a fictional owner who requires a cookbook app for users to log in and share recipes for a community culinary experience.
## Visitor/User Goals
### Logged in user goals

As a logged in user, I would like to be able to contribute my own recipes to the site

As a logged in user, I would like to be able to adjust and delete the recipes I have submitted on the website at my own leisure

As a logged in user, I would like the flexibility to change my email and password when I need to

As a logged in user I would like to be able to navigate around the site structure easily and understand the layout of the site instinctively

As a logged user, I would like to be able to delete my account if I decide to leave the site at a later date

### Logged out user goals

As a logged out user, I would like to be able to access the register page to create an account and get feedback based on a successful registration

As a logged out user, I would like to be able to sign in and access the site

As a logged out user, I would like feedback on my form submissions and and confirmation of loggin out successfully

### Logged in admin goals

As an admin, I would like to be able to grant/remove admin access to trusted users on the site

As an admin, I would like to see which users currently have admin privileges on the site for a clear picture of who has access

As a admin, I would like to be able to police the site using my permissions as a way to edit/remove other users recipes if they are used inappropriately on the site.
</details>

<details>
<summary><b>Features</b></summary>

## Site wide
The implementation of a global navbar and footer to make a uniform user experience has been completed site wide
- As a logged in user I would like to be able to navigate around the site structure easily and understand the layout of the site instinctively
## Pre Login
The user experience is limited to only 2 pages before logging in, from here they can navigate to the login page or sign up page
## Home Page
On the home page, users can take the opportunity to view both their own created recipes, and also the communities additions to the site, the CRUD functionality on the home page is read only by design to ensure that the recipes of other users are protected and cannot be edited or deleted. If a user clicks on view recipe to expand this page, they can see a more in depth view of the recipe they have clicked, and if they are an administrator of the site or the owner of the recipe they will have access to edit or delete on that page.
## Account Page
In the account page the user is presented with a collapsible set of forms offering multiple functionalities
### Change Password
The user can opt to change the password in the database by supplying the app with the old password and the new request to take its place, the user is once again given a modal to confirm and guard against accidental changes. The act of supplying the old password is used as a security measure to prevent malicious intent on the site.
### Change email
In the email section of the page the user is presented with the current email address linked to the account for reference, they are given the option to change to a new email via a form and presented with a modal to confirm the selection and submit to the database. Due to the database model requiring each email to be unique, if the user requests an email already in the database it will reject the request and provide feedback to the user on the nature of the rejection.
### Delete account
The user is provided with an option to remove the account from the database after supplying the form with the email associated to their own account, the function queries the email provided with the current session user to prevent and foul play and only allow for the deletion of the logged in account.
## Recipes Page
In the recipes page, the user is able to view all recipe submissions made by themselves with the option to update the recipes and also to delete them.

Upon clicking the edit button, the user is directed to a prefilled form referencing all of the recipes current values, allowing the user to change whatever is neccessary and resubmit the form back to the database to be updated.

To ensure no accidental deletions of the recipes, a modal has been implemented requiring the user to confirm the attempt before the recipe is removed from the database
## Admin Features
On the admin page, an admin can add or remove access to admin features using the user email of the account needing the access using a simple form with a checkbox to add/remove privilege

The admin page also allows admins to view other admins on the site for clarity to protect against unwanted or unneccesary access of the privileges.

Additionally, having admin permission also lets users edit and delete recipes on the home page that they do not own to ensure compliance with site etiquette.

## Error Pages
### 404 Error
An error page was designed for a 404 error and allows the user to navigate back to the home page if logged in using a button on the page, if the user is not logged in it will direct them to the login page
### 500 Error
An error page was designed for a 500 error and allows the user to navigate back to the home page if logged in using a button on the page, if the user is not logged in it will direct them to the login page

## If/Else statement for admins
The site was built using an if else statement regarding admins and will only display the admin page on the navigation menu if the user does have admin permissions, if a non admin user tries to access this page via the URL they will be returned home and have a message flashed on screen to inform them they are not an administrator

## Features left to implement
### Forgot Password Form
A feature that can be implemented in the future would be the forgot password form, I would place this at the bottom of the login page and use the following steps to implement the feature.

- Fill email form
- Query database for email
- If it exists, connect to an API to send email and allow the user to change password using the change password function.
</details>

<details>
<summary><b>CRUD Functions</b></summary>

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
</details>

<details>
<summary><b>Wireframes</b></summary>

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
The admin page was designed to allow admin access on the site.

![Admin Desktop Wireframe](/cookbook/docs/Wireframes/Desktop/admin-desktop.png "Admin Desktop Wireframe")
## Expand Recipe 
The expand recipe page is active when clicking view on a recipe and queries the individual recipe for display on its own page for viewing.

![Expand recipe Desktop Wireframe](/cookbook/docs/Wireframes/Desktop/expand-recipe-desktop.png "Expand recipe Desktop Wireframe")
</details>
<details>
<summary><b>Entity Relationship Diagram & Flow Chart</b></summary>

## ERD Diagram

![ERD Diagram](/cookbook/docs/Diagrams/erd-diagram.png "ERD Diagram")

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
The admin toggle function allows for a user to use the admin access panel to enable or disable additional permissions to users on the site, the checkbox next to the input field will (if ticked) enable permissions to the email submitted, if not checked and an email is submitted it will remove permissions. The function does not allow the user with the id of 1 to have permissions removed. 
</details>
<details>
<summary><b>Testing</b></summary>

## Wave testing
### 404
The 404 page was wave tested and reported the following.

![Wave testing 404](/cookbook/docs/testing/wave/desktop/wave-404-desktop.png "Wave testing 404")
### 500
The 500 page fed these stats back when wave tested

![Wave testing 500](/cookbook/docs/testing/wave/desktop/wave-500-desktop.png "Wave testing 500")
### Home
The home page gave the following results when ran through the wave tool

![Wave testing Home](/cookbook/docs/testing/wave/desktop/wave-home-desktop.png "Wave testing Home")
### Admin
The admin page reported the following results when using the wave tool.

![Wave testing Admin](/cookbook/docs/testing/wave/desktop/wave-admin-desktop.png "Wave testing Admin")
### Account
The account page was also waved, and returned these results

![Wave testing Account](/cookbook/docs/testing/wave/desktop/wave-account-desktop.png "Wave testing Account")
### Add Recipe
The add a recipe page returned the following

![Wave testing Add Recipe](/cookbook/docs/testing/wave/desktop/wave-add-recipe-desktop.png "Wave testing Add Recipe")
### Edit Recipe
The edit recipe page returned these results when waved

![Wave testing Edit Recipe](/cookbook/docs/testing/wave/desktop/wave-edit-recipe-desktop.png "Wave testing Edit Recipe")
### Recipes
The recipe page was waved and gave the below stats

![Wave testing Recipes](/cookbook/docs/testing/wave/desktop/wave-recipes-desktop.png "Wave testing Recipes")
### Sign up
The sign-up page also was ran through the tool, here are the results

![Wave testing Sign up](/cookbook/docs/testing/wave/desktop/wave-signup-desktop.png "Wave testing Sign up")
### Login
The login page returned the following results

![Wave testing Login](/cookbook/docs/testing/wave/desktop/wave-login-desktop.png "Wave testing Login")

## Lighthouse Testing
### Home
The website, in addition to using the wave tool was assessed using the Lighthouse technology of Google chrome, when using that technology on the home page it gave these stats.

![Lighthouse testing Home](/cookbook/docs/testing/lighthouse/home-lighthouse.png "Lighthouse testing Home")
### Admin
The admin page related the below stats when using the tool.

![Lighthouse testing Admin](/cookbook/docs/testing/lighthouse/admin-lighthouse.png "Lighthouse testing Admin")
### Account
the account page was also put in to lighthouse and returned these values.

![Lighthouse testing Account](/cookbook/docs/testing/lighthouse/account-lighthouse.png "Lighthouse testing Account")
### Add Recipe
When using Lighthouse on the add recipe page, it returns this analysis.

![Lighthouse testing Add Recipe](/cookbook/docs/testing/lighthouse/add-recipe-lighthouse.png "Lighthouse testing Add Recipe")
### Edit Recipe
The edit recipe page analysis from lighthouse is as follows.

![Lighthouse testing Edit Recipe](/cookbook/docs/testing/lighthouse/edit-recipe-lighthouse.png "Lighthouse testing Edit Recipe")
### Recipes
When assessing the recipes page in lighthouse, it returns these values.

![Lighthouse testing Recipes](/cookbook/docs/testing/lighthouse/recipes-lighthouse.png "Lighthouse testing Recipes")
### Sign up
The sign-up page was also assessed, the report purported the following. The page unfortunately did not return as high a score as the others majoritively due to unused JavaScript. These scripts are inherited from the base template as initializes site wide.

![Lighthouse testing Sign up](/cookbook/docs/testing/lighthouse/signup-lighthouse.png "Lighthouse testing Sign up")
### Login
The login page was also assessed and returned the following, again this page was negatively impacted during these tests by loading unused JavaScript on the page as a result of inheriting from the base template.

![Lighthouse testing Login](/cookbook/docs/testing/lighthouse/login-lighthouse.png "Lighthouse testing Login")
## Functional Testing
### Base Template
Functional testing on the navigation menu of the base template was as follows

![Base functional tests](/cookbook/docs/testing/functional/base-tests.png "Base functional tests")

![Base Admin functional tests](/cookbook/docs/testing/functional/base-admin-tests.png "Base Admin functional tests")

### Home

Functional testing of the home template was as follows

![Home functional tests](/cookbook/docs/testing/functional/home-tests.png "Home functional tests")

### 404

The 404 page testing purported the following

![404 functional tests](/cookbook/docs/testing/functional/404-tests.png "404 functional tests")

### 500

The 500 page purports the following

![500 functional tests](/cookbook/docs/testing/functional/500-tests.png "500 functional tests")

### Account

Testing on the account page shows the following

![Account functional tests](/cookbook/docs/testing/functional/account-tests.png "Account functional tests")

### Add Recipe

The testing on the add recipe page shows the following

![Add recipe functional tests](/cookbook/docs/testing/functional/add-recipe-tests.png "Add recipe functional tests")

### Edit Recipe

The testing on the edit recipe page shows the following

![Edit recipe functional tests](/cookbook/docs/testing/functional/edit-recipe-tests.png "Edit recipe functional tests")

### Recipe

The recipe page testing was as follows

![Recipe functional tests](/cookbook/docs/testing/functional/recipe-tests.png "Recipe functional tests")

### Admin

The admin page was also tested for functionality

![Admin functional tests](/cookbook/docs/testing/functional/admin-tests.png "Admin functional tests")

### Login

The login page was tested as follows

![Login functional tests](/cookbook/docs/testing/functional/login-tests.png "Login functional tests")

### Sign Up

The sign up page was tested for the following criteria

![Sign up functional tests](/cookbook/docs/testing/functional/signup-tests.png "Sign up functional tests")

### Bugs

</details>
<details>
<summary>Language Validation</summary>

## HTML
The html parts of the website have been ran through validation software to ensure compliance with HTML standards on the web. You can see the reports below.
### Home
![Home HTML Validation](/cookbook/docs/testing/validators/html/home-html.png "Home HTML Validation")
### Account
![Account HTML Validation](/cookbook/docs/testing/validators/html/account-html.png "Account HTML Validation")
### Admin
![Admin HTML Validation](/cookbook/docs/testing/validators/html/admin-html.png "Admin HTML Validation")
### Recipes
![Recipes HTML Validation](/cookbook/docs/testing/validators/html/recipes-html.png "Recipes HTML Validation")
### Add Recipe
![Add Recipe HTML Validation](/cookbook/docs/testing/validators/html/add-recipe-html.png "Add Recipe HTML Validation")
### Edit Recipe
![Edit Recipe HTML Validation](/cookbook/docs/testing/validators/html/edit-recipe-html.png "Edit Recipe HTML Validation")
### Expand Recipe
#### Admin
![Expand Admin HTML Validation](/cookbook/docs/testing/validators/html/expand-recipe-admin-html.png "Expand Admin HTML Validation")
#### Non Admin
![Expand Non Admin HTML Validation](/cookbook/docs/testing/validators/html/expand-recipe-html.png "Expand Non Admin HTML Validation")
### Login
![Login HTML Validation](/cookbook/docs/testing/validators/html/login-html.png "Login HTML Validation")
### Sign Up
![Sign Up HTML Validation](/cookbook/docs/testing/validators/html/signup-html.png "Sign Up HTML Validation")

## CSS
The stylesheets were assessed using jigsaw to analyse CSS compliance with standard practises and returned the following.
![CSS Validation](/cookbook/docs/testing/validators/css/styles-css.png "CSS Validation")
## JavaScript/jQuery
The JavaScript/JQuery initialisation code was assessed using JSLint and returned the following.
![JS Validation](/cookbook/docs/testing/validators/js/initialiser-js.png "JS Validation")
## Python
The python code was ran through the validation software to ensure it is pep8 compliant and returned the following.
### Init
The init.py file returned 3 hints on validation, the hints were as follows:
1. Put white spaces around the operators. 

        app.register_blueprint(routes, url_prefix="/")

2. Put white spaces around the operators.

        app.register_blueprint(auth, url_prefix="/")

3. Add two empty lines in front of function definition

        @login_manager.user_loader

        def load_user(id):
        
            return User.query.get(int(id))

The whitespace hints refers to the slash for the url prefix

The line hint is caused by to the decorator above the function

![Auth Validation](/cookbook/docs/testing/validators/python/auth-pep8.png "Auth Validation")
### Auth
Auth file produced 6 hints in total for the following code snippets:
1. Put white spaces around the operators
2. Add two empty lines in front of function definition

        @auth.route('/login', methods = ['GET', 'POST'])

        def login():

3. Put white spaces around the operators
4. Add two empty lines in front of function definition

        @auth.route('/logout')

        @login_required

        def logout():

5. Put white spaces around the operators
6. Add two empty lines in front of function definition

        @auth.route('/signup', methods=['GET', 'POST'])

        def signup():

The whitespace hints refers to the slash before the route e.g "/login"

The line hints are caused due to the decorator above the function

![Auth Validation](/cookbook/docs/testing/validators/python/auth-pep8.png "Auth Validation")
### Models
The model evaluation returned 2 lines with hints, both lines returned were in regards to f strings returned by the model.

![Models Validation](/cookbook/docs/testing/validators/python/models-pep8.png "Models Validation")
### Routes
The routes function also returned 2 hints on lines regarding the length of statements inside of if statements, see below:

    if checkbox == 'on':

            user_exists.is_admin = True

            print(user_exists.first_name, user_exists.is_admin)

            db.session.commit()

            flash('User is now an admin', category="success")

            return redirect(url_for('routes.admin'))

The second if statements is as follows:

    if admin.is_admin:

            name = f"{admin.first_name} {admin.last_name}"

            current_admin_names.append(name)

            current_admin_names.sort()

![Routes Validation](/cookbook/docs/testing/validators/python/routes-pep8.png "Routes Validation")
</details>
<details>
<summary><b>Technologies Utilized</b></summary>

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

</details>
<details>
<summary><b>Deployment</b></summary>

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

</details>

<details>
<summary><b>Credits / Acknowledgements</b></summary>

## Books
During the creation of this site I used the book "Building Web Apps with Python and Flask" by Malhar Lathkar for help troubleshooting and general tips on creating the site

## Code
Code written inside the files was written by myself solely with the exception of components and javascript to utilize the respective components, in which I gained the structure through the materialize framework was used.

Site made for educational purposes only for assessment by Code Institute
