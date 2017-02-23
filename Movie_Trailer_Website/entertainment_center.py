import media
import fresh_tomatoes


# Movie Intance
Spider_Man = media.Movie(
    "Spider-Man: Homecoming",
    "A young Peter Parker/Spider-Man begins"
    " to navigate his newfound identity"
    " as the web-slinging superhero.",
    "http://www.mrmovie-review.com/wp-content/uploads"
    "/2016/12/spider-man-homecoming-movie-poster.jpg?x26928",
    "https://youtu.be/n9DwoQ7HWvI")
# Movie Intance
Despicable_Me = media.Movie(
    "Despicable Me 3",
    "The adventures of Gru, Lucy, their adorable daughters Margo,"\
    " Edith and Agnes and the Minions.",
    "https://latestmovieposters.files.wordpress.com/"
    "2015/06/despicable_me_3_poster.png",
    "https://youtu.be/6DBi41reeF0")
# Movie Intance
Justice_League = media.Movie(
    "Justice League",
    "Fueled by his restored faith in"
    " humanity and inspired"
    " by Superman's selfless act, Bruce Wayne"
    " enlists the help of his newfound ally,"
    " Diana Prince, to face an even greater enemy.",
    "https://static1.squarespace.com/static/"
    "51b3dc8ee4b051b96ceb10de/t/"
    "520670e3e4b0bdc260062d14/1376153828097/"
    "DefendersOfEarth.jpg",
    "https://youtu.be/fIHH5-HVS9o")
# Movie List
movies = [Spider_Man, Despicable_Me, Justice_League]
# Call page generator
fresh_tomatoes.open_movies_page(movies)
