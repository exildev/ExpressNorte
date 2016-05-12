create or replace function tabla_moto(id_des integer,search_ text,order_ text,start_ integer,length_ integer) returns text as $$
declare 
	l json;
	t integer;
begin
	select count(id) from domicilios_cliente into t;
	SELECT COALESCE(array_to_json(array_agg(row_to_json(p))), '[]') from (
		  select m.placa,m.tipo,m.marca,m.t_propiedad,t."numeroT",s."numeroS",m.id from domicilios_moto as m inner join domicilios_soat as s on (m.soat_id=s.id) inner join domicilios_tecno as t on(t.id=m.tecno_id) where 
		  m.placa like '%'||search_||'%' or m.tipo like '%'||search_||'%' or m.marca like '%'||search_||'%' or m.t_propiedad like '%'||search_||'%' or t."numeroT" like '%'||search_||'%' or s."numeroS" like '%'||search_||'%' limit length_ offset start_
	) p into l;
	return '{"recordsFiltered": '|| t ||', "recordsTotal": '|| t ||', "data": '|| l||'}';
end;
$$language plpgsql;