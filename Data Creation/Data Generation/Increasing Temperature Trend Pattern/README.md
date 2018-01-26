# Generate Increasing Temperature Trend
Problem Statement/Background :- Generate two Increasing temperature trend pattern with 100 set each. Each sample in a pattern must not be duplicate.Each sample must have some variance with respect to other sample.

High Level Requirement :- Python 3.6  

Implementation :-  
We made two simple pattern  
•Linear increasing Trend pattern  
•Convex increasing Trend pattern  

Steps to follow :  
1. Generate Basic Pattern:  
    a. Generate a straight line from 0 to 100.  
    b. It could be drawn in 50 set of points or 70 set of points or 80 set of points, difference will only be in slope.  
    c. If drawing straight line in 50 set of points, we still left with 50 points, since total points are 100.  
    d. Among this 50 points, some points can be at start of line having value 0 and some points at end of line having          value 100 as shown in figure.  
    <img src='/Images/linear_rise.PNG'>  
    This is Linear Increasing Temperature Trend Pattern  
    e. Now if we apply cube root to whole set of points,we would get somethng like this.  
    <img src='/Images/convex_rise.PNG'>  
    This is our Convex Increasing Temperature Trend Pattern

2. Generate Multiple Variation:  
    a. After we created basic pattern, we can change different start & end no of points(Those points which will stay at min or max value). Soo choosing start & end points, we can find left no of points to draw our straight line from min to max.  
