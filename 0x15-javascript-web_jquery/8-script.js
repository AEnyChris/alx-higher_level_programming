$.getJSON('https://swapi-api.alx-tools.com/api/films/?format=json', function (data)
  for (const n in data.results)
    $('UL#list_movies').append(`<li>${data.results[n].title}</li>`);
});
