import fresh_tomatoes
import media

brothers = media.Movie("BROTHERS",
                       "A movie about two brothers divided due to misunderstanding and fighting each other in boxing championship finals",
                       "https://images-na.ssl-images-amazon.com/images/M/MV5BNzQ4Njg3Mjg5Nl5BMl5BanBnXkFtZTgwODE5MDg1NjE@._V1_QL50_.jpg",
                       "https://www.youtube.com/watch?v=QuRSCU0tOKs")

partition_1947 = media.Movie("PARTITION 1947",
                             "A movie based on the hidden facts of the british rule and freedom fights",
                             "https://upload.wikimedia.org/wikipedia/en/f/f3/Viceroy%27s_House_%28film%29.png",
                             "https://www.youtube.com/watch?v=YGb2W3USPBU")

coco_before_chanel = media.Movie("COCO BEFORE CHANEL",
                                 "First lady to start a very popular brand",
                                 "https://images-na.ssl-images-amazon.com/images/M/MV5BMTA0NjYzMzQxNzBeQTJeQWpwZ15BbWU3MDI2MDA0ODI@._V1_QL50_SY1000_CR0,0,674,1000_AL_.jpg",
                                 "https://www.youtube.com/watch?v=bvDFPjx-uBU")

devil_wears_prada = media.Movie("THE DEVIL WEARS PRADA",
                                "Movie depicting a life of a girl who ends up in a fashion designing company but at the end finds her way out to a successfull carrer of her choice",
                                "https://images-na.ssl-images-amazon.com/images/M/MV5BMTMyNjk4Njc3NV5BMl5BanBnXkFtZTcwNDkyMTEzMw@@._V1_QL50_SY1000_CR0,0,654,1000_AL_.jpg",
                                "https://www.youtube.com/watch?v=zicgut4gpwU")

lights_out = media.Movie("LIGHTS OUT",
                         "A horror movies on a ghost which only appears when lights go off",
                         "https://images-na.ssl-images-amazon.com/images/M/MV5BMTg1OTkxNDgyMV5BMl5BanBnXkFtZTgwMjEzNTc0ODE@._V1_QL50_SY1000_CR0,0,674,1000_AL_.jpg",
                         "https://www.youtube.com/watch?v=6LiKKFZyhRU"
                         )



movies=[brothers,partition_1947,coco_before_chanel,devil_wears_prada,lights_out]
fresh_tomatoes.open_movies_page(movies)
