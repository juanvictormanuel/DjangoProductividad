function agregarFila(){
    document.getElementById("DataTable").insertRow(-1).innerHTML = '<td>asas</td><td>asas</td><td>asas</td><td>asas</td><td>asas</td>';
  }
  
  function eliminarFila(){
    var table = document.getElementById("DataTable");
    var rowCount = table.rows.length;
    // console.log(rowCount);
    
    if(rowCount <= 1)
      alert('No se puede eliminar el encabezado');
    else
      table.deleteRow(rowCount -1);
  }

  