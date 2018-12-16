from flask import Flask, render_template, flash, request, redirect, session

app=Flask(__name__)

# @app.route("/")
# def index():
#     return render_template("index.html")

@app.route("/")
def home():
    if not session.get('islogged_in'):
        return render_template("signin.html")
    else:
        return render_template("home.html")

# @app.route('/login', methods=['POST'])
# def user_login():
#     user_id = request.form.get("user_id")
#     password = request.form.get("password")

    #session['islogged_in'] = True
# else:
#     flash('wrong password!')
#     return render_template('home')


# import os
#
# from flask import Flask, render_template, request
# from sqlalchemy import create_engine
# from sqlalchemy.orm import scoped_session, sessionmaker
#
# app = Flask(__name__)
#
# engine = create_engine(os.getenv("DATABASE_URL"))
# db = scoped_session(sessionmaker(bind=engine))
#
# @app.route("/")
# def index():
#     flights = db.execute("SELECT * FROM flights").fetchall()
#     return render_template("index.html", flights=flights)
#
# @app.route("/book", methods=["POST"])
# def book():
#     """Book a flight."""
#
#     # Get form information.
#     name = request.form.get("name")
#     try:
#         flight_id = int(request.form.get("flight_id"))
#     except ValueError:
#         return render_template("error.html", message="Invalid flight number.")
#
#     # Make sure the flight exists.
#     if db.execute("SELECT * FROM flights WHERE id = :id", {"id": flight_id}).rowcount == 0:
#         return render_template("error.html", message="No such flight with that id.")
#     db.execute("INSERT INTO passengers (name, flight_id) VALUES (:name, :flight_id)",
#             {"name": name, "flight_id": flight_id})
#     db.commit()
#     return render_template("success.html")
#
