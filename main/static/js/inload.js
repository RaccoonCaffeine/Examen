document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById("buscar");

    form.addEventListener("submit", function(event) {
        // Mostrar la alerta de carga
        Swal.fire({
            title: 'Cargando...',
            text: 'Por favor espera mientras se realiza la búsqueda',
            allowOutsideClick: false,
            didOpen: () => {
                Swal.showLoading();
            }
        });
    });
});