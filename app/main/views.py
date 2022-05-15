from flask import render_template,request,redirect,url_for
from . import main
from ..models import Blog,User
from ..request import get_quotes
from flask_login import login_required,current_user
from .forms import BlogForm,UpdateProfile
from .. import db,photos

@main.route('/')
def index():
    title='E-Blogs'
    blogs=Blog.query.all()
    random_quotes=get_quotes()


    return render_template('index.html', title=title, quotes=random_quotes, post=blogs)

@main.route('/pitch/create', methods=['POST','GET'])
@login_required
def create_blog():
    form=BlogForm()
    if form.validate_on_submit():
        title = form.title.data
        post = form.post.data
        user_id=current_user
        
        new_blog_object = Blog(post=post,user_id=current_user._get_current_object().id,title=title)
        new_blog_object.save_pitch()
        return redirect(url_for('main.index'))
        
    return render_template('newblog.html', form = form)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()
    user_id = current_user._get_current_object().id
    posts = Blog.query.filter_by(user_id = user_id).all()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user,posts=posts)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def upload_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))