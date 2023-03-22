1.sql
SELECT title
FROM movies
WHERE year = 2008;

2.sql
SELECT title
FROM movies
WHERE year = 2008;

3.sql
/*list the titles of all movies with a release date on or after 2018, in alphabetical order.*/
SELECT title
FROM movies
WHERE year >= "2018"
    order by title ASC;
    
4.sql
/* number of movies with an IMDb rating of 10.0 */
SELECT count(*)
FROM ratings
WHERE rating = "10.0";

5.sql
/* list the titles and release years of  Harry Potter movies, in chronological order */
SELECT title, year
FROM movies
where title
like "Harry Potter%"
order by year;

6.sql
/* average rating of all movies released in 2012*/
SELECT avg(rating)
FROM ratings JOIN movies ON movies.id = ratings.movie_id
WHERE year = 2012;

7.sql
/*list movies released in 2010 and their ratings,in descending order by rating For movies with the same rating,
order them alphabetically by title.*/
SELECT title, rating
FROM movies JOIN ratings ON movies.id = ratings.movie_id
WHERE year = '2010'
ORDER BY rating
DESC, title;

8.sql
/* list the names of all people who starred in Toy Story. */
SELECT name
FROM people JOIN stars ON people.id = stars.person_id
JOIN movies ON movies.id = stars.movie_id
WHERE title = "Toy Story";

9.sql
/* list the names of all people who starred in a movie released in 2004, ordered by birth year */
SELECT DISTINCT name
FROM people JOIN stars ON people.id = stars.person_id
JOIN movies ON movies.id = stars.movie_id
WHERE year = 2004
ORDER BY birth;

10.sql
/*list the names of all people who have directe da movie that received a rating of 9.0  */
SELECT name
FROM people
JOIN directors ON directors.person_id = people.id
JOIN ratings ON directors.movie_id = ratings.movie_id
WHERE rating >= 9.0;

11.sql
/* list the titles of the five highest rated movies (in order) that Chadwick Boseman starred in, starting with the highest rated.  */
SELECT DISTINCT title
FROM people JOIN stars ON people.id = stars.person_id
JOIN ratings ON ratings.movie_id = stars.movie_id
JOIN movies on movies.id = stars.movie_id
WHERE name = "Chadwick Boseman"
ORDER BY rating DESC
limit 5;

12.sql
/*list the titles of all movies in which both Johnny Depp and Helena Bonham Carter   */
SELECT title
FROM people JOIN stars on stars.person_id = people.id
JOIN movies ON stars.movie_id = movies.id
WHERE name = "Johnny Depp"
AND movie_id IN (
        SELECT movie_id
        from people join stars on stars.person_id = people.id
        where name = 'Helena Bonham Carter'
);

13.sql
/*  list the names of all people who starred in a movie in which Kevin Bacon also starred */
SELECT DISTINCT name
FROM people JOIN stars ON stars.person_id = people.id
WHERE name != "Kevin Bacon"
AND movie_id IN (
    SELECT movie_id
    FROM people JOIN stars ON stars.person_id = people.id
    WHERE name = "Kevin Bacon" AND birth = 1958
);






