from flask import Flask, render_template, url_for
from xl2dict import XlToDict  # https://pypi.org/project/xl2dict/
from forms import AddGameForm, AddGenreForm, AddCreatorForm, AddPlatformForm, AddEpisodeForm, \
    AddDistributionPlatformForm, AddPost, RemoveTheThing

app = Flask(__name__)

app.config['SECRET_KEY'] = 'oTv!5ox8LB#A&@cBHpa@onsKU'

lorem_ipsum = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi vulputate diam at nisl fringilla sodales. Mauris cursus porta porttitor. In pellentesque sapien lacus, quis feugiat turpis blandit et. Aenean porta ornare lorem at pellentesque. Vestibulum viverra rhoncus massa et pharetra. Sed ornare tristique volutpat. Aliquam tortor erat, feugiat nec aliquet non, hendrerit ut felis. Nunc viverra pellentesque nibh, at tincidunt nisl tincidunt id. Nunc congue sit amet odio id efficitur. Sed dictum orci ut felis facilisis suscipit. Fusce a lectus odio. Quisque nisl sem, tristique id turpis at, varius porttitor libero. Donec varius vitae leo quis maximus. Mauris fermentum ante sapien, id laoreet dolor ultrices in. Ut ac scelerisque leo, sit amet tristique sem. Nunc gravida sit amet enim vitae tristique. Donec imperdiet nunc non pellentesque mattis. Integer accumsan mi vel leo congue tincidunt. Maecenas posuere, lorem id vulputate viverra, turpis ex dictum massa, non imperdiet neque augue id leo. Cras vehicula dapibus lacinia. Phasellus vestibulum diam velit, id aliquam nisl venenatis sed. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Vivamus vitae magna magna. Morbi at gravida lacus. Proin vel lacinia justo, vitae malesuada justo. Cras quis tortor a augue sollicitudin finibus sed et sem. Nunc lorem lacus, rutrum ac dui eu, viverra maximus sem. Nunc purus metus, viverra et diam ac, efficitur pellentesque sem. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent in est dolor.'

excel_to_dictionary = XlToDict()

game = excel_to_dictionary.convert_sheet_to_dict(file_path="website_sheets/game.xls",
                                                 sheet="Sheet1")

gameGenre = excel_to_dictionary.convert_sheet_to_dict(file_path="website_sheets/gameGenre.xls",
                                                 sheet="Sheet1")

gameCreator = excel_to_dictionary.convert_sheet_to_dict(file_path="website_sheets/gameCreator.xls",
                                                 sheet="Sheet1")

platform = excel_to_dictionary.convert_sheet_to_dict(
    file_path="website_sheets/platform.xls", sheet="Sheet1")

distributionPlatform = excel_to_dictionary.convert_sheet_to_dict(
    file_path="website_sheets/distribution_platform.xls", sheet="Sheet1")

podcastEpisode = excel_to_dictionary.convert_sheet_to_dict(
    file_path="website_sheets/podcast_episode.xls", sheet="Sheet1")

platform_combo_FK_zz = excel_to_dictionary.convert_sheet_to_dict(
    file_path="website_sheets/platform_combo_FK_zz.xls", sheet="Sheet1")

platform_FK_zz = excel_to_dictionary.convert_sheet_to_dict(
    file_path="website_sheets/platform_FK_zz.xls", sheet="Sheet1")

distribution_plat_FK_zz = excel_to_dictionary.convert_sheet_to_dict(
    file_path="website_sheets/distribution_plat_FK_zz.xls", sheet="Sheet1")

posts = [
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


@app.route("/", methods=['POST', 'GET'])
@app.route("/home", methods=['POST', 'GET'])
def home():
    return render_template('home.html', posts=posts)


@app.route("/addpost", methods=['POST', 'GET'])
def addHomePost():
    form = AddPost()
    return render_template('add_post.html', title='Add a Post', form=form)


@app.route("/games", methods=['POST', 'GET'])
def games():
    return render_template('games.html', game=game)


@app.route("/addgame", methods=['POST', 'GET'])
def addGame():
    form = AddGameForm()
    return render_template('add_game.html', title='Add a Game', form=form)


@app.route("/gamegenres", methods=['POST', 'GET'])
def gameGenres():
    return render_template('gameGenres.html', gameGenre=gameGenre)


@app.route("/addgenre", methods=['POST', 'GET'])
def addGenre():
    form = AddGenreForm()
    return render_template('add_genre.html', title='Add a Genre', form=form)


@app.route("/podcastepisodes", methods=['POST', 'GET'])
def podcastEpisodes():
    return render_template('podcastEpisode.html', podcastEpisode=podcastEpisode)


@app.route("/addepisode", methods=['POST', 'GET'])
def addEpisode():
    form = AddEpisodeForm()
    return render_template('add_episode.html', title='Add an Episode', form=form)


@app.route("/distributionplatforms", methods=['POST', 'GET'])
def distributionPlatforms():
    return render_template('distributionPlatform.html', distributionPlatform=distributionPlatform)


@app.route("/adddistribplat", methods=['POST', 'GET'])
def addDistributionPlatform():
    form = AddDistributionPlatformForm()
    return render_template('add_distrib_plat.html', form=form)


@app.route("/platforms", methods=['POST', 'GET'])
def platforms():
    return render_template('platforms.html', platform=platform)


@app.route("/addplatform", methods=['POST', 'GET'])
def addPlatforms():
    form = AddPlatformForm()
    return render_template('add_platform.html', title='Add a Platform', form=form)


@app.route("/gamecreators", methods=['POST', 'GET'])
def gameCreators():
    return render_template('gameCreators.html', gameCreator=gameCreator)


@app.route("/addcreator", methods=['POST', 'GET'])
def addCreator():
    form = AddCreatorForm()
    return render_template('add_creator.html', title='Add a Creator', form=form)


@app.route("/gamesandplatforms", methods=['POST', 'GET'])
def m2m_GameAndPlatform():
    return render_template('PlatformFKzz.html', platform_FK_zz=platform_FK_zz)


@app.route("/gamesanddistributionplatforms", methods=['POST', 'GET'])
def m2m_GameAndDistribPlatform():
    return render_template('DistributionPlatFKzz.html', distribution_plat_FK_zz=distribution_plat_FK_zz)


@app.route("/platformcombo", methods=['POST', 'GET'])
def m2m_PlatformCombo():
    return render_template('PlatformComboFKzz.html', platform_combo_FK_zz=platform_combo_FK_zz)


@app.route("/remove", methods=['POST', 'GET'])
def remove():
    form = RemoveTheThing()
    return render_template('remove.html', title='Remove', form=form)


if __name__ == '__main__':
    app.run(debug=True)
