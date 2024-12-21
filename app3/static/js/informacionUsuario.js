
function cargarPub(idPub)
{
    fetch(`/devolverPublicacion?idPub=${idPub}`)
    .then(response => response.json())
    .then(data => {
        tituloPub = document.getElementById('tituloPub')
        autorPub = document.getElementById('autorPub')
        descripcionPub = document.getElementById('descripcionPub')
        idPublicacion = document.getElementById('idPublicacion')
        comentariosTotales = document.getElementById('comentariosTotales')

        imagenPub = document.getElementById('imagenPub')

        if(data.imgPub !== null)
        {
            imagenPub.src = `data:image/jpeg;base64,${data.imgPub}`
            imagenPub.style.display = 'block'
        }
        else
        {
            imagenPub.style.display = 'none'
        }

        tituloPub.value = ''
        autorPub.value = ''
        descripcionPub.value = ''
        idPublicacion.innerHTML = ''
        comentariosTotales.innerHTML = ''

        tituloPub.value = data.titulo
        autorPub.value = data.autor
        descripcionPub.value = data.descripcion
        idPublicacion.innerHTML = String(idPub)

        for(let j = 0; j < data.datosComentarios.length; j++)
        {
            seccionComentario = `
            <div class="row mb-3">
                <div class="col-3">
                    ${data.datosComentarios[j].autor}
                </div>
                <div class="col-9">
                    ${data.datosComentarios[j].descripcion}
                </div>
            </div>
            `
            comentariosTotales.innerHTML = comentariosTotales.innerHTML + seccionComentario
        }
    })
}

function enviarComentario()
{
    comentarioUsuario = document.getElementById('comentarioUsuario')
    idPublicacion = document.getElementById('idPublicacion')

    datos = {
        'comentario':comentarioUsuario.value,
        'idPublicacion': idPublicacion.innerHTML
    }

    fetch('/publicarComentario',
    {
        method:"POST",
        headers:
        {
            "X-Requested-With": "XMLHttpRequest",
            "X-CSRFToken": getCookie("csrftoken"),
        },
        body:JSON.stringify(datos)
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('comentarioUsuario').value = ''
        cargarPub(idPublicacion.innerHTML)
    })
}

function getCookie(name)
{
    let cookieValue = null;
    if (document.cookie && document.cookie !== "")
    {
        const cookies = document.cookie.split(";");
        for (let i = 0; i < cookies.length; i++)
        {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + "="))
            {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function cargarInformacionUsuario(idUsuario)
{
    // Llamar a la función del backend usando fetch
    fetch(`/obtenerDatosUsuario?idUsuario=${idUsuario}`)
        .then(response => response.json())
        .then(data => {
            if (data.resp === '200') {
                // Aquí puedes llenar el modal con los datos recibidos
                
                idUsuario1 = document.getElementById('idUsuario')
                username = document.getElementById('usernameUsuario')
                first_name = document.getElementById('nombreUsuario')
                last_name = document.getElementById('apellidoUsuario')
                nroCelular = document.getElementById('nroCelular')
                email = document.getElementById('emailUsuario')
                profesion = document.getElementById('profesionUsuario')

                idUsuario1.value = ''
                username.value = ''
                first_name.value = ''
                last_name.value = ''
                nroCelular.value = ''
                email.value = ''
                profesion.value = ''
                
                idUsuario1.value = String(idUsuario)
                username.value = data.username
                first_name.value = data.first_name
                last_name.value = data.last_name
                nroCelular.value = data.nroCelular
                email.value = data.email
                profesion.value = data.profesion

            } else {
                console.error("Error al obtener los datos del usuario.");
            }
        })
        .catch(error => {
            console.error("Error en la solicitud:", error);
        });
}