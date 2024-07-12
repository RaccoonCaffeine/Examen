$(document).ready(function() {
    $('#random').on('click', function() {
        $.ajax({
            url: '/rdn/',  // Debe coincidir con el nombre definido en urls.py
            type: 'GET',
            success: function(data) {
                // Actualizar la sección de libros random con los nuevos datos
                $('#libros-random').html(data);
            },
            error: function(xhr, status, error) {
                console.error('Error al regenerar libros random:', error);
            }
        });
    });
});
