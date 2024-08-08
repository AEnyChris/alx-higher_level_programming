$.getJSON('https://swapi-api.alx-tools.com/api/people/2/?format=json', function (data) {
  $('DIV#character').text(data.name);
});
