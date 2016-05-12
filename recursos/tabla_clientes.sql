CREATE OR REPLACE FUNCTION tabla_cliente(id_des integer, search_ text, order_ text, start_ integer, length_ integer)
  RETURNS text AS
$BODY$
declare 
	l json;
	t integer;
begin
	select count(id) from domicilios_cliente into t;
	SELECT COALESCE(array_to_json(array_agg(row_to_json(p))), '[]') from (
		 select first_name as nom,last_name as ape,identificacion as id,id as id2 from domicilios_cliente where 
		 first_name like '%'||search_||'%' or last_name like '%'||search_||'%' or identificacion like '%'||search_||'%' limit length_ offset start_
	) p into l;
	return '{"recordsFiltered": '|| t ||', "recordsTotal": '|| json_array_length(l) ||', "data": '|| l||'}';
end;
$BODY$
  LANGUAGE plpgsql VOLATILE
  COST 100;
ALTER FUNCTION tabla_cliente(integer, text, text, integer, integer)
  OWNER TO postgres;