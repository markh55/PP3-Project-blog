# PP3-Project-blog

## Devbase

Devbase is to share content and give users the ability to fully interact with it. You can create your own posts, read what others have shared, update your entries, or delete them whenever you like. Whether you're here to write, browse, or both, the goal is to make the experience smooth, enjoyable, and engaging. Dive in and be part of the journey!

### Table of Content

* [Planning](#planning)
   * [User Stories](#user-stories)
   * [Wireframes](#wireframes)
   * [Logo](#logo)
* [Final Design](#final-design)
* [Deployment](#deployment)
    * [GitHub](#git-hub)
    * [Heroku](#heroku)
* [Testing](#testing)
    * [lighthouse](#lighthouse)
    * [CI Python Linter](#ci-python-linter)
* [Feedback](#feedback)
* [Tech Stack](#tech-stack)
* [Resources](#resources)
* [Credits / Tutorials](#credits--tutorials)


## Planning

### User Stories

* As a user, I want to browse and read blog posts created by others so I can engage with their content.

* As a logged-in user, I want to edit my own blog posts so I can update or improve my content.

* As a logged-in user, I want to delete my blog posts so I can remove content I no longer want to share.

* As a user, I want a simple and responsive layout with clear navigation so I can easily find what I’m looking for.

* As a developer, I want to ensure blog posts are stored in a relational database linked to user accounts so that data is organized and secure.


### Wireframes
With the design the aim was to make it clean and simple for you user to be able to navigate the site with ease, before any coding have taken place i came up with the below wireframe to repesent the vision i had for the project site.

### Welcome Page - 
![Welcome page](https://github.com/user-attachments/assets/8dd0a206-6e3b-4659-bd20-bf09ae1fb627)

### Sign up Page -
![SignIn ](https://github.com/user-attachments/assets/cab34964-6a65-4fed-9f56-d283b1e8a7a8)


### Blog Homepage - 
![Blog homepage](https://github.com/user-attachments/assets/f6200832-18ee-4d6a-813d-e3a295013f36)


### Blog Page - 
![Blog Page](https://github.com/user-attachments/assets/84e90daf-46d2-49ff-9d10-5328887007be)

### Logo
I came up with the devbase logo when thinking of things to call my blog instead of the classic "My Blog" so my thought process was;

Dev - This is just developer but shortened.

Base - The thinking behind this part of the name is that the developer would have somewhere to connect and make a digital home.

the logo itself is something unique and relevent, the logo is made up of a < symbol and a curly brace }, when you put them together like this <} it forms the D from Devbase but also repesenting the world of programming at the same time.

![11F745C7-7B4A-4E7E-81A7-753B950155AE_1_102_o](https://github.com/user-attachments/assets/03ad06b2-1292-4c75-8cff-30fb8bb22862)

* Darkmode
<img width="1024" height="1024" alt="dark_mode_logo" src="https://github.com/user-attachments/assets/56a60d4a-326a-4d63-b6b4-dbb1d9417b25" />


## Final Design

## Deployment 

### Git Hub

with this project all i needed to do on github was create the PP3-Project-blog repository as the main deployment was handled via Heroku (steps below)

### Heroku

First step i did was create the blog-pp3 app within Heroku by creating the app name and ajusting the location to europe, once they was done i clicked create app.

<img width="1701" alt="Screenshot 2025-07-02 at 21 07 05" src="https://github.com/user-attachments/assets/277987d0-e7ac-4f30-9ff1-4878420b3617" />


Second step was to navigate to the 'Deploy" tab and link my Github account once that was linked i could then search for my repository i would like to link.


<img width="1463" alt="Screenshot 2025-07-02 at 21 22 10" src="https://github.com/user-attachments/assets/5f6560d0-ef17-412f-9c8b-989fbc97977e" />

Following on from step two once that was all linking up i go to the bottom of the page and click "deploy now".


<img width="1671" alt="Screenshot 2025-07-03 at 18 01 52" src="https://github.com/user-attachments/assets/2f818c9c-f895-4aef-9c72-0b7b1934b68c" />


Then when they deployment is compeleted it would go back to the top of the page to click "open app" to ensure my project was all linked and working as it should.

<img width="1668" alt="Screenshot 2025-07-03 at 18 02 07" src="https://github.com/user-attachments/assets/122f7c6f-9268-4157-86c8-067b7d8b85cc" />

## Testing

### Lighthouse

To ensure quality and performance of my project, I  preformed  multiple testing:

Lighthouse: I ran Lighthouse tests on both desktop and mobile to evaluate the site performance, accessibility, best practices.

Python Code Linting: I ran a CI linter on important Python files like forms.py, admin.py, urls.py, and models.py to catch style and syntax problems. The screenshots show the code follows PEP8 and stays clean, which makes it easier to read and less likely to have bugs.

These automated checks back up the manual testing and functional checks, so I’m confident the code is solid, easy to maintain, and works well for users.



### Desktop

<img width="806" height="568" alt="Lighthouse - Desktop" src="https://github.com/user-attachments/assets/41f30220-ddaf-47d9-ab13-93323a99f54f" />

### Mobile

<img width="806" height="568" alt="Lighthouse - Desktop" src="https://github.com/user-attachments/assets/de1cc564-52cc-4c1b-8ac9-9ab2caf9f02a" />

### CI Python Linter

### forms.py
<img width="1381" height="798" alt="Screenshot 2025-07-12 at 23 45 13" src="https://github.com/user-attachments/assets/55134698-6ad6-40d8-8d2a-7ff923aad759" />

### Admin.py

<img width="1370" height="766" alt="Screenshot 2025-07-12 at 23 43 50" src="https://github.com/user-attachments/assets/634699cf-7a9e-438a-8a98-2413f75e9ef5" />

### urls.py

<img width="1500" height="819" alt="Screenshot 2025-07-12 at 23 41 26" src="https://github.com/user-attachments/assets/9066f6e9-78f4-4753-805a-5bfad76060f9" />

### models.py

<img width="1553" height="853" alt="Screenshot 2025-07-12 at 23 37 55" src="https://github.com/user-attachments/assets/df5104b4-d7a2-4c1a-ae9b-ffe09f4d4d30" />


## Feedback
The only feed back i got was to do with the darkmode icon while on mobile screens it was diplaying outside of the hamburger menu causing the alignment to be out.

![IMG_8472](https://github.com/user-attachments/assets/00677a49-3e75-499b-807a-07ff3ff4cc4c)

This was fixed but replacing the line of code for the darkmode item within the nav items section, by doing this the icon is hidden within the hamburger menu and the hamburger menu icon is back in the original position of the top right hand side.
![IMG_8486](https://github.com/user-attachments/assets/5e8963fb-d367-443e-b1af-516e133604c5)


## Tech Stack
*	Django 5.0.14
*	HTML
*	CSS / Bootstrap 5
*	PostgreSQL
*	Heroku (deployment)




## Resources

* Code Institute
  * Love Sandwiches
  * I Think Therefore I Blog

* Djnago 5 By Example by Antonio Mele

* Documentation for Django - https://docs.djangoproject.com/en/5.2/
  
* Stack Overflow

    
## Credits / Tutorials

### Source used

* Correy Schafer - Python Django Tutorial: Full-Featured Web App Part 10 - Create, Update, and Delete Posts 
[Watched on YouTube](https://www.youtube.com/watch?v=-s7e_Fy6NRU&list=PL3ogf06gmD4herEB1HXBkfFBsTtZjGBuh)
I used this tutorial to help implement the functionality for users to add blog posts. The tutorial served as a guide, and I adapted the code to fit the needs of my project.

* Django Documentation – Limiting QuerySets
[Limiting QuerySets](https://docs.djangoproject.com/en/5.2/ref/models/querysets/#limiting-querysets)

   I referenced this documentation to learn how to limit the number of posts shown on the homepage. I modified the example code to display the latest 3 posts in    my own template.
  
* stack overflow - Show latest blog posts
[Show latest blog posts](https://stackoverflow.com/questions/75190346/way-to-show-latest-4-blog-posts-on-my-page)

   Question by David Henson, answered by Mas Zero. I used this as a reference for structuring the query and template logic to display the most recent posts. The    code was adapted to suit my models and template structure.
