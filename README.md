# PP3-Project-blog

## Devbase

Devbase is to share content and give users the ability to fully interact with it. You can create your own posts, read what others have shared, update your entries, or delete them whenever you like. Whether you're here to write, browse, or both, the goal is to make the experience smooth, enjoyable, and engaging. Dive in and be part of the journey!

[Project link (right click to open in new window)](https://blog-pp3-22938c709acc.herokuapp.com/)

### Table of Content

- [PP3-Project-blog](#pp3-project-blog)
  - [Devbase](#devbase)
    - [Table of Content](#table-of-content)
  - [Planning](#planning)
    - [User Stories](#user-stories)
    - [Wireframes](#wireframes)
    - [Welcome Page -](#welcome-page--)
    - [Sign up Page -](#sign-up-page--)
    - [Blog Homepage -](#blog-homepage--)
    - [Blog Page -](#blog-page--)
    - [Entity Relationship Diagram](#entity-relationship-diagram)
    - [Logo](#logo)
    - [Colour Theme](#colour-theme)
  - [Final Design](#final-design)
  - [Features](#features)
  - [Deployment](#deployment)
    - [Git Hub](#git-hub)
    - [Heroku](#heroku)
  - [Testing](#testing)
    - [Manual Testing](#manual-testing) 
    - [Lighthouse](#lighthouse)
    - [Desktop](#desktop)
    - [Mobile](#mobile)
    - [CI Python Linter](#ci-python-linter)
    - [forms.py](#formspy)
    - [Admin.py](#adminpy)
    - [urls.py](#urlspy)
    - [models.py](#modelspy)
  - [Feedback](#feedback)
  - [Tech Stack](#tech-stack)
  - [Resources](#resources)
  - [Credits / Tutorials](#credits--tutorials)
    - [Source used](#source-used)

## Planning

### User Stories

For the design of the blog, I want it to be clean, user-friendly, and easy to navigate for everyone.

I will achieve this by doing the following:

- Listing blog posts clearly
- Allowing logged-in users to edit or delete only their own posts or comments
- Enabling visitors to browse and read posts without needing to log in
- Creating a responsive layout that works well on all screen sizes
- Storing all blog posts in a relational database linked to user accounts for secure management

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

### Entity Relationship Diagram

Following on from designing the wireframes, I needed to think about a model structure to be used for the project. I opted for a simple setup based around two core models: Post and Comment.

The Post model is composed of the following:

- ID
- Title
- Slug
- Author
- Body
- Publish

The Comment model is composed of the following:

- ID
- Post
- Author
- Body
- Approved
- Created_on

This structure allows each post to have multiple comments, while keeping the relationships clear and easy to manage.

![A4475DAA-AACD-4342-BF8C-858C7BD76209 2](https://github.com/user-attachments/assets/fcff6d67-2a52-40e2-ab19-d3eb3ead1192)

### Logo

I came up with the devbase logo when thinking of things to call my blog instead of the classic "My Blog" so my thought process was;

Dev - This is just developer but shortened.

Base - The thinking behind this part of the name is that the developer would have somewhere to connect and make a digital home.

the logo itself is something unique and relevent, the logo is made up of a < symbol and a curly brace }, when you put them together like this <} it forms the D from Devbase but also repesenting the world of programming at the same time.

![11F745C7-7B4A-4E7E-81A7-753B950155AE_1_102_o](https://github.com/user-attachments/assets/03ad06b2-1292-4c75-8cff-30fb8bb22862)

- Darkmode
![dark_mode_logo](https://github.com/user-attachments/assets/56a60d4a-326a-4d63-b6b4-dbb1d9417b25)

### Colour Theme

When planning what colour pallet i wanted to go with i needed to decide early on if i wanted the user to have the ability to change themes, this played a big part in the colours i picked as i wanted to keep it clean and minimal;

![Devbase](https://github.com/user-attachments/assets/f65e0d68-110e-49d5-add6-8fb5016a923b)

- #007bff – Light Mode Primary (Button Blue)
- #222 – Light Mode Text (Primary Text)
- #fff – Light Mode Background
- #121212 – Dark Mode Background
- #e0e0e0 – Dark Mode Text

## Final Design

<img width="1420" height="647" alt="screenshot_2025-07-17_at_19 56 05" src="https://github.com/user-attachments/assets/074fe390-40f6-48c6-befc-fd3a3afe504c" />

## Features

Devbase as a whole has a pretty minimal and clean interface, as I’m aiming for zero distractions from the purpose of the blog — to read, comment, and post blogs. That being said, the two standout features I focused on, other than the required CRUD, are:

### Dark / Light mode 
This feature allows users to set their preferred theme, recognizing that we all have different needs. For example, light mode can be too bright for some users’ eyes, while dark mode may be more difficult to read for others.

### Light Mode - Desktop
<img width="1280" height="208" alt="Screenshot 2025-07-28 at 21 18 08" src="https://github.com/user-attachments/assets/4535355b-86fa-4bd7-bbf0-d5cc813ffd13" />

### Light Mode - Mobile
<img width="465" height="323" alt="Screenshot 2025-07-28 at 21 18 36" src="https://github.com/user-attachments/assets/31c51a2a-44bc-461a-ba59-85319567482c" />

### Dark Mode - Desktop
<img width="1266" height="218" alt="Screenshot 2025-07-28 at 21 28 05" src="https://github.com/user-attachments/assets/039afb96-d86e-42b5-8306-7155056a4e24" />

### Dark Mode - Mobile
<img width="466" height="334" alt="Screenshot 2025-07-28 at 21 28 53" src="https://github.com/user-attachments/assets/0d2018dc-e715-4812-86ef-a04e62c40d45" />


### Email a Post
Underneath each blog but above the comment section is a “share this post” button that lets readers recommend blogs to friends or family who they think will find value in the content. This is done via a form that allows the user to enter:


 * Sender name

 * Sender email

 * The email address to send it to

 * A comment section

I have also set this feature to require the user to be logged in to prevent misuse, and the superuser/Admin has content control if any issues arise.

### Share this post button
<img width="901" height="600" alt="Screenshot 2025-07-28 at 21 17 32" src="https://github.com/user-attachments/assets/6aefaa2d-528a-4db4-99a1-3832ef7ea4d2" />

### Share form
<img width="827" height="910" alt="Screenshot 2025-07-28 at 21 17 53" src="https://github.com/user-attachments/assets/d39e6f14-7ddc-4a31-a6cb-34d791a8fe16" />

### Confirmation
<img width="1249" height="619" alt="Screenshot 2025-07-28 at 21 30 53" src="https://github.com/user-attachments/assets/15a7cb9a-1253-4195-b9bd-846ed0118fd3" />

### Custom 404 Error Page
A styled "Page Not Found" screen with a friendly message and a link back to the homepage, providing a better user experience when an incorrect URL is entered.

<img width="805" height="600" alt="Screenshot 2025-07-29 at 00 03 12" src="https://github.com/user-attachments/assets/5349bab2-f655-4b64-8c2a-1f3feb796661" />



## Deployment

### Git Hub

with this project all i needed to do on github was create the PP3-Project-blog repository as the main deployment was handled via Heroku (steps below)

### Heroku

First step i did was create the blog-pp3 app within Heroku by creating the app name and ajusting the location to europe, once they was done i clicked create app.

![Screenshot 2025-07-02 at 21 07 05](https://github.com/user-attachments/assets/277987d0-e7ac-4f30-9ff1-4878420b3617)

Second step was to navigate to the 'Deploy" tab and link my Github account once that was linked i could then search for my repository i would like to link.

![Screenshot 2025-07-02 at 21 22 10](https://github.com/user-attachments/assets/5f6560d0-ef17-412f-9c8b-989fbc97977e)

Following on from step two once that was all linking up i go to the bottom of the page and click "deploy now".

![Screenshot 2025-07-03 at 18 01 52](https://github.com/user-attachments/assets/2f818c9c-f895-4aef-9c72-0b7b1934b68c)

Then when they deployment is compeleted it would go back to the top of the page to click "open app" to ensure my project was all linked and working as it should.

![Screenshot 2025-07-03 at 18 02 07](https://github.com/user-attachments/assets/122f7c6f-9268-4157-86c8-067b7d8b85cc)

## Testing

To ensure quality and performance of my project, I performed multiple tests:

Manual Testing - My manual testing is made up of 4 main components Authentication, Blog features, Commenting and UI/UX to test that each component was fully working as it should to deliver the best experience to the user possible

Lighthouse: I ran Lighthouse tests on both desktop and mobile to evaluate the site performance, accessibility, best practices.

Python Code Linting: I ran a CI linter on important Python files like forms.py, admin.py, urls.py, and models.py to catch style and syntax problems. The screenshots show the code follows PEP8 and stays clean, which makes it easier to read and less likely to have bugs.

These checks are backed up below;

### Manual Testing 

#### 🧑‍💻 Authentication

| Feature       | Test Performed                                                                            | Outcome    |
|---------------|--------------------------------------------------------------------------------------------|------------|
| Login page    | Tested all components of page was working as they should by logging in as user            | Completed ✅ |
| Sign-up page  | Completed the sign-up process to ensure features working as intended                      | Completed ✅ |
| Log-out page  | Logged out of account to ensure working as should                                          | Completed ✅ |

#### 📝 Blog Features

| Feature      | Test Performed                                                                 | Outcome    |
|--------------|----------------------------------------------------------------------------------|------------|
| Add Blog     | Added a blog post via frontend                                                  | Completed ✅ |
| Edit Blog    | Updated my blog to ensure this was working as should                            | Completed ✅ |
| Delete Blog  | Deleted my blog to ensure it would be removed from the site                     | Completed ✅ |
| View only if not logged in | Viewed a post while not being logged in to ensure it was view only and if you wanted to leave a comment you need to have an account | Completed ✅ |

#### 💬 Commenting

| Feature        | Test Performed                     | Outcome    |
|----------------|------------------------------------|------------|
| Add a comment  | Added a comment to blog            | Completed ✅ |
| Edit Comment   | Updated my comment                 | Completed ✅ |
| Delete Comment | Deleted my comment from blog       | Completed ✅ |

#### 🌙 UI / UX

| Feature                 | Test Performed                                                                 | Outcome    |
|--------------------------|-------------------------------------------------------------------------------|------------|
| Light / Dark mode Switch | I tested that the different modes worked as should and ensured all text was readable in both modes | Completed ✅ |
| Responsive Design        | Tested my blog across multiple devices and used google chrome inspect view to view my blog in responsive mode | Completed ✅ |


### Lighthouse

### Desktop

![Lighthouse - Desktop](https://github.com/user-attachments/assets/41f30220-ddaf-47d9-ab13-93323a99f54f)

### Mobile

![Lighthouse - Desktop](https://github.com/user-attachments/assets/de1cc564-52cc-4c1b-8ac9-9ab2caf9f02a)

### CI Python Linter

### forms.py

![Screenshot 2025-07-12 at 23 45 13](https://github.com/user-attachments/assets/55134698-6ad6-40d8-8d2a-7ff923aad759)

### Admin.py

![Screenshot 2025-07-12 at 23 43 50](https://github.com/user-attachments/assets/634699cf-7a9e-438a-8a98-2413f75e9ef5)

### urls.py

![Screenshot 2025-07-12 at 23 41 26](https://github.com/user-attachments/assets/9066f6e9-78f4-4753-805a-5bfad76060f9)

### models.py

![Screenshot 2025-07-12 at 23 37 55](https://github.com/user-attachments/assets/df5104b4-d7a2-4c1a-ae9b-ffe09f4d4d30)

## Feedback

The only feed back i got was to do with the darkmode icon while on mobile screens it was displaying outside of the hamburger menu causing the alignment to be out.

![IMG_8472](https://github.com/user-attachments/assets/00677a49-3e75-499b-807a-07ff3ff4cc4c)

This was fixed but replacing the line of code for the darkmode item within the nav items section, by doing this the icon is hidden within the hamburger menu and the hamburger menu icon is back in the original position of the top right hand side.
![IMG_8486](https://github.com/user-attachments/assets/5e8963fb-d367-443e-b1af-516e133604c5)

## Tech Stack

- Django 5.0.14

- HTML
- CSS / Bootstrap 5
- JavaScript
- PostgreSQL
- Heroku (deployment)

## Resources

- Code Institute
  - Love Sandwiches
  - I Think Therefore I Blog

- Djnago 5 By Example by Antonio Mele

- Documentation for Django - <https://docs.djangoproject.com/en/5.2/>
  
- Stack Overflow

## Credits / Tutorials

### Source used

- Correy Schafer - Python Django Tutorial: Full-Featured Web App Part 10 - Create, Update, and Delete Posts
[Watched on YouTube](https://www.youtube.com/watch?v=-s7e_Fy6NRU&list=PL3ogf06gmD4herEB1HXBkfFBsTtZjGBuh)
I used this tutorial to help implement the functionality for users to add blog posts. The tutorial served as a guide, and I adapted the code to fit the needs of my project.

- Django Documentation – Limiting QuerySets
[Limiting QuerySets](https://docs.djangoproject.com/en/5.2/ref/models/querysets/#limiting-querysets)

   I referenced this documentation to learn how to limit the number of posts shown on the homepage. I modified the example code to display the latest 3 posts in    my own template.
  
- stack overflow - Show latest blog posts
[Show latest blog posts](https://stackoverflow.com/questions/75190346/way-to-show-latest-4-blog-posts-on-my-page)

   Question by David Henson, answered by Mas Zero. I used this as a reference for structuring the query and template logic to display the most recent posts. The    code was adapted to suit my models and template structure.

- Blog Posts are from ChatGPT
