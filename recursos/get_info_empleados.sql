create or replace function get_info_empleados_report(id_emp integer,fecha1 text,fecha2 text) returns json as $$
declare 
	emp json;
	dat json;
begin
	SELECT COALESCE(array_to_json(array_agg(row_to_json(p))), '[]') from (
		select u.identificacion as iden,a.first_name||' '||a.last_name as nom,e.direccion as dir,
			'Tel : '||u.telefono_fijo||'-'||u.telefono_celular,a.email as correo 
			from domicilios_empleado as e 
			inner join domicilios_usuario as u on (e.usuario_ptr_id=u.user_ptr_id) 
			inner join auth_user as a on(a.id=u.user_ptr_id and a.id=id_emp) limit 1
	) p into emp; 
	SELECT COALESCE(array_to_json(array_agg(row_to_json(p))), '[]') from (
		select cliente,total,direccion,motori,alistar,despacho,entrega from pedidos_tiempos where fecha BETWEEN fecha1 AND fecha2
	) p into dat;
	return (array_to_json(array_agg(row_to_json(row(emp,dat)))));
end;
$$language plpgsql;
