from flask import Blueprint, abort
from flask import flash, render_template, redirect, url_for, request
from flask_login import (
    current_user,
    login_user,
    logout_user,
    login_required,
    user_accessed,
)
from flask_mail import Message
from luna.forms import (
    RegistrationForm,
    LoginForm,
    UpdateAccountForm,
    EmailForm,
    PasswordForm,
)
from luna.models import db, User
from luna.instance import bcrypt, mail
from luna.util import ts
from itsdangerous import SignatureExpired


# creating an instance of Blueprint in routes
users = Blueprint("users", __name__, static_folder="static")


# Home route
@users.route("/")
@users.route("/home")
def home():
    # noOfItems = getLoginDetails()
    return render_template("home.html")


# Registration route
@users.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("users.home"))
    form = RegistrationForm()

    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode(
            "utf-8"
        )
        user = User(
            firstname=form.firstname.data,
            lastname=form.lastname.data,
            email=form.email.data,
            password=hashed_password,
        )
        db.session.add(user)
        db.session.commit()
        flash("Your account has been created!", "success")
        return redirect(url_for("users.login"))
    return render_template(
        "register.html",
        title="Register",
        form=form,
    )


# Login route
@users.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("users.home"))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get("next")
            return redirect(next_page) if next_page else redirect(url_for("users.home"))
        else:
            flash("Login Unsuccessful. Please check username and password", "danger")
    return render_template("login.html", title="Login", form=form)


@users.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("users.home"))


@users.route("/account", methods=["GET", "POST"])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        current_user.firstname = form.firstname.data
        current_user.lastname = form.lastname.data
        current_user.email = form.email.data
        db.session.commit()
        flash("Your account has been updated!", "success")
        return redirect(url_for("users.account"))
    elif request.method == "GET":
        form.firstname.data = current_user.firstname
        form.lastname.data = current_user.lastname
        form.email.data = current_user.email
    return render_template("account.html", title="Account", form=form)


@users.route("/reset", methods=["GET", "POST"])
def reset_password():
    if current_user.is_authenticated:
        return redirect(url_for("users.home"))

    form = EmailForm()
    if form.validate_on_submit():
        # verify if user exists
        email = User.query.filter_by(email=form.email.data).first()
        form_mail = form.email.data

        # sending the email confirmation link
        msg = Message("Confirm Email", recipients=[form_mail])

        token = ts.dumps(form_mail, salt="password-reset-salt")

        recover_url = url_for("users.token_reset", token=token, _external=True)

        msg.body = "Your link is {}".format(recover_url)
        mail.send(msg)
        flash(
            "An email has been sent with instructions to reset your password.", "info"
        )

        return redirect(url_for("users.home"))
    return render_template("reset.html", form=form)


@users.route("/reset/<token>", methods=["POST","GET"])
def token_reset(token):
    # if current_user.is_authenticated:
    #     return redirect(url_for('users.home'))
    try:
        # token generated
        email = ts.loads(token, salt="password-reset-salt", max_age=36000)
        print(email)
    except SignatureExpired:
        flash("The password reset link is invalid or has expired.", "info")
        return redirect(url_for("users.login"))
    form = PasswordForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode("utf-8" )
        print(hashed_password)
        user = User.query.filter_by(email=email).first()
        print(user)
        user.password=hashed_password
        print(user.password)
        db.session.commit()
        flash("Your password has been updated! You are now able to log in", "success")
        return redirect(url_for("users.login"))
    return render_template("reset_with_token.html", token=token, form=form)


