from flask import Flask, render_template, flash, redirect, url_for
import Database.db_connector as db
import pymysql.cursors
import time
# from xl2dict import XlToDict  # https://pypi.org/project/xl2dict/
from forms import AddGameForm, AddGenreForm, AddCreatorForm, AddPlatformForm, \
    AddEpisodeForm, AddToM2MPlatformGame, \
    EditTheGame, SearchForm, RemoveGame, RemoveGenre, RemoveCreator, \
    RemovePlatform, RemoveEpisode, RemoveGameAndPlatform, SearchPageForm

# Connect to the database
app = Flask(__name__)

app.config['SECRET_KEY'] = 'oTv!5ox8LB#A&@cBHpa@onsKU'

lorem_ipsum = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi vulputate diam at nisl fringilla sodales. Mauris cursus porta porttitor. In pellentesque sapien lacus, quis feugiat turpis blandit et. Aenean porta ornare lorem at pellentesque. Vestibulum viverra rhoncus massa et pharetra. Sed ornare tristique volutpat. Aliquam tortor erat, feugiat nec aliquet non, hendrerit ut felis. Nunc viverra pellentesque nibh, at tincidunt nisl tincidunt id. Nunc congue sit amet odio id efficitur. Sed dictum orci ut felis facilisis suscipit. Fusce a lectus odio. Quisque nisl sem, tristique id turpis at, varius porttitor libero. Donec varius vitae leo quis maximus. Mauris fermentum ante sapien, id laoreet dolor ultrices in. Ut ac scelerisque leo, sit amet tristique sem. Nunc gravida sit amet enim vitae tristique. Donec imperdiet nunc non pellentesque mattis. Integer accumsan mi vel leo congue tincidunt. Maecenas posuere, lorem id vulputate viverra, turpis ex dictum massa, non imperdiet neque augue id leo. Cras vehicula dapibus lacinia. Phasellus vestibulum diam velit, id aliquam nisl venenatis sed. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Vivamus vitae magna magna. Morbi at gravida lacus. Proin vel lacinia justo, vitae malesuada justo. Cras quis tortor a augue sollicitudin finibus sed et sem. Nunc lorem lacus, rutrum ac dui eu, viverra maximus sem. Nunc purus metus, viverra et diam ac, efficitur pellentesque sem. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent in est dolor.'

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
    """This provides the index page route."""
    return render_template('index.html')


@app.route("/", methods=['POST', 'GET'])
@app.route("/home", methods=['POST', 'GET'])
def home():
    """This provides the home page route."""
    return render_template('home.html', posts=posts)


@app.route("/search", methods=['POST', 'GET'])
def search():
    """This provides the search page route."""
    # connect to DB
    conn = db.connect_to_database()
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    # populate forms
    form = SearchPageForm()
    # game names -------
    query = "SELECT nameGame FROM game"
    cursor.execute(query)
    games_list_unsorted = [item['nameGame'] for item in cursor.fetchall()]
    games_list = ['NULL']
    for item in games_list_unsorted:
        games_list.append(item)
    form.name.choices = games_list
    # game genres ------
    query = "SELECT nameGenre FROM gameGenre"
    cursor.execute(query)
    genre_list = ['NULL']
    second_list = [item['nameGenre'] for item in cursor.fetchall()]
    # order elements and remove duplicates
    second_list = list(set(second_list))
    for item in second_list:
        genre_list.append(item)
    form.genre.choices = genre_list
    # creators --------
    query = "SELECT nameCreator FROM gameCreator"
    cursor.execute(query)
    creator_list = ['NULL']
    tmp = [item['nameCreator'] for item in cursor.fetchall()]
    tmp = list(set(tmp))
    for item in tmp:
        creator_list.append(item)
    form.creator.choices = creator_list
    # episodes --------
    query = "SELECT title FROM podcastEpisode"
    cursor.execute(query)
    ep_list = ['NULL']
    tmp = [item['title'] for item in cursor.fetchall()]
    tmp = list(set(tmp))
    for item in tmp:
        ep_list.append(item)
    form.episode.choices = ep_list
    # dates -------------
    query = "SELECT releaseDate FROM game"
    cursor.execute(query)
    date_list = ['NULL']
    tmp = [item['releaseDate'] for item in cursor.fetchall()]
    tmp = list(set(tmp))
    for item in tmp:
        date_list.append(item)
    form.date.choices = date_list
    # costs ------------
    query = "SELECT cost FROM game"
    cursor.execute(query)
    cost_list = ['NULL']
    tmp = [item['cost'] for item in cursor.fetchall()]
    tmp = list(set(tmp))
    for item in tmp:
        cost_list.append(item)
    form.cost.choices = cost_list
    # platforms --------
    cursor.execute("SELECT namePlatform FROM platform")
    platforms = ['NULL']
    tmp = [item['namePlatform'] for item in cursor.fetchall()]
    tmp = list(set(tmp))
    for item in tmp:
        platforms.append(item)
    form.platform.choices = platforms

    counter = 0

    # Booleans used to track which dropdowns have been used.
    name_bool = False
    genre_bool = False
    ep_bool = False
    creator_bool = False
    date_bool = False
    cost_bool = False
    platform_bool = False
    bool_list = [name_bool, genre_bool, ep_bool, creator_bool, date_bool,
                 cost_bool, platform_bool]

    # Checks which dropdowns have been used.
    if form.name.data is not None and form.name.data != 'NULL':
        name_bool = True
        bool_list[0] = True
    if form.genre.data is not None and form.genre.data != 'NULL':
        genre_bool = True
        bool_list[1] = True
    if form.episode.data is not None and form.episode.data != 'NULL':
        ep_bool = True
        bool_list[2] = True
    if form.creator.data is not None and form.creator.data != 'NULL':
        creator_bool = True
        bool_list[3] = True
    if form.date.data is not None and form.date.data != 'NULL':
        date_bool = True
        bool_list[4] = True
    if form.cost.data is not None and form.cost.data != 'NULL':
        cost_bool = True
        bool_list[5] = True
    if form.platform.data is not None and form.platform.data != 'NULL':
        platform_bool = True
        bool_list[6] = True

    # If any dropdowns have been used to search, render page with results.
    if name_bool or genre_bool or ep_bool or creator_bool or date_bool or cost_bool or platform_bool:
        counter = 0
        render = []
        query_prefix = "SELECT * FROM game WHERE "
        search = []

        # counts how many dropdowns have been used.
        for b in bool_list:
            if b == True:
                counter += 1

        # Build SQL query based on one dropdown used.
        if counter == 1:
            if name_bool:
                search.append(form.name.data)
                query = "SELECT * FROM game WHERE nameGame = %s"
                cursor.execute(query, search)
                render = cursor.fetchall()
            if genre_bool:
                # 1 Get nameGenre
                genre_name = form.genre.data
                # 2 Get idGenre
                alt_query = "SELECT nameGenre FROM gameGenre"
                cursor.execute(alt_query)
                names = [item['nameGenre'] for item in cursor.fetchall()]
                alt_query = "SELECT idGenre FROM gameGenre"
                cursor.execute(alt_query)
                ids = [item['idGenre'] for item in cursor.fetchall()]
                index = -1
                for name in names:
                    index += 1
                    if genre_name == name:
                        break
                idx_count = -1
                if index != -1:
                    for id in ids:
                        idx_count += 1
                        if idx_count == index:
                            search.append(str(id))
                query = "SELECT * FROM game WHERE gameGenre = %s"
                cursor.execute(query, search)
                render = cursor.fetchall()
            if ep_bool:
                # 1 - Get the name from dropdown
                tmp = form.episode.data
                query = ''
                if tmp == 'None':
                    query = "SELECT * FROM game WHERE podcastEpisode IS NULL"
                    cursor.execute(query)
                    render = cursor.fetchall()
                else:
                    # 2 - Get corresponding ID
                    ep_query = "SELECT title FROM podcastEpisode"
                    cursor.execute(ep_query)
                    ep_titles = [item['title'] for item in cursor.fetchall()]
                    ep_query = "SELECT episodeNumber FROM podcastEpisode"
                    cursor.execute(ep_query)
                    ep_ids = [item['episodeNumber'] for item in
                              cursor.fetchall()]
                    idx = -1
                    for title in ep_titles:
                        idx += 1
                        if title == tmp:
                            break
                    idx_2 = -1
                    for id in ep_ids:
                        idx_2 += 1
                        if idx_2 == idx:
                            tmp = id
                    # 3 - Execute DB search from ID
                    search.append(tmp)
                    query = "SELECT * FROM game WHERE podcastEpisode = %s"
                    cursor.execute(query, search)
                    render = cursor.fetchall()
            if creator_bool:
                # 1 - Get the name from dropdown
                creator_name = form.creator.data
                # 2 - Get corresponding ID
                creator_query = "SELECT nameCreator FROM gameCreator"
                cursor.execute(creator_query)
                creator_names = [item['nameCreator'] for item in
                                 cursor.fetchall()]
                creator_query = "SELECT idCreator FROM gameCreator"
                cursor.execute(creator_query)
                creator_ids = [item['idCreator'] for item in cursor.fetchall()]
                index = -1
                for c_name in creator_names:
                    index += 1
                    if c_name == creator_name:
                        break
                idx_2 = -1
                search_ID = ''
                for c_id in creator_ids:
                    idx_2 += 1
                    if idx_2 == index:
                        search_ID = c_id
                search.append(search_ID)
                # 3 - Execute DB search from ID
                query = "SELECT * FROM game WHERE gameCreator = %s"
                cursor.execute(query, search)
                render = cursor.fetchall()
            if date_bool:
                search.append(form.date.data)
                query = "SELECT * FROM game WHERE releaseDate = %s"
                cursor.execute(query, search)
                render = cursor.fetchall()
            if cost_bool:
                search.append(form.cost.data)
                query = "SELECT * FROM game WHERE cost = %s"
                cursor.execute(query, search)
                render = cursor.fetchall()
            if platform_bool:
                # 1 Get the ID matching the name
                p_name = form.platform.data
                print(f"{p_name}")
                cursor.execute("SELECT namePlatform FROM platform")
                tmp = [item['namePlatform'] for item in cursor.fetchall()]
                counter = -1
                for item in tmp:
                    counter += 1
                    if item == p_name:
                        break

                cursor.execute("SELECT idPlatform FROM platform")
                tmp2 = [item['idPlatform'] for item in cursor.fetchall()]
                id = ''
                counter2 = -1
                for item in tmp2:
                    counter2 += 1
                    if counter2 == counter:
                        id = item

                print(f"{id}")
                # 2 get the game name from platformFKzz with the ID
                cursor.execute("SELECT idPlatform FROM platformFKzz")
                tmp3 = [item['idPlatform'] for item in cursor.fetchall()]
                counter3 = -1
                for item in tmp3:
                    counter3 += 1
                    if item == id:
                        break

                cursor.execute("SELECT nameGame FROM platformFKzz")
                tmp4 = [item['nameGame'] for item in cursor.fetchall()]
                counter4 = -1
                game_name = ''
                for item in tmp4:
                    counter4 += 1
                    if counter4 == counter3:
                        game_name = item
                        break

                print(f"{game_name}")
                # 3 get the game data from game with the name of game
                game_search = "SELECT * FROM game WHERE nameGame = %s"
                game_search_list = [game_name]
                cursor.execute(game_search, game_search_list)
                render = cursor.fetchall()

        # Build SQL query for more than one dropdown.
        if counter > 1:
            if name_bool:
                search.append(form.name.data)
                query_prefix += "nameGame = %s AND "
            if genre_bool:
                # 1 Get nameGenre
                genre_name = form.genre.data
                # 2 Get idGenre
                alt_query = "SELECT nameGenre FROM gameGenre"
                cursor.execute(alt_query)
                names = [item['nameGenre'] for item in cursor.fetchall()]
                alt_query = "SELECT idGenre FROM gameGenre"
                cursor.execute(alt_query)
                ids = [item['idGenre'] for item in cursor.fetchall()]
                index = -1
                for name in names:
                    index += 1
                    if genre_name == name:
                        break
                idx_count = -1
                if index != -1:
                    for id in ids:
                        idx_count += 1
                        if idx_count == index:
                            search.append(str(id))
                query_prefix += "gameGenre = %s AND "
            if ep_bool:
                tmp = form.episode.data
                if tmp == 'None':
                    query_prefix += "podcastEpisode IS NULL AND "
                else:
                    # 2 - Get corresponding ID
                    ep_query = "SELECT title FROM podcastEpisode"
                    cursor.execute(ep_query)
                    ep_titles = [item['title'] for item in cursor.fetchall()]
                    ep_query = "SELECT episodeNumber FROM podcastEpisode"
                    cursor.execute(ep_query)
                    ep_ids = [item['episodeNumber'] for item in
                              cursor.fetchall()]
                    idx = -1
                    for title in ep_titles:
                        idx += 1
                        if title == tmp:
                            break
                    idx_2 = -1
                    for id in ep_ids:
                        idx_2 += 1
                        if idx_2 == idx:
                            tmp = id
                    # 3 - Execute DB search from ID
                    search.append(tmp)
                    query_prefix += "podcastEpisode = %s AND "
            if creator_bool:
                # 1 - Get the name from dropdown
                creator_name = form.creator.data
                # 2 - Get corresponding ID
                creator_query = "SELECT nameCreator FROM gameCreator"
                cursor.execute(creator_query)
                creator_names = [item['nameCreator'] for item in
                                 cursor.fetchall()]
                creator_query = "SELECT idCreator FROM gameCreator"
                cursor.execute(creator_query)
                creator_ids = [item['idCreator'] for item in cursor.fetchall()]
                index = -1
                for c_name in creator_names:
                    index += 1
                    if c_name == creator_name:
                        break
                idx_2 = -1
                search_ID = ''
                for c_id in creator_ids:
                    idx_2 += 1
                    if idx_2 == index:
                        search_ID = c_id
                search.append(search_ID)
                query_prefix += "gameCreator = %s AND "
            if date_bool:
                search.append(form.date.data)
                query_prefix += "releaseDate = %s AND "
            if cost_bool:
                search.append(form.cost.data)
                query_prefix += "cost = %s AND "
            if platform_bool:
                # 1 Get the ID matching the name
                p_name = form.platform.data
                print(f"{p_name}")
                cursor.execute("SELECT namePlatform FROM platform")
                tmp = [item['namePlatform'] for item in cursor.fetchall()]
                counter = -1
                for item in tmp:
                    counter += 1
                    if item == p_name:
                        break
                cursor.execute("SELECT idPlatform FROM platform")
                tmp2 = [item['idPlatform'] for item in cursor.fetchall()]
                id = ''
                counter2 = -1
                for item in tmp2:
                    counter2 += 1
                    if counter2 == counter:
                        id = item
                print(f"{id}")
                # 2 get the game name from platformFKzz with the ID
                cursor.execute("SELECT idPlatform FROM platformFKzz")
                tmp3 = [item['idPlatform'] for item in cursor.fetchall()]
                counter3 = -1
                for item in tmp3:
                    counter3 += 1
                    if item == id:
                        break
                cursor.execute("SELECT nameGame FROM platformFKzz")
                tmp4 = [item['nameGame'] for item in cursor.fetchall()]
                counter4 = -1
                game_name = ''
                for item in tmp4:
                    counter4 += 1
                    if counter4 == counter3:
                        game_name = item
                        break
                if not name_bool:
                    search.append(game_name)
                    query_prefix += "nameGame = %s AND "

            # builds the SQL query and executes it
            query_length = len(query_prefix)
            query = query_prefix[:query_length - 5]  # Remove trailing ' AND '
            cursor.execute(query, search)
            render = cursor.fetchall()

        # if we have results from SQL query, render them.
        if len(render) > 0:
            # reset booleans
            for b in bool_list:
                b = False
            return render_template('search.html', form=form, render=render)
        # otherwise, redirect to homepage with notification of no results.
        else:
            # reset booleans
            for b in bool_list:
                b = False
            flash(f'No search results found!', 'success')
            return redirect(url_for('home'))
    else:
        return render_template('search.html', form=form)


@app.route("/games", methods=['POST', 'GET'])
def games():
    """This provides the games page route."""
    conn = db.connect_to_database()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    results = {}
    game = {}
    form = SearchForm()
    results.clear()
    # renders the page based on search results.
    if form.is_submitted():
        game.clear()  # ensure game is empty so results is rendered
        search_str = [form.search.data]  # gets user's search input
        query = "SELECT * FROM game WHERE nameGame = %s"
        cursor.execute(query, search_str)  # queries DB
        results = cursor.fetchall()  # assigns results of query
        return render_template('games.html', results=results, form=form)
    else:
        # renders the page before form is submitted.
        query = "SELECT * FROM game"
        cursor.execute(query)
        game = cursor.fetchall()
        return render_template('games.html', game=game, form=form)


@app.route("/addgame", methods=['POST', 'GET'])
def addGame():
    """This provides the addgame page route."""
    # connect to DB
    conn = db.connect_to_database()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    # add form and populate the dropdowns
    form = AddGameForm()
    # genre IDs ----------
    query = "SELECT idGenre FROM gameGenre"
    cursor.execute(query)
    genre_list = [item['idGenre'] for item in cursor.fetchall()]
    form.gameGenre.choices = genre_list
    # creators ----------
    query = "SELECT idCreator FROM gameCreator"
    cursor.execute(query)
    creator_list = [item['idCreator'] for item in cursor.fetchall()]
    form.gameCreator.choices = creator_list
    # podcast episodes -----------
    query = "SELECT episodeNumber FROM podcastEpisode"
    cursor.execute(query)
    episode_list = ["NULL"]
    results = cursor.fetchall()
    for item in results:
        episode_list.append(item['episodeNumber'])
    form.podcastEpisode.choices = episode_list
    # platforms -------------------
    query = "SELECT idPlatform FROM platform"
    cursor.execute(query)
    platform_list = [item['idPlatform'] for item in cursor.fetchall()]
    form.platformList.choices = platform_list

    # adds the new game to the game table.
    if form.is_submitted():
        # gets values from form to be used in insert statement
        name = form.nameGame.data
        date = form.releaseDate.data
        cost = form.cost.data
        genre = form.gameGenre.data
        creator = form.gameCreator.data
        episode = []
        episode = form.podcastEpisode.data
        insert = ""
        insert_list = []
        # inserts game when no podcast episode is entered.
        if episode == 'NULL':
            insert += "INSERT INTO game(nameGame, releaseDate, cost, gameGenre, gameCreator)VALUES(%s, %s, %s, %s, %s)"
            insert_list = [name, date, cost, genre, creator]
            cursor.execute(insert, insert_list)
            conn.commit()
        else:
            # inserts game when a podcast episode is entered.
            insert += "INSERT INTO game(nameGame, releaseDate, cost, gameGenre, gameCreator, podcastEpisode)VALUES(%s, %s, %s, %s, %s, %s)"
            insert_list = [name, date, cost, genre, creator, episode]
            cursor.execute(insert, insert_list)
            conn.commit()
        # gets platform value and inserts the game/platform combo in platformFKzz
        platform = form.platformList.data
        platform_value = [platform, name]
        time.sleep(1)  # debugging
        insert = "INSERT INTO platformFKzz(idPlatform, nameGame)VALUES(%s, %s)"
        cursor.execute(insert, platform_value)
        conn.commit()
        # redirects to home with success message.
        flash(f'{form.nameGame.data} added to the database!', 'success')
        return redirect(url_for('home'))
    else:
        return render_template('add_game.html', title='Add a Game', form=form)


@app.route("/gamegenres", methods=['POST', 'GET'])
def gameGenres():
    """This provides the gameGenres page route."""
    conn = db.connect_to_database()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    results = {}
    gameGenre = {}
    form = SearchForm()
    results.clear()
    # renders the page based on search results
    if form.is_submitted():
        gameGenre.clear()
        search_str = [form.search.data]  # gets user's search input
        print(search_str)
        query = "SELECT * FROM gameGenre WHERE nameGenre = %s"
        cursor.execute(query, search_str)  # queries DB
        results = cursor.fetchall()  # assigns results of query
        return render_template('gameGenres.html', results=results, form=form)
    else:
        # renders the page before form is submitted.
        query = "SELECT * FROM gameGenre"
        cursor.execute(query)
        gameGenre = cursor.fetchall()
        return render_template('gameGenres.html', gameGenre=gameGenre,
                               form=form)


@app.route("/addgenre", methods=['POST', 'GET'])
def addGenre():
    """This provides the addGenre page route."""
    conn = db.connect_to_database()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    form = AddGenreForm()
    # adds the new genre to the genre table
    if form.is_submitted():
        name_of_genre = form.nameGenre.data
        insert_statement = "INSERT INTO gameGenre(nameGenre) VALUE (%s)"
        insert_list = [name_of_genre]
        cursor.execute(insert_statement, insert_list)
        conn.commit()
        flash(f'{form.nameGenre.data} genre added to the database!', 'success')
        return redirect(url_for('home'))
    else:
        # renders the page before form is submitted.
        return render_template('add_genre.html', title='Add a Genre',
                               form=form)


@app.route("/podcastepisodes", methods=['POST', 'GET'])
def podcastEpisodes():
    """This provides the pordcastEpisodes page route."""
    conn = db.connect_to_database()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    podcastEpisode = {}
    results = {}
    form = SearchForm()
    results.clear()
    # renders the page based on search results.
    if form.is_submitted():
        podcastEpisode.clear()
        search_str = [form.search.data]  # gets user's search input
        query = 'SELECT * FROM podcastEpisode WHERE title = "%s"'
        cursor.execute(query, search_str)  # queries DB
        podcastEpisode = cursor.fetchall()  # assigns results of query
        return render_template('podcastEpisode.html',
                               podcastEpisode=podcastEpisode, form=form)
    else:
        # renders the page before form is submitted.
        query = "SELECT * FROM podcastEpisode"
        cursor.execute(query)
        podcastEpisode = cursor.fetchall()
        return render_template('podcastEpisode.html',
                               podcastEpisode=podcastEpisode, form=form)


@app.route("/addepisode", methods=['POST', 'GET'])
def addEpisode():
    """This provides the addEpisode page route."""
    conn = db.connect_to_database()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    form = AddEpisodeForm()
    # adds the episode to the table that was entered into the form
    if form.is_submitted():
        ep_title = form.title.data
        ep_date = form.episodeDate.data
        insert_statement = 'INSERT INTO podcastEpisode(title, episodeDate) VALUES (%s, %s)'
        insert_list = [ep_title, ep_date]
        cursor.execute(insert_statement, insert_list)
        conn.commit()
        flash(f'{ep_title} episode added to the database!', 'success')
        return redirect(url_for('home'))
    else:
        # renders the page before form is submitted.
        return render_template('add_episode.html', title='Add an Episode',
                               form=form)


@app.route("/platforms", methods=['POST', 'GET'])
def platforms():
    """This provides the platforms page route."""
    conn = db.connect_to_database()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    platform = {}
    form = SearchForm()
    # renders the page based on search results if search form is used.
    if form.is_submitted():
        platform.clear()
        search_str = [form.search.data]  # gets user's search input
        query = "SELECT * FROM platform WHERE namePlatform = %s"
        cursor.execute(query, search_str)  # queries DB
        platform = cursor.fetchall()  # assigns results of query
        return render_template('platforms.html', platform=platform, form=form)
    else:
        # renders the page before form submission.
        query = "SELECT * FROM platform"
        cursor.execute(query)
        platform = cursor.fetchall()
        return render_template('platforms.html', platform=platform, form=form)

    return render_template('platforms.html', platform=platform)


@app.route("/addplatform", methods=['POST', 'GET'])
def addPlatforms():
    """This provides the addPlatforms page route."""
    conn = db.connect_to_database()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    form = AddPlatformForm()
    # adds platform to platform table if form is submitted.
    if form.is_submitted():
        # gets values for the insert statement
        name = form.namePlatform.data
        online = form.playedOnline.data
        many_plat = form.multiPlat.data
        insert_statement = 'INSERT INTO platform(namePlatform, playedOnline, multiPlat) VALUES (%s, %s, %s)'
        insert_list = [name, online, many_plat]
        cursor.execute(insert_statement, insert_list)
        conn.commit()
        # redirect to home with success message
        flash(f'{name} platform added to the database!', 'success')
        return redirect(url_for('home'))
    else:
        # renders page before form submission.
        return render_template('add_platform.html', title='Add a Platform',
                               form=form)


@app.route("/gamecreators", methods=['POST', 'GET'])
def gameCreators():
    """This provides the gameCreators page route."""
    conn = db.connect_to_database()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    gameCreator = {}
    form = SearchForm()
    # renders page based on search results if search form is submitted.
    if form.is_submitted():
        gameCreator.clear()
        search_str = [form.search.data]  # gets user's search input
        query = "SELECT * FROM gameCreator WHERE nameCreator = %s"
        cursor.execute(query, search_str)  # queries DB
        gameCreator = cursor.fetchall()  # assigns results of query
        return render_template('gameCreators.html', gameCreator=gameCreator,
                               form=form)
    else:
        # renders page before form submission.
        query = "SELECT * FROM gameCreator"
        cursor.execute(query)
        gameCreator = cursor.fetchall()
        return render_template('gameCreators.html', gameCreator=gameCreator,
                               form=form)


@app.route("/addcreator", methods=['POST', 'GET'])
def addCreator():
    """This provides the addCreator page route."""
    conn = db.connect_to_database()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    form = AddCreatorForm()
    # adds the creator to the gameCreator table if form is submitted.
    if form.is_submitted():
        name = form.nameCreator.data
        insert_statement = 'INSERT INTO gameCreator(nameCreator) VALUES (%s)'
        insert_list = [name]
        cursor.execute(insert_statement, insert_list)
        conn.commit()
        flash(f'{name} creator added to the database!', 'success')
        return redirect(url_for('home'))
    else:
        # renders page before form submission.
        return render_template('add_creator.html', title='Add a Creator',
                               form=form)


@app.route("/gamesandplatforms", methods=['POST', 'GET'])
def m2m_GameAndPlatform():
    """This provides the gamesandplatforms page route."""
    conn = db.connect_to_database()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    platform_FK_zz = {}
    form = SearchForm()

    # renders page based on search results if the search form is submitted.
    if form.is_submitted():
        search_str = [form.search.data]  # gets user's search input
        query = "SELECT * FROM platformFKzz WHERE nameGame = %s"
        cursor.execute(query, search_str)  # queries DB
        platform_FK_zz = cursor.fetchall()  # assigns results of query
        return render_template('PlatformFKzz.html',
                               platform_FK_zz=platform_FK_zz, form=form)
    else:
        # renders page normally.
        query = "SELECT * FROM platformFKzz"
        cursor.execute(query)
        platform_FK_zz = cursor.fetchall()
        return render_template('PlatformFKzz.html',
                               platform_FK_zz=platform_FK_zz, form=form)


@app.route("/addm2mgameandplatform", methods=['POST', 'GET'])
def add_m2m_GameAndPlatform():
    """This provides the addm2mgameandplatform page route."""
    # Connect to DB.
    conn = db.connect_to_database()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    # Populate the form
    form = AddToM2MPlatformGame()
    # game names -------------------
    query = "SELECT nameGame FROM game"
    cursor.execute(query)
    games_list_unsorted = [item['nameGame'] for item in cursor.fetchall()]
    games_list = sorted(games_list_unsorted)
    form.nameGame.choices = games_list
    # platforms -------------------
    query = "SELECT idPlatform FROM platform"
    cursor.execute(query)
    platform_list = [item['idPlatform'] for item in cursor.fetchall()]
    form.idPlatform.choices = platform_list

    # adds the selected combination into platformFKzz
    if form.is_submitted():
        name = form.nameGame.data
        idPlat = form.idPlatform.data
        insert_statement = 'INSERT INTO platformFKzz (nameGame, idPlatform) VALUES (%s, %s)'
        insert_list = [name, idPlat]
        cursor.execute(insert_statement, insert_list)
        conn.commit()
        flash(f'{name} creator added to the database!', 'success')
        return redirect(url_for('home'))
    else:
        # renders page before submission.
        return render_template('add_gameandplatform.html',
                               title='Add a Creator',
                               form=form)


@app.route("/removegame", methods=['POST', 'GET'])
def remove_game():
    """This provides the removegame page route."""
    # Connect to DB
    conn = db.connect_to_database()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    # Populate the form and its data
    form = RemoveGame()
    # game names ------------
    query = "SELECT nameGame FROM game"
    cursor.execute(query)
    games_list_unsorted = [item['nameGame'] for item in cursor.fetchall()]
    games_list = sorted(games_list_unsorted)
    form.name.choices = games_list
    if form.is_submitted():
        remove = 'DELETE FROM game WHERE nameGame = %s'

        # gets the name of this game (selected game) and get its podcast.
        nm = [form.name.data]
        gm_q = 'SELECT podcastEpisode FROM game WHERE nameGame = %s'
        cursor.execute(gm_q, nm)
        game_ep = [item['podcastEpisode'] for item in cursor.fetchall()]

        # get games in platformFKzz and check if this game is there.
        cursor.execute('SELECT nameGame FROM platformFKzz')
        name_list = [item['nameGame'] for item in cursor.fetchall()]
        game_found = False
        for x in name_list:
            # toggle the boolean if it's there
            if x == form.name.data:
                game_found = True

        # if this game is in platformFKzz, remove it.
        if game_found:
            cursor.execute('DELETE FROM platformFKzz WHERE nameGame = %s', nm)
            conn.commit()

        print(f"PODCAST EPISODE = {game_ep}")
        # if this game has no podcast, give it one before deleting the game.
        if not game_ep[0]:
            game_name = form.name.data
            # gets a list of current episodes
            cursor.execute("SELECT episodeNumber FROM podcastEpisode")
            eps = [item['episodeNumber'] for item in cursor.fetchall()]
            name_val = [eps[0], game_name]

            # gives this game a currently existing podcast episode
            insert = 'UPDATE game SET podcastEpisode = (SELECT episodeNumber FROM podcastEpisode WHERE episodeNumber = %s) WHERE nameGame = %s'
            cursor.execute(insert, name_val)
            conn.commit()

            # now remove the game from the game table.
            cursor.execute(remove, game_name)
            conn.commit()
        else:
            # removes game from game table
            remove_list = [form.name.data]
            cursor.execute(remove, remove_list)
            conn.commit()
        # redirect to home with removal success message.
        flash(f'{form.name.data} removed from the database!', 'success')
        return redirect(url_for('home'))
    else:
        # renders the page before form submission.
        query = "SELECT * FROM game"
        cursor.execute(query)
        game = cursor.fetchall()
        return render_template('remove_game.html', title='Remove Game',
                               form=form, game=game)


@app.route("/removegenre", methods=['POST', 'GET'])
def remove_genre():
    """This provides the removegenre page route."""
    # connect to DB
    conn = db.connect_to_database()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    # populate the form data
    form = RemoveGenre()
    # genre name -------------------
    query = "SELECT nameGenre FROM gameGenre"
    cursor.execute(query)
    genre_list = [item['nameGenre'] for item in cursor.fetchall()]
    form.name.choices = genre_list
    if form.is_submitted():
        remove = 'DELETE FROM gameGenre WHERE nameGenre = %s'
        remove_list = [form.name.data]
        # removes selection from the table
        cursor.execute(remove, remove_list)
        conn.commit()
        flash(f'{form.name.data} removed from the database!', 'success')
        return redirect(url_for('home'))
    else:
        # renders the page before form submission
        query = "SELECT * FROM gameGenre"
        cursor.execute(query)
        gameGenre = cursor.fetchall()
        return render_template('remove_genre.html', title='Remove Genre',
                               form=form, gameGenre=gameGenre)


@app.route("/removecreator", methods=['POST', 'GET'])
def remove_creator():
    """This provides the removecreator page route."""
    # Connect to DB
    conn = db.connect_to_database()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    # Populate the form data
    form = RemoveCreator()
    # Creator name -----------------
    query = "SELECT nameCreator FROM gameCreator"
    cursor.execute(query)
    creator_list = [item['nameCreator'] for item in cursor.fetchall()]
    form.name.choices = creator_list

    if form.is_submitted():
        remove = 'DELETE FROM gameCreator WHERE nameCreator = %s'
        remove_list = [form.name.data]
        # removes the selection from the table
        cursor.execute(remove, remove_list)
        conn.commit()
        flash(f'{form.name.data} removed from the database!', 'success')
        return redirect(url_for('home'))
    else:
        # renders the page before form submission
        query = "SELECT * FROM gameCreator"
        cursor.execute(query)
        gameCreator = cursor.fetchall()
        return render_template('remove_creator.html', title='Remove Creator',
                               form=form, gameCreator=gameCreator)


@app.route("/removeplatform", methods=['POST', 'GET'])
def remove_platform():
    """This provides the removeplatform page route."""
    # Connect to the DB
    conn = db.connect_to_database()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    # Populate the form
    form = RemovePlatform()
    # platform name ----------------
    query = "SELECT namePlatform FROM platform"
    cursor.execute(query)
    plat_list = [item['namePlatform'] for item in cursor.fetchall()]
    form.name.choices = plat_list

    if form.is_submitted():
        remove = 'DELETE FROM platform WHERE namePlatform =  %s'
        remove_list = [form.name.data]
        # removes the selection from the table
        cursor.execute(remove, remove_list)
        conn.commit()
        flash(f'{form.name.data} removed from the database!', 'success')
        return redirect(url_for('home'))
    else:
        # renders the page before form submission
        query = "SELECT * FROM platform"
        cursor.execute(query)
        platform = cursor.fetchall()
        return render_template('remove_platform.html', title='Remove Platform',
                               form=form, platform=platform)


@app.route("/removeepisode", methods=['POST', 'GET'])
def remove_episode():
    """This provides the remove_episode page route."""
    # Connect to the DB
    conn = db.connect_to_database()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    # Populate the form
    form = RemoveEpisode()
    # Episode names -----------
    query = "SELECT title FROM podcastEpisode"
    cursor.execute(query)
    ep_list = [item['title'] for item in cursor.fetchall()]
    form.name.choices = ep_list

    if form.is_submitted():
        # Removes selection from the table.
        remove = 'DELETE FROM podcastEpisode WHERE title = %s'
        remove_list = [form.name.data]
        cursor.execute(remove, remove_list)
        conn.commit()
        flash(f'{form.name.data} removed from the database!', 'success')
        return redirect(url_for('home'))
    else:
        # renders page before form is submitted
        query = "SELECT * FROM podcastEpisode"
        cursor.execute(query)
        podcastEpisode = cursor.fetchall()
        return render_template('remove_episode.html', title='Remove Episode',
                               form=form, podcastEpisode=podcastEpisode)


@app.route("/removem2mgameandplatform", methods=['POST', 'GET'])
def remove_m2m_GameAndPlatform():
    """This provides the removem2mgameandplatform page route."""
    # Connect to DB
    conn = db.connect_to_database()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    # Populate the form data
    form = RemoveGameAndPlatform()
    query = "SELECT nameGame FROM platformFKzz"
    cursor.execute(query)
    nm_list = [item['nameGame'] for item in cursor.fetchall()]
    form.name.choices = nm_list

    # if the form has been submitted, delete the selection from table.
    if form.is_submitted():
        remove = 'DELETE FROM platformFKzz WHERE nameGame = %s'
        remove_list = [form.name.data]
        cursor.execute(remove, remove_list)
        conn.commit()
        # redirect to home with success message
        flash(f'{form.name.data} removed from the database!', 'success')
        return redirect(url_for('home'))
    else:
        # renders page before form is submitted
        query = "SELECT * FROM platformFKzz"
        cursor.execute(query)
        post = cursor.fetchall()
        return render_template('remove_gameandplatform.html',
                               title='Remove a Combo',
                               form=form, post=post)


@app.route("/editgame", methods=['POST', 'GET'])
def editgame():
    """This provides the editgame page route."""
    # connect to DB
    conn = db.connect_to_database()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    # populate the form and form data
    form = EditTheGame()
    # original game names ------------------
    query = "SELECT nameGame FROM game"
    cursor.execute(query)
    games_list_unsorted = [item['nameGame'] for item in cursor.fetchall()]
    games_list = sorted(games_list_unsorted)
    form.originalName.choices = games_list
    # game genre ---------------------------
    query = "SELECT idGenre FROM gameGenre"
    cursor.execute(query)
    genre_list = [item['idGenre'] for item in cursor.fetchall()]
    form.gameGenre.choices = genre_list
    # game creator --------------------------
    query = "SELECT idCreator FROM gameCreator"
    cursor.execute(query)
    creator_list = [item['idCreator'] for item in cursor.fetchall()]
    form.gameCreator.choices = creator_list
    # episodes ------------------------------
    query = "SELECT episodeNumber FROM podcastEpisode"
    cursor.execute(query)
    episode_list = [item['episodeNumber'] for item in cursor.fetchall()]
    form.podcastEpisode.choices = episode_list

    if form.is_submitted():
        # define the update query
        update_entry = 'UPDATE game SET nameGame = %s, releaseDate = %s, cost = %s,  ' \
                 'gameGenre = (SELECT idGenre FROM gameGenre WHERE idGenre = %s), ' \
                 'gameCreator = (SELECT idCreator FROM gameCreator WHERE idCreator = %s), ' \
                 'podcastEpisode = (SELECT episodeNumber FROM podcastEpisode WHERE episodeNumber = %s) WHERE nameGame = %s'
        # get the values used in the query
        orig_name = form.originalName.data
        name = form.nameGame.data
        date = form.releaseDate.data
        cost = form.cost.data
        genre = form.gameGenre.data
        creator = form.gameCreator.data
        episode = []
        episode = form.podcastEpisode.data
        # checks if podcastEpisode is left blank
        if not form.podcastEpisode.data:
            episode = form.podcastEpisode.data
        insert_list = [name, date, cost, genre, creator, episode, orig_name]

        # check if the game is in platformFKzz
        cursor.execute("SELECT nameGame FROM platformFKzz")
        tmp = [item['nameGame'] for item in cursor.fetchall()]
        name_found_in_platformFKzz = False
        idx = -1
        for tmp_name in tmp:
            idx += 1
            if tmp_name == orig_name:
                name_found_in_platformFKzz = True

        if name_found_in_platformFKzz:
            # get the list of platform IDs associated with this game
            search_id = [orig_name]
            cursor.execute("SELECT idPlatform FROM platformFKzz WHERE nameGame = %s", search_id)
            orig_IDs = [item['idPlatform'] for item in cursor.fetchall()]

            # delete entries in platformFKzz for this game
            cursor.execute("DELETE FROM platformFKzz WHERE nameGame = %s", search_id)
            conn.commit()

            # edit this game in the game table now
            cursor.execute(update_entry, insert_list)
            conn.commit()

            # recreate all of the platformFKzz relations with updated game name.
            for plat_id in orig_IDs:
                insert_statement = 'INSERT INTO platformFKzz (nameGame, idPlatform) VALUES (%s, %s)'
                insert_l = [name, plat_id]
                cursor.execute(insert_statement, insert_l)
                conn.commit()
        else:
            cursor.execute(update_entry, insert_list)
            conn.commit()
        # show success message on home redirect
        flash(f'{orig_name} changed the database!', 'success')
        return redirect(url_for('home'))
    else:
        # renders the page before the form is submitted
        query = "SELECT * FROM game"
        cursor.execute(query)
        game = cursor.fetchall()
        return render_template('editgame.html', title='Edit a Game', form=form,
                               game=game)


if __name__ == '__main__':
    app.run(debug=True)
