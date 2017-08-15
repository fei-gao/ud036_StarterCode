'''

'''
import media
import fresh_tomatoes

# call the movie constructor in media.py file to initiate each movie object
avatar = media.Movie("Avatar",
                     "Story of a marine on a alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/"
                     "Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

finding_nemo = media.Movie("Finding Nemo",
                           "The story about how a lost fish finds "
                           "his way back home",
                           "https://upload.wikimedia.org/wikipedia/en/2/29/"
                           "Finding_Nemo.jpg",
                           "https://www.youtube.com/watch?v=wZdpNglLbt8")

midnight_in_paris = media.Movie("Midnight in Paris",
                                "The story about going back in time to meet "
                                "authors",
                                "https://upload.wikimedia.org/wikipedia/en/9/"
                                "9f/Midnight_in_Paris_Poster.jpg",
                                "https://www.youtube.com/watch?v=FAfR8omt-CY")

ratatouille = media.Movie("Ratatouille",
                          "The story about a rat who can cook",
                          "https://upload.wikimedia.org/wikipedia/en/5/50/"
                          "RatatouillePoster.jpg",
                          "https://www.youtube.com/watch?v=c3sBBRxDAqk")

the_prestige = media.Movie("The Prestige",
                           "Two stage magicians engage in competitive "
                           "one-upmanship in an attempt to create the"
                           " ultimate stage illusion",
                           "https://upload.wikimedia.org/wikipedia/en/d/d2/"
                           "Prestige_poster.jpg",
                           "https://www.youtube.com/watch?v=o4gHCmTQDVI")

save_private_ryan = media.Movie("Save Private Ryan",
                                "Following the Normandy Landings, a group of"
                                " U.S. soldiers go behind enemy lines to "
                                "retrieve a paratrooper whose brothers "
                                "have been killed in action",
                                "https://upload.wikimedia.org/wikipedia/en/a/"
                                "ac/Saving_Private_Ryan_poster.jpg",
                                "https://www.youtube.com/watch?v=RYID71hYHzg")

# make a movie list
movies = [avatar, finding_nemo, midnight_in_paris, ratatouille, the_prestige,
          save_private_ryan]

fresh_tomatoes.open_movies_page(movies)
