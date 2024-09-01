from crypt import methods
from app.models import Post, db
from flask import render_template, request, redirect, url_for
from app.posts import  posts_blueprint


@posts_blueprint.route("/index")
def index():
    posts=Post.query.all()
    return render_template("posts/index.html", posts=posts)

@posts_blueprint.route("/posts/<int:id>", endpoint="show")
def show(id):
    post=Post.query.get_or_404(id)
    return render_template("posts/show.html", post=post)



@posts_blueprint.route("/create", endpoint="create", methods=["GET","POST" ])
def create():
    if request.method == "POST":
        name = request.form['name']
        description = request.form['description']
        image =  request.form['image']
        post= Post (name=name, description=description, image=image)
        db.session.add (post)
        db.session.commit()
        return redirect(url_for('posts.index'))
    return render_template("posts/create.html")


@posts_blueprint.route("/Delete/<int:id>", endpoint="delete")
def delete(id):
    post = Post.query.get(id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for("posts.index"))


@posts_blueprint.route('/edit/<int:id>',methods=["GET","POST"], endpoint='edit_post')
def edit(id):
    post= Post.query.get_or_404(id)
    if request.method == 'POST':
        post.name = request.form.get('name')
        post.description = request.form.get('description')
        db.session.commit()
        return redirect(url_for('posts.index'))
    return render_template('posts/edit.html', post=post)
