$(function(){
  $('#next').click(function(){
    let h2 = $('<h2>').text('Cat Name Goes Here');
    let img = $('<img width="90%"><hr/>');
    $('#list')
        .prepend(img)
        .prepend(h2);
    $.getJSON('http://localhost:8000/api/next/')
    .done(function(json) {
      h2.text(json.name);
      img.prop('src', json.image);

    });
  });

  $('#reset').click(function(){

    let token = $('input[name="csrfmiddlewaretoken"]').val();

    $.post('http://localhost:8000/api/reset/', {
      'csrfmiddlewaretoken': token
    });
    $('#list').empty();

  })
});
