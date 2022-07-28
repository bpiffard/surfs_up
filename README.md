# surfs_up
## Analysis Overview
The goal of this analysis was to get a picture of the weather conditions on Oahu to determine if it was a good island to set up a surf and ice cream shop. Rainy conditions are not favorable to either surfing or ice cream eatsing, and neithger are cold conditions. The analysis only covers the months of June and December, as these are the month with the solstices, thus the apex of both Summer and Winter conditions. This eases the burden of looking at all data over a year.
## Results
### First a look at the precipitation data...
![June Precipitation](https://github.com/bpiffard/surfs_up/blob/27a17006513c8b17299a63f3dc35f4b21f4cb0eb/Images/June%20precipitation.png)
![December Precipitation](https://github.com/bpiffard/surfs_up/blob/27a17006513c8b17299a63f3dc35f4b21f4cb0eb/Images/December%20precipitation.png)
- As you can see, the average daily rainfall between the two months of June and December are incredibly close. Closer thatn 0.01 units. This suggests that the monthly variation of rain is low in Hawaii, which makes sense as it is located in the tropics. Weather in the tropics varies little throughout the year, as well as the length of the day. 
### Now a look at temperatures
![June Temps](https://github.com/bpiffard/surfs_up/blob/27a17006513c8b17299a63f3dc35f4b21f4cb0eb/Images/June%20temps.png)
![December Temps](https://github.com/bpiffard/surfs_up/blob/27a17006513c8b17299a63f3dc35f4b21f4cb0eb/Images/December%20temps.png)
- As with precipitation, the variation between the two monts hs is low. THe average temperature between June and December are only different by three degrees, truly hardly noticible
- The difference in the lowest recorded temperature between these two months was higher than the difference in averages and in maximum tempoeratures. This is mildly interesting, but the difference is only 8 degrees. Nothing to write home about. THe difference between the maximum temperature and minimum temperature per month respectively is higher than this difference.
## Summary
I think I misunderstood this question, and simply read two additional queries in general, and not for June amd December in particular. However, I only noticed this error after spending considerable time doing a different analysis, and as I am very proud of that work, I am going to present the data from the work that I did do. Please enjoy these bar charts that present precipitation and temperature averages per month.
### Average Precipitation per Month (Month = x-axis as "01" for Jan, etc.)
![Average Precipitation per Month Bar Chart](https://github.com/bpiffard/surfs_up/blob/4b369ecd5d25c775c4a12476fb602a703e4fec55/Images/avg_prcp_barchart.png)
### Average Temperature per Month (Month = x-axis as "01" for Jan, etc.)
![Average Temperature per Month Bar Chart](https://github.com/bpiffard/surfs_up/blob/4b369ecd5d25c775c4a12476fb602a703e4fec55/Images/avg_temps_barchart.png)

I did this as it made much more sense to me to compare across all months, not simply two. By doing so we are able to see that March is also a month that had high precipitation. Perhaps that was an anomaly and not typical of March, but I am glad to see that data. The temperature barchart proves that there is low variation in temperature throughout the year. The precipitation barchart makes it look that perhaps rainfall varies a bit more, but that may have to do with the automatic scaling of the chart. By which I mean, perhaps the program defaults to zooming in on the bars to clearly show differences when perhaps the real, practical differences between precipitation values are very small. As an example of what I mean, if I told you I doubled my money you might be very impressed, but perhaps the reality is that I went from having one dollar to two dollars. A big relative change, but two dollars still isn't much money. I digress.

The ultimate conclusion should be that any month in Oahu, Hawaii will hbave similar weather to any other month, and that that uniform weather is balmy, and mostly sunshine. The perfect place for an ice cream and surf shop.

As a last note, I pulled the data for the bar charts using for loops. I made the barcharts using matplotlib. The code for this can be found on the SurfsUp_Challenge.ipnyb file. The comments there will explain what I was doing.

Okay, thank you for reading, bye!
