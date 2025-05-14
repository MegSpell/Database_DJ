Make sure you download the starter code and run the following:

```sh
  psql < movies.sql
  psql movies_db
```

In markdown, you can place a code block inside of three backticks (```) followed by the syntax highlighting you want, for example

\```sql

SELECT \* FROM users;

\```

Using the `movies_db` database, write the correct SQL queries for each of these tasks:

1.  The title of every movie.

SELECT title FROM movies;


/////////////
movies_db=# SELECT title FROM movies;
                       title                        
*----------------------------------------------------
 Star Wars: The Force Awakens
 Marvel's The Avengers
 Star Wars: The Last Jedi
 Black Panther
 Rogue One: A Star Wars Story
 Beauty and the Beast
 Finding Dory
 Avengers: Age of Ultron
 Pirates of the Caribbean: Dead Man's Chest
 The Lion King
 Avatar
 Star Wars: Episode I - The Phantom Menace
 Star Wars
 Star Wars: Episode III - Revenge of the Sith
 Deadpool
 Star Wars: Episode II - Attack of the Clones
 Return of the Jedi
 Independence Day
 The Empire Strikes Back
 Home Alone
 Titanic
 Transformers: Revenge of the Fallen
 Transformers: Dark of the Moon
 Forrest Gump
 Shrek the Third
 Transformers
 Iron Man
 Indiana Jones & Kingdom of the Crystal Skull
 Iron Man 2
 Jurassic World
 E. T.: The Extra-Terrestrial
 Jurassic Park
 The Secret Life of Pets
 Despicable Me 2
 Furious 7
 Minions
 Meet the Fockers
 Sing
 Despicable Me 3
 The Dark Knight
 The Dark Knight Rises
 Wonder Woman
 Harry Potter and the Deathly Hallows: Part 2
 American Sniper
 Batman v Superman: Dawn of Justice
 It
 Suicide Squad
 Harry Potter and the Sorcerer's Stone
 The Hobbit: An Unexpected Journey
 Harry Potter and the Half-Blood Prince
 Harry Potter and the Deathly Hallows: Part 1
 Inception
 Harry Potter and the Order of the Phoenix
 Man of Steel
 The Matrix Reloaded
 Shrek 2
 Shrek
 The Hunger Games: Catching Fire
 The Hunger Games
 The Hunger Games: Mockingjay - Part 1
 The Twilight Saga: Breaking Dawn Part 2
 The Hunger Games: Mockingjay - Part 2
 Spider-Man
 Jumanji: Welcome to the Jungle
 Spider-Man 2
 Spider-Man 3
 Spider-Man: Homecoming
 Skyfall
 The Amazing Spider-Man
 The Lord of the Rings: Return of the King
 The Lord of the Rings: The Two Towers
 The Lord of the Rings: Fellowship of the Ring
 The Passion of the Christ
 The Twilight Saga: Eclipse
 The Twilight Saga: New Moon
 The Twilight Saga: Breaking Dawn Part 1
 Toy Story 3
 Iron Man 3
 Captain America: Civil War
 Frozen
 Guardians of the Galaxy Vol. 2
 Finding Nemo
 The Jungle Book
 Inside Out
 Zootopia
 Alice in Wonderland
 Guardians of the Galaxy
 Thor: Ragnarok
 Pirates of the Caribbean: At World's End
 Pirates of the Caribbean: Curse of the Black Pearl
 The Sixth Sense
 Up
 The Chronicles of Narnia: Lion, Witch & Wardrobe
 Monsters, Inc.
 Monsters University
 The Incredibles
 Toy Story 2
 Harry Potter and the Goblet of Fire
 The Hangover
 Gravity
 Harry Potter and the Chamber of Secrets
(101 rows)

*****************************************************************

2.  All information on the G-rated movies.

SELECT * FROM movies
WHERE rating = 'G';


//////////////
movies_db=# SELECT * FROM movies
movies_db-# WHERE rating = 'G';
 id  |        title        | release_year | runtime | rating | studio_id 
-----+---------------------+--------------+---------+--------+-----------
  20 | The Lion King       |         1994 |      89 | G      |         1
  21 | Toy Story 3         |         2010 |     103 | G      |         1
  33 | Finding Nemo        |         2003 |     104 | G      |         1
  86 | Monsters, Inc.      |         2001 |      90 | G      |         1
  95 | Monsters University |         2013 |     107 | G      |         1
 101 | Toy Story 2         |         1999 |      95 | G      |         1
(6 rows)

*****************************************************************

3.  The title and release year of every movie, ordered with the
    oldest movie first.

SELECT title, release_year
FROM movies
ORDER BY release_year ASC;


//////////////
movies_db=# SELECT title, release_year
movies_db-# FROM movies
movies_db-# ORDER BY release_year ASC;
                       title                        | release_year 
----------------------------------------------------+--------------
 Star Wars                                          |         1977
 The Empire Strikes Back                            |         1980
 E. T.: The Extra-Terrestrial                       |         1982
 Return of the Jedi                                 |         1983
 Home Alone                                         |         1990
 Jurassic Park                                      |         1993
 The Lion King                                      |         1994
 Forrest Gump                                       |         1994
 Independence Day                                   |         1996
 Titanic                                            |         1997
 The Sixth Sense                                    |         1999
 Star Wars: Episode I - The Phantom Menace          |         1999
 Toy Story 2                                        |         1999
 Harry Potter and the Sorcerer's Stone              |         2001
 Monsters, Inc.                                     |         2001
 The Lord of the Rings: Fellowship of the Ring      |         2001
 Shrek                                              |         2001
 Harry Potter and the Chamber of Secrets            |         2002
 The Lord of the Rings: The Two Towers              |         2002
 Star Wars: Episode II - Attack of the Clones       |         2002
 Spider-Man                                         |         2002
 Finding Nemo                                       |         2003
 Pirates of the Caribbean: Curse of the Black Pearl |         2003
 The Lord of the Rings: Return of the King          |         2003
 The Matrix Reloaded                                |         2003
 The Passion of the Christ                          |         2004
 Spider-Man 2                                       |         2004
 Meet the Fockers                                   |         2004
 The Incredibles                                    |         2004
 Shrek 2                                            |         2004
 Harry Potter and the Goblet of Fire                |         2005
 The Chronicles of Narnia: Lion, Witch & Wardrobe   |         2005
 Star Wars: Episode III - Revenge of the Sith       |         2005
 Pirates of the Caribbean: Dead Man's Chest         |         2006
 Shrek the Third                                    |         2007
 Transformers                                       |         2007
 Harry Potter and the Order of the Phoenix          |         2007
 Spider-Man 3                                       |         2007
 Pirates of the Caribbean: At World's End           |         2007
 Indiana Jones & Kingdom of the Crystal Skull       |         2008
 The Dark Knight                                    |         2008
 Iron Man                                           |         2008
 Transformers: Revenge of the Fallen                |         2009
 The Hangover                                       |         2009
 Up                                                 |         2009
 Avatar                                             |         2009
 Harry Potter and the Half-Blood Prince             |         2009
 The Twilight Saga: New Moon                        |         2009
 The Twilight Saga: Eclipse                         |         2010
 Toy Story 3                                        |         2010
 Harry Potter and the Deathly Hallows: Part 1       |         2010
 Inception                                          |         2010
 Iron Man 2                                         |         2010
 Alice in Wonderland                                |         2010
 Harry Potter and the Deathly Hallows: Part 2       |         2011
 Transformers: Dark of the Moon                     |         2011
 The Twilight Saga: Breaking Dawn Part 1            |         2011
 The Amazing Spider-Man                             |         2012
 The Dark Knight Rises                              |         2012
 The Twilight Saga: Breaking Dawn Part 2            |         2012
 The Hobbit: An Unexpected Journey                  |         2012
 Marvel's The Avengers                              |         2012
 The Hunger Games                                   |         2012
 Skyfall                                            |         2012
 Man of Steel                                       |         2013
 Monsters University                                |         2013
 The Hunger Games: Catching Fire                    |         2013
 Iron Man 3                                         |         2013
 Gravity                                            |         2013
 Frozen                                             |         2013
 Despicable Me 2                                    |         2013
 The Hunger Games: Mockingjay - Part 1              |         2014
 Guardians of the Galaxy                            |         2014
 American Sniper                                    |         2014
 Star Wars: The Force Awakens                       |         2015
 Furious 7                                          |         2015
 Jurassic World                                     |         2015
 The Hunger Games: Mockingjay - Part 2              |         2015
 Inside Out                                         |         2015
 Avengers: Age of Ultron                            |         2015
 Minions                                            |         2015
 Deadpool                                           |         2016
 The Jungle Book                                    |         2016
 Zootopia                                           |         2016
 The Secret Life of Pets                            |         2016
 Suicide Squad                                      |         2016
 Sing                                               |         2016
 Batman v Superman: Dawn of Justice                 |         2016
 Finding Dory                                       |         2016
 Rogue One: A Star Wars Story                       |         2016
 Captain America: Civil War                         |         2016
 Star Wars: The Last Jedi                           |         2017
 Guardians of the Galaxy Vol. 2                     |         2017
 Despicable Me 3                                    |         2017
 Beauty and the Beast                               |         2017
 Spider-Man: Homecoming                             |         2017
 It                                                 |         2017
 Wonder Woman                                       |         2017
 Thor: Ragnarok                                     |         2017
 Jumanji: Welcome to the Jungle                     |         2018
 Black Panther                                      |         2018
(101 rows)

*****************************************************************
    
4.  All information on the 5 longest movies.

SELECT *
FROM movies
ORDER BY runtime DESC
LIMIT 5;


///////////////
movies_db=# SELECT *
movies_db-# FROM movies
movies_db-# ORDER BY runtime DESC
movies_db-# LIMIT 5;
 id |                     title                     | release_year | runtime | rating | studio_id 
----+-----------------------------------------------+--------------+---------+--------+-----------
 35 | The Lord of the Rings: Return of the King     |         2003 |     200 | PG-13  |         9
  3 | Titanic                                       |         1997 |     194 | PG-13  |         3
 46 | The Lord of the Rings: The Two Towers         |         2002 |     179 | PG-13  |         9
 63 | The Lord of the Rings: Fellowship of the Ring |         2001 |     178 | PG-13  |         9
 67 | Pirates of the Caribbean: At World's End      |         2007 |     168 | PG-13  |         1
(5 rows)

*****************************************************************

5.  A query that returns the columns of `rating` and `total`, tabulating the
    total number of G, PG, PG-13, and R-rated movies.

SELECT rating, COUNT(*) AS total
FROM movies
GROUP BY rating;


//////////////
movies_db=# SELECT rating, COUNT(*) AS total
movies_db-# FROM movies
movies_db-# GROUP BY rating;
 rating | total 
--------+-------
 PG-13  |    64
 R      |     6
 G      |     6
 PG     |    25
(4 rows)

*****************************************************************

6.  A table with columns of `release_year` and `average_runtime`,
    tabulating the average runtime by year for every movie in the database. The data should be in reverse chronological order (i.e. the most recent year should be first).

SELECT release_year, AVG(runtime) AS average_runtime
FROM movies
GROUP BY release_year
ORDER BY release_year DESC;


/////////////
movies_db=# SELECT release_year, AVG(runtime) AS average_runtime
movies_db-# FROM movies
movies_db-# GROUP BY release_year
movies_db-# ORDER BY release_year DESC;
 release_year |   average_runtime    
--------------+----------------------
         2018 | 129.5000000000000000
         2017 | 130.7500000000000000
         2016 | 118.3000000000000000
         2015 | 122.8571428571428571
         2014 | 125.3333333333333333
         2013 | 117.4285714285714286
         2012 | 144.2857142857142857
         2011 | 130.6666666666666667
         2010 | 126.5000000000000000
         2009 | 129.8333333333333333
         2008 | 132.0000000000000000
         2007 | 136.4000000000000000
         2006 | 151.0000000000000000
         2005 | 143.6666666666666667
         2004 | 115.0000000000000000
         2003 | 144.2500000000000000
         2002 | 148.2500000000000000
         2001 | 127.7500000000000000
         1999 | 111.6666666666666667
         1997 | 194.0000000000000000
         1996 | 153.0000000000000000
         1994 | 115.0000000000000000
         1993 | 127.0000000000000000
         1990 | 105.0000000000000000
         1983 | 134.0000000000000000
         1982 | 117.0000000000000000
         1980 | 129.0000000000000000
         1977 | 121.0000000000000000
(28 rows)


*****************************************************************

7.  The movie title and studio name for every movie in the
    database.

SELECT movies.title, studios.name
FROM movies
JOIN studios ON movies.studio_id = studios.id;


////////////
movies_db=# SELECT movies.title, studios.name
movies_db-# FROM movies
movies_db-# JOIN studios ON movies.studio_id = studios.id;
                       title                        |                name                 
----------------------------------------------------+-------------------------------------
 Star Wars: The Force Awakens                       | Walt Disney Studios Motion Pictures
 Marvel's The Avengers                              | Walt Disney Studios Motion Pictures
 Star Wars: The Last Jedi                           | Walt Disney Studios Motion Pictures
 Black Panther                                      | Walt Disney Studios Motion Pictures
 Rogue One: A Star Wars Story                       | Walt Disney Studios Motion Pictures
 Beauty and the Beast                               | Walt Disney Studios Motion Pictures
 Finding Dory                                       | Walt Disney Studios Motion Pictures
 Avengers: Age of Ultron                            | Walt Disney Studios Motion Pictures
 Pirates of the Caribbean: Dead Man's Chest         | Walt Disney Studios Motion Pictures
 The Lion King                                      | Walt Disney Studios Motion Pictures
 Avatar                                             | 20th Century Fox
 Star Wars: Episode I - The Phantom Menace          | 20th Century Fox
 Star Wars                                          | 20th Century Fox
 Star Wars: Episode III - Revenge of the Sith       | 20th Century Fox
 Deadpool                                           | 20th Century Fox
 Star Wars: Episode II - Attack of the Clones       | 20th Century Fox
 Return of the Jedi                                 | 20th Century Fox
 Independence Day                                   | 20th Century Fox
 The Empire Strikes Back                            | 20th Century Fox
 Home Alone                                         | 20th Century Fox
 Titanic                                            | Paramount Pictures
 Transformers: Revenge of the Fallen                | Paramount Pictures
 Transformers: Dark of the Moon                     | Paramount Pictures
 Forrest Gump                                       | Paramount Pictures
 Shrek the Third                                    | Paramount Pictures
 Transformers                                       | Paramount Pictures
 Iron Man                                           | Paramount Pictures
 Indiana Jones & Kingdom of the Crystal Skull       | Paramount Pictures
 Iron Man 2                                         | Paramount Pictures
 Jurassic World                                     | Universal Pictures
 E. T.: The Extra-Terrestrial                       | Universal Pictures
 Jurassic Park                                      | Universal Pictures
 The Secret Life of Pets                            | Universal Pictures
 Despicable Me 2                                    | Universal Pictures
 Furious 7                                          | Universal Pictures
 Minions                                            | Universal Pictures
 Meet the Fockers                                   | Universal Pictures
 Sing                                               | Universal Pictures
 Despicable Me 3                                    | Universal Pictures
 The Dark Knight                                    | Warner Bros.
 The Dark Knight Rises                              | Warner Bros.
 Wonder Woman                                       | Warner Bros.
 Harry Potter and the Deathly Hallows: Part 2       | Warner Bros.
 American Sniper                                    | Warner Bros.
 Batman v Superman: Dawn of Justice                 | Warner Bros.
 It                                                 | Warner Bros.
 Suicide Squad                                      | Warner Bros.
 Harry Potter and the Sorcerer's Stone              | Warner Bros.
 The Hobbit: An Unexpected Journey                  | Warner Bros.
 Harry Potter and the Half-Blood Prince             | Warner Bros.
 Harry Potter and the Deathly Hallows: Part 1       | Warner Bros.
 Inception                                          | Warner Bros.
 Harry Potter and the Order of the Phoenix          | Warner Bros.
 Man of Steel                                       | Warner Bros.
 The Matrix Reloaded                                | Warner Bros.
 Shrek 2                                            | Dreamworks SKG
 Shrek                                              | Dreamworks SKG
 The Hunger Games: Catching Fire                    | Lionsgate
 The Hunger Games                                   | Lionsgate
 The Hunger Games: Mockingjay - Part 1              | Lionsgate
 The Twilight Saga: Breaking Dawn Part 2            | Lionsgate
 The Hunger Games: Mockingjay - Part 2              | Lionsgate
 Spider-Man                                         | Sony / Columbia Pictures
 Jumanji: Welcome to the Jungle                     | Sony / Columbia Pictures
 Spider-Man 2                                       | Sony / Columbia Pictures
 Spider-Man 3                                       | Sony / Columbia Pictures
 Spider-Man: Homecoming                             | Sony / Columbia Pictures
 Skyfall                                            | Sony / Columbia Pictures
 The Amazing Spider-Man                             | Sony / Columbia Pictures
 The Lord of the Rings: Return of the King          | New Line Cinema
 The Lord of the Rings: The Two Towers              | New Line Cinema
 The Lord of the Rings: Fellowship of the Ring      | New Line Cinema
 The Passion of the Christ                          | Newmarket Films
 The Twilight Saga: Eclipse                         | Summit Entertainment
 The Twilight Saga: New Moon                        | Summit Entertainment
 The Twilight Saga: Breaking Dawn Part 1            | Summit Entertainment
 Toy Story 3                                        | Walt Disney Studios Motion Pictures
 Iron Man 3                                         | Walt Disney Studios Motion Pictures
 Captain America: Civil War                         | Walt Disney Studios Motion Pictures
 Frozen                                             | Walt Disney Studios Motion Pictures
 Guardians of the Galaxy Vol. 2                     | Walt Disney Studios Motion Pictures
 Finding Nemo                                       | Walt Disney Studios Motion Pictures
 The Jungle Book                                    | Walt Disney Studios Motion Pictures
 Inside Out                                         | Walt Disney Studios Motion Pictures
 Zootopia                                           | Walt Disney Studios Motion Pictures
 Alice in Wonderland                                | Walt Disney Studios Motion Pictures
 Guardians of the Galaxy                            | Walt Disney Studios Motion Pictures
 Thor: Ragnarok                                     | Walt Disney Studios Motion Pictures
 Pirates of the Caribbean: At World's End           | Walt Disney Studios Motion Pictures
 Pirates of the Caribbean: Curse of the Black Pearl | Walt Disney Studios Motion Pictures
 The Sixth Sense                                    | Walt Disney Studios Motion Pictures
 Up                                                 | Walt Disney Studios Motion Pictures
 The Chronicles of Narnia: Lion, Witch & Wardrobe   | Walt Disney Studios Motion Pictures
 Monsters, Inc.                                     | Walt Disney Studios Motion Pictures
 Monsters University                                | Walt Disney Studios Motion Pictures
 The Incredibles                                    | Walt Disney Studios Motion Pictures
 Toy Story 2                                        | Walt Disney Studios Motion Pictures
 Harry Potter and the Goblet of Fire                | Warner Bros.
 The Hangover                                       | Warner Bros.
 Gravity                                            | Warner Bros.
 Harry Potter and the Chamber of Secrets            | Warner Bros.
(101 rows)

*****************************************************************

8.  The star first name, star last name, and movie title for every
    matching movie and star pair in the database.

SELECT stars.first_name, stars.last_name, movies.title
FROM roles
JOIN stars ON roles.star_id = stars.id
JOIN movies ON roles.movie_id = movies.id;


///////////
movies_db=# SELECT stars.first_name, stars.last_name, movies.title
movies_db-# FROM roles
movies_db-# JOIN stars ON roles.star_id = stars.id
movies_db-# JOIN movies ON roles.movie_id = movies.id;
 first_name  |   last_name   |                       title                        
-------------+---------------+----------------------------------------------------
 Frances     | McDormand     | Transformers: Dark of the Moon
 Emma        | Watson        | Beauty and the Beast
 Emma        | Watson        | Harry Potter and the Sorcerer's Stone
 Emma        | Watson        | Harry Potter and the Half-Blood Prince
 Emma        | Watson        | Harry Potter and the Order of the Phoenix
 Emma        | Watson        | Harry Potter and the Goblet of Fire
 Emma        | Watson        | Harry Potter and the Chamber of Secrets
 Emma        | Watson        | Harry Potter and the Deathly Hallows: Part 2
 Emma        | Watson        | Harry Potter and the Deathly Hallows: Part 1
 Daniel      | Radcliffe     | Harry Potter and the Deathly Hallows: Part 2
 Daniel      | Radcliffe     | Harry Potter and the Sorcerer's Stone
 Daniel      | Radcliffe     | Harry Potter and the Half-Blood Prince
 Daniel      | Radcliffe     | Harry Potter and the Deathly Hallows: Part 1
 Daniel      | Radcliffe     | Harry Potter and the Order of the Phoenix
 Daniel      | Radcliffe     | Harry Potter and the Goblet of Fire
 Daniel      | Radcliffe     | Harry Potter and the Chamber of Secrets
 Morgan      | Freeman       | The Dark Knight
 Morgan      | Freeman       | The Dark Knight Rises
 Will        | Smith         | Suicide Squad
 Will        | Smith         | Independence Day
 Cameron     | Diaz          | Shrek 2
 Cameron     | Diaz          | Shrek the Third
 Cameron     | Diaz          | Shrek
 Kate        | Winslet       | Titanic
 Natalie     | Portman       | Star Wars: Episode I - The Phantom Menace
 Natalie     | Portman       | Star Wars: Episode III - Revenge of the Sith
 Natalie     | Portman       | Star Wars: Episode II - Attack of the Clones
 Dwayne      | Johnson       | Jumanji: Welcome to the Jungle
 Dwayne      | Johnson       | Furious 7
 Scarlett    | Johansson     | Marvel's The Avengers
 Scarlett    | Johansson     | Avengers: Age of Ultron
 Scarlett    | Johansson     | Captain America: Civil War
 Scarlett    | Johansson     | The Jungle Book
 Scarlett    | Johansson     | Iron Man 2
 Scarlett    | Johansson     | Sing
 Keira       | Knightley     | Star Wars: Episode I - The Phantom Menace
 Keira       | Knightley     | Pirates of the Caribbean: Dead Man's Chest
 Keira       | Knightley     | Pirates of the Caribbean: At World's End
 Keira       | Knightley     | Pirates of the Caribbean: Curse of the Black Pearl
 Samuel      | Jackson       | Marvel's The Avengers
 Samuel      | Jackson       | Star Wars: Episode I - The Phantom Menace
 Samuel      | Jackson       | Avengers: Age of Ultron
 Samuel      | Jackson       | Jurassic Park
 Samuel      | Jackson       | Star Wars: Episode III - Revenge of the Sith
 Samuel      | Jackson       | Iron Man
 Samuel      | Jackson       | Iron Man 2
 Samuel      | Jackson       | Star Wars: Episode II - Attack of the Clones
 Samuel      | Jackson       | The Incredibles
 Tom         | Hanks         | Toy Story 3
 Tom         | Hanks         | Forrest Gump
 Tom         | Hanks         | Toy Story 2
 Christopher | Plummer       | Up
 Jennifer    | Lawrence      | The Hunger Games: Catching Fire
 Jennifer    | Lawrence      | The Hunger Games
 Jennifer    | Lawrence      | The Hunger Games: Mockingjay - Part 1
 Jennifer    | Lawrence      | The Hunger Games: Mockingjay - Part 2
 Kathy       | Bates         | Titanic
 Harrison    | Ford          | Star Wars: The Force Awakens
 Harrison    | Ford          | Star Wars
 Harrison    | Ford          | Indiana Jones & Kingdom of the Crystal Skull
 Harrison    | Ford          | Return of the Jedi
 Harrison    | Ford          | The Empire Strikes Back
 Viola       | Davis         | Suicide Squad
 Bradley     | Cooper        | Guardians of the Galaxy Vol. 2
 Bradley     | Cooper        | American Sniper
 Bradley     | Cooper        | Guardians of the Galaxy
 Bradley     | Cooper        | The Hangover
 Amy         | Poehler       | Inside Out
 Amy         | Poehler       | Shrek the Third
 Joseph      | Gordon-Levitt | Star Wars: The Last Jedi
 Joseph      | Gordon-Levitt | The Dark Knight Rises
 Joseph      | Gordon-Levitt | Inception
 Danai       | Gurira        | Black Panther
 Angela      | Bassett       | Black Panther
 Ian         | McKellen      | Beauty and the Beast
 Ian         | McKellen      | The Lord of the Rings: Return of the King
 Ian         | McKellen      | The Lord of the Rings: The Two Towers
 Ian         | McKellen      | The Lord of the Rings: Fellowship of the Ring
 Ian         | McKellen      | The Hobbit: An Unexpected Journey
 Maya        | Rudolph       | Shrek the Third
 Jenny       | Slate         | The Secret Life of Pets
 Jenny       | Slate         | Zootopia
 Jenny       | Slate         | Despicable Me 3
 Idris       | Elba          | Finding Dory
 Idris       | Elba          | Avengers: Age of Ultron
 Idris       | Elba          | The Jungle Book
 Idris       | Elba          | Zootopia
 Idris       | Elba          | Thor: Ragnarok
 Octavia     | Spencer       | Spider-Man
 Octavia     | Spencer       | Zootopia
 Chadwick    | Boseman       | Black Panther
 Chadwick    | Boseman       | Captain America: Civil War
 Michael     | Keaton        | Toy Story 3
 Michael     | Keaton        | Minions
 Michael     | Keaton        | Spider-Man: Homecoming
 Kristen     | Wiig          | Despicable Me 2
 Kristen     | Wiig          | Despicable Me 3
 Keanu       | Reeves        | The Matrix Reloaded
 Helena      | Carter        | Harry Potter and the Deathly Hallows: Part 2
 Helena      | Carter        | Alice in Wonderland
 Helena      | Carter        | Harry Potter and the Half-Blood Prince
 Helena      | Carter        | Harry Potter and the Deathly Hallows: Part 1
 Helena      | Carter        | Harry Potter and the Order of the Phoenix
 Daniel      | Craig         | Star Wars: The Force Awakens
 Daniel      | Craig         | Skyfall
 Emma        | Stone         | The Amazing Spider-Man
 Zoe         | Saldana       | Avatar
 Zoe         | Saldana       | Guardians of the Galaxy Vol. 2
 Zoe         | Saldana       | Guardians of the Galaxy
 Zoe         | Saldana       | Pirates of the Caribbean: Curse of the Black Pearl
 Chris       | Pratt         | Jurassic World
 Chris       | Pratt         | Star Wars
 Chris       | Pratt         | Guardians of the Galaxy Vol. 2
 Chris       | Pratt         | Guardians of the Galaxy
 Anne        | Hathaway      | The Dark Knight Rises
 Anne        | Hathaway      | Alice in Wonderland
 Ellen       | DeGeneres     | Finding Dory
 Ellen       | DeGeneres     | Finding Nemo
 Robert      | Downey Jr.    | Marvel's The Avengers
 Robert      | Downey Jr.    | Avengers: Age of Ultron
 Robert      | Downey Jr.    | Iron Man 3
 Robert      | Downey Jr.    | Captain America: Civil War
 Robert      | Downey Jr.    | Spider-Man: Homecoming
 Robert      | Downey Jr.    | Iron Man
 Robert      | Downey Jr.    | Iron Man 2
(125 rows)

*****************************************************************

9.  The first and last names of every star who has been in a G-rated movie. The first and last name should appear only once for each star, even if they are in several G-rated movies. *IMPORTANT NOTE*: it's possible that there can be two *different* actors with the same name, so make sure your solution accounts for that.

SELECT DISTINCT stars.id, stars.first_name, stars.last_name
FROM stars
JOIN roles ON stars.id = roles.star_id
JOIN movies ON roles.movie_id = movies.id
WHERE movies.rating = 'G';


////////////
movies_db=# SELECT DISTINCT stars.id, stars.first_name, stars.last_name
movies_db-# FROM stars
movies_db-# JOIN roles ON stars.id = roles.star_id
movies_db-# JOIN movies ON roles.movie_id = movies.id
movies_db-# WHERE movies.rating = 'G';
 id | first_name | last_name 
----+------------+-----------
 18 | Tom        | Hanks
 39 | Michael    | Keaton
 49 | Ellen      | DeGeneres
(3 rows)

*****************************************************************

10. The first and last names of every star along with the number
    of movies they have been in, in descending order by the number of movies. (Similar to #9, make sure
    that two different actors with the same name are considered separately).

SELECT stars.id, stars.first_name, stars.last_name, COUNT(roles.movie_id) AS movie_count
FROM stars
JOIN roles ON stars.id = roles.star_id
GROUP BY stars.id, stars.first_name, stars.last_name
ORDER BY movie_count DESC;


//////////////
movies_db=# SELECT stars.id, stars.first_name, stars.last_name, COUNT(roles.movie_id) AS movie_count
movies_db-# FROM stars
movies_db-# JOIN roles ON stars.id = roles.star_id
movies_db-# GROUP BY stars.id, stars.first_name, stars.last_name
movies_db-# ORDER BY movie_count DESC;
 id | first_name  |   last_name   | movie_count 
----+-------------+---------------+-------------
 17 | Samuel      | Jackson       |           9
  3 | Emma        | Watson        |           8
  4 | Daniel      | Radcliffe     |           7
 50 | Robert      | Downey Jr.    |           7
 14 | Scarlett    | Johansson     |           6
 24 | Harrison    | Ford          |           5
 36 | Idris       | Elba          |           5
 43 | Helena      | Carter        |           5
 33 | Ian         | McKellen      |           5
 27 | Bradley     | Cooper        |           4
 20 | Jennifer    | Lawrence      |           4
 15 | Keira       | Knightley     |           4
 46 | Zoe         | Saldana       |           4
 47 | Chris       | Pratt         |           4
 35 | Jenny       | Slate         |           3
 18 | Tom         | Hanks         |           3
  8 | Cameron     | Diaz          |           3
 29 | Joseph      | Gordon-Levitt |           3
 39 | Michael     | Keaton        |           3
 10 | Natalie     | Portman       |           3
  6 | Morgan      | Freeman       |           2
 44 | Daniel      | Craig         |           2
 40 | Kristen     | Wiig          |           2
 48 | Anne        | Hathaway      |           2
 37 | Octavia     | Spencer       |           2
 28 | Amy         | Poehler       |           2
  7 | Will        | Smith         |           2
 38 | Chadwick    | Boseman       |           2
 12 | Dwayne      | Johnson       |           2
 49 | Ellen       | DeGeneres     |           2
 26 | Viola       | Davis         |           1
 22 | Kathy       | Bates         |           1
  9 | Kate        | Winslet       |           1
 45 | Emma        | Stone         |           1
 34 | Maya        | Rudolph       |           1
 30 | Danai       | Gurira        |           1
 41 | Keanu       | Reeves        |           1
 32 | Angela      | Bassett       |           1
  1 | Frances     | McDormand     |           1
 19 | Christopher | Plummer       |           1
(40 rows)

*****************************************************************

### The rest of these are bonuses

11. The title of every movie along with the number of stars in
    that movie, in descending order by the number of stars.

SELECT movies.title, COUNT(roles.star_id) AS star_count
FROM movies
JOIN roles ON movies.id = roles.movie_id
GROUP BY movies.id, movies.title
ORDER BY star_count DESC;


//////////////
movies_db=# SELECT movies.title, COUNT(roles.star_id) AS star_count
movies_db-# FROM movies
movies_db-# JOIN roles ON movies.id = roles.movie_id
movies_db-# GROUP BY movies.id, movies.title
movies_db-# ORDER BY star_count DESC;
                       title                        | star_count 
----------------------------------------------------+------------
 Avengers: Age of Ultron                            |          4
 Black Panther                                      |          3
 The Dark Knight Rises                              |          3
 Iron Man 2                                         |          3
 Star Wars: Episode I - The Phantom Menace          |          3
 Captain America: Civil War                         |          3
 Harry Potter and the Half-Blood Prince             |          3
 Harry Potter and the Order of the Phoenix          |          3
 Guardians of the Galaxy Vol. 2                     |          3
 Zootopia                                           |          3
 Harry Potter and the Deathly Hallows: Part 1       |          3
 Marvel's The Avengers                              |          3
 Guardians of the Galaxy                            |          3
 Shrek the Third                                    |          3
 Harry Potter and the Deathly Hallows: Part 2       |          3
 Harry Potter and the Sorcerer's Stone              |          2
 Finding Dory                                       |          2
 Iron Man                                           |          2
 Beauty and the Beast                               |          2
 Toy Story 3                                        |          2
 Star Wars                                          |          2
 Despicable Me 3                                    |          2
 Titanic                                            |          2
 Alice in Wonderland                                |          2
 Pirates of the Caribbean: Curse of the Black Pearl |          2
 Harry Potter and the Chamber of Secrets            |          2
 Harry Potter and the Goblet of Fire                |          2
 Spider-Man: Homecoming                             |          2
 Star Wars: Episode III - Revenge of the Sith       |          2
 Star Wars: The Force Awakens                       |          2
 Suicide Squad                                      |          2
 The Jungle Book                                    |          2
 Star Wars: Episode II - Attack of the Clones       |          2
 The Hunger Games                                   |          1
 Sing                                               |          1
 Jumanji: Welcome to the Jungle                     |          1
 Finding Nemo                                       |          1
 The Hunger Games: Catching Fire                    |          1
 Thor: Ragnarok                                     |          1
 Forrest Gump                                       |          1
 Jurassic Park                                      |          1
 Iron Man 3                                         |          1
 The Dark Knight                                    |          1
 Inception                                          |          1
 Jurassic World                                     |          1
 Return of the Jedi                                 |          1
 Shrek                                              |          1
 Pirates of the Caribbean: At World's End           |          1
 The Lord of the Rings: Fellowship of the Ring      |          1
 The Lord of the Rings: Return of the King          |          1
 American Sniper                                    |          1
 Star Wars: The Last Jedi                           |          1
 The Empire Strikes Back                            |          1
 Despicable Me 2                                    |          1
 The Hangover                                       |          1
 The Matrix Reloaded                                |          1
 Toy Story 2                                        |          1
 Independence Day                                   |          1
 Minions                                            |          1
 Avatar                                             |          1
 Shrek 2                                            |          1
 Indiana Jones & Kingdom of the Crystal Skull       |          1
 The Amazing Spider-Man                             |          1
 Transformers: Dark of the Moon                     |          1
 Inside Out                                         |          1
 The Hunger Games: Mockingjay - Part 2              |          1
 The Lord of the Rings: The Two Towers              |          1
 Furious 7                                          |          1
 The Incredibles                                    |          1
 The Secret Life of Pets                            |          1
 Skyfall                                            |          1
 Spider-Man                                         |          1
 The Hunger Games: Mockingjay - Part 1              |          1
 The Hobbit: An Unexpected Journey                  |          1
 Up                                                 |          1
 Pirates of the Caribbean: Dead Man's Chest         |          1
(76 rows)

*****************************************************************

12. The first name, last name, and average runtime of the five
    stars whose movies have the longest average.

SELECT stars.first_name, stars.last_name, AVG(movies.runtime) AS avg_runtime
FROM stars
JOIN roles ON stars.id = roles.star_id
JOIN movies ON roles.movie_id = movies.id
GROUP BY stars.id, stars.first_name, stars.last_name
ORDER BY avg_runtime DESC
LIMIT 5;


/////////////
movies_db=# SELECT stars.first_name, stars.last_name, AVG(movies.runtime) AS avg_runtime
movies_db-# FROM stars
movies_db-# JOIN roles ON stars.id = roles.star_id
movies_db-# JOIN movies ON roles.movie_id = movies.id
movies_db-# GROUP BY stars.id, stars.first_name, stars.last_name
movies_db-# ORDER BY avg_runtime DESC
movies_db-# LIMIT 5;
 first_name |   last_name   |     avg_runtime      
------------+---------------+----------------------
 Kate       | Winslet       | 194.0000000000000000
 Kathy      | Bates         | 194.0000000000000000
 Ian        | McKellen      | 170.4000000000000000
 Morgan     | Freeman       | 157.5000000000000000
 Joseph     | Gordon-Levitt | 154.6666666666666667
(5 rows)


*****************************************************************

13. The first name, last name, and average runtime of the five
    stars whose movies have the longest average, among stars who have more than one movie in the database.

SELECT stars.first_name, stars.last_name, AVG(movies.runtime) AS avg_runtime
FROM stars
JOIN roles ON stars.id = roles.star_id
JOIN movies ON roles.movie_id = movies.id
GROUP BY stars.id, stars.first_name, stars.last_name
HAVING COUNT(movies.id) > 1
ORDER BY avg_runtime DESC
LIMIT 5;



/////////////
movies_db=# SELECT stars.first_name, stars.last_name, AVG(movies.runtime) AS avg_runtime
movies_db-# FROM stars
movies_db-# JOIN roles ON stars.id = roles.star_id
movies_db-# JOIN movies ON roles.movie_id = movies.id
movies_db-# GROUP BY stars.id, stars.first_name, stars.last_name
movies_db-# HAVING COUNT(movies.id) > 1
movies_db-# ORDER BY avg_runtime DESC
movies_db-# LIMIT 5;
 first_name |   last_name   |     avg_runtime      
------------+---------------+----------------------
 Ian        | McKellen      | 170.4000000000000000
 Morgan     | Freeman       | 157.5000000000000000
 Joseph     | Gordon-Levitt | 154.6666666666666667
 Daniel     | Radcliffe     | 148.4285714285714286
 Keira      | Knightley     | 146.7500000000000000
(5 rows)

*****************************************************************

14. The titles of all movies that don't feature any stars in our
    database.

SELECT title
FROM movies
WHERE id NOT IN (
  SELECT movie_id FROM roles
);


//////////////
movies_db=# SELECT title
movies_db-# FROM movies
movies_db-# WHERE id NOT IN (
movies_db(#   SELECT movie_id FROM roles
movies_db(# );
                      title                       
*--------------------------------------------------
 Rogue One: A Star Wars Story
 The Lion King
 Deadpool
 Home Alone
 Transformers: Revenge of the Fallen
 Transformers
 E. T.: The Extra-Terrestrial
 Meet the Fockers
 Wonder Woman
 Batman v Superman: Dawn of Justice
 It
 Man of Steel
 The Twilight Saga: Breaking Dawn Part 2
 Spider-Man 2
 Spider-Man 3
 The Passion of the Christ
 The Twilight Saga: Eclipse
 The Twilight Saga: New Moon
 The Twilight Saga: Breaking Dawn Part 1
 Frozen
 The Sixth Sense
 The Chronicles of Narnia: Lion, Witch & Wardrobe
 Monsters, Inc.
 Monsters University
 Gravity
(25 rows)

*****************************************************************

15. The first and last names of all stars that don't appear in any movies in our database.

SELECT first_name, last_name
FROM stars
WHERE id NOT IN (
  SELECT star_id FROM roles
);


/////////////
movies_db=# SELECT first_name, last_name
movies_db-# FROM stars
movies_db-# WHERE id NOT IN (
movies_db(#   SELECT star_id FROM roles
movies_db(# );
 first_name | last_name 
------------+-----------
 Jim        | Carrey
 Charles    | Chaplin
 Sean       | Connery
 Angelina   | Jolie
 Halle      | Berry
 Mila       | Kunis
 Chris      | Rock
 Wesley     | Snipes
 Jamie      | Foxx
 Charlize   | Theron
(10 rows)

*****************************************************************

16. The first names, last names, and titles corresponding to every
    role in the database, along with every movie title that doesn't have a star, and the first and last names of every star not in a movie.

-- 1. Roles: Stars in movies
SELECT 
  stars.first_name, 
  stars.last_name, 
  movies.title,
  'Role' AS entry_type
FROM roles
JOIN stars ON roles.star_id = stars.id
JOIN movies ON roles.movie_id = movies.id

UNION ALL

-- 2. Movies with no stars
SELECT 
  NULL AS first_name, 
  NULL AS last_name, 
  movies.title,
  'Movie without star' AS entry_type
FROM movies
WHERE id NOT IN (
  SELECT movie_id FROM roles
)

UNION ALL

-- 3. Stars in no movies
SELECT 
  stars.first_name, 
  stars.last_name, 
  NULL AS title,
  'Star without movie' AS entry_type
FROM stars
WHERE id NOT IN (
  SELECT star_id FROM roles
);



///////////
movies_db=# -- 1. Roles: Stars in movies
movies_db=# SELECT 
movies_db-#   stars.first_name, 
movies_db-#   stars.last_name, 
movies_db-#   movies.title,
movies_db-#   'Role' AS entry_type
movies_db-# FROM roles
movies_db-# JOIN stars ON roles.star_id = stars.id
movies_db-# JOIN movies ON roles.movie_id = movies.id
movies_db-# 
movies_db-# UNION ALL
movies_db-# 
movies_db-# -- 2. Movies with no stars
movies_db-# SELECT 
movies_db-#   NULL AS first_name, 
movies_db-#   NULL AS last_name, 
movies_db-#   movies.title,
movies_db-#   'Movie without star' AS entry_type
movies_db-# FROM movies
movies_db-# WHERE id NOT IN (
movies_db(#   SELECT movie_id FROM roles
movies_db(# )
movies_db-# 
movies_db-# UNION ALL
movies_db-# 
movies_db-# -- 3. Stars in no movies
movies_db-# SELECT 
movies_db-#   stars.first_name, 
movies_db-#   stars.last_name, 
movies_db-#   NULL AS title,
movies_db-#   'Star without movie' AS entry_type
movies_db-# FROM stars
movies_db-# WHERE id NOT IN (
movies_db(#   SELECT star_id FROM roles
movies_db(# );
 first_name  |   last_name   |                       title                        |     entry_type     
-------------+---------------+----------------------------------------------------+--------------------
 Frances     | McDormand     | Transformers: Dark of the Moon                     | Role
 Emma        | Watson        | Beauty and the Beast                               | Role
 Emma        | Watson        | Harry Potter and the Sorcerer's Stone              | Role
 Emma        | Watson        | Harry Potter and the Half-Blood Prince             | Role
 Emma        | Watson        | Harry Potter and the Order of the Phoenix          | Role
 Emma        | Watson        | Harry Potter and the Goblet of Fire                | Role
 Emma        | Watson        | Harry Potter and the Chamber of Secrets            | Role
 Emma        | Watson        | Harry Potter and the Deathly Hallows: Part 2       | Role
 Emma        | Watson        | Harry Potter and the Deathly Hallows: Part 1       | Role
 Daniel      | Radcliffe     | Harry Potter and the Deathly Hallows: Part 2       | Role
 Daniel      | Radcliffe     | Harry Potter and the Sorcerer's Stone              | Role
 Daniel      | Radcliffe     | Harry Potter and the Half-Blood Prince             | Role
 Daniel      | Radcliffe     | Harry Potter and the Deathly Hallows: Part 1       | Role
 Daniel      | Radcliffe     | Harry Potter and the Order of the Phoenix          | Role
 Daniel      | Radcliffe     | Harry Potter and the Goblet of Fire                | Role
 Daniel      | Radcliffe     | Harry Potter and the Chamber of Secrets            | Role
 Morgan      | Freeman       | The Dark Knight                                    | Role
 Morgan      | Freeman       | The Dark Knight Rises                              | Role
 Will        | Smith         | Suicide Squad                                      | Role
 Will        | Smith         | Independence Day                                   | Role
 Cameron     | Diaz          | Shrek 2                                            | Role
 Cameron     | Diaz          | Shrek the Third                                    | Role
 Cameron     | Diaz          | Shrek                                              | Role
 Kate        | Winslet       | Titanic                                            | Role
 Natalie     | Portman       | Star Wars: Episode I - The Phantom Menace          | Role
 Natalie     | Portman       | Star Wars: Episode III - Revenge of the Sith       | Role
 Natalie     | Portman       | Star Wars: Episode II - Attack of the Clones       | Role
 Dwayne      | Johnson       | Jumanji: Welcome to the Jungle                     | Role
 Dwayne      | Johnson       | Furious 7                                          | Role
 Scarlett    | Johansson     | Marvel's The Avengers                              | Role
 Scarlett    | Johansson     | Avengers: Age of Ultron                            | Role
 Scarlett    | Johansson     | Captain America: Civil War                         | Role
 Scarlett    | Johansson     | The Jungle Book                                    | Role
 Scarlett    | Johansson     | Iron Man 2                                         | Role
 Scarlett    | Johansson     | Sing                                               | Role
 Keira       | Knightley     | Star Wars: Episode I - The Phantom Menace          | Role
 Keira       | Knightley     | Pirates of the Caribbean: Dead Man's Chest         | Role
 Keira       | Knightley     | Pirates of the Caribbean: At World's End           | Role
 Keira       | Knightley     | Pirates of the Caribbean: Curse of the Black Pearl | Role
 Samuel      | Jackson       | Marvel's The Avengers                              | Role
 Samuel      | Jackson       | Star Wars: Episode I - The Phantom Menace          | Role
 Samuel      | Jackson       | Avengers: Age of Ultron                            | Role
 Samuel      | Jackson       | Jurassic Park                                      | Role
 Samuel      | Jackson       | Star Wars: Episode III - Revenge of the Sith       | Role
 Samuel      | Jackson       | Iron Man                                           | Role
 Samuel      | Jackson       | Iron Man 2                                         | Role
 Samuel      | Jackson       | Star Wars: Episode II - Attack of the Clones       | Role
 Samuel      | Jackson       | The Incredibles                                    | Role
 Tom         | Hanks         | Toy Story 3                                        | Role
 Tom         | Hanks         | Forrest Gump                                       | Role
 Tom         | Hanks         | Toy Story 2                                        | Role
 Christopher | Plummer       | Up                                                 | Role
 Jennifer    | Lawrence      | The Hunger Games: Catching Fire                    | Role
 Jennifer    | Lawrence      | The Hunger Games                                   | Role
 Jennifer    | Lawrence      | The Hunger Games: Mockingjay - Part 1              | Role
 Jennifer    | Lawrence      | The Hunger Games: Mockingjay - Part 2              | Role
 Kathy       | Bates         | Titanic                                            | Role
 Harrison    | Ford          | Star Wars: The Force Awakens                       | Role
 Harrison    | Ford          | Star Wars                                          | Role
 Harrison    | Ford          | Indiana Jones & Kingdom of the Crystal Skull       | Role
 Harrison    | Ford          | Return of the Jedi                                 | Role
 Harrison    | Ford          | The Empire Strikes Back                            | Role
 Viola       | Davis         | Suicide Squad                                      | Role
 Bradley     | Cooper        | Guardians of the Galaxy Vol. 2                     | Role
 Bradley     | Cooper        | American Sniper                                    | Role
 Bradley     | Cooper        | Guardians of the Galaxy                            | Role
 Bradley     | Cooper        | The Hangover                                       | Role
 Amy         | Poehler       | Inside Out                                         | Role
 Amy         | Poehler       | Shrek the Third                                    | Role
 Joseph      | Gordon-Levitt | Star Wars: The Last Jedi                           | Role
 Joseph      | Gordon-Levitt | The Dark Knight Rises                              | Role
 Joseph      | Gordon-Levitt | Inception                                          | Role
 Danai       | Gurira        | Black Panther                                      | Role
 Angela      | Bassett       | Black Panther                                      | Role
 Ian         | McKellen      | Beauty and the Beast                               | Role
 Ian         | McKellen      | The Lord of the Rings: Return of the King          | Role
 Ian         | McKellen      | The Lord of the Rings: The Two Towers              | Role
 Ian         | McKellen      | The Lord of the Rings: Fellowship of the Ring      | Role
 Ian         | McKellen      | The Hobbit: An Unexpected Journey                  | Role
 Maya        | Rudolph       | Shrek the Third                                    | Role
 Jenny       | Slate         | The Secret Life of Pets                            | Role
 Jenny       | Slate         | Zootopia                                           | Role
 Jenny       | Slate         | Despicable Me 3                                    | Role
 Idris       | Elba          | Finding Dory                                       | Role
 Idris       | Elba          | Avengers: Age of Ultron                            | Role
 Idris       | Elba          | The Jungle Book                                    | Role
 Idris       | Elba          | Zootopia                                           | Role
 Idris       | Elba          | Thor: Ragnarok                                     | Role
 Octavia     | Spencer       | Spider-Man                                         | Role
 Octavia     | Spencer       | Zootopia                                           | Role
 Chadwick    | Boseman       | Black Panther                                      | Role
 Chadwick    | Boseman       | Captain America: Civil War                         | Role
 Michael     | Keaton        | Toy Story 3                                        | Role
 Michael     | Keaton        | Minions                                            | Role
 Michael     | Keaton        | Spider-Man: Homecoming                             | Role
 Kristen     | Wiig          | Despicable Me 2                                    | Role
 Kristen     | Wiig          | Despicable Me 3                                    | Role
 Keanu       | Reeves        | The Matrix Reloaded                                | Role
 Helena      | Carter        | Harry Potter and the Deathly Hallows: Part 2       | Role
 Helena      | Carter        | Alice in Wonderland                                | Role
 Helena      | Carter        | Harry Potter and the Half-Blood Prince             | Role
 Helena      | Carter        | Harry Potter and the Deathly Hallows: Part 1       | Role
 Helena      | Carter        | Harry Potter and the Order of the Phoenix          | Role
 Daniel      | Craig         | Star Wars: The Force Awakens                       | Role
 Daniel      | Craig         | Skyfall                                            | Role
 Emma        | Stone         | The Amazing Spider-Man                             | Role
 Zoe         | Saldana       | Avatar                                             | Role
 Zoe         | Saldana       | Guardians of the Galaxy Vol. 2                     | Role
 Zoe         | Saldana       | Guardians of the Galaxy                            | Role
 Zoe         | Saldana       | Pirates of the Caribbean: Curse of the Black Pearl | Role
 Chris       | Pratt         | Jurassic World                                     | Role
 Chris       | Pratt         | Star Wars                                          | Role
 Chris       | Pratt         | Guardians of the Galaxy Vol. 2                     | Role
 Chris       | Pratt         | Guardians of the Galaxy                            | Role
 Anne        | Hathaway      | The Dark Knight Rises                              | Role
 Anne        | Hathaway      | Alice in Wonderland                                | Role
 Ellen       | DeGeneres     | Finding Dory                                       | Role
 Ellen       | DeGeneres     | Finding Nemo                                       | Role
 Robert      | Downey Jr.    | Marvel's The Avengers                              | Role
 Robert      | Downey Jr.    | Avengers: Age of Ultron                            | Role
 Robert      | Downey Jr.    | Iron Man 3                                         | Role
 Robert      | Downey Jr.    | Captain America: Civil War                         | Role
 Robert      | Downey Jr.    | Spider-Man: Homecoming                             | Role
 Robert      | Downey Jr.    | Iron Man                                           | Role
 Robert      | Downey Jr.    | Iron Man 2                                         | Role
             |               | Rogue One: A Star Wars Story                       | Movie without star
             |               | The Lion King                                      | Movie without star
             |               | Deadpool                                           | Movie without star
             |               | Home Alone                                         | Movie without star
             |               | Transformers: Revenge of the Fallen                | Movie without star
             |               | Transformers                                       | Movie without star
             |               | E. T.: The Extra-Terrestrial                       | Movie without star
             |               | Meet the Fockers                                   | Movie without star
             |               | Wonder Woman                                       | Movie without star
             |               | Batman v Superman: Dawn of Justice                 | Movie without star
             |               | It                                                 | Movie without star
             |               | Man of Steel                                       | Movie without star
             |               | The Twilight Saga: Breaking Dawn Part 2            | Movie without star
             |               | Spider-Man 2                                       | Movie without star
             |               | Spider-Man 3                                       | Movie without star
             |               | The Passion of the Christ                          | Movie without star
             |               | The Twilight Saga: Eclipse                         | Movie without star
             |               | The Twilight Saga: New Moon                        | Movie without star
             |               | The Twilight Saga: Breaking Dawn Part 1            | Movie without star
             |               | Frozen                                             | Movie without star
             |               | The Sixth Sense                                    | Movie without star
             |               | The Chronicles of Narnia: Lion, Witch & Wardrobe   | Movie without star
             |               | Monsters, Inc.                                     | Movie without star
             |               | Monsters University                                | Movie without star
             |               | Gravity                                            | Movie without star
 Jim         | Carrey        |                                                    | Star without movie
 Charles     | Chaplin       |                                                    | Star without movie
 Sean        | Connery       |                                                    | Star without movie
 Angelina    | Jolie         |                                                    | Star without movie
 Halle       | Berry         |                                                    | Star without movie
 Mila        | Kunis         |                                                    | Star without movie
 Chris       | Rock          |                                                    | Star without movie
 Wesley      | Snipes        |                                                    | Star without movie
 Jamie       | Foxx          |                                                    | Star without movie
 Charlize    | Theron        |                                                    | Star without movie
(160 rows)
