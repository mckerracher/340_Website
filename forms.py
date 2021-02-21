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
    cost = IntegerField('Game Cost (Required)', validators=[DataRequired()])

    query = "SELECT idGenre FROM gameGenre"
    cursor.execute(query)
    genre_list = [item['idGenre'] for item in cursor.fetchall()]
    gameGenre = SelectField('Game Genre (Required)', choices=genre_list, validators=[DataRequired()])

    query = "SELECT idCreator FROM gameCreator"
    cursor.execute(query)
    creator_list = [item['idCreator'] for item in cursor.fetchall()]
    gameCreator = SelectField('Game Creator (Required)', choices=creator_list, validators=[DataRequired()])

    query = "SELECT episodeNumber FROM podcastEpisode"
    cursor.execute(query)
    episode_list = [item['episodeNumber'] for item in cursor.fetchall()]
    podcastEpisode = SelectField('Podcast Episode (Optional)', choices=episode_list)
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
    query = "SELECT nameGame FROM game"
    cursor.execute(query)
    games_list_unsorted = [item['nameGame'] for item in cursor.fetchall()]
    games_list = sorted(games_list_unsorted)
    name = SelectField('Game Name', choices=games_list, validators=[DataRequired()])
    submit = SubmitField('Submit')


class RemoveGenre(FlaskForm):
    query = "SELECT nameGenre FROM gameGenre"
    cursor.execute(query)
    genre_list = [item['nameGenre'] for item in cursor.fetchall()]
    name = SelectField('Game Genre', choices=genre_list, validators=[DataRequired()])
    submit = SubmitField('Submit')


class RemoveCreator(FlaskForm):
    query = "SELECT nameCreator FROM gameCreator"
    cursor.execute(query)
    creator_list = [item['nameCreator'] for item in cursor.fetchall()]
    name = SelectField('Game Creator',
                              choices=creator_list,
                              validators=[DataRequired()])
    submit = SubmitField('Submit')


class RemovePlatform(FlaskForm):
    query = "SELECT namePlatform FROM platform"
    cursor.execute(query)
    plat_list = [item['namePlatform'] for item in cursor.fetchall()]
    name = SelectField('Platform',
                       choices=plat_list,
                       validators=[DataRequired()])
    submit = SubmitField('Submit')


class RemoveEpisode(FlaskForm):
    query = "SELECT title FROM podcastEpisode"
    cursor.execute(query)
    ep_list = [item['title'] for item in cursor.fetchall()]
    name = SelectField('Episode',
                       choices=ep_list,
                       validators=[DataRequired()])
    submit = SubmitField('Submit')


class RemoveGameAndPlatform(FlaskForm):
    query = "SELECT nameGame FROM platformFKzz"
    cursor.execute(query)
    ep_list = [item['nameGame'] for item in cursor.fetchall()]
    name = SelectField('Game',
                       choices=ep_list,
                       validators=[DataRequired()])
    submit = SubmitField('Submit')


class SearchPageForm(FlaskForm):
    query = "SELECT nameGame FROM game"
    cursor.execute(query)
    games_list_unsorted = [item['nameGame'] for item in cursor.fetchall()]
    games_list = ['NULL']
    for item in games_list_unsorted:
        games_list.append(item)
    name = SelectField('Game Name', choices=games_list)

    query = "SELECT gameGenre FROM game"
    cursor.execute(query)
    genre_list = ['NULL']
    second_list = [item['gameGenre'] for item in cursor.fetchall()]
    second_list = list(set(second_list))  # order elements and remove duplicates
    for item in second_list:
        genre_list.append(item)
    genre = SelectField('Game Genre', choices=genre_list)

    query = "SELECT gameCreator FROM game"
    cursor.execute(query)
    creator_list = ['NULL']
    tmp = [item['gameCreator'] for item in cursor.fetchall()]
    tmp = list(set(tmp))
    for item in tmp:
        creator_list.append(item)
    creator = SelectField('Game Creator', choices=creator_list)

    query = "SELECT podcastEpisode FROM game"
    cursor.execute(query)
    ep_list = ['NULL']
    tmp = [item['podcastEpisode'] for item in cursor.fetchall()]
    tmp = list(set(tmp))
    for item in tmp:
        ep_list.append(item)
    episode = SelectField('Podcast Episode', choices=ep_list)

    query = "SELECT releaseDate FROM game"
    cursor.execute(query)
    date_list = ['NULL']
    tmp = [item['releaseDate'] for item in cursor.fetchall()]
    tmp = list(set(tmp))
    for item in tmp:
        date_list.append(item)
    date = SelectField('Release Date', choices=date_list)

    query = "SELECT cost FROM game"
    cursor.execute(query)
    cost_list = ['NULL']
    tmp = [item['cost'] for item in cursor.fetchall()]
    tmp = list(set(tmp))
    for item in tmp:
        cost_list.append(item)
    cost = SelectField('Game Cost', choices=cost_list)
    submit = SubmitField('Search')
