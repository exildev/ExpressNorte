-- Function: update_tiempo_pedido()

-- DROP FUNCTION update_tiempo_pedido();

CREATE OR REPLACE FUNCTION update_tiempo_pedido()
  RETURNS trigger AS
$BODY$
declare
begin
	if new.confirmado and old.confirmado=false then
		update domicilios_time set confirmado = now() where pedido_id= old.id;
	elsif new.entregado and old.entregado=false then
		update domicilios_time set entregado = now() where pedido_id= old.id;
	elsif new.alistado and old.alistado=false then 
		update domicilios_time set alistado = now() where pedido_id= old.id;
	elsif new.despachado  and old.despachado=false then 
		update domicilios_time set despachado = now() where pedido_id= old.id;
	end if;
	return new;
end;
$BODY$
  LANGUAGE plpgsql VOLATILE
  COST 100;
ALTER FUNCTION update_tiempo_pedido()
  OWNER TO postgres;


CREATE TRIGGER update_tiempo_pedido
  BEFORE UPDATE
  ON domicilios_pedido
  FOR EACH ROW
  EXECUTE PROCEDURE update_tiempo_pedido();
