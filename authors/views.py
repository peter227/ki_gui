import datetime

from flask import (render_template, request, url_for, redirect, flash)
from authors import bp
from authors.models import Authors
from nationalities.models import Nationalities
from db import db


@bp.route("/")
def index_view():
    authors = db.paginate(db.select(Authors).order_by(Authors.id_a), per_page=3)

    return render_template("authors/index.html", authors=authors, title="SQLAlchemyORM - Authors", name=authors,
                           url='authors.index_view')


@bp.route("/edit/<id>", methods=["POST", "GET"])
def update_view(id):
    if not id:
        return redirect(url_for("authors.index_view"))
    try:
        author = db.session.execute(db.select(Authors).filter_by(id_a=id)).first()
        nationalities = db.session.execute(db.select(Nationalities)).unique().all()

    except Exception:
        flash("This author does not exist", "error")
        return redirect(url_for("authors.index_view"))

    if request.method == "POST":
        print(request.form["name"])
        author[0].name = request.form["name"]
        author[0].nationality_id = request.form["nationality"]
        author[0].number_of_songs = request.form["number_of_songs"]
        author[0].number_of_albums = request.form["number_of_albums"]
        author[0].url_photo = request.form["url_photo"]
        author[0].updated_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        author[0].verified = True
        db.session.add(author[0])
        db.session.commit()

        flash("Author was updated", "success")
        return redirect(url_for("authors.index_view"))

    return render_template("authors/update.html", author=author, nationalities=nationalities)


@bp.route("/inspect/<id>", methods=["POST", "GET"])
def inspect_view(id):
    try:
        author = db.session.execute(db.select(Authors).filter_by(id_a=id)).first()
        nationalities = db.session.execute(db.select(Nationalities)).unique().all()
    except Exception:
        flash("This author does not exist", "error")
        return redirect(url_for("authors.index_view"))

    return render_template("authors/inspect.html", author=author, nationalities=nationalities)


@bp.route("/add", methods=["POST", "GET"])
def add_view():
    if request.method == "POST":
        author_name = request.form["name"]
        author_nationality = request.form["nationality"]
        author_number_of_songs = request.form["number_of_songs"]
        author_number_of_albums = request.form["number_of_albums"]
        author_url_photo = request.form["url_photo"]
        author_short_description = request.form["short_description"]
        author_created_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        author_updated_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if author_url_photo == "NULL":
            author = Authors(name=author_name, nationality_id=author_nationality, number_of_songs=author_number_of_songs,
                         number_of_albums=author_number_of_albums,
                         short_description=author_short_description, created_at=author_created_at,
                         updated_at=author_updated_at)
        else:
            author = Authors(name=author_name, nationality_id=author_nationality,
                             number_of_songs=author_number_of_songs,
                             number_of_albums=author_number_of_albums, url_photo=author_url_photo,
                             short_description=author_short_description, created_at=author_created_at,
                             updated_at=author_updated_at)

        db.session.add(author)
        db.session.commit()

        flash("Author was successfully added to database!", "success")
        return redirect(url_for("authors.index_view"))

    else:
        nationalities = db.session.execute(db.select(Nationalities)).unique().all()
        return render_template("authors/add.html", nationalites=nationalities)


@bp.route("/delete/<id>", methods=["POST", "DELETE"])
def delete_record(id):
    if not id:
        return redirect(url_for("authors.index_view"))
    try:
        author = db.session.execute(db.select(Authors).filter_by(id_a=id)).first()
    except Exception:
        flash("This author does not exist", "error")
        return redirect(url_for("authors.index_view"))

    if request.method == "POST":
        db.session.delete(author[0])
        print(author[0].id_a)
        db.session.commit()
        flash('Author was successfully deleted from database', 'success')
        return redirect(url_for("authors.index_view"))
