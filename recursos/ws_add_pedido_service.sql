CREATE OR REPLACE FUNCTION ws_add_pedido_service(_json json)
  RETURNS text AS
$BODY$
declare
	x record;
	y record;
	tem json;
	t text;
	id_emp text;
	ot text;
	id_inser integer;
begin
		for x in select * from json_each(_json) loop
			id_emp :=cast(x."value"::json->>'tienda' as json)->>'identificador'::text;
			select id::text from domicilios_empresa where nit like ''||case when id_emp is not null then id_emp::text else '0' end||'' limit 1 into id_emp;
			if id_emp is not null then
				for y in select * from json_populate_recordset(null::ws_descripcion,cast(x."value"::json->>'descripcion' as json)) loop
					raise notice '% % %',y.nombre,y.cantidad,y.valor;
				end loop;
				insert into domicilios_pedidows
					(num_pedido,npedido_express,cliente,empresa_id,fecha_pedido,tienda,tipo_pago,total,entregado,despachado,confirmado,alistado)
				values	('','',x."value"::json->>'cliente',cast(id_emp as integer),now(),cast(x."value"::json->>'tienda' as json)->>'tienda'::text,case when x."value"::json->>'tipo_pago'= '1' then 'Efectivo' when x."value"::json->>'tipo_pago' = '2' then 'Tarjeta' else 'Remision' end,cast(x."value"::json->>'total_pedido' as numeric),false,false,false,false)RETURNING id into id_inser;
				insert into domicilios_timews(creado,pedido_id) values (now(),id_inser);
			end if;
		end loop;
	return '{"respuesta":true}';
EXCEPTION WHEN others THEN
	raise notice 'descripcion';
	return '{"respuesta":false,"mensage":"Error en la estructura del json"}';
end;
$BODY$
  LANGUAGE plpgsql VOLATILE
  COST 100;
ALTER FUNCTION ws_add_pedido_service(json)
  OWNER TO postgres;
