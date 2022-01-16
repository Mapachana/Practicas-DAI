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

        // Cojo los datos del pokemon
        datos = msg['pokemon'].split(',')
        id = datos[0].split(":")[1]
        nombre = datos[1].split(":")[1]
        aux_img = datos[2].split(":")
        img = ""
        for(j=1; j<aux_img.length; j++){
          img += aux_img[j]
          if (j < aux_img.length-1)
            img+=":"
        }
        type = datos[3].split(":")[1]
        height = datos[4].split(":")[1]
        weight = datos[5].split(":")[1]
        console.log(datos)

          document.getElementById("informacion").innerHTML = "<ul><li>Id: "+id+"</li><li>Tipo:"+type+"</li><li>Altura:"+height+"</li><li>Peso: "+weight+"</li></ul>"
        
      }
    }
  })
}

function buscar(){
  texto = $("#texto").val()

  if (texto != ""){
    $.ajax({
      type: "POST",
      url: "/pokemon_get_nombre_p6/"+texto,
      dataType: "json",
      data: JSON.stringify(texto),
      success: function(msg){
        alert(msg['estado'])
        document.getElementById("lista").innerHTML = ""
  
  
        if (msg['codigo'] < 300){
          var lista_datos = msg['lista_pokemon'];
          var datos = []
  
          for(i=0; i < lista_datos.length; i++){
            // Cojo los datos del pokemon
            datos = lista_datos[i].split(',')
            id = datos[0].split(":")[1]
            nombre = datos[1].split(":")[1]
            aux_img = datos[2].split(":")
            img = ""
            for(j=1; j<aux_img.length; j++){
              img += aux_img[j]
              if (j < aux_img.length-1)
                img+=":"
            }
            type = datos[3].split(":")[1]
            height = datos[4].split(":")[1]
            weight = datos[5].split(":")[1]

  
  
            // Imprimo el html con la info
            informacion = ""
            
            informacion += "<div>"
            informacion += "<h4>" + nombre +"</h4>"
            informacion += '<div class="d-flex flex-row flex-shrink-0">'
            informacion += '<img src="'+ img + '" width="128" height="128" class="rounded-circle me-2">'
            informacion += "<ul>"
            informacion += "<li>Id: "+id+"</li><li>Tipo:"+type+"</li><li>Altura:"+height+"</li><li>Peso: "+weight+"</li>"
            informacion += "</ul>"
            informacion += "</div>"
            informacion += ' <a  class="btn btn btn-dark text-center" href="modificar_pokemon/'+id+'">Modificar pokemon</a>'
            informacion += '<a  class="btn btn btn-dark text-center" href="borrar_pokemon/'+id+'">Borrar pokemon</a>'
            informacion += '<a  class="btn btn btn-dark text-center" href="obtener_pokemon/'+id+'">Detalles pokemon</a>'
            informacion += "</div>"
            document.getElementById("lista").innerHTML += informacion
          }
      
        }
      }
    })
  }

  
}



function modo_noche(){
  if (document.getElementById("contenido").classList.contains('bg-light')){
    $("#contenido").removeClass('bg-light text-white').addClass('bg-secondary text-white');
  }
  else{
    $("#contenido").removeClass('bg-secondary text-white').addClass('bg-light text-black');
  }

}


function aumentar_tamanio(){
  tamanio_actual = parseFloat(getComputedStyle(document.body).getPropertyValue('font-size'))
  
  var constante = 2
  var tamanio_nuevo = tamanio_actual + constante

  $('body').css("font-size", tamanio_nuevo)
}

function disminuir_tamanio(){
  tamanio_actual = parseFloat(getComputedStyle(document.body).getPropertyValue('font-size'))
  
  var constante = 2
  var tamanio_nuevo = tamanio_actual - constante

  if (tamanio_nuevo < 4){
    tamanio_nuevo = 4
  }
  
  $('body').css("font-size", tamanio_nuevo)
}