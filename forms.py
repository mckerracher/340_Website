from flask_wtf import FlaskForm
from wtforms import StringField, DateField, IntegerField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length
import MySQLdb
import Database.db_connector as db

conn = db.connect_to_database()
cursor = conn.cursor(MySQLdb.cursors.DictCursor)

class AddGameForm(FlaskForm):
    nameGame = StringField('Game Name (Required)',
                           validators=[DataRequired(), Length(min=1, max=255)])
    releaseDate = DateField('Release Date (Required)',
                            validators=[DataRequired()])
    cost = IntegerField('Game Cost', validators=[DataRequired()])
    gameGenre = StringField('Game Genre (Required)',
                            validators=[DataRequired(),
                                        Length(min=1, max=255)])
    gameCreator = StringField('Game Creator (Required)',
                              validators=[DataRequired(),
                                          Length(min=1, max=255)])
    podcastEpisode = IntegerField('Podcast Episode')
    submit = SubmitField('Submit')


class AddGenreForm(FlaskForm):
    nameGenre = StringField('Genre Name (Required)',
                            validators=[DataRequired()])
    submit = SubmitField('Submit')


class AddCreatorForm(FlaskForm):
    nameCreator = StringField('Creator Name (Required)',
                              validators=[DataRequired()])
    submit = SubmitField('Submit')


class AddPlatformForm(FlaskForm):
    namePlatform = StringField('Platform Name (Required)',
                               validators=[DataRequired()])
    playedOnline = StringField('Playable Online? T/F (Required)',
                               validators=[DataRequired()])
    multiPlat = StringField('Playable on Multiple Platforms? T/F (Required)',
                            validators=[DataRequired()])
    submit = SubmitField('Submit')


class AddEpisodeForm(FlaskForm):
    episodeNumber = IntegerField('Episode Number')
    title = StringField('Episode Title (Required)',
                        validators=[DataRequired()])
    episodeDate = DateField('Episode Date (Required: YYYY-MM-DD)',
                            validators=[DataRequired()])
    submit = SubmitField('Submit')


class AddPost(FlaskForm):
    author = StringField('Author')
    date_posted = DateField('Date')
    title = StringField('Post Title')
    content = StringField('Content')
    submit = SubmitField('Post')


class AddToM2MPlatformGame(FlaskForm):
    nameGame = StringField('Game Name (Required)', validators=[DataRequired()])
    idPlatform = IntegerField('Platform ID (Required)',
                              validators=[DataRequired()])
    submit = SubmitField('Submit')


class AddToM2MPlatformGame(FlaskForm):
    nameGame = StringField('Game Name (Required)', validators=[DataRequired()])
    idPlatform = IntegerField('Platform ID (Required)',
                              validators=[DataRequired()])
    submit = SubmitField('Submit')


class EditTheGame(FlaskForm):
    query = "SELECT nameGame FROM game"
    cursor.execute(query)
    games_list_unsorted = [item['nameGame'] for item in cursor.fetchall()]
    games_list = sorted(games_list_unsorted)
    originalName = SelectField('*Original* Game Name (Required)', choices=games_list, validators=[DataRequired()])

    nameGame = StringField('Updated Game Name (Required)', validators=[DataRequired(), Length(min=1, max=255)])
    releaseDate = DateField('Updated Release Date (Required)', validators=[DataRequired()])
    cost = IntegerField('Updated Game Cost (Required)', validators=[DataRequired()])

    query = "SELECT idGenre FROM gameGenre"
    cursor.execute(query)
    genre_list = [item['idGenre'] for item in cursor.fetchall()]
    gameGenre = SelectField('Updated Game Genre (Required)', choices=genre_list, validators=[DataRequired()])

    query = "SELECT idCreator FROM gameCreator"
    cursor.execute(query)
    creator_list = [item['idCreator'] for item in cursor.fetchall()]
    gameCreator = SelectField('Updated Game Creator (Required)', choices=creator_list, validators=[DataRequired()])

    query = "SELECT episodeNumber FROM podcastEpisode"
    cursor.execute(query)
    episode_list = [item['episodeNumber'] for item in cursor.fetchall()]
    podcastEpisode = SelectField('(Optional) Updated Podcast Episode', choices=episode_list)

    submit = SubmitField('Submit Change')


class SearchForm(FlaskForm):
    search = StringField('Search', validators=[DataRequired()])
    submit = SubmitField('Search')


class RemoveGame(FlaskForm):
    name = StringField('Game', validators=[DataRequired()])
    submit = SubmitField('Submit')


class RemoveGenre(FlaskForm):
    name = StringField('Genre ID (You must use the Genre ID number)', validators=[DataRequired()])
    submit = SubmitField('Submit')


class RemoveCreator(FlaskForm):
    name = StringField('Creator ID (You must use the Creator ID number)', validators=[DataRequired()])
    submit = SubmitField('Submit')


class RemovePlatform(FlaskForm):
    name = StringField('Platform (You must use the Platform ID number)', validators=[DataRequired()])
    submit = SubmitField('Submit')


class RemoveEpisode(FlaskForm):
    name = StringField('Episode (You must use the Episode number)', validators=[DataRequired()])
    submit = SubmitField('Submit')


class RemoveGameAndPlatform(FlaskForm):
    name = StringField('Combo Name', validators=[DataRequired()])
    submit = SubmitField('Submit')
