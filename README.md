# CRUD movieblog

## Milestone Project 3

![Am I Responsive](documentation/readme/amiresponsive.png)

### I have created this web page as a part of  my Milestone Project 3 for educational purposes only

## Live Project

[Live Webpage](https://crud-movieblog-3cd9ad6260c9.herokuapp.com/index)


## Repository

[My repository](https://github.com/EdgarKlavins/crud-movieblog)
<br>

# UX

### Project goals

The main purpose of this project is to create a user-friendly website with a Back end, designed to find and share movies, providing CRUD operations. (Create, Read, Update and Delete.)

## Project Goals
<ul>
<li>To create a website that can be navigated easily and intuitively.</li>
<li>To implement simple and clean design</li>
<li>To create a good looking website that responds correctly on all device sizes.</li>
<li>A website that has user authentication</li>
<li>A website that has user uuthorization</li>
<li>A website that is providing CRUD operations</li>
<li>A website which is linked to external database</li>
</ul>
<br>

## User Goals
<ul>
<li>Visually appealing design.</li>
<li>Links and buttons that work as expected</li>
<li>Quick and easy way to register</li>
<li>Simple and easy way to login</li>
<li>Ability to add, edit or delete own data</li>
<li>Being sure, that your data is protected</li>
<li>Accessibility.</li>
</ul>
<br>

## User stories
<ul>
<li>As a User, I want to know the purpose of the site immediately.</li>
<li>As a user, I want to view the website and content clearly on any device and resolution</li>
<li>As a user, I want to be able to easily register a new account.</li>
<li>As a user, I want an easy way to login</li>
<li>As a User, I want to add and share titles of my favourite movies</li>
<li>As a User, I want to be able to edit my posts or even delete them</li>
<li>As a User, I want to see, what movies other users are suggesting</li>
<li>As a User, I want to add and see, movie title, genre, year and comment section </li>
<li>As a user, I want to see contact information for the site owner in case I want to reach out </li>
<li>As a user, I want to be able to send messages directly through the website </li>
</ul>

## Design

### Wireframes

1. **Home page** displays the introduction and purpose of the website.

[Home page](documentation/readme/Home.png)

2. **About page** displays brief history of movie.

[About page](documentation/readme/About.png)

3. **Contact page** provides form with name, e-mail and message input.

[Contact page](documentation/readme/Contact.png)

4. **Register page** provides registry form.

[Register page](documentation/readme/Register.png)

5. **Add movie** Allows users to add, edit, delete movies or just browse other user movies

[Add movie page](documentation/readme/Addmovie.png)



### Database

In this case I have used one to many information flow, as you can see in the chart, I have two Primary keys and one Foreign key,<br>
 making movies related to user, who created them.


![dbchart](documentation/readme/dbchart.png)


### CRUD

CRUD operations

1. Create

* Registeres and logged in users can create their own movie list

2. Read 

* Movies added by users can be easily viewed

3. Update 

* Logged in users can easily edit their own movies.

4. Delete

* Logged in users can delete their own movies.



### Flash messages

I have implemented flash message notifications using Jinja templating language.

User will get notification when:

* Creates a new account
* Gets logged in
* Creates new movie
* Movie gets edited
* Sends message in contact form
* Gets logged out
* If user name already exists
* If password or username is incorrect


### Colour scheme

As the main colour I chosed materialize built in class color "grey darken-1", <br>
which makes a good contrast with white and fits realy good with my background image and other tones of grey.

![Colour palette](documentation/readme/pallete.png)



### Imagery

Images from "about" page are takken from https://www.scienceandmediamuseum.org.uk , <br>
so as the informative text about movie beginnings

Background image link - from https://www.screenrant.com
<br>


## Features

### Existing Features

### All Pages

**Navigation Bar**


* Fully responsive; collapapses into a toggler menu on small devices;
* Features a logo which leads to the Index page when clicked;
* Features links to the Home, About, Contact pages;
* For users that are not logged in, it features links to the Register and Log In pages;
* For logged in users, it provides links to the Top movies and Log Out functionallity;
* Links are selected with darker grey colour  on hover.

![Navbar](documentation/readme/navbar.png)
![Navbarloggedin](documentation/readme/Navbar_l.png)
![Navbarphone](documentation/readme/navbarphone.png)
<br>

**Footer**

* Contains credits and a link to the developer's Github and Linkedin accounts;

![footer](documentation/readme/footer.png)
<br>

**Home page**

* Informs the user about the purpose of the website;
* Gives information how to access functionality.
* Shows recent activity of other users

![homepage](documentation/readme/homep.png)
<br>

**About page**

* Tells user a short introduction to history of movie creation;

![homepage](documentation/readme/aboutp.png)
<br>

**Contact page**

* Allows user to send message and leave contact data to receive an answer;

![homepage](documentation/readme/contactp.png)
<br>

**Register page**

* Allows user to create account or if he  has it switch to login page;

![homepage](documentation/readme/registerp.png)
<br>

**Login page**

* Allows user to log in or if he does not have an account switch to register page;

![homepage](documentation/readme/loginp.png)
<br>

**Top movies page**

* Allows user to browse all already added movies;

![homepage](documentation/readme/moviesp.png)
<br>

* Allows user to add, edit or delete his/her movies ;

![homepage](documentation/readme/aboutp.png)
<br>
![homepage](documentation/readme/editp.png)
<br>

**Flash messages**

User gets flash message if:

* Creates a new account
* Gets logged in
* Creates new movie
* Movie gets edited
* Sends message in contact form
* Gets logged out
* If user name already exists
* If password or username is incorrect

![homepage](documentation/readme/flash.png)
![homepage](documentation/readme/flash2.png)
![homepage](documentation/readme/flash3.png)
<br>

# Testing






