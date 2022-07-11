
// document.addEventListener("DOMContentLoaded", function() {
// document.getElementById("formularios").addEventListener('submit', alert); 

// });


function alert(titulo, texto, icon) {

    // var nombre = document.getElementById("name");
    // var actividades = document.getElementById("activity") ;
    Swal.fire({
        title: titulo,
        text: texto,
        icon: icon,
        confirmButtonText: 'Ok',
    }).then((result) => {
        if (result.isConfirmed) {
            // navigateByUrl('home');
        }
    });

    // this.submit();

}

function zfill(number, width) {
    var numberOutput = Math.abs(number); /* Valor absoluto del número */
    var length = number.toString().length; /* Largo del número */ 
    var zero = "0"; /* String de cero */  
    
    if (width <= length) {
        if (number < 0) {
             return ("-" + numberOutput.toString()); 
        } else {
             return numberOutput.toString(); 
        }
    } else {
        if (number < 0) {
            return ("-" + (zero.repeat(width - length)) + numberOutput.toString()); 
        } else {
            return ((zero.repeat(width - length)) + numberOutput.toString()); 
        }
    }
}


function fecha(){
    let dias = document.getElementById("txtDias").value;
    let fecha = document.getElementById("txtFechaIn").value;
    

    var res = new Date(fecha);
    res.setDate(res.getDate() + parseInt(dias) + 1);
    
    let mes =  parseInt(res.getMonth()) + parseInt(1)

    let mes2 = 0

    if (mes <= parseInt(12)){
        mes2 =  parseInt(res.getMonth()) + parseInt(1)

    }else{

        mes2 =  parseInt(res.getMonth())
    }

    
    let text = res.getFullYear().toString() +"-"+zfill(mes2, 2) +"-"+zfill(res.getDate(), 2);
    document.getElementById("txtFechaFin").value = text;
    // console.log(text)

}

function consumirServideo(ruta, token){

    const userAction = async () => {
        const response = await fetch(ruta, {
          method: 'GET',
          //body: json, // string or object
          headers: {
            'Authorization': 'Token '+ token.toString()
          }
        });
        const myJson = await response.json(); //extract JSON from the http response
        // do something with myJson
        // console.log(myJson)
      }

    userAction()
}

function cambiarActividad(idActividad, h, ruta, token ){
    
    let value =  document.getElementById('btnTerminar'+ h.toString()).value;

    if (value == 'Falso'){

        consumirServideo(ruta+idActividad, token)
        
        document.getElementById('btnTerminar'+ h.toString()).className = 'btn btn-info mr-2';
        document.getElementById('btnTerminar'+ h.toString()).textContent = 'Terminar';
        document.getElementById('btnTerminar'+ h.toString()).value = "Verdadero";

    }
    else{
        consumirServideo(ruta+idActividad, token)

        document.getElementById('btnTerminar'+ h.toString()).className = 'btn btn-warning mr-2';
        document.getElementById('btnTerminar'+ h.toString()).textContent = 'Activar';
        document.getElementById('btnTerminar'+ h.toString()).value = "Falso";

        
    }
    

}


  