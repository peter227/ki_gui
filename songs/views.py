import datetime

from flask import (render_template, request, url_for, redirect, flash)

from authors.models import Authors
from songs import bp

from songs.models import Songs
from genres.models import Genres
from albums.models import Albums
from db import db


@bp.route("/")
def index_view():

    songs = Songs.query.all()
    return render_template("songs/index.html",
                           songs=songs, title="SQLAlchemyORM - Songs",
                           name=songs, url='songs.index_view')


@bp.route("/edit/<id>", methods=["POST", "GET"])
def update_view(id):
    if not id:
        return redirect(url_for("songs.index_view"))
    try:
        song = Songs.query.get(id)
        genres = Genres.query.all()
        albums = Albums.query.all()
    except Exception:
        flash("This song does not exist", "error")
        return redirect(url_for("songs.index_view"))

    if request.method == "POST":
        song.name = request.form["name"]
        song.genre_id = request.form["genre"]
        song.length = request.form["length"]
        song.number_of_plays = request.form["number_of_plays"]
        if song.album_id is "None":
            print(song.album_id)
            song.album_id = None
        else:
            song.album_id = request.form["album"]
        song.release_year = request.form["release_year"]
        song.url_cover = request.form["url_cover"]
        song.updated_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        song.verified = True
        db.session.add(song)
        db.session.commit()

        flash("Song updated", "success")
        return redirect(url_for("songs.index_view"))

    return render_template("songs/update.html", song=song, albums=albums, genres=genres)


@bp.route("/inspect/<id>", methods=["POST", "GET"])
def inspect_view(id):
    try:
        song = db.session.execute(db.select(Songs).filter_by(id_s=id)).first()
    except Exception:
        flash("This song does not exist", "error")
        return redirect(url_for("songs.index_view"))

    return render_template("songs/inspect.html", song=song)


@bp.route("/add", methods=["POST", "GET"])
def add_view():
    if request.method == "POST":
        song_name = request.form["name"]
        song_genre_id = request.form["genre"]
        song_length = request.form["length"]
        song_number_plays = request.form["number_of_plays"]
        song_album_id = request.form["album"]
        song_release_year = request.form["release_year"]
        song_url_cover = request.form["url_cover"]
        song_created_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        song_updated_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if song_album_id == "NULL" or song_url_cover == "NULL":
            song = Songs(name=song_name, genre_id=song_genre_id, length=song_length, number_of_plays=song_number_plays, release_year=song_release_year, created_at=song_created_at ,updated_at=song_updated_at)
        else:
            song = Songs(name=song_name, genre_id=song_genre_id, length=song_length, urL_cover = song_url_cover,number_of_plays=song_number_plays, album_id=song_album_id,release_year=song_release_year, created_at=song_created_at ,updated_at=song_updated_at)

        db.session.add(song)

        authors = request.form.getlist("author")
        print(authors)
        for author_id in authors:
            author = Authors.query.filter_by(id_a=author_id).first()
            if author:
                song.authors.append(author)

        db.session.commit()

        flash("Song was successfully added to database!", "success")
        return redirect(url_for("songs.index_view"))

    else:
        genres = Genres.query.all()
        albums = Albums.query.all()
        authors = Authors.query.all()
        return render_template("songs/add.html", albums=albums, genres=genres, authors=authors)


@bp.route("/delete/<id>", methods=["POST", "DELETE"])
def delete_record(id):
    if not id:
        return redirect(url_for("songs.index_view"))
    try:
        song = Songs.query.get(id)
    except Exception:
        flash("This song does not exist", "error")
        return redirect(url_for("songs.index_view"))

    if request.method == "POST":
        db.session.delete(song)
        print(song.id_s)
        db.session.commit()
        flash("Song was successfully deleted from database", "success")
        return redirect(url_for("songs.index_view"))