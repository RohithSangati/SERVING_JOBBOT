# Main Motto :
# Our bot is a jobbot, we named it as j-bot.
# which helps to find a required job for the user.

# Bot interface :

## Firstly our bot greets the user with a greeting message.
## Next to that, bot shows some options to the user which helps in entering input.
## Bot responds to the user based on the input given by the user appropriately.
## If user wishes to end the chat, If we enter Bye, It will ends the conversation.

# How we made it :

## First of all our bot starts with main.py
## For "/" route it calls introduce function, in the introduce function it imports bot data from the about.py in the datafolder and returns index.html template along with the bot information
## After returning index.html extension template of chatbot.html if we run the flask it returns response link
## After running the link in chrome chatbot user interface appears which is styled with chatbot.css file and make responsive with chatbot.js
## After entering the user input and submiting the input it calls send_response function in java script which make a post request of "/message"
## After getting the response for the post request from the main.py which returns suitable output template for input, it appends into the message box
## Finally if we type end it will end the chat.

# Heroku link :
https://j-bot04.herokuapp.com/

# Video
[![IMAGE ALT TEXT HERE](https://i2.wp.com/jobbot.ai/wp-content/uploads/2017/05/jobbot-wide-primary.png?fit=600%2C221)](https://youtu.be/o8NgYJMMyZc)