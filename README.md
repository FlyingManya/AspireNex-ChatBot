# CHAT-BOT
***Greetings Everyone🌻, This is my ChatBot built using Flask and Python***<br>

*This task was assigned by AspireNex for the Artificial Intelligence Internship Selection Process*.<br>
<hr>

**TASK 1 - CHATBOT WITH RULE-BASED RESPONSES**<br>
Build a simple chatbot that responds to user inputs based on predefined rules. Use if-else statements or pattern matching techniques to identify user queries and provide appropriate responses. This task will help us understand your knowledge of natural language processing and conversation flow.

<hr>
<br>

![chatbot Banner](https://github.com/FlyingManya/AspireNex-ChatBot/assets/98754211/55315719-5cba-4f58-a2cd-5b7983debf7c)

*This chatbot is built using Flask and Python and utilizes regular expressions to handle various user inputs accurately. <br>
The main goal is to create a versatile chatbot that can manage different edge cases in user queries.<br>
This chatbot is built using Flask and Python, and it leverages regular expressions for advanced pattern matching to provide accurate responses to user queries*
<br>

## DEMO
***Let's see how it works 🌻***
<table style="border: none">
  <tr style="border: none;">
    <td style="border: none; vertical-align: top">
      <h3>Greeting Edge Cases:</h3>
      <hr>
      <p>Type: <em>"Hi there!"</em><br>
      Response: "Hello! How can I help you today?"<br>
      Type: <em>"Hello, how are you?"</em><br>
      Response: "I'm just a chatbot, but I'm here to assist you."<br>
      Explain: As you can see, the <strong>chatbot correctly identifies different greeting forms, even with additional words or punctuation</strong>.</p> <br>
      <h3>Technical Inquiries:</h3>
      <hr>
      <p>Type: <em>"Can you help me with Python programming?"</em><br>
      Response: "Absolutely! I can assist you with programming questions."<br>
      Type: <em>"Do you have any hobbies or interests?"</em><br>
      Response: "I'm always busy helping users, so my hobby is chatting with people like you!"<br>
      Explain: <strong>It responds to technical and personal interest questions, even when phrased differently</strong>.</p>
    </td>
    <td style="border: none; vertical-align: top">
      <img src="./ChatBot1.png" alt="ChatBot Image">
    </td>
  </tr>
</table>

<table style="border: none">
  <tr style="border: none;">
    <td style="border: none; vertical-align: top;">
      <img src="./ChatBot2.png" alt="ChatBot Image">
    </td>
    <td style="border: none; vertical-align: top">
      <h3>Personal Questions:</h3>
      <hr>
      <p>Type: <em>"What do you do for fun"</em> <strong>(no question mark)</strong><br>
      Response: "Chatting with users like you is what I enjoy the most!"<br>
      Type: <em>"What Do you do for fun?"</em> <strong>(varied capitalization)</strong><br>
      Response: "Chatting with users like you is what I enjoy the most!"<br>
      Explain: <strong>The chatbot handles variations in capitalization and punctuation thanks to regex pattern matching.</strong></p>
      <h3>Humor and Trivia:</h3>
      <hr>
      <p>Type: <em>"Tell me a joke"</em><br>
      Response: "Sure! Why don't scientists trust atoms? Because they make up everything!"<br>
      Type: <em>"Tell me something interesting."</em><br>
      Response: "Did you know that the world's oldest piece of chewing gum is over 9,000 years old?"<br>
      Explain: <strong>It can share jokes and trivia, adding an element of fun to the interaction.</strong></p>
    </td>
  </tr>
</table>
<br>

## Languages and Tools
<p align="left"> <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="60" height="60"/> </a> <a href="https://www.w3.org/html/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/html5/html5-original-wordmark.svg" alt="html5" width="60" height="60"/> </a> <a href="https://www.w3schools.com/css/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/css3/css3-original-wordmark.svg" alt="css3" width="60" height="60"/></a> <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/javascript/javascript-original.svg" alt="javascript" width="50" height="60"/></a> </p>
<br>

## CODE EXPLANATION
*Let’s take a quick look at how the code works*

## app.py
**Flask Setup:**
*The chatbot is built using Flask, a lightweight web framework for Python*<br>

- **Pattern Matching with Regex:**
  - *We use regular expressions to match user inputs with predefined patterns*<br>

     ![Patterns](https://github.com/FlyingManya/AspireNex-ChatBot/assets/98754211/4bd594fc-cd7e-4219-bfda-8ab42a417dcb)
    <br>

  - *This allows the chatbot to handle various inputs, even if they're phrased differently or include punctuation*

- **Response Generation:**
  - *The **get_response** function uses regex to find the appropriate response for each user input*<br>

    ![get response](https://github.com/FlyingManya/AspireNex-ChatBot/assets/98754211/96955e49-97f1-428d-be27-1d2d3968dcad)

  - *It searches through the patterns and returns the corresponding response.*

- **Routing and Handling Requests:**
  - *The Flask routes handle incoming requests and return the chatbot's response* <br>

## static
- style.css: Contains the CSS styles used to customize the appearance and layout of HTML elements in the project.
- script.js: Includes JavaScript code that provides dynamic behavior and interactivity to the web pages, enhancing user experience.

## templates 
- index.html: This HTML file serves as the main template for your web application, defining the structure and content that Flask will render and serve to users.

<br>

## CONCLUSION
*In summary, this chatbot project effectively handles a wide range of user inputs by using regular expressions for pattern matching. It recognizes and responds to various edge cases, providing a seamless user experience.
Moving forward, I plan to enhance its capabilities further by integrating more advanced natural language processing techniques.
Thank you for Visiting*

<br>
<br>
<br>

<br>
<image align="right" alt="coding" width="250" src="https://github.com/FlyingManya/FlyingManya/assets/98754211/0a854199-b287-4dca-a4cc-8265cbd3335e" alt="flyingmanya"></p>

<h3 align="left">Connect with me:</h3>
<p align="left">
<a href="https://linkedin.com/in/flyingmanya" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="flyingmanya" height="30" width="40" /></a>
<a href="https://instagram.com/flying_manya" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/instagram.svg" alt="flying_manya" height="30" width="40" /></a>
<a href="https://www.leetcode.com/flying_manya" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/leet-code.svg" alt="flying_manya" height="30" width="40" /></a>
</p>

🌵 https://gautamrajputmanya.wixsite.com/mysite 

📫 *gautamrajputmanya@gmail.com*
