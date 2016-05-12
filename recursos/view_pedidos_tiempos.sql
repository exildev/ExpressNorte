create or replace view pedidos_tiempos as select * from (
	select nump,cliente,supervisor,alistador,motori,total,cliente_id,supervisor_id,alistador_id,motorizado_id,empresa_id,fecha,
	case when alistamiento is not null then round(alistamiento::numeric,2)::text else 'No asignado' end::text as alistar,
	case when despacho is not null then round(despacho::numeric,2)::text else 'No asignado' end::text as despacho ,
	case when entrega is not null then round(entrega::numeric,2)::text else 'No asignado' end::text as entrega 
	from (
		select p.id,p.num_pedido as nump,c.first_name||' '||c.last_name as cliente,s.first_name||' '||s.last_name as supervisor,p.cliente_id,p.alistador_id,p.motorizado_id,p.supervisor_id,
		       a.first_name||' '||a.last_name as alistador,m.first_name||' '||m.last_name as motori,p.empresa_id,p.fecha_pedido as fecha,
		       case when p.total is not null then p.total else 0 end::text as total,
		       (EXTRACT(EPOCH from t.confirmado)-EXTRACT(EPOCH from t.creado)) /60 as alistamiento,
		       (EXTRACT(EPOCH from t.despachado)-EXTRACT(EPOCH from t.confirmado)) /60 as despacho,
		       (EXTRACT(EPOCH from t.entregado)-EXTRACT(EPOCH from t.despachado)) /60 as entrega
				from domicilios_pedido as p inner join auth_user as m on(p.motorizado_id=m.id)  
				inner join auth_user as a on (p.alistador_id=a.id) inner join auth_user as s on (p.supervisor_id=s.id)
				inner join domicilios_cliente as c on (p.cliente_id=c.id) inner join domicilios_time as t on (p.id=t.pedido_id) 
				inner join domicilios_time as ti on(ti.pedido_id=p.id) where p.empresa_id=2 order by p.fecha_pedido desc) as p) as pf
