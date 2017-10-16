1. What is the function of the following technologies in your assignment:
   HTML:
      includes codes that set up layout of the website. 
   CSS:
      decorates the website. 
   JavaScript:
      applies the validations. 
   Python:
      the promgram in language. 
   Flask:
      a type of framework 
   HTTP:
      connection between server and web 
   GET and POST requests:
      GET requests information from the server
      POST gets information and sends it to the server(MAILGUN) 

2. How does HTML, CSS, and JavaScript work together in the browser for this assignment?
   HTML sets up the layout, CSS decorates it, and JavaScript implement the program.

3. How does Python and Flask work together in the server for this assignment?
   Flask is programmed in python, and python is used to make server work with the code. 


4. List all of the possible GET and POST requests that your server returns a response for and describes what happens for each GET and POST request
GET:/
   renders the index.html template file
GET: /index
   renders the index.html template file
GET: /contact
   renders the contact.html template file
GET: /about
   renders the about.html template file
GET: /blog/(title)
   renders each blogs in blog folder
POST: /contact
   submits the data within the form as an email to the MAILGUN api and also renders the contact.html