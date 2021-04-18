# The Daily Planet

This project was generated using Python and Flask micro-framework.

# Author

[Ian Kiplagat](https://github.com/kasparov-creat/)

## Description

A Python and Flask micro-framework application that consumes data from the [News-API](https://newsapi.org/) and returns general news, headline news, and their sources and categories in multiple languages as selected by the program. The application displays this information in several routes that make it easier to go to a specific category of news.

## User Stories

These are the behaviours/features that the application implements for use by a user.

A user can:
- See various news sources
- Select the ones they prefer
- See the top news articles from that news source
- See the image, description and time the news article was created
- Click on an article and read it fully from the news source

## Setup/Installation Requirements

### Prerequisites

- Python3.8
- Pip
- Virtualvenv

### Cloning

In your terminal:
          $ https://github.com/kasparov-creat/The-Daily-Planet.git
          $ cd News-App

## Running the Application

- Creating the virtual environment

          $ python3.8 -m venv --without-pip virtual
          $ source virtual/bin/env
          $ curl https://bootstrap.pypa.io/get-pip.py | python

- Installing Flask and other Modules

          $ python3.8 -m pip install Flask
          $ python3.8 -m pip install Flask-Bootstrap
          $ python3.8 -m pip install Flask-Script

- Setting up the API Key

  To be able to gather article info from the News API you will need an API Key.

  * Visit https://newsapi.org/ and register for an API key.
  * In the root directory of the project folder create a file: start.sh
  * Insert the following info into it:

          export NEWS_API_KEY='<Your-Api-Key>'
          python3.8 manage.py server

  * Insert the API Key you received from News Api where <Your-Api-Key> is.

## Testing the Application

To run the tests for the class files:

          $ python3.8 manage.py tests

## Technologies Used

- Python3.8
- Flask
- Bootstrap

## Known Bugs

No known bugs

## Support and contact details

Please feel free to contact me incase you run into any issues or have questions, ideas or concerns. You can contact me or make a contribution to the code. Please find my contact information listed below:

- Email: ianjkiplagat@gmail.com
- Telephone: +254742579020

## License

\*MIT License

Copyright (c) 2021 Ian Kiplagat

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.\* Copyright (c) 2021 Ian Kiplagat
