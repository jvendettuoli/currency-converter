### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?

  - Python has a wide range of applications, but is primarily used for backend/server side development, whereas Javascript is typically a frontend language.
  - Python has a built in REPL and can run in the terminal, while Javascript typically runs in the browser.
  - Python requires indentation formatting as part of its syntax, whereas Javascript uses {} for code blocks, and uses indentation for readability and convention.
  - Python seems to be favored for data science, and Javascript seems favored for web development.

- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you 
  can try to get a missing key (like "c") *without* your programming 
  crashing.

  - You could use defualt values when setting variables, such as JS's let missing_key = dict.c || undefined, or python's get() or setdefualt() methods.
  - You could use error handling in the form if-else statements or a try-catch/try-except

- What is a unit test?
  - A unit test is for individual components of a larger code base. It tests specific funcionality, such as of one function.

- What is an integration test?
  - An integration test tests how different units interact together. It is a step up from unit tests.

- What is the role of web application framework, like Flask?
  - Web application frameworks handle a great deal of the work behind making handling routes, handling requests, handling cookies, handling html templates, and overall reduce much of the "busy work" of building a web application, at the cost of some lost control. They also help by running a local server to allow for visualizing and testing while developing.

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?
  - Generally route URL parameters are better for subject of a page, something broader.
  - URL query parameters are better for handling from data, or other more specific information about a page.

- How do you collect data from a URL placeholder parameter using Flask?
  - You pass the parameter into your route definition using the same name as the placeholder. @app.route("/page/<parameter>) \ def some_page(parameter):

- How do you collect data from the query string using Flask?
  - By requesting it via the request method of Flask, if imported. parameter = request.args['parameter']

- How do you collect data from the body of the request using Flask?
  - data = request.form

- What is a cookie and what kinds of things are they commonly used for?
  - A cookies are key value pairs of strings stored on a client, as directed by a server when the client iteracts with that server. They store information such as preferences, login information, game states, user info, etc. 

- What is the session object in Flask?
  - The session object is similar to localStorage in JavaScript. It stores information in a dictionary like object that can then be accessed with the approriate key later on. They generally last as long as a browser session does, though that can be changed. They can store more complex data than cookies, and are also signed as a means of encryption. 

- What does Flask's `jsonify()` do?
  - jsonify() allows you to convert a data structure into json as part of a Flask reponse.

- What was the hardest part of this past week for you?
  What was the most interesting?
  - The hardest part was not realizing that the .js and .css files stored in /static would not update automatically as I had grown accustomed to. I spent too long trying to debug code that was fine, but just wasn't being updated. Eventually I figured it out and could hard refresh to get moving again.

  - The most intresting was combining all the different components into one project (Boogle Exercise) and seeing everything interact.
