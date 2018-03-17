# Project 2
<h2>Project 2: Group 13</h2>
<p>Bret McSpadden</p>
<p>Jen Liu</p>
<p>Jordan Wirfs-Brock</p>
<p>Justin Chin</p>
<p>Will Temple</p>

<h2>Overview: </h2>
To begin the process our group worked individually and then met via Skype and after class to brainstorm initial ideas. After speaking with Lecia, we worked in groups of 2 (Justin/Bret, Will/Bret, and Jordan/Jen) to design 4 visualizations. Throughout the process we met as a group after class, and in groups as needed. We also collaborated over Slack and GitHub.

### [You can view all of our visualizations on this page.](https://info-4602-5602.github.io/project-2-ncwit-team-13/dashboard.html)


<h2>Visualization Descriptions</h2>
<h3>Vizualization 0 - Preliminary/Exploratory Visualizations</h3>
<p>The following visualizations shows the average Female GPA by Major (Computer Engineering, Comupter Sciecne, Mechanical Engineering) by year, and college standings </p>

<p><b>Design Process</b></p>
We began by looking over the data and designing questions to answer with the data, as well as questions about the data. After meeting with Lecia from NCWIT, we took her guidance and attempted to generate more questions that we could answer through visualization.
Because Lecia was focused on retention, we decided to attempt to tackle that problem. Justin and Bret met on Sunday to further analyze the date and begin cleaning the data. We decided to focus on “Extension Service” schools because the data was better. Initial graphs using the raw data built in Tableau also showed that many schools did not provide data before 2007/2008 since that was when the extension services began, and more data was provided by consultants from the program.  The graph shown is one example where the schools did not provide data for years before 2007/2008.

![alt text](https://github.com/INFO-4602-5602/project-2-ncwit-team-13/blob/master/avg-gpa-major-year-college.PNG "Average Female GPA by Major (Computer Engineering, Comupter Sciecne, Mechanical Engineering) by Year, and College Standings ")

Finding total enrollment year to year was a challenge as there was no total for male or female enrollment, and it was not clear which numbers should be added or subtracted to find a total. We decided to calculate enrollment as Different Major + Same Major – Graduated – New Enrollment – Transfer Enrollments. We did this for Males, Females, and added for a Total.

The calculation for Male and Female enrollment for each year, was applied to create a new metric in the data.  The raw dataset was processed using Panda's library to automate our calculations: filtering out “Extension Services”, including years 2007-2008 to 2015-20016, and calculating Male, Female, and Total enrollment. We also calculated retention, which we defined as Previous Year / Current Year = Retention. For records where different enrollment data used to calculated total enrollments was not provided, we decided to use 0 as a placeholder.  We had to further filter the data by “Major Program Name” to eliminate a problem having multiple records under the same year for the same institution.

After our initial preprocessing of the data, it was obvious that the data was sparse, due to records missing/incomplete data provided by the schools, or not having enough year after year data.  This preprocessed data was plotted using Bokeh in a [Jupyter Notebook](https://github.com/INFO-4602-5602/project-2-ncwit-team-13/blob/master/Jupyter%20Notebooks/Retention%20by%20Gender%20Graphs.ipynb), allowing the user to view total enrollment retention, as well and individual male and female retention to view the difference between Male, Female and Overall Retention for the filtered institution, and years 2007-2015.  This initial attempt to calculate retention and graph the Male and Female retention brought up additional questions about the data and helped give direction to what attributes should be filtered for the other visualizations.

![alt text](https://github.com/INFO-4602-5602/project-2-ncwit-team-13/blob/master/interactive-bokeh-plot.PNG "Male/Female/Overall Enrollment by Institution and Year")

</p>

<h3>Visualization 1 - Average GPA vs. Major, by Gender</h3>
<p>This visualization is a scatterplot with major plotted on the x-axis and GPA on the y-axis. Average GPA is calculated for each instituation per major, and broken down by males and females. Individual points represent either female GPA in purple, male GPA in orange, or the cobined GPA in green for an individual institution. The size of the point represents the number of students enrolled. The user can scroll through the years using a scroll tool to display individual years and potentially see changes over time. Comparison is a bit difficult due to change blindness as well as overlap in the data.</p>

#### How to view
You can view the visualization in the dashboard. 

Use the sliter at the top to scroll through individual years. The slider also responds to the keyboard arrow keys once clicked.

Mouse over each point to display a tooltip showing the record with number of students and average GPA.

#### Design Process 
After working on the attrition visualization, we needed to complete one additional visualization as Jen and Jordan were working on 2 as well. We decided to use GPA to have a simpler calculation, and look at a less specific data set since the attrition calculation eliminated around 1500 rows of data. A similar script to the attrition calculation was used to calculate GPA.

We drew the visualization on a white board, showing the line graph, plots for M and F GPA over time, and the interaction of scrolling trough the data. Will then looked for examples for building the slider in D3. We coordinated on color for the graphic.

<h3>Visualization 2 - Violin/Swarm Plots</h3>

#### Description and Overview
This visualization addresses the question: **Does when a student has to declare a major (upon enrollment, after the first year, after the second year, or some other time) have an effect on how many female students enroll in STEM programs?**

To address this question, we created a visualization showing the distribution, across all of the school and programs, of the percent of female students. This is shown as both a violin plot and an overlying swarmplot. On the swarmplot, each dot is a unique institution/program/year combination. The distribution statistics used to render the violin plot are used on those unique rows as well.

The position/space channel separates majors/programs (which we lumped into broad categories) into clusters. The color channel reflects when students must declare a major.

We were curious what patterns would emerge, and were somewhat surprised to note that there doesn’t seem to be a noticeable relationship between when students must declare and what the female enrollment rate is. This may seem like a null result, but it’s still useful: Perhaps, instead of worrying about how to tweak the enrollment timeline, schools can focus on other factors that have more of an effect on outcomes for females in STEM.

However, some interesting patterns are evident: In media and design, nearly all programs have students selecting their major upon enrollment. It’s more common in computer science and engineering for students to have to declare later on in their college career. You can see that in the all-female programs in computer science (represented by the line up at the top at 100% female), there are no programs where students choose a major upon enrollment. Alternatively, in the CS programs with no women (the line at 0%), choosing a major upon enrollment dominates.

Jordan took the lead on this visualization, with Jen providing a supporting role by giving feedback and guidance on design decisions.

#### How to view
You can view this visualization in our dashboard, [or as a standalone graphic here](https://info-4602-5602.github.io/project-2-ncwit-team-13/viz_gender_enrollment/).

Use the buttons at the top to switch between which declaration-group is highlighted: upon enrollment, after the first year, after the second year, or other. (Note, there was an additional category, “university close” -- because this was so small we chose not to include it in the interface.)

Mouse over the “expand distribution” lab next to “Computer Science” or “Engineering” to see a pop-out view of these majors.

#### Design Process

The first phase of the design process was selecting a question to guide our inquiry. Our team brainstormed questions and topics after looking at the dataset, and narrowed it down to our favorites. This question was selected because Lecia Barker explicitly called out the fact that students have to declare majors at different times as something that schools were interested in learning about -- does this have an effect on enrollment, retention, and success in the programs?

The next phase was doing some data cleaning and preliminary analysis using Python, pandas and Jupyter notebooks. [You can see the notebook with both data cleaning and visualizations here.](https://github.com/INFO-4602-5602/project-2-ncwit-team-13/blob/master/viz_gender_enrollment/data-analysis/JWB-NCWIT-analysis.ipynb) [Note that it takes a while to load because the plots take time to render.]

We cleaned the data by making sure the values for the “When do students typically declare their major?” column were normalized by fixing misspelled values (i.e. “Upon Enrollent”). We also added in calculated fields for percent of females enrolled and percent of females graduated. During this process, we saw that there were many institution/year/program entries that were missing data. To deal with this, we dropped rows that had no values, and created a data frame for schools with enrollment data and a separate frame for schools with graduation data (a much smaller subset of the original dataset). Originally, our plan was to see if there was a relationship between when students have to declare a major and what percent of graduates are females, but upon looking at the data we decided that this winnowed the results too much. We chose to use percent of females enrolled in the major as the main metric to display because it is both meaningful and there is more data.

Another visualization decision we had to make was whether to aggregate the data based on school, program, year, etc. We did some data crunching where we aggregated based on school and program (i.e., computer science data at a given institution would be summed across all years, and then a percent of female enrollees could be calculated from that aggregate number). This has the advantage of averaging out year-to-year noise, but the disadvantage that it doesn’t reflect changes that a program/school may have made to improve female enrollment. Also, the data availability year to year is quite variable: some schools have only a year or two of data, whereas others have ten years. A multi-year average is potentially difficult to explain to the end user. Visually, it would mean fewer points to plot on the graph. After looking at some prototype plots of these two options, ultimately, we decided to visualize the full data, non-aggregated.

Our next design choice was what visualization to make. We knew that we wanted to emphasize the distribution of female enrollment, so we looked at box plots, scatter plots, violin plots and swarmplots. Using [Andrew Sielen’s suite of distribution plots for d3](http://bl.ocks.org/asielen/92929960988a8935d907e39e60ea8417) as a guide, we tried out some of the different possibilities. We also looked at the plots available in [Seaborn](https://seaborn.pydata.org/index.html), a visualization package for Python that handles distribution plots well. We ended up choosing a violin plot with a swarmplot overlay. This allows the user to get an impression/gist of the overall distribution, while also being able to see individual values. We felt this met the overview/detail requirement nicely. We adjusted the violin plot settings so that the total area of each violin is proportional to the number of data points in each category (note: it’s NOT proportional to the number of total students in each category, which also would have been interesting). We chose to “clip” the violin plots at 0 percent and 100 percent, because it was confusing to see them extend into, say, negative numbers, when we know there are no negative values for percent females.

Here's an example of an unstyled violin plot made using Seaborn. Note that it has tips that extend beyond 0 and 1, the widths are uniform (that is, the area isn't scaled by number of data points), and it has the default color palette:

![Violin plots without dots](https://i.imgur.com/uqdb503.png)

The next choice was which data to encode in which channels. We knew that we would keep percent females enrolled on the y-axis, but weren’t sure whether to put major or when students must decide on a major on the x-axis. To decide, we made prototype plots of each and circulated them among the team to get feedback.

Here’s an example of a design we didn’t use, which encodes when students must declare a major by position:

![Swarm plots arranged by wheb students declare a major](https://i.imgur.com/Otqvzmh.png)

Next, we had to decide what interaction to include. We decided that the import elements a user might want to explore in this visualization would be how the patterns change based on when a student enrolls. So we made plots that highlight each category using color pop-out (muting the other categories) and gave the user the ability to toggle between them.

Another major design decision we had to make was how to handle the “overlapping” points. If you look at the edges of the CS and engineering clusters, you’ll see that they appear to be bounded, and there are a bunch of points piled up on top of eachother at the edges. This is because there are so many data point in those groups, and the distribution is so highly clustered  around the 15% to 20% female zone, that the point clustering algorithm in Seaborn breaks. First, we considered reducing the size of the points. While this worked in terms of being able to display all points without overlap (see below), it made it much harder to see individual points in the color “pop-out” views.

![Swarm plots with tiny dots](https://i.imgur.com/YmzU5DG.png)

We also considered making the frame wider, or reducing the number of categories shown. These were also non-ideal options. In the end, we decided to show a coordinated view that displays the full distribution for the large categories, CS and engineering, on a tooltip when you mouse over the title. This of course has its flaws, too -- we’re really curious to hear what you think about this design choice.

Throughout this process, Jordan worked on crafting and refining the prototype, frequently sending Jen in-progress images over slack with design decision questions. While most of our interaction was online, via Slack, we also met in person to hash out some decisions. Here's the whiteboard from one of our in-person meeting:
![White board listing some design decisions](https://i.imgur.com/luYv0VN.jpg)

If we had more time, we would have tried to implement the visualization in D3 instead of in Seaborn and Javascript. This would have allowed us to add enhanced interactivity, such as a mouseover feature for each dot that shows you the institution code, total enrollment, and other related data. With more time, we also could have explored the time dimension in these relationships.

<h3>Visualization 3 - Attrition/Institution, Male/F/Tot.</h3>
This visualization is a bubble chart showing attrition for each major from institutions that have enough data to calculate attrition. Each circle represents a major, with the size of the circles encoding the total number of students enrolled in that major. The color scale displays whether the major has higher attrition for males or females, with more green showing higher levels of female attrition and more purple showing higher levels of male attrition. The user can mouse over to display the major, number of students, and rows of data for that major.

#### How to view
Mouse over the circles to display the tooltip.

#### Design Process
This design built on Justin and Bret’s exploration and attempts to calculate and display retention rates in a line graph. Bret and Will met on Monday and discussed better ways to calculate retention and alternatives to using a line graph as the graph was muddled and spaghetti-like making it hard compare the information among schools. After discussing the challenges Justin and Bret were having, Will devised a better way calculate attrition using Total Declared Major and Left Institution data. He also cleaned the data well, making sure to only pull from institutions matching our unique key and with data to compare year over year. After the initial calculations, we also corrected for a few instances with zeros and where the calculation was below zero or over one, indicating a problem with the data, by dropping the values. We further refined the data correcting for irregularities in naming NCWIT Participant type and Major Program Name. Major Program Name was a unique challenge as there were many variations among the CIP code and program name.

<p>After exporting the csv with the cleaned data, we used Tableau to prototype the bubble chart. Here we added the color features and discussed the possibility of further interaction via clicking on each circle to display the data within each major.
</p>

<h3>Visualization 4 - DataFry: Interactive line graph with sound</h3>
#### Description
<p>DataFry is a visualization that uses interactivity to sonify data. For this visualization, we are using line graphs that show the changes in percentage of female enrollment in particular majors over a set of years, in our case we compared the enrollment percentages for computer science and engineering. The line graph is made using conductive ink, turning the graph into a conductive trace. The circuit for the visualization is completed when the person places their fingers along this trace. As they trace their finger along the path, it changes the resistance value which alters the output of the sound. For example, when the finger is near the beginning of the line graph on the left, the resistance is higher, which yields a lower pitch in our circuit. As the finger moves towards the right, the resistance decreases, producing a higher pitch.</p>


<p><b>Design Process</b></p>
<p>We built the circuit based off of Jay Silver's Drawdio circuit. The Drawdio circuit is centered around a 555 timer that changes the frequency depending on the resistance provided by the human input. The original Drawdio circuit is attached to a pencil and uses graphite to complete the circuit. We built the circuit onto a breadboard, and experimented with a number of materials for the trace of our line graph such as copper fabric, graphite, and conductive ink. We decided to work with conductive ink because it provided the most variability in sound than the fabric, yet was more durable to work with than the graphite.</p>

![Building the circuit](https://i.imgur.com/RClP73x.jpg)

![Circuit diagram and breadboard](https://i.imgur.com/ZUSyZVD.jpg)


<p>We also experimented with the use of overlays for DataFry. We used a transparency to put another line graph on top of our existing graph. For our graph, we overlaid the enrollment percentage for engineering over the graph for enrollment percentage for computer science. This allows for a visual and tangible experience of comparing the data.</p>

<p>Although the current  version of DataFry is a working proof of concept, there are changes that could made going forward. In future iterations, we hope to incorporate a microcontroller, such as an Arduino. Using a microcontroller could allow us to sense with more accuracy where the person is touching the graph. This could also open up potentials in connecting the tangible graph with a digital interface so that additional information could pop up on a nearby screen as the person is exploring the graph. We also see the possibility for additional iterations being for the way the graph is made. While the conductive ink made for an effective trace for our prototype, we had difficulty in controlling the flow in the ink. Future work can include working with stencils or diluting the ink so that is easier to apply to a surface.</p>

<p><b>How to run</b></p>

<p>To run DataFry, put one finger on the button in the lower left corner. Then put another finger on the line graph. As your body completes the circuit, you'll hear the sound of the data.  Trace the line and hear how the sound changes across the graph. </p>

<p>Or just watch the video!</p>
![DataFry](https://player.vimeo.com/video/260492997)

<h2>Team Roles: </h2>
<p>Bret – Assisted Documenting project. Helped organize meetings, work on analyzing data, and designing visualizations.</p>
<p>Jen – Worked on analyzing data and designing visualizations. Designed color palette and built physical visualization.</p>
<p>Jordan – Worked on analyzing data and designing visualizations. Built violin/swarm plot visualization.</p>
<p>Justin – Worked on analyzing data and designing visualizations. Assisted cleaning data and working with Bokeh and other libraries to assist building visualizations.</p>
<p>Will -Worked on analyzing data and designing visualizations. Built attrition and GPA visualizations.</p>

<h2>Above and Beyond Included:</h2>
<ul>
<li>Dashboarding</li>
<li>Added Visualizations: 3+1</li>
<li>Missing Data: We filtered data that did not include all the parameters, threw out zero values, and filtered outliers that did not make sense.</li>
<li>Overview+Detail: Highlight declaration year in visualization 3, greying out background information.</li>
<li>Style: Color palette and font are the same</li></ul>
