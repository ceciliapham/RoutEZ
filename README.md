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

Even with all of these flaws the line of best fit seems to suggest that there's a relation between the commute taking longer and with the # of stops

This confirmed our hypothesis and gave us the go to make a system to implement an algorithm for the traffic lights to follow in davis to reduce the number of stops to decrease commute time and commuting cost(s)

[Link to dataset](https://gis.data.ca.gov/datasets/d8833219913c44358f2a9a71bda57f76_0/explore?location=38.538938%2C-121.450097%2C14.00&showTable=true)
