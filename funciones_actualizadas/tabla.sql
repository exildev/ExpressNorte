-- Function: tabla(integer, text, integer, integer, integer)

-- DROP FUNCTION tabla(integer, text, integer, integer, integer);

CREATE OR REPLACE FUNCTION tabla(id_des integer, search_ text, order_ integer, start_ integer, length_ integer)
  RETURNS json AS
$BODY$
declare 
	l json;
begin
	return (SELECT COALESCE(array_to_json(array_agg(row_to_json(p))), '[]') from (
		 select first_name as nom,last_name as ape from auth_user where 
		 first_name like '%'||search_||'%' or last_name like '%'||search_||'%'  limit length_ offset start_
	) p) ;
end;
$BODY$
  LANGUAGE plpgsql VOLATILE
  COST 100;
ALTER FUNCTION tabla(integer, text, integer, integer, integer)
  OWNER TO postgres;

