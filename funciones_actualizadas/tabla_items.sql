-- Function: tabla_items(integer, text, text, integer, integer)

-- DROP FUNCTION tabla_items(integer, text, text, integer, integer);

CREATE OR REPLACE FUNCTION tabla_items(id_des integer, search_ text, order_ text, start_ integer, length_ integer)
  RETURNS text AS
$BODY$
declare 
	l json;
	t integer;
	id_emp integer :=0;
begin
	select empresa_id from domicilios_empleado where usuario_ptr_id = 14 limit 1 into id_emp;
	if id_emp is null then
		id_emp=0;
	end if;
	select count(id) from domicilios_items where "empresaI_id"=id_emp into t;
	SELECT COALESCE(array_to_json(array_agg(row_to_json(p))), '[]') from (
		 select codigo,initcap(descripcion) as descripcion,initcap(presentacion) as presentacion,id from domicilios_items where "empresaI_id"=id_emp and
		 (codigo like '%'||search_||'%' or descripcion like '%'||search_||'%' or presentacion like '%'||search_||'%') limit length_ offset start_
	) p into l;
	return '{"recordsFiltered": '|| t ||', "recordsTotal": '|| t ||', "data": '|| l||'}';
end;
$BODY$
  LANGUAGE plpgsql VOLATILE
  COST 100;
ALTER FUNCTION tabla_items(integer, text, text, integer, integer)
  OWNER TO postgres;

