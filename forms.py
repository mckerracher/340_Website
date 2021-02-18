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
    idCreator = IntegerField('Genre ID (Required)',
                             validators=[DataRequired()])
    nameCreator = StringField('Creator Name (Required)',
                              validators=[DataRequired()])
    submit = SubmitField('Submit')


class AddPlatformForm(FlaskForm):
    idPlatform = IntegerField('Platform ID (Required)',
                              validators=[DataRequired()])
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


class AddDistributionPlatformForm(FlaskForm):
    idDistribPlat = IntegerField('Distribution Platform ID (Required)',
                                 validators=[DataRequired()])
    nameDistrib = StringField('Distribution Platform Name (Required)',
                              validators=[DataRequired()])
    platformRel = StringField('Platform Relation', validators=[DataRequired()])
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


class AddToM2MDistribPlatformGame(FlaskForm):
    nameGame = StringField('Game Name (Required)', validators=[DataRequired()])
    idPlatform = IntegerField('Distribution Platform ID (Required)',
                              validators=[DataRequired()])
    submit = SubmitField('Submit')


class RemoveTheThing(FlaskForm):
    item = StringField('Item ID', validators=[DataRequired()])
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
