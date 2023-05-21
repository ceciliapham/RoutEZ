# RoutEZ

## What is it?

RoutEZ is an application which uses LLMs (in the future Neural Networks) to analayze real time data of traffic to determine which of the traffic lights should be red and which should be green.

In our research we discovered an average commuter to work spends around 4.7 months of their life sitting in front of a traffic light (Assuming you started driving at age 15 and end at the age of 75) so we decided to do something about it as this time is being wasted, this could potentially be someone's luxury time or even time that can be put into the economy.

Turns out the city of Sydney in Australia had already done something about it by implementing the system SCATS (Sydney Coordinated Adaptive Traffic System)

According to the government SCATS has resulted in
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

Even with all of these flaws the line of best fit seems to suggest that there's a relation between the commute taking longer and with the # of stops

This confirmed our hypothesis and gave us the go to make a system to implement an algorithm for the traffic lights to follow in davis to reduce the number of stops to decrease commute time and commuting cost(s)

## Real Experiment

Due to the nature of this hackathon we didn't have time to analyze all of the streets connecting University of California Davis with the outside world so we diverted our attention to one of the streets, Russell Blvd Davis. Since the dataset wasn't as detailed as we wanted it to be (we didn't expect it to be as it's a very large database) we decided to use logical reasoning and some google research to make a dataset of how the Russell Blvd would look like 7 days a week 24 hours a day (as we needed this data for the project we're doing)

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
Friday     10 AM  4
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

At the time of writing this README file it is 4:27 AM and it's too late to make code surrounding this dataset, so we did what we do best! Use LLMs such as ChatGPT and Co:here! Although, we wanted to try something new hence we tried Prompt Engineering hoping that LLMs would be able to analyze our data and provide appropriate feedback. 

[Link to dataset](https://gis.data.ca.gov/datasets/d8833219913c44358f2a9a71bda57f76_0/explore?location=38.538938%2C-121.450097%2C14.00&showTable=true)
