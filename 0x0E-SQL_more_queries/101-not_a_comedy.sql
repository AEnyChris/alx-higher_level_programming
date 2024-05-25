-- list show title that are not Comedy in the database

SELECT DISTINCT(tv_shows.title)
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id
WHERE tv_genres.name != 'Comedy' OR tv_genres.name IS NULL
ORDER BY tv_shows.title;