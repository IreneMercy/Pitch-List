from flask import render_template, request,redirect,url_for,abort,flash
from ..models import User, Post
from . import main
from flask_login import login_required, current_user,logout_user
from .. import db
from .forms import UpdateProfile, PostPitch

@main.route('/')
@login_required
def index():
    posts = Post.query.all()
    return render_template('index.html',posts = posts)


@main.route('/user<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)
    return render_template('profile/profile.html',user = user)


@main.route('/user/<uname>/update', methods=['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username=uname).first()
    if user is None:
        abort(404)
    form = UpdateProfile()
    if form.validate_on_submit():
        user.bio = form.bio.data
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('.profile',uname=user.username))
    return render_template('profile/update.html', form=form)


@main.route('/post/new', methods=['GET','POST'])
@login_required
def new_post():
    form = PostPitch()
    if form.validate_on_submit():
        posts = Post(title=form.title.data,content=form.content.data,author=current_user)
        db.session.add(posts)
        db.session.commit()
        flash('your post has been created','success')
        return redirect(url_for('main.index'))
    return render_template('create_post.html',title="New Post",form=form)


@main.route('/post/<int:post_id>', methods=["POST"])
@login_required
def del_post(post_id):
    post = Post.query.get(post_id)
    if post.author != current_user:
        abort(403)
    post.delete()
    return redirect(url_for('main.index'))
