## E-Blog
No idea of where and when to do those blogs, E-blog got you...holding hands to create that blog that was only a thought


## Author
Pauline Wafula

## Description
E-Blog is a web application that allows a user to create a blog of choice.This is through posting blogs with a title and a blog. On clicking on the create a blog button, it displays a form to create a blog and post.A new user can also log in\register to create a blog of choice and also comment on other people blogs,downvote, upvote,edit or delete a blog posted by other people.A user can also see the blog on main page and the random quotes displayed by consuming api. 


## User Stories
These are the behaviours/features that the application implements for use by a user.

As a user I would like to:
* See random quotes on the main page
* Create a blog og any type
* See blogs posted by other people.
* See the uploded profile image,option to edit my bio. 
* upvote,downvote, comment, edit or delete on the blogs posted. 

## Specifications
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Display random quotes and blogs posted by other users  | **On page load** | Display random quotes and blogs posted by other users  |
| Display page with blogs  | **On clicking a 'create a blog' button** | takes you to the form to create a blog |
| Display blogs posted by other users | **Click an upvote,downvote,comment,edit or delete** | Redirected to a main page with an increase in one |
| Display the comments from a related pitch | **On clicking comments button** | Displays all|
| Deleting the blog | **On clicking deleting button** | 
| Editing the blog | **On clicking editing button** | takes you to the already filled form to edit |
| Registration/login required  | **** | Redirected to creating a blog if you already have an account  |


## SetUp / Installation Requirements
### Prerequisites
* python3.8
* pip
* activate virtual environment

### Cloning
* In your terminal:

        $ git clone https://github.com/paulinenanzala19/E-Blog.git
        $ cd blog

## Running the Application
* Creating the virtual environment

        $ python3.8 -m venv --without-pip virtual
        $ source virtual/bin/activate
        $ curl https://bootstrap.pypa.io/get-pip.py | python

* Installing Flask and other Modules

        $ python3.8  pip install flask
        $ python3.8  pip install flask-Bootstrap
        $ python3.8  pip install flask-Script
        $ python3.8  pip install flask-migrate
        $ python3.8  pip install flask-sqlalchemy
        $ python3.8  pip install flask-Reuploded
        $ python3.8  pip install flask-login
        $ python3.8  pip install flask-WTF

* To run the application, in your terminal:

        $ chmod +x start.sh
        $ ./start.sh

## Testing the Application
* To run the tests for the class files:

        $ python3.8 manage.py test

## Technologies Used
* Python3.8
* Flask
* HTML
* CSS(Bootstrap)

## live link
[]

## known bugs
Not any at the moment but am open to suggestion


## License
MIT License

Copyright (c) 2022 Pauline Nanzala

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.