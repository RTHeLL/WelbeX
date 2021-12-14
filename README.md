# Requirements
- PostgresSQL
- Python 3.8
- NodeJS 10+
- npm 6+

# Install and start
Clone `https://github.com/RTHeLL/WelbeXTZ.git`
###### Install requirements for back-end ######
1. Go to `backend` folder
2. Use command `pip install -r requirements.txt` or use pipenv

###### Install requirements for front-end ######
1. Go to `client` folder
2. Use command `npm install`

###### Configure PostgreSQL ######
1. Go to `backend` folder
2. Open `app.py` file
3. Change first `welbextz` on `username`
4. Change `123456` on `password`
5. Change second `welbextz` on `database`
6. Save and exit

###### Make migrations ######
1. Go to `backend` folder
2. Use command `flask db upgrade`

###### Run ######
1. Go to `backend` folder
2. Use command `python main.app`
3. Go to `client` folder
4. Use command `npm start`
