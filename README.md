![Screenshot 2022-05-17 at 10 38 51](https://user-images.githubusercontent.com/93173575/168781385-45998e52-8785-4e1d-8c7a-cb1c5e1636b4.jpg)


# Alien GamePy

A backend turn based Python Game where the player can battle against Xenomorph XX121!

Live site [here](https://alien-gamepy.herokuapp.com/).

## Table of Contents

- [User Experience (UX)]()
- [Design]()
- [Features]()
- [Languages]()
- [Programs]()
- [Testing]()
- [Deployment]()
- [Cloning]()
- [Credits]()

# User Experience (UX)

## User Story

### Intended Audience

The intended audience is for children (7+) and adults of all ages. 

This is a turn based game where both the Player and Alien start with 100 Health. The players Attack yields 10 damage to the Alien's health whereas the Alien has a dymanic level of attack ranging randomly from 7 to 16! 

The player can opt, instead of an Attack, for a Heal which replenishes health by 12. Let's hope the Alien's return attack is less than 12!!

The first to deplete their health to 0 looses the battle.

# Design

The player is greeted with a Welcome to Alien GamePy message, ASCII Alien Art along with a player name input.

<img width="550" alt="1" src="https://user-images.githubusercontent.com/93173575/168786948-370d11aa-4ba9-409f-b626-7f5b1cead406.png">


Here's the Player (Dallas) enters his name and 4 actions options are loaded up.

<img width="555" alt="2" src="https://user-images.githubusercontent.com/93173575/168786959-8c3239b1-46b5-4377-8776-24c2e104aeb5.png">


The Player chooses action 1. Attack and we can see the Player recieved 13 damage to his health and the Alien recieved 10 as expected.

<img width="553" alt="3" src="https://user-images.githubusercontent.com/93173575/168786978-daae18cd-2892-4b20-8d41-f2faaffe0f9b.png">


Here the Player chose action 2. Heal and we can see the Alien didnt recieve damage and Player was healed and subsequently attacked by the Alien

<img width="564" alt="4" src="https://user-images.githubusercontent.com/93173575/168786996-2ed5b791-4515-4ead-9c17-e1e7a0425300.png">


The game continued on until a winner was declared and new Player Bob entered his name and checked previous players stats. Included are previous players name, what their remaining health was and how many rounds the battle took.
<img width="555" alt="5" src="https://user-images.githubusercontent.com/93173575/168787011-ffd7af90-9cbb-4081-a411-cee222c088f8.png">

## Flowchart

Lucidchart a diagramming application was used to create the flowchart for the game
![Flowchart pp3 (1)](https://user-images.githubusercontent.com/93173575/168798240-4be911da-d948-4812-aca7-f3bf2cacdc81.png)

# Features

## - Health level

- The Health level of both Player and Alien is updated after every turn.

## - Player Stats

- Player stats (name, health and rounds) are recorded so players can easily compare stats to other players.

## - Heal

- Heal action grants the player 12 extra health.

# Technology Used

## Languages

- Python

![pnghut_programming-python-logo-language-computer-imperative-yellow](https://user-images.githubusercontent.com/93173575/168800528-edce3989-e5a3-467d-8e01-57f479d33372.png)

## Programs

- [GitPod:](https://gitpod.io/) was used as the main language editor for programming the project.
- [GitHub:](https://github.com/) was used to back up instances of the GitPod repository.
- [Flowchart](https://www.lucidchart.com/) was used for flow structure on the project.
- [PythonTutor](https://pythontutor.com/) was used for to see a visualised step by step of executed Python code.

# Testing

## Devices used

### MacbookPro 

- The game was tested on an MacbookPro. The game was fully responsive on Google Chrome, Brave & Firefox. The game loaded on Safari but the keyboard was unresponsive.


<img width="909" alt="Screenshot 2022-05-17 at 12 43 40" src="https://user-images.githubusercontent.com/93173575/168803453-8de3470a-15be-4b6a-a5fe-7d81153715f1.png"> <img width="913" alt="Screenshot 2022-05-17 at 12 44 17" src="https://user-images.githubusercontent.com/93173575/168803459-1e76df6c-b4f9-4315-9718-987ce04edbf1.png">
 
 ### Samsung Galaxy Note 20 Ultra
 
 
 - The test on Galaxy Note using Google Chrome & Firefox browsers showed the game to be responsive and in working order. 

![My project](https://user-images.githubusercontent.com/93173575/168805776-9a47eab1-81e2-4182-a8a2-38090b3da077.png)

![My project (1)](https://user-images.githubusercontent.com/93173575/168806043-6421ea62-60a8-4971-84ef-7cf4ff29ad30.png)


## Bug Testing

Bugs were introduced to the code when trying to refactor the code in order not to exceed the 80 character line limit in GitPod.
After noticing that the Alien was not taking damage code was rewriiten to not exceed the line limit and the Alien was able to recieve damage.

Errors were created when importing the ASCII Alien Art. Triple Quotation marks were removed and periods were put after every line ending with a backstroke.

## Python Validation

- [PEP8 online](http://pep8online.com/)
No errors were found.

![PEP8 Online-resized](https://user-images.githubusercontent.com/93173575/168808097-a81d8a41-2a97-411d-8d0d-c95c8a167ba1.jpg)

# Deployment

Due to a security issue, Heroku has disabled automated deployments from GitHub. In order to deploy while this situation persists, the following the steps below were used to deploy from the Gitpod workspace:

Open the terminal.

Log in to Heroku and enter details.

```
heroku login -i
```

Get app name from heroku.

```
heroku apps
```

Set the heroku remote. (Replace <app_name> with actual app name and remove the <> characters)

```
heroku git:remote -a <app_name>
```

Add and commit any changes to code if applicable

```
git add . 
```
```
git commit -m "Deploy to Heroku via CLI"
```

Push to both GitHub and Heroku

```
git push origin main
```
```
command: git push heroku main
```

## GitHub

For deployment of the website to a live publicly accessible website, the following steps were required:

- Confirmed that correct repository is selected as 'rock_paper_scissors'.
- Select 'Settings'.
- Scroll down to 'GitHub Pages' and click on 'Check it out here!'.
- On the 'Source' section, select Branch as 'main' and click on 'Save'.
- Your site is published at 'https://alien-gamepy.herokuapp.com/'

## Gitpod

For deployment of the website to a local environment, the following steps were required:

- Confirmed that correct repository is selected as 'alien-gamepy'.
- To run a new Python server, open a terminal window and type the following code and hit enter:
  python3 run.py

# Cloning 

To clone a copy of the code in the repository, the following steps are required:

- Go to https://github.com and select the Repository called 'rock_paper_scissors'
- Click on the button called 'Code" and a pop-out window will show options to Clone through: 
   - HTTPS
   - SSH
   - GitHub CLI

1. On GitHub.com, navigate to the main page of the repository.
2. Above the list of files, click Code.
3. To clone the repository using HTTPS, under "Clone with HTTPS", click 'Clipboard to copy'. To clone the repository using an SSH key, including a certificate issued by your organization's SSH certificate authority, click Use SSH, then click 'Clipboard to copy'. To clone a repository using GitHub CLI, click Use GitHub CLI, then click 'Clipboard to copy'.
4. Open Terminal.
5. Change the current working directory to the location where you want the cloned directory.
6. Type > git clone and then paste the URL you copied earlier.
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY

7. Press Enter to create your local clone.
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY Cloning into Spoon-Knife... remote: Counting objects: 10, done. remote: Compressing objects: 100% (8/8), done. remove: Total 10 (delta 1), reused 10 (delta 1) Unpacking objects: 100% (10/10), done.

8. Repository Clone is now complete.

# Credits

## Tutorials & Resources

- [ASCII Art Archive](https://www.asciiart.eu/) was used for the alien character text image on the UI.
- [PNGhut](https://pnghut.com/) was used in sourcing the Python png.
- [LucidChart](https://www.lucidchart.com/) was used for the diagramming the flow structure.
- [Academind](https://www.youtube.com/c/Academind) was used for extra tutourials


## Acknowledgements

- [Code Institute](https://learn.codeinstitute.net/)
- Thanks to fellow students in our Code Institute Slack Channels.
- Thanks to Code Institute Student Care Support & Kasia for all the help and support.
