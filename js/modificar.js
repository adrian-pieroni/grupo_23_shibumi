const URL = "http://localhost:4000"

const queryString = window.location.search; // Obtener la query string de la URL
const urlParams = new URLSearchParams(queryString); // Obtener los parámetros de la query string

const id = urlParams.get('id'); // Obtener el código del producto

fetch(URL + '/prueba/' + id) // Obtener el producto
.then(res => res.json()) // Convertir la respuesta a JSON
.then(data => { // Mostrar los datos en consola
    console.log(data);
    document.getElementById('id').value = data[0];
    document.getElementById('nombre').value = data[1];
    document.getElementById('apellido').value = data[2];
    document.getElementById('edad').value = data[3];
    document.getElementById('calle').value = data[4];
    document.getElementById('numero').value = data[5];
    document.getElementById('ciudad').value = data[6];
    document.getElementById('provincia').value = data[7];
    document.getElementById('pais').value = data[8];
    document.getElementById('codpos').value = data[9];
    document.getElementById('tel').value = data[10];
    document.getElementById('prefer').value = data[11];

});

const documento = document.getElementById('formulario');

documento.addEventListener('submit', e => {
    e.preventDefault();

    const formData = new FormData(documento); // Obtener los datos del formulario

    fetch(URL + '/prueba/' + id, { // Enviar los datos al servidor
        method: 'POST', // Metodo de envio
        body: formData // Los datos del formulario
    })
     .then(res => res.json()) // Convertir la respuesta a JSON
     .then(data => { // Mostrar los datos en consola
        console.log(data);
        alert('Registro modificado correctamente');
        window.location.reload(); // Recargar la página
    })
})
