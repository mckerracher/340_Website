from flask_wtf import FlaskForm
from wtforms import StringField, DateField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Length


class AddGameForm(FlaskForm):
    nameGame = StringField('Game Name', validators=[DataRequired(), Length(min=1, max=255)])
    releaseDate = DateField('Release Date', validators=[DataRequired()])
    cost = IntegerField('Game Cost', validators=[DataRequired()])
    gameGenre = StringField('Game Genre', validators=[DataRequired(), Length(min=1, max=255)])
    gameCreator = StringField('Game Creator', validators=[DataRequired(), Length(min=1, max=255)])
    podcastEpisode = IntegerField('Podcast Episode', validators=[DataRequired()])
    submit = SubmitField('Submit')


class AddGenreForm(FlaskForm):
    idGenre = IntegerField('Genre ID', validators=[DataRequired()])
    nameGenre = StringField('Genre Name', validators=[DataRequired()])
    submit = SubmitField('Submit')


class AddCreatorForm(FlaskForm):
    idCreator = IntegerField('Genre ID', validators=[DataRequired()])
    nameCreator = StringField('Creator Name', validators=[DataRequired()])
    submit = SubmitField('Submit')


class AddPlatformForm(FlaskForm):
    idPlatform = IntegerField('Platform ID', validators=[DataRequired()])
    namePlatform = StringField('Platform Name', validators=[DataRequired()])
    playedOnline = StringField('Playable Online? (True or False)', validators=[DataRequired()])
    multiPlat = StringField('Playable on Multiple Platforms? (T/F)', validators=[DataRequired()])
    submit = SubmitField('Submit')


class AddEpisodeForm(FlaskForm):
    episodeNumber = IntegerField('Episode Number', validators=[DataRequired()])
    title = StringField('Episode Title', validators=[DataRequired()])
    episodeDate = DateField('Episode Date', validators=[DataRequired()])
    submit = SubmitField('Submit')


class AddDistributionPlatformForm(FlaskForm):
    idDistribPlat = IntegerField('Distribution Platform ID', validators=[DataRequired()])
    nameDistrib = StringField('Distribution Platform Name', validators=[DataRequired()])
    platformRel = StringField('Platform Relation', validators=[DataRequired()])
    submit = SubmitField('Submit')


class AddPost(FlaskForm):
    author = StringField('Author')
    date_posted = DateField('Date')
    title = StringField('Post Title')
    content = StringField('Content')
    submit = SubmitField('Post')


class AddToM2MPlatformGame(FlaskForm):
    nameGame = StringField('Game Name', validators=[DataRequired()])
    idPlatform = IntegerField('Platform ID', validators=[DataRequired()])
    submit = SubmitField('Submit')


class AddToM2MDistribPlatformGame(FlaskForm):
    nameGame = StringField('Game Name', validators=[DataRequired()])
    idPlatform = IntegerField('Distribution Platform ID', validators=[DataRequired()])
    submit = SubmitField('Submit')


class RemoveTheThing(FlaskForm):
    item = StringField('Item ID', validators=[DataRequired()])
    submit = SubmitField('Submit')

