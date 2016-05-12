create or replace function update_tiempo_pedidos() returns trigger as $update_tiempo_pedido$
declare
begin
	if new.confirmado then
		update domicilios_time set confirmado = now() where pedido_id= old.id;
	elsif new.entregado then
		update domicilios_time set entregado = now() where pedido_id= old.id;
	elsif new.alistado then 
		update domicilios_time set alistado = now() where pedido_id= old.id;
	elsif new.despachado then 
		update domicilios_time set despachado = now() where pedido_id= old.id;
	end if;
	return true;
end;
$update_tiempo_pedido$ language plpgsql;

CREATE TRIGGER update_tiempo_pedidos
  BEFORE update
  ON domicilios_pedido
  FOR EACH ROW
  EXECUTE PROCEDURE update_tiempo_pedidos();