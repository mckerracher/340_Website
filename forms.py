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
    episode_list = ["NULL"]
    results = cursor.fetchall()
    for item in results:
        episode_list.append(item['episodeNumber'])
    podcastEpisode = SelectField('Podcast Episode (Optional)', choices=episode_list)

    query = "SELECT idPlatform FROM platform"
    cursor.execute(query)
    platform_list = [item['idPlatform'] for item in cursor.fetchall()]
    platformList = SelectField('Platform (Required)', choices=platform_list)

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
    query = "SELECT nameGame FROM game"
    cursor.execute(query)
    games_list_unsorted = [item['nameGame'] for item in cursor.fetchall()]
    games_list = sorted(games_list_unsorted)
    nameGame = SelectField('Game Name (Required)', choices=games_list,
                           validators=[DataRequired()])

    query = "SELECT idPlatform FROM platform"
    cursor.execute(query)
    platform_list = [item['idPlatform'] for
                     item in cursor.fetchall()]

    idPlatform = SelectField('Platform ID (Required)', choices=platform_list,
                             validators=[DataRequired()])

    submit = SubmitField('Submit')


class AddToM2MPlatformGame(FlaskForm):
    """This defines the add game/platform form"""
    query = "SELECT nameGame FROM game"
    cursor.execute(query)
    games_list_unsorted = [item['nameGame'] for item in cursor.fetchall()]
    games_list = sorted(games_list_unsorted)
    nameGame = SelectField('Game Name (Required)', choices=games_list,
                           validators=[DataRequired()])

    query = "SELECT idPlatform FROM platform"
    cursor.execute(query)
    platform_list = [item['idPlatform'] for
                     item in cursor.fetchall()]

    idPlatform = SelectField('Platform ID (Required)', choices=platform_list,
                             validators=[DataRequired()])

    submit = SubmitField('Submit')


class EditTheGame(FlaskForm):
    """This defines the edit game form"""
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
    """This defines the search form"""
    search = StringField('Search', validators=[DataRequired()])
    submit = SubmitField('Search')


class RemoveGame(FlaskForm):
    """This defines the remove game form"""
    query = "SELECT nameGame FROM game"
    cursor.execute(query)
    games_list_unsorted = [item['nameGame'] for item in cursor.fetchall()]
    games_list = sorted(games_list_unsorted)
    name = SelectField('Game Name', choices=games_list, validators=[DataRequired()])
    submit = SubmitField('Submit')


class RemoveGenre(FlaskForm):
    """This defines the remove genre form"""
    query = "SELECT nameGenre FROM gameGenre"
    cursor.execute(query)
    genre_list = [item['nameGenre'] for item in cursor.fetchall()]
    name = SelectField('Game Genre', choices=genre_list, validators=[DataRequired()])
    submit = SubmitField('Submit')


class RemoveCreator(FlaskForm):
    """This defines the remove creator form"""
    query = "SELECT nameCreator FROM gameCreator"
    cursor.execute(query)
    creator_list = [item['nameCreator'] for item in cursor.fetchall()]
    name = SelectField('Game Creator',
                       choices=creator_list,
                       validators=[DataRequired()])
    submit = SubmitField('Submit')


class RemovePlatform(FlaskForm):
    """This defines the remove platform form"""
    query = "SELECT namePlatform FROM platform"
    cursor.execute(query)
    plat_list = [item['namePlatform'] for item in cursor.fetchall()]
    name = SelectField('Platform',
                       choices=plat_list,
                       validators=[DataRequired()])
    submit = SubmitField('Submit')


class RemoveEpisode(FlaskForm):
    """This defines the remove episode form"""
    query = "SELECT title FROM podcastEpisode"
    cursor.execute(query)
    ep_list = [item['title'] for item in cursor.fetchall()]
    name = SelectField('Episode',
                       choices=ep_list,
                       validators=[DataRequired()])
    submit = SubmitField('Submit')


class RemoveGameAndPlatform(FlaskForm):
    """This defines the remove game/platform form"""
    query = "SELECT nameGame FROM platformFKzz"
    cursor.execute(query)
    ep_list = [item['nameGame'] for item in cursor.fetchall()]
    name = SelectField('Game',
                       choices=ep_list,
                       validators=[DataRequired()])
    submit = SubmitField('Submit')


class SearchPageForm(FlaskForm):
    """This defines the search page form"""
    query = "SELECT nameGame FROM game"
    cursor.execute(query)
    games_list_unsorted = [item['nameGame'] for item in cursor.fetchall()]
    games_list = ['NULL']
    for item in games_list_unsorted:
        games_list.append(item)
    name = SelectField('Game Name', choices=games_list)

    query = "SELECT nameGenre FROM gameGenre"
    cursor.execute(query)
    genre_list = ['NULL']
    second_list = [item['nameGenre'] for item in cursor.fetchall()]
    # order elements and remove duplicates
    second_list = list(set(second_list))
    for item in second_list:
        genre_list.append(item)
    genre = SelectField('Game Genre', choices=genre_list)

    query = "SELECT nameCreator FROM gameCreator"
    cursor.execute(query)
    creator_list = ['NULL']
    tmp = [item['nameCreator'] for item in cursor.fetchall()]
    tmp = list(set(tmp))
    for item in tmp:
        creator_list.append(item)
    creator = SelectField('Game Creator', choices=creator_list)

    query = "SELECT title FROM podcastEpisode"
    cursor.execute(query)
    ep_list = ['NULL']
    tmp = [item['title'] for item in cursor.fetchall()]
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

    cursor.execute("SELECT namePlatform FROM platform")
    platforms = ['NULL']
    tmp = [item['namePlatform'] for item in cursor.fetchall()]
    tmp = list(set(tmp))
    for item in tmp:
        platforms.append(item)
    platform = SelectField('Platforms', choices=platforms)
    submit = SubmitField('Search')
