from flask import Flask, render_template, flash, redirect, url_for
import MySQLdb
import Database.db_connector as db
from xl2dict import XlToDict  # https://pypi.org/project/xl2dict/
from forms import AddGameForm, AddGenreForm, AddCreatorForm, AddPlatformForm, \
    AddEpisodeForm, \
    AddDistributionPlatformForm, AddPost, RemoveTheThing, AddToM2MPlatformGame, \
    AddToM2MDistribPlatformGame, EditTheGame, SearchForm

app = Flask(__name__)
conn = db.connect_to_database()
cursor = conn.cursor(MySQLdb.cursors.DictCursor)

app.config['SECRET_KEY'] = 'oTv!5ox8LB#A&@cBHpa@onsKU'

lorem_ipsum = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi vulputate diam at nisl fringilla sodales. Mauris cursus porta porttitor. In pellentesque sapien lacus, quis feugiat turpis blandit et. Aenean porta ornare lorem at pellentesque. Vestibulum viverra rhoncus massa et pharetra. Sed ornare tristique volutpat. Aliquam tortor erat, feugiat nec aliquet non, hendrerit ut felis. Nunc viverra pellentesque nibh, at tincidunt nisl tincidunt id. Nunc congue sit amet odio id efficitur. Sed dictum orci ut felis facilisis suscipit. Fusce a lectus odio. Quisque nisl sem, tristique id turpis at, varius porttitor libero. Donec varius vitae leo quis maximus. Mauris fermentum ante sapien, id laoreet dolor ultrices in. Ut ac scelerisque leo, sit amet tristique sem. Nunc gravida sit amet enim vitae tristique. Donec imperdiet nunc non pellentesque mattis. Integer accumsan mi vel leo congue tincidunt. Maecenas posuere, lorem id vulputate viverra, turpis ex dictum massa, non imperdiet neque augue id leo. Cras vehicula dapibus lacinia. Phasellus vestibulum diam velit, id aliquam nisl venenatis sed. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Vivamus vitae magna magna. Morbi at gravida lacus. Proin vel lacinia justo, vitae malesuada justo. Cras quis tortor a augue sollicitudin finibus sed et sem. Nunc lorem lacus, rutrum ac dui eu, viverra maximus sem. Nunc purus metus, viverra et diam ac, efficitur pellentesque sem. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent in est dolor.'

excel_to_dictionary = XlToDict()

gameCreator = excel_to_dictionary.convert_sheet_to_dict(
    file_path="website_sheets/gameCreator.xls",
    sheet="Sheet1")

distributionPlatform = excel_to_dictionary.convert_sheet_to_dict(
    file_path="website_sheets/distribution_platform.xls", sheet="Sheet1")

platform_combo_FK_zz = excel_to_dictionary.convert_sheet_to_dict(
    file_path="website_sheets/platform_combo_FK_zz.xls", sheet="Sheet1")

platform_FK_zz = excel_to_dictionary.convert_sheet_to_dict(
    file_path="website_sheets/platform_FK_zz.xls", sheet="Sheet1")

distribution_plat_FK_zz = excel_to_dictionary.convert_sheet_to_dict(
    file_path="website_sheets/distribution_plat_FK_zz.xls", sheet="Sheet1")

posts = [
    {
        'author': 'Admin',
        'title': 'Welcome to The Backlog! Links to all pages are in the nav bar above or on the sidebar.',
        'content': 'The Backlog is a podcast is done by the Friedrich brothers covering a wide variety of games, and The Backlog website is going to cover the ever-growing list of games that the Friedrich brothers have previously talked about in the podcast and games that they plan on covering but have not yet talked about in depth.  The database supporting this website is going to contain that list. In other words, the database will contain games that the Backlog Podcast has talked about or thinks that it may have plans on covering in a future episode. With over 1,000 games released commercially every year, and more games on PC and Xbox coming out on GamePass, there’s a need for a database that records the details for each game.',
        'date_posted': 'January 30, 2021',
        'image': 'static/chars.png'
    },
    {
        'author': 'Andy',
        'title': 'Planned Episode on Fortnite',
        'content': lorem_ipsum,
        'date_posted': 'August 27, 2018',
        'image': 'static/vlad-gorshkov-G1jbCAqp5sk-unsplash.jpg'
    },
    {
        'author': 'Andy',
        'title': 'Planned Episode on Mario Kart 8',
        'content': lorem_ipsum,
        'date_posted': 'August 28, 2018',
        'image': 'static/ravi-palwe-CHAqx7kpnLQ-unsplash.jpg'
    }
]


@app.route("/index", methods=['POST', 'GET'])
@app.route("/index.html", methods=['POST', 'GET'])
def index():
    return render_template('index.html')


@app.route("/", methods=['POST', 'GET'])
@app.route("/home", methods=['POST', 'GET'])
def home():
    return render_template('home.html', posts=posts)


@app.route("/search", methods=['POST', 'GET'])
def search():
    query = "SELECT nameGame FROM game"
    cursor.execute(query)
    game = cursor.fetchall()

    query = "SELECT nameGenre FROM gameGenre"
    cursor.execute(query)
    gameGenre = cursor.fetchall()

    query = "SELECT nameCreator FROM gameCreator"
    cursor.execute(query)
    gameCreator = cursor.fetchall()

    query = "SELECT namePlatform FROM platform"
    cursor.execute(query)
    platform = cursor.fetchall()

    query = "SELECT nameDistrib FROM distributionPlatform"
    cursor.execute(query)
    distributionPlatform = cursor.fetchall()

    query = "SELECT title FROM podcastEpisode"
    cursor.execute(query)
    podcastEpisode = cursor.fetchall()

    return render_template('search.html', game=game, gameGenre=gameGenre,
                           gameCreator=gameCreator,
                           platform=platform,
                           distributionPlatform=distributionPlatform,
                           podcastEpisode=podcastEpisode)


@app.route("/addpost", methods=['POST', 'GET'])
def addHomePost():
    form = AddPost()
    return render_template('add_post.html', title='Add a Post', form=form)


@app.route("/games", methods=['POST', 'GET'])
def games():
    results = {}
    game = {}
    form = SearchForm()
    results.clear()
    if form.is_submitted():
        game.clear()  # ensure game is empty so results is rendered
        search_str = [form.search.data]  # gets user's search input
        query = "SELECT * FROM game WHERE nameGame = %s"
        cursor.execute(query, search_str)  # queries DB
        results = cursor.fetchall()  # assigns results of query
        return render_template('games.html', results=results, form=form)
    else:
        query = "SELECT * FROM game"
        cursor.execute(query)
        game = cursor.fetchall()
        return render_template('games.html', game=game, form=form)


@app.route("/addgame", methods=['POST', 'GET'])
def addGame():
    form = AddGameForm()
    if form.is_submitted():
        # TODO: FIX THIS INSERT STATEMENT
        insert = "INSERT INTO game(nameGame, releaseDate, cost, podcastEpisode, gameGenre, gameCreator)VALUES(%s, %s, %s, %s, %s, %s)"
        name = form.nameGame.data
        date = form.releaseDate.data
        cost = form.cost.data
        genre = form.gameGenre.data
        creator = form.gameCreator.data
        if form.podcastEpisode.data == '':
            episode = form.podcastEpisode.data
        insert_list = [name, date, cost, genre, creator, episode]
        cursor.execute(insert, insert_list)
        flash(f'{form.nameGame.data} added to the database!', 'success')
        return redirect(url_for('home'))
    else:
        return render_template('add_game.html', title='Add a Game', form=form)


@app.route("/gamegenres", methods=['POST', 'GET'])
def gameGenres():
    results = {}
    gameGenre = {}
    form = SearchForm()
    results.clear()
    if form.is_submitted():
        gameGenre.clear()
        search_str = [form.search.data]  # gets user's search input
        print(search_str)
        query = "SELECT * FROM gameGenre WHERE nameGenre = %s"
        cursor.execute(query, search_str)  # queries DB
        results = cursor.fetchall()  # assigns results of query
        return render_template('gameGenres.html', results=results, form=form)
    else:
        query = "SELECT * FROM gameGenre"
        cursor.execute(query)
        gameGenre = cursor.fetchall()
        return render_template('gameGenres.html', gameGenre=gameGenre,
                               form=form)


@app.route("/addgenre", methods=['POST', 'GET'])
def addGenre():
    form = AddGenreForm()
    if form.is_submitted():
        name_of_genre = form.nameGenre.data
        insert_statement = "INSERT INTO gameGenre(nameGenre) VALUE (%s)"  # TODO: FIX - NOT INSERTING
        insert_list = [name_of_genre]
        cursor.execute(insert_statement, insert_list)
        flash(f'{form.nameGenre.data} genre added to the database!', 'success')
        return redirect(url_for('home'))
    else:
        return render_template('add_genre.html', title='Add a Genre',
                               form=form)


@app.route("/podcastepisodes", methods=['POST', 'GET'])
def podcastEpisodes():
    podcastEpisode = {}
    results = {}
    form = SearchForm()
    results.clear()
    if form.is_submitted():
        podcastEpisode.clear()
        search_str = [form.search.data]  # gets user's search input
        query = 'SELECT * FROM podcastEpisode WHERE title = "%s"'  # TODO - NOT RETURNING ANYTHING
        cursor.execute(query, search_str)  # queries DB
        podcastEpisode = cursor.fetchall()  # assigns results of query
        return render_template('podcastEpisode.html',
                               podcastEpisode=podcastEpisode, form=form)
    else:
        query = "SELECT * FROM podcastEpisode"
        cursor.execute(query)
        podcastEpisode = cursor.fetchall()
        return render_template('podcastEpisode.html',
                               podcastEpisode=podcastEpisode, form=form)


@app.route("/addepisode", methods=['POST', 'GET'])
def addEpisode():
    form = AddEpisodeForm()
    if form.is_submitted():
        ep_title = form.title.data
        ep_date = form.episodeDate.data
        # TODO: FIX - NOT INSERTING
        insert_statement = 'INSERT INTO podcastEpisode(title, episodeDate) VALUES (%s, %s)'
        insert_list = [ep_title, ep_date]
        cursor.execute(insert_statement, insert_list)
        flash(f'{ep_title} episode added to the database!', 'success')
        return redirect(url_for('home'))
    else:
        return render_template('add_episode.html', title='Add an Episode',
                               form=form)


@app.route("/distributionplatforms", methods=['POST', 'GET'])
def distributionPlatforms():
    distributionPlatform = {}
    form = SearchForm()
    if form.is_submitted():
        distributionPlatform.clear()
        search_str = [form.search.data]  # gets user's search input
        query = "SELECT * FROM distributionPlatform WHERE nameDistrib = %s"
        cursor.execute(query, search_str)  # queries DB
        distributionPlatform = cursor.fetchall()  # assigns results of query
        return render_template('distributionPlatform.html',
                               distributionPlatform=distributionPlatform,
                               form=form)
    else:
        query = "SELECT * FROM distributionPlatform"
        cursor.execute(query)
        distributionPlatform = cursor.fetchall()
        return render_template('distributionPlatform.html',
                               distributionPlatform=distributionPlatform,
                               form=form)


@app.route("/adddistribplat", methods=['POST', 'GET'])
def addDistributionPlatform():
    form = AddDistributionPlatformForm()
    if form.is_submitted():
        name = form.nameDistrib.data
        rel = form.platformRel.data
        # TODO: FIX - NOT INSERTING
        insert_statement = 'INSERT INTO distributionPlatform(nameDistrib, platformRel) VALUES (%s, %s)'
        insert_list = [name, rel]
        cursor.execute(insert_statement, insert_list)
        flash(f'{name} distribution platform added to the database!',
              'success')
        return redirect(url_for('home'))
    else:
        return render_template('add_distrib_plat.html', title='Add an Episode',
                               form=form)


@app.route("/platforms", methods=['POST', 'GET'])
def platforms():
    platform = {}
    form = SearchForm()
    if form.is_submitted():
        platform.clear()
        search_str = [form.search.data]  # gets user's search input
        query = "SELECT * FROM platform WHERE namePlatform = %s"
        cursor.execute(query, search_str)  # queries DB
        platform = cursor.fetchall()  # assigns results of query
        return render_template('platforms.html', platform=platform, form=form)
    else:
        query = "SELECT * FROM platform"
        cursor.execute(query)
        platform = cursor.fetchall()
        return render_template('platforms.html', platform=platform, form=form)

    return render_template('platforms.html', platform=platform)


@app.route("/addplatform", methods=['POST', 'GET'])
def addPlatforms():
    form = AddPlatformForm()
    if form.is_submitted():
        name = form.namePlatform.data
        online = form.playedOnline.data
        many_plat = form.multiPlat.data
        # TODO: FIX - NOT INSERTING
        insert_statement = 'INSERT INTO platform(namePlatform, playedOnline, multiPlat) VALUES (%s, %s, %s)'
        insert_list = [name, online, many_plat]
        cursor.execute(insert_statement, insert_list)
        flash(f'{name} platform added to the database!', 'success')
        return redirect(url_for('home'))
    else:
        return render_template('add_platform.html', title='Add a Platform',
                               form=form)


@app.route("/gamecreators", methods=['POST', 'GET'])
def gameCreators():
    gameCreator = {}
    form = SearchForm()
    if form.is_submitted():
        gameCreator.clear()
        search_str = [form.search.data]  # gets user's search input
        query = "SELECT * FROM gameCreator WHERE nameCreator = %s"
        cursor.execute(query, search_str)  # queries DB
        gameCreator = cursor.fetchall()  # assigns results of query
        return render_template('gameCreators.html', gameCreator=gameCreator,
                               form=form)
    else:
        query = "SELECT * FROM gameCreator"
        cursor.execute(query)
        gameCreator = cursor.fetchall()
        return render_template('gameCreators.html', gameCreator=gameCreator,
                               form=form)


@app.route("/addcreator", methods=['POST', 'GET'])
def addCreator():
    form = AddCreatorForm()
    if form.is_submitted():
        name = form.nameCreator.data
        # TODO: FIX - NOT INSERTING
        insert_statement = 'INSERT INTO gameCreator(nameCreator) VALUES (%s)'
        insert_list = [name]
        cursor.execute(insert_statement, insert_list)
        flash(f'{name} creator added to the database!', 'success')
        return redirect(url_for('home'))
    else:
        return render_template('add_creator.html', title='Add a Creator',
                               form=form)


@app.route("/gamesandplatforms", methods=['POST', 'GET'])
def m2m_GameAndPlatform():
    return render_template('PlatformFKzz.html', platform_FK_zz=platform_FK_zz)


@app.route("/gamesanddistributionplatforms", methods=['POST', 'GET'])
def m2m_GameAndDistribPlatform():
    return render_template('DistributionPlatFKzz.html',
                           distribution_plat_FK_zz=distribution_plat_FK_zz)


@app.route("/addm2mgameandplatform", methods=['POST', 'GET'])
def add_m2m_GameAndPlatform():
    form = AddToM2MPlatformGame()
    return render_template('add_gameandplatform.html', title='Add a Combo',
                           form=form)


@app.route("/addm2mgameanddistribplatform", methods=['POST', 'GET'])
def add_m2m_GameAndDistribPlatform():
    form = AddToM2MDistribPlatformGame()
    return render_template('add_gameanddistribplatform.html',
                           title='Add a Combo', form=form)


@app.route("/remove", methods=['POST', 'GET'])
def remove():
    form = RemoveTheThing()
    return render_template('remove.html', title='Remove', form=form)


@app.route("/editgame", methods=['POST', 'GET'])
def editgame():
    form = EditTheGame()
    return render_template('editgame.html', title='Edit', form=form)


if __name__ == '__main__':
    app.run(debug=True)
