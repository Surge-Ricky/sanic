This is a simple CRUD app made with Sanic, Postgres, and SQLALchemy (Asyngpg).

Example website - http://174.138.64.173:8000

In this example project are blueprints. Routes are split up. 

Note: 

If this app doesn't run for you, feel free to let me know. Doing "sanic server.py" should in theory work. I personally do python3 server.py. I am not an expert with this.

Debug is turned on but can be switched off in server.py.

You will need to install postgres and sqlalchemy, then configure your database details in database.py.

To read my basic instructions on how to set up a server with Sanic and all of this extra stuff, feel free to check out my tutorial here - https://pastebin.com/c0mJXPw6

CONTACT: 

If you have any feedback for me, feel free to send me a message on discord at 'ricky.bob'. I am a newb at this myself, so this isn't perfect by any means and welcome feedback. I am also on the Sanic server (which you can find at https://discord.gg/mXKyC6kh7c) under the nickname "Anonymoose".


Requirements:

Check requirements.txt. Do a 'pip install -r requirements.txt'. You may need to use the tutorial link above to set-up other stuff(like postgres). This project uses markdown (which is only implemented on one page as an example, might I add. I will get around to adding it to all pages), Jinja (this must be installed separately from Sanic), and SQLAlchemy/asyncpg. If something doesn't load due to a missing requirement, import it and please let me know so I can fix this.

TO-DO:

- Add markdown to all pages.
- Add Flask-WTForms
- Add a basic Sanic-security demo with login, rate limiting, etc..