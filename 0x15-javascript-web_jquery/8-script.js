// Queries an API and fetches all movie titles then inserts them
// into the UL#list_movies tag

const url = 'https://swapi.co/api/films/?format=json';
$.get(url, function (data) {
  const films = data.results;
  for (const film of films) {
    $('ul#list_movies').append(`<li>${film.title}</li>`);
  }
});
