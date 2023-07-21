from app import app
from routes.blueprints import blueprints
from routes.blueprints import bp_user_comments, bp_user_posts
from database import database

@app.listener('before_server_start')
async def connect_to_db(app, loop):
    await database.connect()

for bp in blueprints:
    app.blueprint(bp)
    print(bp)  
app.blueprint(bp_user_comments)
app.blueprint(bp_user_posts)
app.static("/static", "./static")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, auto_reload=True, debug=True)