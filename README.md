


# Project
Awwar

## Author
Steve Mitto

## Description
The awards website allows different web and mobile developers to post their websites online to be rated by people globally

## Technologies Used
* Python
* Django
* HTML
* CSS
* Jquery

## Setup and Installation
This installation considers you have already installed [python](https://linuxize.com/post/how-to-install-python-3-7-on-ubuntu-18-04/) and [postgresql](https://www.postgresql.org/download/)

1. **Clone The Project**
	create a folder and run the following command considering [git](https://gist.github.com/derhuerst/1b15ff4652a867391f03)	is already installed
 ` git clone https://github.com/SteveMitto/awwwards`

2. **Virtual Environment**
 In the same folder run this command to create a virtual environment
    `python -m venv --without-pip virtual`
  once the command is done running you can install the requirements using this command
  `pip install -r requirements.txt`
  then activate the environment using the command `source virtual/bin/activate`
  3. **Setup Database**
     open postgres in the terminal by typing the command ` psql`

     then it will request for your details which you will be reuested to fill
     then create a database by typing  
     `CREATE DATABASE awards `

     open the app on your text editor
	`atom .`  for Atom and `code .` for Visual Studio Code

		Create a `.env` file and add the following configurations
 - DATABASE_URL='postgres://*database-username*->:*database-password*@localhost/awards'
- MODE=dev
-  ALLOWED_HOSTS='*'
- SECRET_KEY=*add_yours*
4. **Running the app**
  At this point you can run your migrations to apply changes to your database
  `python manage.py migrate`
  once migrations are done, you can run the app typing
   `python manage.py run server`

## Bugs and Errors

 1. The page is not that responsive on the profole section

## Link to Website
Visit this [link](https://n0tawwwards.herokuapp.com/) to see the live deployment

## Contacts
find me at gmail at mittosteve@gmail.com

## License
> My Awards project under the [MIT LICENSE](https://github.com/SteveMitto/awwwards/blob/master/LICENSE)
Copyright (c) 2019 Steve Mitto

## Acknowledgements

> Moringa Shool
