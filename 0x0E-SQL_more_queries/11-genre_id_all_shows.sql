-- list all tv shows and the genre id

SELECT tv_shows.title, tv_show_genre.genre_id
FROM tv_shows
LEFT JOIN tv_show_genre ON tv_shows.id = tv_show_genre.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
