-- show show titles by genre using join
-- in order and joined
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows
RIGHT JOIN tv_show_genres ON tv_shows.id=tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
