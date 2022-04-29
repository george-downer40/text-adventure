# Adventure Game

- [Adventure Game](#adventure-game)
  * [ReadMe Contents](#readme-contents)
    + [Introduction](#introduction)
    + [Technologies Used](#technologies-used)
    + [Features](#features)
    + [Testing](#testing)
      - [Bugs](#bugs) 
      - [Restrictions](#restrictions)    
    + [Deployment](#deployment)
    + [Credits](#credits)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>

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

![dictionary](/assets/images/castle_knightmare_flowchart.png "PLAYER_STATS dictionary")

The game provides the user with choices to make them feel more involved in playing. Some of these affect chance based outcomes whereas others are based on skill / knowledge.

![chance](/assets/images/castle_knightmare_flowchart.png "chance based outcome")

![knowledge](/assets/images/castle_knightmare_flowchart.png "skill / knowledge based outcome")

## Technologies Used

* Ecotrust-Canada Markdown (update with link and explanation)





## Testing
### Bugs
While writing the README document, I was unable to see a preview in Gitpod. This meant in order for me to check the layout of my README file, I had to commit each change, push that version, and view the README in the Adventure Game Github Repo.


## Deployment

as of 25/04/22, due to an issue with Heroku and Github (a recent security attack), Heroku have removed removed the ability to automatically login to Github from their site. This means that the method described in the Love Sandwiches project no longer works. You currently cannot deploy apps from the Heroku dashboard, nor will those apps automatically update/redeploy in the future. A workaround was provided in the Code Institute Slack Announcements channel. The current method is as follows:

* ADD STEPS BEFORE SUCH AS CREATING NEW HEROKU ACCOUNT AND IF ANY DEPENDENCIES OR INSTALLS MADE, USING THE COMMAND 'PIP3 FREEEZE > REQUIREMENTS.TXT
* Run the command heroku login -i in the terminal in your Gitpod workspace and login when prompted. 
* Run the command heroku create your_app_name_here to create a new app, replacing your_app_name_here with the name you want to give your  app. In this specific case the command heroku castle knightmare was used. 
* This will create a new Heroku app and link it to your Gitpod terminal. You can then access the app via the Heroku dashboard and set up your config vars.
* EXPLAIN ANY CONFIG VARS THAT WERE USED. IF NONE, DO NOT FORGET THE KEY: PORT / VALUE: 8000 CONFIG VAR
* ANY OTHER STEPS?


## Credits

INCLUDE ANY TUTORIALS USED IN THIS FORMAT

* NAME OF TUTORIAL: [YouTube Video](LINK TO VIDEO)