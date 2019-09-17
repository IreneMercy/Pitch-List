from flask import render_template, request,redirect,url_for,abort,flash
from ..models import User, Post, Commenting
from . import main
from flask_login import login_required, current_user,logout_user
from .. import db, photos
from .forms import CommentPitch, PostPitch

@main.route('/')
@login_required
def index():
    posts = Post.query.all()
    comment_post = Commenting.query.all()
    return render_template('index.html',posts = posts,comment_post=comment_post)


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
    if request.method == "POST":
        user.bio = request.form.get('bio')
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('main.profile',uname=user.username))
    return render_template('profile/profile.html', user=user)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'images/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))



@main.route('/post/new', methods=['GET','POST'])
@login_required
def new_post():
    form = PostPitch()
    if form.validate_on_submit():
        posts = Post(category=form.category.data,title=form.title.data,content=form.content.data,author=current_user)
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
        error = "You can't delete this Pitch"
        return redirect(url_for('main.index'))
    post.delete()
    return redirect(url_for('main.index'))

@main.route('/comments', methods=['GET','POST'])
@login_required
def Comment():
    form = CommentPitch()
    if form.validate_on_submit():
        comments = Commenting(comment=form.comment.data,comm=current_user)
        db.session.add(comments)
        db.session.commit()
        flash('Your comment has been posted,success')
        return redirect(url_for('main.index'))
    return render_template('index.html',form=form)
