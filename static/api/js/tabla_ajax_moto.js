function tablaMotorizado(){
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
		            "url": "/plataforma/motorizado/search/moto/"

		        },
		        "drawCallback": function (row, data) {
		           	//funciones a cargar luego de el llamado
		        },
		        "columns": [
		            {
		                "data": "placa"
		            },
		            {
		                "data": "tipo"
		            },
		            {
		            	"data":"marca"
		            },
		            {
		                "data": "t_propiedad"
		            },
		            {
		                "data": "numeroS"
		            },
		            {
		                "data": "numeroT"
		            },
		            {
		            	"className":"left aligned",
		                "data": "id",
		                "render": function ( data, type, full, meta ) {
		                	var m="";
		                	m="<a href=\"/plataforma/motorizado/moto/"+data+"/details/\" class=\"ui icon green\"><i class=\"unhide large green icon\"></i></a>";
		                	m+="<a href=\"/plataforma/motorizado/moto/"+data+"/edit/\" class=\"ui icon green \"><i class=\"express-editar large green icon\"></i></a>";
		                	m+="<a id=\"eliminar\" href=\"/plataforma/motorizado/delete/"+data+"/\" class=\"ui icon green\"><i class=\"trash outline large red icon\"></i></a>";
		                	return m;
						}
		            }
		        ]
		    });
		}
		function hides(){
			$('#search-results_filter,#dataTables_length').hide();
		}
		tablaMotorizado();
		init();
		window.onload = hides;