from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from puppycompanyblog import db
from puppycompanyblog.models import User, BlogPost
from puppycompanyblog.users.forms import RegistrationForm, LoginForm, UpdateUserForm
from puppycompanyblog.users.picture_handler import add_profile_pic

# register this as a Blueprint
users = Blueprint('users', __name__)


# register
@users.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        # create new user
        user = User(email=form.email.data,
                    username=form.username.data, password=form.password.data)
        # add to the db
        db.session.add(User)
        db.session.commit()
        # redirect to users login
        flash("Thanks for registration.")
        return redirect(url_for('users.login'))
    # if it is not a POST request just show the form
    return render_template('register.html', form=form)


# login

@users.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        # query the user that already exists
        user = User.query.filter_by(
            email=form.email.data).first()  # grab the first user
        # make sure they provided the correct password
        if user.check_password(form.password.data) and user is not None:
            login_user(user)
            flash("Login success")

            # grab what the user was trying to access
            next = request.args.get('next')

            if next == None or not next[0] == '/':
                next = url_for('core.index')

            return redirect(next)

    return render_template('login.html', form=form)


# logout
@users.route("/logout")
def logout():
    logout_user()
    # logout and redirect the user back home
    return redirect(url_for("core.index"))


# account (update user)

@users.route('/account', methods=['GET', 'POST'])
@login_required  # you have to be loggin in to see this update page
def account():

    form = UpdateUserForm()
    if form.validate_on_submit():

                # handle picture upload
        if form.picture.data:  # if they upload picture data
            username = current_user.username
            pic = add_profile_pic(form.picture.data, username)
            current_user.profile_image = pic

        # POST
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('User Account Updated!')
        return redirect(url_for('users.account'))

    # user is not submitting anything
    # we are grabbing their current information
    elif request.method == "GET":
        form.username.data = current_user.username
        form.email.data = current_user.email

    # grab the profile image and send it to template to render
    profile_image = url_for(
        'static', filename='profile_pics/'+current_user.profile_image)
    return render_template('account.html', profile_image=profile_image, form=form)


# user's list of blog posts
@users.route("/<username>")
def user_posts(username):

	# grab the page itself
    # grab blog posts associated with the user
    page = request.args.get('page', 1, type=int)  # this is for pagination

    # either grab the first user or return a 404 error
    user = User.query.filter_by(username=username).first_or_404()
    blog_posts = BlogPost.query.filter_by(author=user).order_by(
        BlogPost.date.desc()).paginate(page=page, per_page=5)
    return render_template('user_blog_posts.html', blog_posts=blog_posts, user=user)

    
