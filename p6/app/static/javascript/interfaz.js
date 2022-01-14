$(function(){                          // jQuery function

    $('#boton').click(function() {
      console.log("hola")
    });
 });

function modificar(){
  pokemon = {
    "id": parseInt($("#id").val()),
    "name": $("#name").val(),
    "height": parseFloat($("#height").val()),
    "img" :"https://avatars.githubusercontent.com/u/32956016?v=4", "type" :"Water",  "weight" :45, "candy" :"Porfa", "egg" :"frito"
  }

  $.ajax({
    type: "PUT",
    url: "/pokemon/"+pokemon["id"],
    dataType: "json",
    data: JSON.stringify(pokemon),
    success: function(msg){
      console.log(msg)
    }
  })
  console.log("/pokemon/"+pokemon["id"])
}