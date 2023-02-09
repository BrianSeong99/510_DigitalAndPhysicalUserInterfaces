# Milestone 1 Requirements
For Milestone 1 you will need to create a chatbot that converses with a user 
and saves their input for later analysis.

You will recall that during week 2 we created an improved chatbot that 
greeted the user and then asked a series of questions before providing a 
text-based summary and analysis of the interaction. Here we want to expand 
upon that design by saving the user input to data structure that we 
hold in in-memory and then write to a CSV for later analysis using Pandas.

## Requirements
In order to successfully complete Milestone 1, your application will need to 
meet the following requirements:
- It must feature a **Chatbot** that captures input from three different users.
- The Chatbot should remember the user's name and ask the user a series of 
  three questions. Your Chatbot will ask questions based on the user's 
  sentiment. For example, if the user indicates they are happy or that 
  their day is going well, then the Chatbot should pursue a line of 
  questioning that aligns with the user's mood. Here is a more specific 
  example:
  ```
  Hi there! What's your name?
    My name is Scott
  Nice to meet you, Scott! How are you today?
    I'm doing really well, thanks.
  Great to hear! Do you have something exciting planned today?
    Yeah, I'm taking my family to dinner this evening.
  Nice! Where to?
    Our favorite pizza place.
  Sounds great. I enjoyed chatting with you. Bye!
  ```
- The Chat bot should save the user's responses to a data structure such as 
  a Python dictionary (`dict`) or to a Pandas `DataFrame`.