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
