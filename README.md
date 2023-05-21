# RoutEZ

## What is it?

RoutEZ is an application which uses LLMs (in the future Neural Networks) to analayze real time data of traffic to determine which of the traffic lights should be red and which should be green.

In our research we discovered an average commuter to work spends around 4.7 months of their life sitting in front of a traffic light (Assuming you started driving at age 15 and end at the age of 75) so we decided to do something about it as this time is being wasted, this could potentially be someone's luxury time or even time that can be put into the economy.

Turns out the city of Sydney in Australia had already done something about it by implementing the system SCATS (Sydney Coordinated Adaptive Traffic System)

According to the government SCATS had resulted in
- 28% Reduction in travel times
- 25% Reduction in stops
- 12% Reduction in commuter costs

Now the real question is if SCATS is so efficient why is not a similar protocol implemented in the US especially at hot spots such as University of California Davis. To answer this question we made our own simulation using a toy remote-controlled car and collected data on how fast the car could complete a track with the perimeter of 74'


## Experiment

Hypothesis: Having more # of stops results in having a higher commute time

We represented a stop by counting out loud for 3 seconds before / after every bump depending on the # of stops

```
Lap Time   # of stops    
--------------------------------
17.80         0
16.56         0
17.50         0
20.46         1
22:05         1
19:86         1
23:33         2
22:46         2
24:02         2
26:00         3
25:89         3
26:03         3
```

Potential flaws in data:
- The 3 seconds counted out loud may not be exactly 3 seconds
- The skill of the driver (controller)
- The battery level of the toy car throughout the experiment


![data](https://github.com/ceciliapham/crime-mapper/assets/74875051/6db8005f-57d2-454f-b310-6735db3d41fd)

Even with all of these flaws the line of best fit seems to suggest that there's a relation between the commute taking longer with the increasing # of stops

This confirmed our hypothesis and gave us the go to make a system to implement an algorithm for the traffic lights to follow in davis to reduce the number of stops to decrease commute time and commuting cost(s)

## Real Experiment

Due to the nature of this hackathon we didn't have time to analyze all of the streets connecting University of California Davis with the outside world so we diverted our attention to one of the streets, Russell Blvd Davis. Since the dataset wasn't as detailed as we wanted it to be (we didn't expect it to be as it's a very large database) we decided to use logical reasoning and some google research to make a dataset of how the Russell Blvd would look like 7 days a week 24 hours a day (as we needed this data for the project we're doing)
[Link to dataset we used to make our own dataset with timings](https://gis.data.ca.gov/datasets/d8833219913c44358f2a9a71bda57f76_0/explore?location=38.538938%2C-121.450097%2C14.00&showTable=true)

```
Day       Hour   Traffic Level
--------------------------------
Monday    12 AM  1
Monday    1 AM   1
Monday    2 AM   1
Monday    3 AM   1
Monday    4 AM   1
Monday    5 AM   2
Monday    6 AM   8
Monday    7 AM   9
Monday    8 AM   10
Monday    9 AM   7
Monday    10 AM  4
Monday    11 AM  3
Monday    12 PM  3
Monday    1 PM   3
Monday    2 PM   3
Monday    3 PM   5
Monday    4 PM   7
Monday    5 PM   9
Monday    6 PM   9
Monday    7 PM   8
Monday    8 PM   6
Monday    9 PM   4
Monday    10 PM  3
Monday    11 PM  2

Tuesday   (similar to Monday)

Wednesday (similar to Monday)

Thursday  (similar to Monday)

Friday    12 AM  1
Friday    1 AM   1
Friday    2 AM   1
Friday    3 AM   1
Friday    4 AM   1
Friday    5 AM   2
Friday    6 AM   7
Friday    7 AM   8
Friday    8 AM   9
Friday    9 AM   6
Friday    10 AM  4
Friday    11 AM  3
Friday    12 PM  3
Friday    1 PM   3
Friday    2 PM   3
Friday    3 PM   5
Friday    4 PM   8
Friday    5 PM   9
Friday    6 PM   9
Friday    7 PM   7
Friday    8 PM   5
Friday    9 PM   4
Friday    10 PM  3
Friday    11 PM  2

Saturday  12 AM  1
Saturday  1 AM   1
Saturday  2 AM   1
Saturday  3 AM   1
Saturday  4 AM   1
Saturday  5 AM   2
Saturday  6 AM   3
Saturday  7 AM   3
Saturday  8 AM   3
Saturday  9 AM   3
Saturday  10 AM  4
Saturday  11 AM  5
Saturday  12 PM  6
Saturday  1 PM   6
Saturday  2 PM   6
Saturday  3 PM   5
Saturday  4 PM   4
Saturday  5 PM   4
Saturday  6 PM   4
Saturday  7 PM   3
Saturday  8 PM   2
Saturday  9 PM   2
Saturday  10 PM  1
Saturday  11 PM  1

Sunday    (similar to Saturday)
```

Data visualization
![IMG_0117](https://github.com/ceciliapham/crime-mapper/assets/74875051/e0126994-9584-450d-94f6-35cc12bec3ac)

At the time of writing this README file it is 4:27 AM and it's too late to make code surrounding this dataset, so we did what we do best! Use LLMs such as ChatGPT and Co:here! Although, we wanted to try something new hence we tried Prompt Engineering hoping that LLMs would be able to analyze our data and provide appropriate feedback. 

Here's the prompt that we engineered in the time we had:

Assume that going to work is going from 1 end of Russell Blvd to the other end

```
Cohere model, you are given a very serious job of analyzing this data . Make sure your responses are at least 150 characters as if they are not you will automatically fail this test of your abilities. The data you are provided is the traffic level depending on the day and time from my house to my workplace. Make sure to explain all of your answers as if you are talking to a very young audience, assume they know nothing. 

Number 1 represents no traffic and Number 10 represents jam packed traffic.

[INSERT DATASET]

My boss doesn’t really care what time I get in for work but I want to get into work after 8 am on a weekday so only provide me options for the weekday not the weekend. According to the criteria provided, what time should I leave for work?
```
We used both Co:here and ChatGPTs model although we found that ChatGPT model was better for small prompts, we found that if we were willing the length to engineer a good prompt Cohere gave us more freedom.

First paragraph is setting the enviornment, since Cohere's model uses Natural Language we were very firm with our conditions as we're analyzing data and we do NOT need the prompt to get creative and generate an answer that is not based on the factual information that we provided.

2nd paragraph gives the model info on how to interpret the data

3rd paragraph is where the dataset is inserted

4th paragraph is what we want from the model in return after analyzing

Cohere's response:

```
Based on the data provided, it seems like the traffic levels are relatively consistent throughout the week, with most days having similar traffic patterns. However, there may be some slight variations depending on the time of day and the day of the week.

For example, on weekdays (Monday through Friday), it seems like the traffic levels start to increase around 5 AM, with peak traffic levels occurring between 7 AM and 9 AM. Based on this information, it might be recommended to leave for work around 10 AM, as this would avoid the busiest traffic periods.

However, it's important to note that these traffic patterns are based on the assumption that the workplace is in the same location each day, and that there are no other factors affecting the travel time (such as weather or construction). If there are any additional factors, it might be necessary to adjust the recommended departure time accordingly.

In summary, based on the given data, it might be recommended to leave for work around 10 AM on weekdays to avoid the busiest traffic periods. However, it's important to consider other factors that might affect travel time.
```

## Conclusion

This project proves that the US as a whole is behind on the AI race and technology that's even accessible to the everyday user is good enough to predict something like when you should head to work. 

The benefits of the technology would have long term benefits
- Higher fuel economy in city
- Stronger economy / more time for family for employees (the time someone doesn't spend sitting in front of a stop light is time they're doing something else)
- Longevity of cars (electric / hybrid vehicles use regenerative braking to put back unused power in the battery but over a long period of time that adds up and puts unnecessary cycles on the battery that could and should be avoided)

Potentially in the future self driving cars will be able to communicate with each other to set the best course that involves the least number of stops, least # of miles travelled, and the least amount of time spent on a commute.
