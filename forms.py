from flask_wtf import FlaskForm
from wtforms import StringField, DateField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Length


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
    idGenre = IntegerField('Genre ID')  # TODO - REMOVE???
    nameGenre = StringField('Genre Name (Required)',
                            validators=[DataRequired()])
    submit = SubmitField('Submit')


class AddCreatorForm(FlaskForm):
    idCreator = IntegerField('Genre ID')
    nameCreator = StringField('Creator Name (Required)',
                              validators=[DataRequired()])
    submit = SubmitField('Submit')


class AddPlatformForm(FlaskForm):
    idPlatform = IntegerField('Platform ID')
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


class EditTheGame(FlaskForm):
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
