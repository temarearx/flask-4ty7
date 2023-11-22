from flask import Flask, render_template, url_for, redirect, request
from flask_login import login_user, LoginManager, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
from werkzeug.utils import secure_filename
from models import db, bcrypt, User, Article

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SECRET_KEY'] = 'thisisasecretkey'
db.init_app(app)
app.app_context().push()

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))




class RegisterForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(
        min=4, max=20)], render_kw={"placeholder": "Username"})

    password = PasswordField(validators=[InputRequired(), Length(
        min=4, max=20)], render_kw={"placeholder": "Password"})

    submit = SubmitField("Register")

    def validate_username(self, username):
        existing_user_username = User.query.filter_by(
            username=username.data).first()
        if existing_user_username:
            raise ValidationError("That username already exists. Please choose a different one.")


class LoginForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(
        min=4, max=20)], render_kw={"placeholder": "Username"})

    password = PasswordField(validators=[InputRequired(), Length(
        min=4, max=20)], render_kw={"placeholder": "Password"})

    submit = SubmitField("Login")





@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", author=current_user)


@app.route("/advices")

def adv():
    return render_template("advices.html")


@app.route("/team")

def team():
    return render_template("team.html")

@app.route("/articles")

def articles():
    articles = Article.query.all()
    users = User.query.order_by(User.username).all()
    return render_template("articles.html", data=articles, names=users)


@app.route('/create_article', methods=['POST', 'GET'])
@login_required
def create_article():
    if request.method == "POST":
        title = request.form['title']
        intro = request.form['intro']
        text = request.form['text']

        article = Article(title=title, intro=intro, text=text, author=current_user)

        try:
            db.session.add(article)
            db.session.commit()
            return redirect('/articles')
        except:
            return "Sorry, Its Rassul's fault"
    else:
        return render_template("create_article.html")




@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/articles')
@login_required
def dashboard():
    return render_template('articles.html')



@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect(url_for('home'))
    return render_template('login.html', form=form)



@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        new_user = User(username=form.username.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))

    return render_template('register.html', form=form)


@app.route('/articles/<int:id>')
@login_required
def detail(id):
    article= Article.query.get(id)
    author_username = article.author.username if article.author else None
    return render_template("details.html", article=article, author_username=author_username)


@app.route('/abort')
@login_required
def abort():
    return render_template("/abort.html")



@app.route('/articles/<int:id>/del')
@login_required
def post_delete(id):
    article=Article.query.get_or_404(id)
    if article.author != current_user:
        return redirect("/abort")
    try:
            db.session.delete(article)
            db.session.commit()
            return redirect('/articles')
    except:
            return "Sory, its Rassul's fault"


@app.route('/articles/<int:id>/update', methods=['POST', 'GET'])
@login_required
def post_update(id):
    article = Article.query.get(id)
    if article.author != current_user:
        return redirect("/abort")


    if request.method == "POST":
        article.title = request.form['title']
        article.intro = request.form['intro']
        article.text = request.form['text']

        try:
            db.session.commit()
            return redirect('/articles')
        except:
            return "Sorry, Its Rassul's fault"
    else:
        article = Article.query.get(id)
        return render_template("update.html", article=article)
