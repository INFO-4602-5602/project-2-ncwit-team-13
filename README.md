# Project 2
<h2>Project 2: Group 13</h2>
<p>Bret McSpadden</p>
<p>Jen Liu</p>
<p>Jordan Wirfs-Brock</p>
<p>Justin Chin</p>
<p>Will Temple</p>

<h2>Overview: </h2>
To begin the process our group worked individually and then met via Skype and after class to brainstorm initial ideas. After speaking with Lecia, we worked in groups of 2 (Justin/Bret, Will/Bret, and Jordan/Jen) to design 4 visualizations. Throughout the process we met as a group after class, and in groups as needed. We also collaborated over Slack and GitHub.


<h2>Visualization Descriptions</h2>
<h3>Preliminary/Exploratory Visualizations</h3>
<p>The following visualizations shows the average Female GPA by Major (Computer Engineering, Comupter Sciecne, Mechanical Engineering) by year, and college standings </p>

<p>Design Process</p>
We began by looking over the data and designing questions to answer with the data, as well as questions about the data. After meeting with Lecia from NCWIT, we took her guidance and attempted to generate more questions that we could answer through visualization.
Because Lecia was focused on retention, we decided to attempt to tackle that problem. Justin and Bret met on Sunday to further analyze the date and begin cleaning the data. We decided to focus on “Extension Service” schools because the data was better. Initial graphs using the raw data built in Tableau also showed that many schools did not provide data before 2007/2008 since that was when the extension services began, and more data was provided by consultants from the program.  The graph shown is one example where the schools did not provide data for years before 2007/2008.

![alt text](https://github.com/INFO-4602-5602/project-2-ncwit-team-13/blob/master/avg-gpa-major-year-college.PNG "Average Female GPA by Major (Computer Engineering, Comupter Sciecne, Mechanical Engineering) by Year, and College Standings ")

Finding total enrollment year to year was a challenge as there was no total for male or female enrollment, and it was not clear which numbers should be added or subtracted to find a total. We decided to calculate enrollment as Different Major + Same Major – Graduated – New Enrollment – Transfer Enrollments. We did this for Males, Females, and added for a Total. 

The calculation for Male and Female enrollment for each year, was applied to create a new metric in the data.  The raw dataset was processed using Panda's library to automate our calculations: filtering out “Extension Services”, including years 2007-2008 to 2015-20016, and calculating Male, Female, and Total enrollment. We also calculated retention, which we defined as Previous Year / Current Year = Retention. For records where different enrollment data used to calculated total enrollments was not provided, we decided to use 0 as a placeholder.  We had to further filter the data by “Major Program Name” to eliminate a problem having multiple records under the same year for the same institution.

After our initial preprocessing of the data, it was obvious that the data was sparse, due to records missing/incomplete data provided by the schools, or not having enough year after year data.  This preprocessed data was plotted using Bokeh in a [Jupyter Notebook] (https://github.com/INFO-4602-5602/project-2-ncwit-team-13/blob/master/Jupyter%20Notebooks/Retention%20by%20Gender%20Graphs.ipynb), allowing the user to view total enrollment retention, as well and individual male and female retention to view the difference between Male, Female and Overall Retention for the filtered institution, and years 2007-2015.  This initial attempt to calculate retention and graph the Male and Female retention brought up additional questions about the data and helped give direction to what attributes should be filtered for the other visualizations.

![alt text](https://github.com/INFO-4602-5602/project-2-ncwit-team-13/blob/master/interactive-bokeh-plot.PNG "Male/Female/Overall Enrollment by Institution and Year")

</p>

<h3>Visualization 1 - Attrition/Institution, Male/F/Tot.</h3>
<p>This visualization is a bubble chart showing attrition for each major from institutions that have enough data to calculate attrition. Each circle represents a major, with the size of the circles encoding the total number of STUDENTS enrolled in that major. The color scale displays whether the major has higher attrition for males or females, with more x showing higher levels of female attrition and x showing higher levels of male attrition. The user can mouse over to display the male, female, and total attrition for each major. When the circle is clicked the display zooms in on the data for that major, displaying each the specific information for each institution.</p>

<p>Design Process</p>
This design built on Justin and Bret’s exploration and attempts to calculate and display retention rates in a line graph. Bret and Will met on Monday and discussed better ways to calculate retention and alternatives to using a line graph as the graph was muddled and spaghetti like, and hard compare the information among schools. After discussing the challenges Justin and Bret were having, Will devised a better way calculate attrition using Total Declared Major and Left Institution data. He also cleaned the data well, making sure to only pull from institutions matching our unique key and with data to compare year over year. After the initial calculations, we also corrected for a few places with zeros and where the calculation was below zero or over one, indicating a problem with the data. We further refined the data correcting for irregularities in naming NCWIT Participant type and Major Program Name. Major Program Name was unique as there were many variations among the CIP code and program name.

After exporting the csv with the cleaned data, we used Tableau to prototype the bubble chart. Here we added the color features and discussed the possibility of further interaction via clicking on each circle to display the data within each major.
</p>

<p>How to run</p>

<h3>Visualization 2 - Male/Female GPA Over Time</h3>
<p>This visualization is a simple line chart with GPA plotted on the x-axis and year on the y-axis. GPA is calculated per major. The user can scroll through the years using a scroll tool for the x-axis to show individual years.</p>

<p>Design Process</p>
After working on the attrition visualization, we needed to complete one additional visualization to have 4 visualizations as Jen and Jordan were working on 2 as well. We decided to use GPA and time to have a simpler calculation and look at a potentially less specific data since the attrition calculation eliminated around 1500 rows of data.

We drew the visualization on a white board, showing the line graph, plots for M and F GPA over time, and the interaction of scrolling trough the data. Will then looked for examples for building the slider in D3.
</p>

<p>How to run</p>

<h3>Visualization 3 - Violin Plot</h3>
#Description
<p></p>

<p>Design Process</p>



</p>

<p>How to run</p>

<h3>Visualization 4 - Interactive line graph with sound</h3>
#Description
<p></p>

<p>Design Process</p>


</p>

<p>How to run</p>



<h2>Team Roles: </h2>
<p>Bret – Documented project. Helped organize meeting, work on analyzing data, and designing visualizations.</p>
<p>Jen – Worked on analyzing data and designing visualizations. Designed color palette and built physical visualization.</p>
<p>Jordan – Worked on analyzing data and designing visualizations. Built violin plot visualization.</p>
<p>Justin – Worked on analyzing data and designing visualizations. Assisted cleaning data and working with Bokeh and other libraries to assist building visualizations.</p>
<p>Will -Worked on analyzing data and designing visualizations. Built attrition and GPA visualizations.</p>



<h2>Above and Beyond Included:</h2>
The above requirements are the minimum for a passing grade on this project. Some ideas to improve your project include:<ul>
<li>Dashboarding</li>
<li>Added Visualizations: 3+1</li>
<li>Dynamic Queries: Zoom in on major in visualization 1.</li>
<li>Missing Data: We filtered data that did not include all the parameters, threw out zero values, and filtered outliers that did not make sense due to bad data.</li>
<li>Coordinated Views: ??  Have two or more visualizations that interact with one another as you move through the data.</li>
<li>Overview+Detail: Highlight declaration year in visualization 3, greying out background information.</li>
<li>Style: Color palette and font are the same.</li></ul>