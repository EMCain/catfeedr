$(function(){
  $('#next').click(function(){
    $.getJSON('http://localhost:8000/api/next/')
    .done(function(json) {
      let h2 = $('<h2>')
        .text(json.name);
      let img =('<img>')
        .attr('src', json.image);
      $('#list')
        .prepend(h2)
        .prepend(img);
    })
    .fail(function() {
      alert("error");
    })
  });
});
