create or replace function crear_tiempo_pedido() returns trigger as $crear_tiempo_pedido$
declare
begin
	insert into domicilios_time(pedido_id,creado) values (new.id,now());
	return new;
end;
$crear_tiempo_pedido$ language plpgsql;

LANGUAGE plpgsql;

create trigger crear_tiempo_pedido after insert on domicilios_pedido for each row
execute procedure crear_tiempo_pedido();