-- list the titles with more than one link to genre

SELECT tv_shows.title AS title, tv_show_genres.genre_id AS genre_id
FROM tvshows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
