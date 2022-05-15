from flask import render_template,request,redirect,url_for
from . import main
from ..models import Blog,User,Upvote,Downvote,Comments
from ..request import get_quotes
from flask_login import login_required,current_user
from .forms import BlogForm,UpdateProfile,CommentForm
from .. import db,photos

@main.route('/')
def index():
    title='E-Blogs'
    blogs=Blog.query.all()
    random_quotes=get_quotes()


    return render_template('index.html', title=title, quotes=random_quotes, post=blogs)

@main.route('/blog/<int:blog_id>', methods = ['GET'])

def blogs(blog_id):
    form = CommentForm()
    blog = Blog.query.get(blog_id)
    # all_comments = Comment.query.filter_by(blog_id = blog_id).all()
   
    return render_template('blog.html', blog = blog)

@main.route('/blog/create', methods=['POST','GET'])
@login_required
def create_blog():
    form=BlogForm()
    if form.validate_on_submit():
        title = form.title.data
        post = form.post.data
        user_id=current_user
        
        new_blog_object = Blog(post=post,user_id=current_user._get_current_object().id,title=title)
        new_blog_object.save_blog()
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

@main.route('/like/<int:id>',methods = ['POST','GET'])
@login_required
def likes(id):
    get_blogs = Upvote.get_upvotes(id)
    valid_string = f'{current_user.id}:{id}'
    for blog in get_blogs:
        to_str = f'{blog}'
        print(valid_string+" "+to_str)
        if valid_string == to_str:
            return redirect(url_for('main.index',id=id))
        else:
            continue
    new_vote = Upvote(user = current_user, blog_id=id)
    new_vote.save_upvote()
    return redirect(url_for('main.index',id=id))

@main.route('/dislike/<int:id>',methods = ['POST','GET'])
@login_required
def dislikes(id):
    blog = Downvote.get_downvotes(id)
    valid_string = f'{current_user.id}:{id}'
    for b in blog:
        to_str = f'{p}'
        print(valid_string+" "+to_str)
        if valid_string == to_str:
            return redirect(url_for('main.index',id=id))
        else:
            continue
    new_downvote = Downvote(user = current_user, blog_id=id)
    new_downvote.save_downvote()
    return redirect(url_for('main.index',id = id))


@main.route('/comment/<int:blog_id>', methods = ['POST','GET'])
@login_required
def comment(blog_id):
  comments = Comments.query.filter_by(blog_id=blog_id).all()
  form = CommentForm()
  if form.validate_on_submit():
    comment = form.comment.data

    new_comment_obj = Comments(comment=comment, blog_id=blog_id, user_id = current_user._get_current_object().id)

    new_comment_obj.save_comment()
    return redirect(url_for('main.comment', blog_id=blog_id))

  return render_template('comment.html', form=form, comments=comments)
