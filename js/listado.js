const URL = "http://localhost:4000"



fetch(URL + '/prueba') // Obtener los productos
    .then(res => res.json()) // Convertir la respuesta a JSON
    .then(data => { // Mostrar los datos en consola
       let html = ''; // Variable para guardar el HTML

       data.forEach(element => {
        //Bucktick `` para concatenar , interpolacion de variables ${}
        html = html + `<tr>
            <td>${element[0]}</td>
            <td>${element[1]}</td>
            <td>${element[2]}</td>
            <td>${element[3]}</td>
            <td>${element[4]}</td>
            <td>${element[5]}</td>
            <td>${element[6]}</td>
            <td>${element[7]}</td>
            <td>${element[8]}</td>
            <td>${element[9]}</td>
            <td>${element[10]}</td>
            <td>${element[11]}</td>
            <td><a href="modificar.html?id=${element[0]}">Modificar</a></td>
            <td><button class="alert" onclick="eliminar(${element[0]});">Eliminar</button></td>
        </tr>`;
       });
       document.getElementById('registrados').innerHTML = html;
    });


function eliminar(id){

    fetch(URL + '/prueba/' + id, { // Hago la petición a la API para eliminar el producto
        method: 'DELETE' // Indico el método HTTP
    }).then(res => res.json()) // Convierto la respuesta a JSON
    .then(data => {
        console.log(data); // Muestro los datos en consola
        alert('registro: ' + id); // Muestro un mensaje al usuario
        window.location.reload(); // Recargo la página
    });


}