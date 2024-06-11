# Mindful-STEM-Camp-Projects

This is about halfway hard-coded. The bot can't yet pick things up, but it can traverse the garden in four stops and 
diferentiate which function to use depending on our input. 
The next most important step is to utilize the pincers and figure out how we will maneuver them in order to accomplish
each function's task.

patrol(gardenfunc) - Input will decide which function to use. Traverses entire garden in 4 stops and returns to starting position.


water() - Will spray water (perhaps nitrogen and baking soda solutions as well?) using the pincers, we should test to see how the bot
can best grab the sprayer.

soilquality() - Will lower soil measurer down into the soil, sleep() for an allotted time, and lift to read data. 

snapshot() - Will take a picture of the garden at each of the 4 designated spots.

initialize() - Starts the bot and gives it time to load. Returns bot value

motor(speed) - I don't have a separate start/stop function, instead we will use a general motor() function to adjust our 
motors and give it the speed we want in that particular case (if we want the bot to stop, the speed would be 0).

obstacle(distance) - Decides how/when the bot will move as an obstacle is in front of it. If something is placed within 5 centimeters
of the sensor at the front of the bot, the motor() function will be called with an input value of 0 to stop the bot.

pickup() - Will focus on an object placed directly in front of the bot to pick it up. Depending on the object, we ought to 
place it strategically so that the bot isn't holding it at a weird angle

