# Castle Knightmare

- [Castle Knightmare](#castle-knightmare)
  * [Introduction](#introduction)
  * [User Stories](#user-stories)
  * [Features](#features)
  * [Technologies Used](#technologies-used)
  * [Code Validation](#code-validation)
    + [Restrictions](#restrictions)
  * [Testing](#testing)
    + [Bugs](#bugs)
  * [Deployment](#deployment)
  * [Credits](#credits)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>



[Link to Heroku app](https://castle-knightmare.herokuapp.com/)

[Link to Github Repo](https://github.com/george-downer40/text-adventure)

## Introduction

I have chosen to create a Python based text-based adventure game for my porfolio project 3. It is largely inspired by traditional fantasy tropes such as Dungeons & Dragons, but also an old children's tv show called Knightmare [Wikipedia link](https://en.wikipedia.org/wiki/Knightmare). This show had a team of contestants guide another player through a series of rooms in a dungeon / castle, with the team having to describe the room and it's contents to the player. 

This game will guide the player through a dungeon, in which they will encounter monsters, traps and a final scenario. There will be 2 stats used during the game; vitality and luck. The player will be able to raise and lower vitality through different scenarios encountered in the game. The game is won if they can pass obstacles in the dungeon and reach the final room. The game is lost if they run out of health, or fall victim to a trap.

In order for me to creat the game and work out the correct paths, I created a flow chart using Lucid Chart. This helped me to work out what functions I needed, where player input would be needed and how to increase replayability.

![flow chart](/assets/images/castle_knightmare_flowchart.png "Lucid Chart flow chart")

## User Stories

* As a fan of the TV show Knightmare, I'd like to play something that invokes nostalgia for the show.
* As a retro gamer, I'd like to play an old style text adventure game.
* As a casual user, I'd like something that will generate my interest and make me want to play more than once.

## Features

The game uses a variable dictionary with 2 keys; vitality and luck. These are used throughout the game to determine outcomes in scenarios.

![dictionary](/assets/images/dictionary.png "PLAYER_STATS dictionary")

The game provides the user with choices to make them feel more involved in playing. Some of these affect chance based outcomes whereas others are based on skill / knowledge.

![chance](/assets/images/chance_based_element.png "chance based outcome")

![knowledge](/assets/images/knowledge_element.png "skill / knowledge based outcome")

## Technologies Used

* Ecotrust-Canada Markdown
* Python
* Github
* Gitpod
* Heroku
* Lucid Chart

## Code Validation

The python script was run through the PEP8 online validator and no errors were raised.

JShint, W3C validator and Jigsaw validator were not used as part of my code validation, as the relevant code from the Code Institute template was not changed and is not required for this project.

### Restrictions

As the only code to be written for this project was in Python, the responsiveness of the Heroku app may not be ideal on any devices other than desktops.






## Testing

The script was run multiple times in the Gitpod workspace, with every combination of routes tried multiple times to ensure there were no errors or dead ends in the code. It was also tested to ensure the game balance was correct and the game is enjoyable.

### Bugs

While writing the README document, I was unable to see a preview in Gitpod. This meant in order for me to check the layout of my README file, I had to commit each change, push that version, and view the README in the Adventure Game Github Repo.

When I initially tried to deploy my app on Heroku I received a message saying Application Error. This was because Heroku wasn't recognising Node in the buildpack properly. I contacted Tutor Support and they identified that it was an issue with my procfile. I pasted in the version they sent to me into my workspace and this resolved the issue.

## Deployment

as of 25/04/22, due to an issue with Heroku and Github (a recent security attack), Heroku have removed removed the ability to automatically login to Github from their site. This means that the method described in the Love Sandwiches project no longer works. You currently cannot deploy apps from the Heroku dashboard, nor will those apps automatically update/redeploy in the future. A workaround was provided in the Code Institute Slack Announcements channel. The current method is as follows:

* create a profile on the Heroku website.
* Run the command heroku login -i in the terminal in your Gitpod workspace and login when prompted. 
* Run the command heroku create your_app_name_here to create a new app, replacing your_app_name_here with the name you want to give your  app. In this specific case the command heroku castle-knightmare was used. 
* This will create a new Heroku app and link it to your Gitpod terminal. You can then access the app via the Heroku dashboard and set up your config vars.
* The only config var needed for this deployment was key: PORT value: 8000
* In the gitpod workspace terminal type git push heroku.main. This pushes all the relevant information to the Heroku site.
* On the Heroku site, on the castle-knightmare app, click on the open app button. This will launch the app in a separate tab.


## Credits

Stack Overflow for various queries and code errors, particularly this one for replacing a value in a dictionary:
* [Python dictionary replace values](https://stackoverflow.com/questions/19773669/python-dictionary-replace-values)

The code institute slack community for helping inspire me to choose a text based adventure for this project.

The code institute tutor support team for helping me solve the bug of my Heroku app not deploying properly.

My mentor Rohit for helping me create a function to refactor my code.
