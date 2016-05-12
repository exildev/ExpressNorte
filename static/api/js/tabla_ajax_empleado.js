function tablaEmpleado(){
			window.table = $('#search-results').DataTable({
		        "bPaginate": true,
		        "bScrollCollapse": true,
		        "sPaginationType": "full_numbers",
		        "bRetrieve": true,
		        "oLanguage": {
		            "sProcessing": "Procesando...",
		            "sLengthMenu": "Mostrar _MENU_ Registros",
		            "sZeroRecords": "No se encontraron resultados",
		            "sInfo": "Mostrando desde _START_ hasta _END_ de _TOTAL_ Registros",
		            "sInfoEmpty": "Mostrando desde 0 hasta 0 de 0 Registros",
		            "sInfoFiltered": "(filtrado de _MAX_ registros en total)",
		            "sInfoPostFix": "",
		            "sSearch": "Buscar:",
		            "sUrl": "",
		            "oPaginate": {
		                "sFirst": "|<<",
		                "sPrevious": "<<",
		                "sNext": ">>",
		                "sLast": ">>|"
		            }
		        },
		        "processing": true,
		        "serverSide": true,
		        "ajax": {
		            "url": "/plataforma/users/empleado/search/empleado/"
 
		        },
		        "drawCallback": function (row, data) {
		           	//funciones a cargar luego de el llamado
		        },
		        "columns": [
		            {
		                "data": "nom"
		            },
		            {
		                "data": "ape"
		            },
		            {
		            	"data":"ced"
		            },
		            {
		                "data": "cargo"
		            },
		            {
		                "data": "first_name"
		            },
		            {
		                "data": "estado"
		            },
		            {
		            	"className":"right aligned",
		                "data": "usuario_ptr_id",
		                "render": function ( data, type, full, meta ) {
		                	var m="";
		                	m="<a href=\"/plataforma/users/empleado/info/"+data+"/empleado/\" class=\"ui icon green\"><i class=\"unhide large green icon\"></i></a>";
		                	m+="<a href=\"/plataforma/users/empleado/edit/"+data+"/info/\" class=\"ui icon green\"><i class=\"express-editar large green icon\"></i></a>";
		                	m+="<a href=\"/plataforma/users/empleado/change/"+data+"/status/\" class=\"ui icon red\"><i class=\"express-denegado large red icon\"></i></a>";
		                	return m;
						}
		            }
		        ]
		    });
		}
		function hides(){
			$('#search-results_filter,#dataTables_length').hide();
		}
		tablaEmpleado();
		init();
		window.onload = hides;




