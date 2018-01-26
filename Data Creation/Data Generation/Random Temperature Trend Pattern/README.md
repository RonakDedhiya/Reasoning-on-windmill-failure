# Generate Random Temperature Trend
Problem Statement/Background :-Generate different data pattern with random spikes and sudden rise and fall in .  

High Level Requirement :- Python 2/3    

Implementation :-    
To create two different data patterns we wrote python script.  

  1. Data with Random Spikes:  
      This type of data ca be used to refer data from sensor which fails some times  
      Steps:  
        a. Generate a random noise of 90 points  
        b. Since Average Temperature is 30 degree, we add 30 to noise.  
        c. We generate 10 random integers and insert 0 to this 10 random integer position.  
        d. This is our signal with random spikes.  
      <img src='/Images/Anemometer_Errors.PNG'>    

  2. Sudden rise and fall in data:  
      Steps:  
        a. Generate a random noise of 100 points  
        b. Since Average Temperature is 30 degree, we add 30 to noise.  
        c. Generate a random number between 1 to 50 && 55 to 90, call them as a & b.  
        d. Insert any value between 65 to 70 over the points between a & b.  
        e. This is our signal with sudden rise and wall.    
      <img src='/Images/Generator_speed_discrepancy.PNG'>    
