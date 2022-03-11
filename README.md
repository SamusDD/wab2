# wab2
A simple warhammer 40k army builder 

(Please note all images referenced can be found here: https://docs.google.com/document/d/1Q5xDq0PDe8swj5jxfoWbdMV5b0iB629JxO1lWtnjDyE/edit?usp=sharing)



Why am I doing this?

I am doing this as a test of my knowledge learned during my time with QA, to gauge my understanding of the different parts of building an multi-relational database integrated with app, using version control on github, MySQL, Python, Jenkins and Junit tests.



The Project:

A short description of the project would be to build an app that can persist data in an SQL database, I chose to create an army builder of Warhammer 40k units.
Initially I started with an ERD of only two tables, Armies and Units, with a one to many relationship (One army can have many units, shown diagram 1). I considered that if I wanted to go beyond the MVP (minimum viable product outlined) that a third table could be populated with weapon information, allowing the user to fully customise each units loadout. This would be a one to many relationship, as one unit could carry many weapons (shown with diagram 2).



Project CI Pipeline:

It is important with any project to track goals and progress made, I chose to use a Kanban board on Jira to track my project. I created a number of user stories that I thought a user might want from my app, as well as a number of tasks which reflected those user stories.

Here is a link to my Jira: https://abi-hunt.atlassian.net/jira/software/projects/WAB/boards/2 (Unsure if I need to add you as a collaborator?) 

I have also added diagrams 3 and 4 to the google doc as a further display of my use of Jira.

I certainly had an issue with staying on top of my work with Jira. I am not used to keeping track of my progress on a regular basis so remembering to update my finished tasks was an issue. 

There are also a few user stories and features that Intended to add and finish as stretch goals, however I ran out of time.

I used a version control system on Github to do my best to adhere to the feature-branch model. While I was mostly successful in this, I think an issue occured on the end of Git-hub at one point. Looking at diagram 5, you can see that the feature1 branch has not been merged back into main, this is because I ended up with merge conflicts due to a huge delay in a pull request on github. I made a push for a few changes, assumed I had made a mistake and committed nothing due to the lack of pull request. By the time the pull request had come in I had started another feature branch and merged it.

During development I used a python3 virtual environment (venv). This is simply because it is a more convenient and secure way of developing an app without causing problems to the app or risking security issues.

I was supposed to use Jenkins as a build server which provides an automated build of the server as well as testing, however due to technical difficulties and time constraint I was unable to fully implement the build. However diagrams 6-9 show that the jenkins build server was ready and available with the correct settings.



Risk Assessment:

Before I started building the app I created a list of problems I might face during my work.
I implemented this into a risk assessment matrix with a key highlight the issues which I considered to be most probable, as well as possibly the most damaging. I also suggested possible fixes/preventative measures that could be taken to lower the level of risk I would face during my project.

This matrix can be seen in diagram 10.



The core app and problems faced:

Due to a last minute technical difficulty, I was unable to fit in the build server as mentioned, as well as being unable to do any testing.

In diagram 11 you can see the extent of my technical difficulty (Luckily, this happened after a push so the majority of my code is unhindered, however it has affected my ability to show that my sqlite database was consistently holding data, had full CRUD functionality and I was in the process of implementing an interface for creating units (as it was by far the larger of the two tables).

If you look closely at diagram 11 you can see that the html files I had created to format my table and form layout have been deleted. I believe I was prompted with something while typing and my fat fingers pushed a 'response' so to speak, and now I am unable to bring those text files back on my local repository (I tried git pull, and I am afraid to try git merge incase it deleted my html filed on my remote repository also).

Unfortunately due to this issue I was unable to get screenshots of my data persisting or my CRUD functionality in action. However, I was able to screenshot functional CRUD through my terminal while running commands. (still after the issue, so no fancy form to use, sadly.)



Lessons learned:

I could absolutely manage my time better as I initially underestimated the amount of work this required. Also, as what happened to me, there is always the chance of technical difficulty or bad luck which could hinder a project. If given the opportunity I will invest far more effort and time into a project earlier on in the development cycle so that I am not rushed into a bad product at the end.





