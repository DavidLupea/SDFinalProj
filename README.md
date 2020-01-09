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
* [IPIFY](https://docs.google.com/document/d/1BBvfxdZET9g7_cKUSUg2so8tvCKWudvVfdHktfMRClg/edit)

Used to obtain IP address of visitor to site

* [MapQuest Place Search](https://docs.google.com/document/d/1s0pH9YNA_j9r2tTLWS5gOZhO5M40VFZID99lQ9LsO44/edit)
* [MapQuest Traffic](https://docs.google.com/document/d/1HZm1bCq7ZOP-POWJMfX13w72XxBn3ejaXkun-KOv_rk/edit)

These are MapQuest APIs which take location and return information about 1) traffic, and 2) businesses in your area

* [MetaWeather](https://docs.google.com/document/d/18uyXB5XPFQoGFJpoa2yQvRPhevc3HaBU4kO-OYN-ieY/edit)

Provides weather in your area based on location.


* [IPAPI](https://docs.google.com/document/d/1FazBlCH4SoM5bKaCs5vr4B7aEgTUVlvFv-1W-LoQmUA/edit)

Provides data on a given IP address (lat, long, country, state, internet service providor)


# How to install and run
First, you will need to obtain a MapQuest API key. 

* Navigate to [their site](https://developer.mapquest.com/plan_purchase/steps/business_edition/business_edition_free/register)
and create an account. The information entered does not have to be accurate in order to obtain a key. 
* You should be taken to a new page titled "Manage Keys". 
* Click on the "My Applcation" tab in the middle. 
* The string of letters and numbers next to "Consumer Key" is your API key.

Second, open your terminal. Then, type in the following commands sequentially:

* git clone https://github.com/athompson00/Friday_Cat_Damage.git
* cd Friday_Cat_Damage
* python3 -m venv superhero
* . superhero/bin/activate
* pip install -r doc/requirements.txt
* python3 app.py

Then, navigate to 127.0.0.1:5000 in a web browser. Copy and past your MapQuest API key into the space indicated on the website.
