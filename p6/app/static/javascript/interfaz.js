$(function(){                          // jQuery function

    $('#boton').click(function() {
      console.log("hola")
    });
 });

function modificar(){
  pokemon = {
    "id": parseInt($("#id").val()),
    "name": $("#name").val(),
    "img": $("#img").val(),
    "type": $("#type").val(),
    "height": parseFloat($("#height").val()),
    "weight": parseFloat($("#weight").val()),
    "candy": $("#candy").val(),
    "egg": $("#egg").val(),
  }

  $.ajax({
    type: "PUT",
    url: "/pokemon/"+pokemon["id"],
    dataType: "json",
    data: JSON.stringify(pokemon),
    success: function(msg){
      alert(msg['estado'])
    }
  })
  console.log("/pokemon/"+pokemon["id"])
}

function crear(){
  pokemon = {
    "name": $("#name").val(),
    "img": $("#img").val(),
    "type": $("#type").val(),
    "height": parseFloat($("#height").val()),
    "weight": parseFloat($("#weight").val()),
    "candy": $("#candy").val(),
    "egg": $("#egg").val(),
  }
  console.log(pokemon)

  $.ajax({
    type: "POST",
    url: "/pokemon",
    dataType: "json",
    data: JSON.stringify(pokemon),
    success: function(msg){
      alert(msg['estado'])
    }
  })
}

function borrar(){
  pokemon = {
    "id": parseInt($("#id").val()),
  }

  $.ajax({
    type: "DELETE",
    url: "/pokemon/"+pokemon['id'],
    dataType: "json",
    data: JSON.stringify(pokemon),
    success: function(msg){
      alert(msg['estado'])
    }
  })
}