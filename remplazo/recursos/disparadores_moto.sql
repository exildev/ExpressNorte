
create or replace function insertar_moto() returns trigger as $insertar_moto$
declare
begin
	IF (TG_OP = 'INSERT') THEN
		update domicilios_moto set estado=true where id = new.id;
	end if;
	return new;
end;
$insertar_moto$ language plpgsql;

create trigger insertar_moto after insert on domicilios_moto for each row
execute procedure insertar_moto();

/*********************************************************/
create or replace function eliminar_moto() returns trigger as $eliminar_moto$
declare
begin
	IF (TG_OP = 'DELETE') THEN
		update domicilios_moto set estado=false where id = old.id;
	end if;
	return null;
end;
$eliminar_moto$ language plpgsql;

create trigger eliminar_moto before delete on domicilios_moto for each row
execute procedure eliminar_moto();