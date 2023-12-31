# Milestone Project Three - Macs Cookbook
# Contents

![Site Mockup](/cookbook/docs/cimp3-mockup.png "Site Mockup")


[**__link to deployed site here__**](https://cimp3-cookbook-147e33c80e2f.herokuapp.com//)

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

As a logged out user, I would like feedback on my form submissions and and confirmation of logging out successfully

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

Upon clicking the edit button, the user is directed to a prefilled form referencing all of the recipes current values, allowing the user to change whatever is necessary and resubmit the form back to the database to be updated.

To ensure no accidental deletions of the recipes, a modal has been implemented requiring the user to confirm the attempt before the recipe is removed from the database

## Add recipe page

The add recipe page allows a user to submit a recipe of their choice by filling out a simple form regarding the recipe name, time ingredients, steps and provide an image URL for a photograph

## Edit recipe

The edit recipe function allows users to click the button to change a mistake in the recipe they have already submitted, the recipe will load into a pre filled form and the user then just makes the necessary changes then submits the form

## Admin Features

On the admin page, an admin can add or remove access to admin features using the user email of the account needing the access using a simple form with a checkbox to add/remove privilege

The admin page also allows admins to view other admins on the site for clarity to protect against unwanted or unnecessary access of the privileges.

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
  
### Sort function on recipes page

Another function left to implement is the sort function on the recipes page which if implemented would allow the page to sort recipe names from a-z.

### Sort recipes on recipe page

Another feature to be implemented on the site is to sort the recipes owned by the user alphabetically. This functionality could be implemented by changing the return function in the models file from an fstring and filtering by the name of the recipe before displaying in the recipes page.

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

The user can change email addresses for the account if necessary in the database
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

### Expand Recipe

The expand recipe page analysis from lighthouse is as follows.

![Lighthouse testing Expand Recipe](/cookbook/docs/testing/lighthouse/expand-recipe-lighthouse.png "Lighthouse testing Expand Recipe")

### Recipes

When assessing the recipes page in lighthouse, it returns these values.

![Lighthouse testing Recipes](/cookbook/docs/testing/lighthouse/recipes-lighthouse.png "Lighthouse testing Recipes")

### Sign up

The sign-up page was also assessed, the report purported the following.

![Lighthouse testing Sign up](/cookbook/docs/testing/lighthouse/signup-lighthouse.png "Lighthouse testing Sign up")

### Login

The login page was also assessed and returned the following.

![Lighthouse testing Login](/cookbook/docs/testing/lighthouse/login-lighthouse.png "Lighthouse testing Login")
 
## Functional Testing

| Base (Admin)                               |                                                                                 |                                                                                                     |        |
| ------------------------------------------ | ------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | ------ |
| Test                                       | Expected                                                                        | Outcome                                                                                             | Result |
| Navigate to home.html (navbar)             | Load home page                                                                  | Loads home                                                                                          | Pass   |
| Navigate to add-recipe.html (navbar)       | load add recipe page                                                            | loads add recipe                                                                                    | Pass   |
| Navigate to recipes.html (navbar)          | load your recipe page                                                           | loads recipes                                                                                       | Pass   |
| Navigate to account.html (navbar)          | load account page                                                               | loads account                                                                                       | Pass   |
| Navigate to admin.html (navbar)            | load admin oage                                                                 | loads admin page                                                                                    | Pass   |
| Click logout (navbar)                      | logout user                                                                     | logs out user                                                                                       | Pass   |
|                                            |                                                                                 |                                                                                                     |        |
| Base (Non Admin)                           |                                                                                 |                                                                                                     |        |
| Test                                       | Expected                                                                        | Outcome                                                                                             | Result |
| Navigate to home.html (navbar)             | Load home page                                                                  | Loads home                                                                                          | Pass   |
| Navigate to add-recipe.html (navbar)       | load add recipe page                                                            | loads add recipe                                                                                    | Pass   |
| Navigate to recipes.html (navbar)          | load your recipe page                                                           | loads recipes                                                                                       | Pass   |
| Navigate to account.html (navbar)          | load account page                                                               | loads account                                                                                       | Pass   |
| Navigate to admin.html (navbar)            | Rejected with feedback                                                          | loads admin page                                                                                    | Pass   |
| Click logout (navbar)                      | logout user                                                                     | logs out user                                                                                       | Pass   |
|                                            |                                                                                 |                                                                                                     |        |
| Login                                      |                                                                                 |                                                                                                     |        |
| Test                                       | Expected                                                                        | Outcome                                                                                             | Result |
| Enter valid email and password and submit  | Log in user                                                                     | User logged in                                                                                      | Pass   |
| Enter email that doesn't exist in db       | Feedback to inform email doesn't exist in db                                    | Flash (email is not in database)                                                                    | Pass   |
| Enter existing email, wrong password       | Feedback to inform incorrect password                                           | Flash (incorrect password)                                                                          | Pass   |
| Navigate to sign up (navbar)                | Load sign up                                                                    | Loaded sign up page                                                                                 | Pass   |
|                                            |                                                                                 |                                                                                                     |        |
| Sign Up                                    |                                                                                 |                                                                                                     |        |
| Test                                       | Expected                                                                        | Outcome                                                                                             | Result |
| Navigate to login (navbar)                 | Load login                                                                      | Loaded login                                                                                        | Pass   |
| Sign up with non-existing email            | Successfully register, redirect to login page                                   | Flash(Welcome aboard!) Direct to login page                                                         | Pass   |
| Sign up with email already existing        | Flash (email already exists)                                                    | Flash(An account already exists using this email)                                                   | Pass   |
| Submit blank form                          | Validator prompts form to be filled properly                                    | Validator prompts user until all fields are filled                                                  | Pass   |
|                                            |                                                                                 |                                                                                                     |        |
| Home                                       |                                                                                 |                                                                                                     |        |
| Test                                       | Expected                                                                        | Outcome                                                                                             | Result |
| Click view on a recipe                     | Redirect to expand recipe page using recipe id                                  | Succesfully redirected to view recipe                                                               | Pass   |
|                                            |                                                                                 |                                                                                                     |        |
| Add Recipe                                 |                                                                                 |                                                                                                     |        |
| Test                                       | Expected                                                                        | Outcome                                                                                             | Result |
| Fill form out correctly and submit         | Recipe uploaded and redirect to user recipe page                                | Recipe submitted, redirected successfully and recipe rendered on recipe page                        | Pass   |
| Miss form sections and submit              | Validator prompt to fill required fields                                        | Validation order successful, prompts on recipe name length, link not provided and ingredients length | Pass   |
|                                            |                                                                                 |                                                                                                     |        |
| Expand Recipe Admin                        |                                                                                 |                                                                                                     |        |
| Test                                       | Expected                                                                        | Outcome                                                                                             | Result |
| Loads recipe successfully                   | Loads recipe to view                                                            | Loaded recipe successfully                                                                           | Pass   |
| Edit button redirects to edit page         | Loads edit recipe template prefilled with recipe                                | Loads recipe for adjustment successfully                                                            | Pass   |
| Delete button deletes recipe               | Deletes recipe from database                                                    | Deletes recipe successfully                                                                          | Pass   |
|                                            |                                                                                 |                                                                                                     |        |
| Expand Recipe Non Admin                    |                                                                                 |                                                                                                     |        |
| Test                                       | Expected                                                                        | Outcome                                                                                             | Result |
| Loads recipe successfully                   | Loads recipe to view                                                            | Loaded recipe successfully                                                                           | Pass   |
|                                            |                                                                                 |                                                                                                     |        |
| Edit Recipe                                |                                                                                 |                                                                                                     |        |
| Test                                       | Expected                                                                        | Outcome                                                                                             | Result |
| Submit recipe fully adjusted               | Recipe is overwritten by input fields correctly and redisplayed on recipes page | Successfully edited recipe                                                                          | Pass   |
| Leave a field blank and submit recipe      | Flash message regarding failure reason, redirect to recipes page                | Flashed message as expected                                                                         | Pass   |
|                                            |                                                                                 |                                                                                                     |        |
| Recipe                                     |                                                                                 |                                                                                                     |        |
| Test                                       | Expected                                                                        | Outcome                                                                                             | Result |
| Displays user recipes on page              | Shows all of user recipes                                                       | Shows user recipes correctly                                                                        | Pass   |
| Edit button redirects to edit recipe page  | Allows user to edit recipe                                                      | Redirects to edit recipe page                                                                       | Pass   |
| Delete button deletes recipe from database | Deletes recipe from database                                                    | Deletes recipe from database                                                                        | Pass   |
|                                            |                                                                                 |                                                                                                     |        |
| Admin                                      |                                                                                 |                                                                                                     |        |
| Test                                       | Expected                                                                        | Outcome                                                                                             | Result |
| Add permissions to user                    | Added permissions, user added to admin list on page                             | User added                                                                                          | Pass   |
| Remove permissions from user               | Removed permissions, user removed from list on page                             | User removed                                                                                        | Pass   |
| Enter empty form                           | Form prompts enter an email                                                     | Flash(Please enter valid email)                                                                     | Pass   |
| Try to remove permissions from ID 1        | Flash (cannot remove owner permissions)                                         | Flash(Cannot strip owner permissions)                                                               | Pass   |
| Enter email not in database                | Flash(User does not exist!)                                                     | Flash(User does not exist!)                                                                         | Pass   |
|                                            |                                                                                 |                                                                                                     |        |
| Account                                    |                                                                                 |                                                                                                     |        |
| Test                                       | Expected                                                                        | Outcome                                                                                             | Result |
| Change email to unique email               | Sets new email                                                                  | New email is set and loaded onto existing email section of page as confirmation                     | Pass   |
| Change email to non-unique email           | Flash(Email in use)                                                             | Flashes email in use                                                                                | Pass   |
| Enter empty form                           | Form validation stops user                                                      | Form promt to add email to form                                                                     | Pass   |
|                                            |                                                                                 |                                                                                                     |        |
| 404 Page                                   |                                                                                 |                                                                                                     |        |
| Test                                       | Expected                                                                        | Outcome                                                                                             | Result |
| If logged in, click button to home page    | Navigate to home page                                                           | Loaded home page                                                                                    | Pass   |
| If logged out, click to login page         | Navigate to login page                                                          | Load login page                                                                                     | Pass   |
|                                            |                                                                                 |                                                                                                     |        |
| 500 Page                                   |                                                                                 |                                                                                                     |        |
| Test                                       | Expected                                                                        | Outcome                                                                                             | Result |
| If logged in, click button to home page    | Navigate to home page                                                           | Loaded home page                                                                                    | Pass   |
| If logged out, click to login page         | Navigate to login page                                                          | Load login page                                                                                     | Pass   |

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

The stylesheets were assessed using jigsaw to analyze CSS compliance with standard practices and returned the following.

![CSS Validation](/cookbook/docs/testing/validators/css/styles-css.png "CSS Validation")

## JavaScript/jQuery

The JavaScript/JQuery initialization code was assessed using JSLint and returned the following.
![JS Validation](/cookbook/docs/testing/validators/js/initialiser-js.png "JS Validation")

## Python

The python code was ran through the validation software to ensure it is pep8 compliant and returned the following.

### Init
The init file returned 1 linting error regarding the module being imported that is not at the top of file, when this error is corrected it creates a circular import bug on the site.

![Init Validation](/cookbook/docs/testing/validators/python/init-pep8.png "Init Validation")

### Auth

The Auth file returned 0 errors when linted.

![Auth Validation](/cookbook/docs/testing/validators/python/auth-pep8.png "Auth Validation")

### Models

The model evaluation returned 2 lines with hints, both lines returned were in regards to f strings returned by the model.

![Models Validation](/cookbook/docs/testing/validators/python/models-pep8.png "Models Validation")

### Routes

Validation testing in the routes file returned errors based on the comparison operators to boolean values. When running this through the linter with a single equals it passed validation but then returned errors in VS code.

![Routes Validation](/cookbook/docs/testing/validators/python/routes-pep8.png "Routes Validation")

</details>
<details>
<summary><b>Technologies Utilized</b></summary>

# Technologies Utilised
## HTML

HTML5 Was used to create the front end skeleton of the website, semantic HTML in the form of Head, Nav, Main and Footer tags were used to create appropriate structure.

## CSS

Custom CSS styles were utilised to resize and reposition some elements on the site in order to maximize the user experience.

### Materialize Framework

The Materialize Framework was used in order to allow for easy to put together structures and fast styles to create a better user experience for the user.

## JavaScript/JQuery

### Materialize Framework

The Materialize Framework was also used in the form of JQuery to initialize some of the components used from the framework such as carousels and collapsible menus

## Python

### Flask Framework

The Flask Framework was used to create and initialize the app in order to run the server and to navigate through the site using routing and login functionality.

### Jinja Templating

Jinja Templating was used alongside Flask modules in order to create Python implementation in the html files rendered by the app

## External utility

### Font Awesome

Font Awesome was used to generate icons for the website and to style the links in a more reader friendly fashion

### Heroku

Heroku was used to deploy the app when ready and allowed for it to become a live site

### ElephantSQL

Elephant SQL was used to connect the database to the app for functionality at deployment

</details>
<details>
<summary><b>Deployment</b></summary>

## GitHub version control

The site was created using the template provided by code institute regarding milestone project 3. The code was written in gitpod and pushed using the gitpod source control option on the side bar of the application.

### Cloning

- Select the github repository to clone.
- Click on the code button to access the dropdown menu.
- Download the file then open with IDE or copy Git URL from the HTTPS dialogue box.
- Open the console window in the IDE of your choice.
- Use the 'git clone' command inside the terminal and follow the command with the url you wish to clone.
- A clone of the project will be created locally on your machine.

## Deployment to Heroku

To deploy the project to Heroku:
1. To get all dependencies of the app, first you need to run the freeze command by typing into the CLI
- pip3 freeze --local > requirements.txt
2. To user Heroku the project will also need a Procfile, named with a capital P and in the content of the file should be the following line
- web: python3 run.py
3. Push the newly created files to github for use
4. Login to heroku and create a new app by providing a name and choosing the relevant region.
5. Click the connect tab and select github, find the repository you wish to use for the heroku app.
6. On the settings tab reveal the config vars and add the additional variables 

| Key | Value |
| :---: | :---: |
| DATABASE_URL | postgresql |
| IP | 0.0.0.0 |
| PORT | 5000 |
| SECRET_KEY | mysecretkey |

Actual env variables not disclosed.

</details>

<details>
<summary><b>Credits / Acknowledgements</b></summary>

## Books

During the creation of this site I used the book "Building Web Apps with Python and Flask" by Malhar Lathkar for help troubleshooting and general tips on creating the site

## Code

Code written inside the files was written by myself solely with the exception of components and javascript to utilize the respective components, in which I gained the structure through the materialize framework was used.

Site made for educational purposes only for assessment by Code Institute
