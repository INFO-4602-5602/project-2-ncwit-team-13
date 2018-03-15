# Project 2
<h2>Project 2: Group 13</h2>
Bret McSpadden
Jen Liu
Jordan Wirfs-Brock
Justin Chin
Will Temple

<h2>Overview: </h2>
To begin the process our group worked individually and then met via Skype and after class to brainstorm initial ideas. After speaking with Lecia, we worked in groups of 2 (Justin/Bret, Will/Bret, and Jordan/Jen) to design 4 visualizations. Throughout the process we met as a group after class, and in groups as needed. We also collaborated over Slack and GitHub. 

<h2>Visualization Descriptions</h2> 
<h3>Visualization 1 - Retention/Institution, Male/F/Tot. (Not Pictured)</h3>
<p>This visualization allows the user to view retention rates for men, women, and all students among extension service schools with CS majors. The user can select which set of data to view via the drop-down menu and can view all the institutions as well as individual schools.
 
Design Process
We began by looking over the data and designing questions to answer with the data, as well as questions about the data. After meeting with Lecia from NCWIT, we took her guidance and attempted to generate more questions that we could answer through visualization.

Because Lecia was focused on retention, we decided to attempt to tackle that problem. Justin and Bret met on Sunday to further analyze the date and begin cleaning the data. We decided to focus on “Extension Service” schools because the data was better. We also only looked at data beginning in school year 2007 to 2008 since that is when the extension services began, and again, the data seemed more complete. Finding total enrollment year to year was a challenge as there was no total for male or female enrollment, and it was not clear which numbers should be added or subtracted to find a total. We decided to calculate enrollment as Different Major + Same Major – Graduated – New Enrollment – Transfer Enrollments. We did this for Males, Females, and added for a Total. We used Tableau to do calculate male and female enrollment and plotted the data in a bar graph. Again, it was clear the data was a bit funky prior to 2007. 

We further outlined our idea by working through the data cleaning steps to filter the data in Python to automate our calculations: filtering out “Extension Services”, including years 2007-2008 to 2015-20016, and calculating Male, Female, and Total enrollment. From there we had to calculate retention, which we defined as Year2/Year1=Retention. Iterating through the data presented a challenge as we did not know the Panda library functions to go through each institution by year, calculate retention rate each year starting in year 2 and then moving on for further years until the data for that institution ended. We had to further filter the data by “Major Program Name” to eliminate a problem having multiple records under the same year for the same institution. 

Overall, after filtering, it was obvious that the data was still incomplete. Our formula for the totals was also uncertain. Regardless, we went ahead and created an interactive chart that allows the user to view total enrollment retention, as well and individual male and female retention in order to get a better idea of Bokeh and using it to display charts. When viewing each set, individual schools can be selected and viewed individually.</p>


Your project must:
<ul>
<li> Include a README.md file that outlines:
  <ul>
  <li>Information about your visualizations and what they show. Include information about interactions as appropriate.</li>
  <li>Your design process (e.g., how did you go about designing, building, and refining your system? Why did you choose these representations?)</li>
  <li>Your team roles for each individual</li>
  <li>How to run your project</li></ul></li>
<li>Include at least three unique visualizations:
  <ul>
  <li>One visualization must include some element of time</li>
  <li>One visualization must not include any elements of time</li>
  <li>Each visualization must be interactive</li>
  <li>Your set of three visualizations should support at least one meaningful comparison between related data attributes</li>
  <li>Your set of three visualizations should visualize at least five data attributes total</li></ul></li>
<li>Be able to work with any dataset of this format (e.g., the numbers are interchangable but the columns and document titles are fixed).</li>
</ul>

<h2>Above and Beyond:</h2> 
The above requirements are the minimum for a passing grade on this project. Some ideas to improve your project include:<ul>
<li>Dashboarding: Show all three visualizations as part of the same screen.</li>
<li>Added Visualizations: Provide more than three visualizations</li>
<li>Dynamic Queries: Including UI widgets that allow you to change the current data field</li>
<li>Missing Data: Not all rows have data for all columns. Design ways of handling missing data intelligently.</li>
<li>Coordinated Views: Have two or more visualizations that interact with one another as you move through the data.</li>
<li>Overview+Detail: Provide a pair of views that allow viewers to retain context as they navigate your data.</li>
<li>Style: Keep the style consistent across all your views, with an eye towards intelligently applying visual design.</li></ul>

<h2>Platforms:</h2> 
You can use any development platform you'd like so long as it is not proprietary (exception: MatLab as we have a University License). Your project readme should include step-by-step instructions on how to run your projects and it should run without me having to modify the code. You are welcome to use different platforms for each visualization.

Some platforms to look at include:
<ul>
<li>D3</li>
<li>R with ggplot</li>
<li>WebGL or Three.js</li>
<li>Processing or ProcessingJS</li>
<li>Google Maps API</li>
<li>Open Street Map API</li>
<li>Bokeh</li>
<li>Creatively engineered tangible/audio artifacts</li>
</ul>

If you would like to use a platform that will push you in creative ways but may not support all of the requirements of the project, please come talk to me. 

<h2>Submissions:</h2>
All submissions must be made through GitHub with a timestamp by 11:59pm on 3.16. Your submission files should include:
<ul>
<li>Your README</li>
<li>Your code and/or project</li>
</ul>
Note that each group only needs to submit one file. 

Each member of the team should also send me a project post-mortem through email with the subject line "INFO 4602/5602: Project 2" documenting the following:
* What you worked on in the project
* What your teammates worked on in the project
* How you would rate your performance and why
* How you would rate each teammates' performance and why

These documents will be kept confidential and will factor into project grades. If you feel all of the team worked hard and performed well, please don't hesitate to tell me that (no curving is necessary on performance reviews :-))! Also, please keep in mind that different team members have different skillsets, roles, and experiences.

<h2>Grading: </h2>
The project will be scored out of 100 points total. Your project will be graded on four different criteria:
<ol>
<li> Creativity</li>
<li> Technical execution</li>
<li> Design (both aesthetic and your visualization choices)</li>
<li> Project Post-Mortems</li>
</ol>
