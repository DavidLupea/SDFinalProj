# Monday.com Productivity Manager by Mathamphetamine

* David Lupea: Project Manager
* Mohidul Abedin: Database/Flask Work
* Devin Lin: HTML/Bootstrap Work
* Brian Moses: Database Operations

## This website allow you to
* Create and manage projects with other members
* Allow members to create and delegate tasks with deadlines
* Allow people to set locations for meetings 
* Once people complete a task, they recieve points which can then be redeemed on some anti-productivity services (reddit posts and Pokemon backgrounds)

## APIs Featured
* [MapQuest Place Search](https://docs.google.com/document/d/1s0pH9YNA_j9r2tTLWS5gOZhO5M40VFZID99lQ9LsO44/edit)
This API will allow people to set meeting locations.

* [Google Calendar](https://docs.google.com/document/d/1atMCAui86AwBSWEz8lCIJFaNkUL4V5fwVecNcnxSpP0/edit)
This API will put incoming tasks at meetups on the person's Google Calendar.

* [Reddit](https://docs.google.com/document/d/1YvhzlfshJvUZ_7GWKKUiI0KUppHE-Ee_l4Xp3jMJuFc/edit)
This API will be used to fetch some popular posts from a user's subreddit of choice. When this happens, the user will be shown these posts as a reward for their productivity.

* [Pokemon API](https://docs.google.com/document/d/1EKiVhWTMo_SuI1Gs8DcHxlvQl2XnFe0mqs9oLaQlaRU/edit)
This API will be used to get the user a random Pokemon for their inventory when they complete five tasks.


# How to install and run

First, you will need to obtain a MapQuest API key. 

* Navigate to [their site](https://developer.mapquest.com/plan_purchase/steps/business_edition/business_edition_free/register)
and create an account. The information entered does not have to be accurate in order to obtain a key. 
* You should be taken to a new page titled "Manage Keys". 
* Click on the "My Applcation" tab in the middle. 
* The string of letters and numbers next to "Consumer Key" is your API key.


Second, open your terminal. Then, type in the following commands sequentially:

* git clone https://github.com/DavidLupea/SDFinalProj.git
* cd SDFinalProj
* pip3 install -r requirements.txt
* python3 app.py

Then, navigate to 127.0.0.1:5000 in a web browser. Copy and paste your MapQuest API key into the space indicated on the website.
