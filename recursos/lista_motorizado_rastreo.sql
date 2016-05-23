CREATE OR REPLACE FUNCTION listar_motorizados_rastreo(id_emp integer, search_ text,start_ integer,pag integer)
  RETURNS text AS
$BODY$
declare 
	l json;
	t integer;
begin
	select count(id) from domicilios_cliente into t;
	SELECT COALESCE(array_to_json(array_agg(row_to_json(p))), '[]') from (
		 select licencia as ident,moto_id as nom,moto_id as ape from motorizado 
	) p into l;
	return '{"recordsFiltered": '|| t ||', "recordsTotal": '|| json_array_length(l) ||', "data": '|| l||'}';
end;
$BODY$
  LANGUAGE plpgsql VOLATILE
  COST 100;
ALTER FUNCTION tabla_cliente(integer, text, integer, integer, integer)
  OWNER TO postgres;