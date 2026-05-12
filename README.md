# README

Individual Flask project.

To see all of the water data for a given location and Year:

http://127.0.0.1:5100/Location/Year

Example: http://127.0.0.1:5100/Afghanistan/2000

To see all of the water data for a given location:

http://127.0.0.1:5100/search/l/Location

Example: http://127.0.0.1:5100/search/l/France


Individual Database deliverable.

One for the Country csv:
\copy water_country FROM 'water_country.csv' DELIMITER ',' CSV HEADER

One for the region csv:
\copy water_region FROM 'water_region.csv' DELIMITER ',' CSV HEADER

Why I did what I did: 

This cleaned dataset makes sure to include the locations and the years. The original dataset included information about rural and urban areas in a location.  However, I wanted to look at the population as a whole to see what the overall population is doing with water. In addition, there was a section talking about the proportion of the poulation using improved water, so I omitted out other things except this because our group is mainly looking at the accessible clean water in an area. From this, this dataset considers the total proportion of the population using improved water. 
Majority of the datatypes I used were integers because a lot of the information was whole numbers, such as years. The location was in text because a user would need to type out the country. Lastly, I used real for the percent urban and basic to consider decimals. 

Relating each query to a user story:

My first query asks a user to input a year and a location, and will output the water information about the location and year. This is important because user story 3 talks about a WHO worker who needed information about the available water in a country. So, this first query allows a user to input a specific location and year to get information on what has happened with the water. This can better support a WHO worker in their field
My second query asks a user to input a location and will output all of the information about the location throughout the years. This is relates to user story 2 because a traveler going to a country will want to know all of data about the clean water in a region. So, by inputting a location, a user can see all the information about the location. 