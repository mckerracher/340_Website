from flask_wtf import FlaskForm
from wtforms import StringField, DateField, IntegerField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length
import Database.db_connector as db
import pymysql.cursors

conn = db.connect_to_database()
cursor = conn.cursor(pymysql.cursors.DictCursor)


class AddGameForm(FlaskForm):
    """This defines the add game form"""
    nameGame = StringField('Game Name (Required)',
                           validators=[DataRequired(), Length(min=1, max=255)])
    releaseDate = DateField('Release Date (Required)',
                            validators=[DataRequired()])
    cost = IntegerField('Game Cost (Required)', validators=[DataRequired()])

    gameGenre = SelectField('Game Genre (Required)', validators=[DataRequired()])

    gameCreator = SelectField('Game Creator (Required)', validators=[DataRequired()])

    podcastEpisode = SelectField('Podcast Episode (Optional)')

    platformList = SelectField('Platform (Required)')

    submit = SubmitField('Submit')


class AddGenreForm(FlaskForm):
    """This defines the add genre form"""
    nameGenre = StringField('Genre Name (Required)',
                            validators=[DataRequired()])
    submit = SubmitField('Submit')


class AddCreatorForm(FlaskForm):
    """This defines the add creator form"""
    nameCreator = StringField('Creator Name (Required)',
                              validators=[DataRequired()])
    submit = SubmitField('Submit')


class AddPlatformForm(FlaskForm):
    """This defines the add platform form"""
    true_false = ["True", "False"]
    namePlatform = StringField('Platform Name (Required)', validators=[DataRequired()])
    playedOnline = SelectField('Playable Online? (Required)', choices=true_false, validators=[DataRequired()])
    multiPlat = SelectField('Playable on Multiple Platforms? (Required)', choices=true_false,
                            validators=[DataRequired()])
    submit = SubmitField('Submit')


class AddEpisodeForm(FlaskForm):
    """This defines the add episode form"""
    episodeNumber = IntegerField('Episode Number')
    title = StringField('Episode Title (Required)',
                        validators=[DataRequired()])
    episodeDate = DateField('Episode Date (Required: YYYY-MM-DD)',
                            validators=[DataRequired()])
    submit = SubmitField('Submit')


class AddToM2MPlatformGame(FlaskForm):
    """This defines the add M2M form"""
    nameGame = SelectField('Game Name (Required)', validators=[DataRequired()])

    idPlatform = SelectField('Platform ID (Required)', validators=[DataRequired()])

    submit = SubmitField('Submit')


class EditTheGame(FlaskForm):
    """This defines the edit game form"""
    originalName = SelectField('*Original* Game Name (Required)', validators=[DataRequired()])

    nameGame = StringField('Updated Game Name (Required)', validators=[DataRequired(), Length(min=1, max=255)])
    releaseDate = DateField('Updated Release Date (Required)', validators=[DataRequired()])
    cost = IntegerField('Updated Game Cost (Required)', validators=[DataRequired()])

    gameGenre = SelectField('Updated Game Genre (Required)', validators=[DataRequired()])

    gameCreator = SelectField('Updated Game Creator (Required)', validators=[DataRequired()])

    podcastEpisode = SelectField('(Optional) Updated Podcast Episode')

    submit = SubmitField('Submit Change')


class SearchForm(FlaskForm):
    """This defines the search form"""
    search = StringField('Search', validators=[DataRequired()])
    submit = SubmitField('Search')


class RemoveGame(FlaskForm):
    """This defines the remove game form"""
    name = SelectField('Game Name', validators=[DataRequired()])
    submit = SubmitField('Submit')


class RemoveGenre(FlaskForm):
    """This defines the remove genre form"""
    name = SelectField('Game Genre', validators=[DataRequired()])
    submit = SubmitField('Submit')


class RemoveCreator(FlaskForm):
    """This defines the remove creator form"""
    name = SelectField('Game Creator', validators=[DataRequired()])
    submit = SubmitField('Submit')


class RemovePlatform(FlaskForm):
    """This defines the remove platform form"""
    name = SelectField('Platform', validators=[DataRequired()])
    submit = SubmitField('Submit')


class RemoveEpisode(FlaskForm):
    """This defines the remove episode form"""
    name = SelectField('Episode', validators=[DataRequired()])
    submit = SubmitField('Submit')


class RemoveGameAndPlatform(FlaskForm):
    """This defines the remove game/platform form"""
    name = SelectField('Game', validators=[DataRequired()])
    submit = SubmitField('Submit')


class SearchPageForm(FlaskForm):
    """This defines the search page form"""
    name = SelectField('Game Name')

    genre = SelectField('Game Genre')

    creator = SelectField('Game Creator')

    episode = SelectField('Podcast Episode')

    date = SelectField('Release Date')

    cost = SelectField('Game Cost')

    platform = SelectField('Platforms')

    submit = SubmitField('Search')
