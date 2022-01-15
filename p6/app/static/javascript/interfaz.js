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

function obtener(){
  pokemon = {
    "id": parseInt($("#id").val()),
  }

  $.ajax({
    type: "POST",
    url: "/pokemon_get_p6/"+pokemon['id'],
    dataType: "json",
    data: JSON.stringify(pokemon),
    success: function(msg){
      alert(msg['estado'])

      if (msg['codigo'] < 300){
        var datos = msg['pokemon'].split(',');
        datos = datos.slice(1, datos.length)

        var suprimir = 5
        for(var i = 0; i < datos.length-suprimir; i++){
          var aux = datos[i].split(':')
          if (aux[0].includes("id")){
            aux[1] = parseInt(aux[1])
          }
          if (aux[0].includes("height") || aux[0].includes("weight")){
            aux[1] = parseFloat(aux[1])
          }

          document.getElementById("informacion").innerHTML += aux[0] + " " + aux[1] + "<br>"
        }
      }
    }
  })
}