function tablaMotos(){
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
		            "url": "/plataforma/motorizado/search/motorizado/"

		        },
		        "drawCallback": function (row, data) {
		           	//funciones a cargar luego de el llamado
		        },
		        "columns": [
		            {
		                "data": "ident"
		            },
		            {
		                "data": "nom"
		            },
		            {
		            	"data":"ape"
		            },
		            {
		                "data": "placa",
		                "render": function ( data, type, full, meta ) {
		                	var m="";
		                	m="<a href=\"/plataforma/motorizado/moto/"+full.id_mot+"/details/\">"+data+"</a>";
		                	return m;
						}
		            },
		            {
		                "data": "gps"
		            },
		            {
		            	"className":"left aligned",
		                "data": "id_emp",
		                "render": function ( data, type, full, meta ) {
		                	var m="";
		                	m="<a href=\"/plataforma/motorizado/"+data+"/edit/\" class=\"ui icon green\"><i class=\"express-editar large green icon\"></i></a>";
		                	return m;
						}
		            }
		        ]
		    });
		}
		function hides(){
			$('#search-results_filter,#dataTables_length').hide();
		}
		tablaMotos();
		init();
		window.onload = hides;