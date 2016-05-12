# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('domicilios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='barrio',
            field=models.CharField(max_length=50, blank=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='ciudad',
            field=models.CharField(blank=True, max_length=50, null=True, choices=[(b'', b'Seleccione una ciudad'), (b'Abejorral', b'Abejorral'), (b'Abrego', b'Abrego'), (b'Abriaqui', b'Abriaqui'), (b'Acacias', b'Acacias'), (b'Acandi', b'Acandi'), (b'Acevedo', b'Acevedo'), (b'Achi', b'Achi'), (b'Agrado', b'Agrado'), (b'Agua de Dios', b'Agua de Dios'), (b'Aguachica', b'Aguachica'), (b'Aguada', b'Aguada'), (b'Aguadas', b'Aguadas'), (b'Aguazul', b'Aguazul'), (b'Agustin Codazzi', b'Agustin Codazzi'), (b'Aipe', b'Aipe'), (b'Alban', b'Alban'), (b'Alban (San Jose)', b'Alban (San Jose)'), (b'Albania', b'Albania'), (b'Alcala', b'Alcala'), (b'Aldana', b'Aldana'), (b'Alejandria', b'Alejandria'), (b'Algeciras', b'Algeciras'), (b'Almaguer', b'Almaguer'), (b'Almeida', b'Almeida'), (b'Alpujarra', b'Alpujarra'), (b'Altamira', b'Altamira'), (b'Alto Baudo (Pie de Pato)', b'Alto Baudo (Pie de Pato)'), (b'Altos del Rosario', b'Altos del Rosario'), (b'Alvarado', b'Alvarado'), (b'Amaga', b'Amaga'), (b'Amalfi', b'Amalfi'), (b'Ambalema', b'Ambalema'), (b'Anapoima', b'Anapoima'), (b'Ancuya', b'Ancuya'), (b'Andalucia', b'Andalucia'), (b'Andes', b'Andes'), (b'Angelopolis', b'Angelopolis'), (b'Angostura', b'Angostura'), (b'Anolaima', b'Anolaima'), (b'Anori', b'Anori'), (b'Anserma', b'Anserma'), (b'Ansermanuevo', b'Ansermanuevo'), (b'Antioquia', b'Antioquia'), (b'Anza', b'Anza'), (b'Anzoategui', b'Anzoategui'), (b'Apartado', b'Apartado'), (b'Apia', b'Apia'), (b'Aquitania', b'Aquitania'), (b'Aracataca', b'Aracataca'), (b'Aranzazu', b'Aranzazu'), (b'Aratoca', b'Aratoca'), (b'Arauca', b'Arauca'), (b'Arauquita', b'Arauquita'), (b'Arbelaez', b'Arbelaez'), (b'Arboleda (Berruecos)', b'Arboleda (Berruecos)'), (b'Arboledas', b'Arboledas'), (b'Arboletes', b'Arboletes'), (b'Arcabuco', b'Arcabuco'), (b'Arenal', b'Arenal'), (b'Argelia', b'Argelia'), (b'Ariguani (El Dificil)', b'Ariguani (El Dificil)'), (b'Arjona', b'Arjona'), (b'Armenia', b'Armenia'), (b'Armero (Guayabal)', b'Armero (Guayabal)'), (b'Arroyohondo', b'Arroyohondo'), (b'Astrea', b'Astrea'), (b'Ataco', b'Ataco'), (b'Atrato (Yuto)', b'Atrato (Yuto)'), (b'Ayapel', b'Ayapel'), (b'Bagado', b'Bagado'), (b'Bahia Solano (M\xc3\xbatis)', b'Bahia Solano (M\xc3\xbatis)'), (b'Bajo Baudo (Pizarro)', b'Bajo Baudo (Pizarro)'), (b'Balboa', b'Balboa'), (b'Baranoa', b'Baranoa'), (b'Baraya', b'Baraya'), (b'Barbacoas', b'Barbacoas'), (b'Barbosa', b'Barbosa'), (b'Barichara', b'Barichara'), (b'Barranca de Upia', b'Barranca de Upia'), (b'Barrancabermeja', b'Barrancabermeja'), (b'Barrancas', b'Barrancas'), (b'Barranco de Loba', b'Barranco de Loba'), (b'Barranquilla', b'Barranquilla'), (b'Becerril', b'Becerril'), (b'Belalcazar', b'Belalcazar'), (b'Belen', b'Belen'), (b'Belen de los Andaquies', b'Belen de los Andaquies'), (b'Belen de Umbria', b'Belen de Umbria'), (b'Bello', b'Bello'), (b'Belmira', b'Belmira'), (b'Beltran', b'Beltran'), (b'Berbeo', b'Berbeo'), (b'Betania', b'Betania'), (b'Beteitiva', b'Beteitiva'), (b'Betulia', b'Betulia'), (b'Bituima', b'Bituima'), (b'Boavita', b'Boavita'), (b'Bochalema', b'Bochalema'), (b'Bojaca', b'Bojaca'), (b'Bojaya (Bellavista)', b'Bojaya (Bellavista)'), (b'Bolivar', b'Bolivar'), (b'Bosconia', b'Bosconia'), (b'Boyaca', b'Boyaca'), (b'Brise\xc3\xb1o', b'Brise\xc3\xb1o'), (b'Bucaramanga', b'Bucaramanga'), (b'Bucarasica', b'Bucarasica'), (b'Buenaventura', b'Buenaventura'), (b'Buenavista', b'Buenavista'), (b'Buenos Aires', b'Buenos Aires'), (b'Buesaco', b'Buesaco'), (b'Buga', b'Buga'), (b'Bugalagrande', b'Bugalagrande'), (b'Buritica', b'Buritica'), (b'Busbanza', b'Busbanza'), (b'Cabrera', b'Cabrera'), (b'Cabuyaro', b'Cabuyaro'), (b'Caceres', b'Caceres'), (b'Cachipay', b'Cachipay'), (b'Cachira', b'Cachira'), (b'Cacota', b'Cacota'), (b'Caicedo', b'Caicedo'), (b'Caicedonia', b'Caicedonia'), (b'Caimito', b'Caimito'), (b'Cajamarca', b'Cajamarca'), (b'Cajibio', b'Cajibio'), (b'Cajica', b'Cajica'), (b'Calamar', b'Calamar'), (b'Calarca', b'Calarca'), (b'Caldas', b'Caldas'), (b'Caldono', b'Caldono'), (b'Cali', b'Cali'), (b'California', b'California'), (b'Calima (Darien)', b'Calima (Darien)'), (b'Caloto', b'Caloto'), (b'Campamento', b'Campamento'), (b'Campo de la Cruz', b'Campo de la Cruz'), (b'Campoalegre', b'Campoalegre'), (b'Campohermoso', b'Campohermoso'), (b'Canalete', b'Canalete'), (b'Candelaria', b'Candelaria'), (b'Cantagallo', b'Cantagallo'), (b'Canton de San Pablo', b'Canton de San Pablo'), (b'Ca\xc3\xb1asgordas', b'Ca\xc3\xb1asgordas'), (b'Caparrapi', b'Caparrapi'), (b'Capitanejo', b'Capitanejo'), (b'Caqueza', b'Caqueza'), (b'Caracoli', b'Caracoli'), (b'Caramanta', b'Caramanta'), (b'Carcasi', b'Carcasi'), (b'Carepa', b'Carepa'), (b'Carmen de Apicala', b'Carmen de Apicala'), (b'Carmen de Carupa', b'Carmen de Carupa'), (b'Carmen de Viboral', b'Carmen de Viboral'), (b'Carolina', b'Carolina'), (b'Cartagena', b'Cartagena'), (b'Cartagena del Chaira', b'Cartagena del Chaira'), (b'Cartago', b'Cartago'), (b'Carur\xc3\xba', b'Carur\xc3\xba'), (b'Casabianca', b'Casabianca'), (b'Castilla la Nueva', b'Castilla la Nueva'), (b'Caucasia', b'Caucasia'), (b'Cepita', b'Cepita'), (b'Cerete', b'Cerete'), (b'Cerinza', b'Cerinza'), (b'Cerrito', b'Cerrito'), (b'Cerro San Antonio', b'Cerro San Antonio'), (b'Chachag\xc3\xbci', b'Chachag\xc3\xbci'), (b'Chaguani', b'Chaguani'), (b'Chalan', b'Chalan'), (b'Chameza', b'Chameza'), (b'Chaparral', b'Chaparral'), (b'Charala', b'Charala'), (b'Charta', b'Charta'), (b'Chia', b'Chia'), (b'Chigorodo', b'Chigorodo'), (b'Chima', b'Chima'), (b'Chimichagua', b'Chimichagua'), (b'Chinacota', b'Chinacota'), (b'Chinavita', b'Chinavita'), (b'Chinchina', b'Chinchina'), (b'Chin\xc3\xba', b'Chin\xc3\xba'), (b'Chipaque', b'Chipaque'), (b'Chipata', b'Chipata'), (b'Chiquinquira', b'Chiquinquira'), (b'Chiquiza', b'Chiquiza'), (b'Chiriguana', b'Chiriguana'), (b'Chiscas', b'Chiscas'), (b'Chita', b'Chita'), (b'Chitaga', b'Chitaga'), (b'Chitaranque', b'Chitaranque'), (b'Chivata', b'Chivata'), (b'Chivolo', b'Chivolo'), (b'Chivor', b'Chivor'), (b'Choachi', b'Choachi'), (b'Choconta', b'Choconta'), (b'Cicuto', b'Cicuto'), (b'Cienaga', b'Cienaga'), (b'Cienaga de Oro', b'Cienaga de Oro'), (b'Cimitarra', b'Cimitarra'), (b'Circasia', b'Circasia'), (b'Cisneros', b'Cisneros'), (b'Clemencia', b'Clemencia'), (b'Cocorna', b'Cocorna'), (b'Coello', b'Coello'), (b'Cogua', b'Cogua'), (b'Colombia', b'Colombia'), (b'Colon', b'Colon'), (b'Colon (Genova)', b'Colon (Genova)'), (b'Coloso (Ricaurte)', b'Coloso (Ricaurte)'), (b'Combita', b'Combita'), (b'Concepcion', b'Concepcion'), (b'Concordia', b'Concordia'), (b'Condoto', b'Condoto'), (b'Confines', b'Confines'), (b'Consaca', b'Consaca'), (b'Contadero', b'Contadero'), (b'Contratacion', b'Contratacion'), (b'Convencion', b'Convencion'), (b'Copacabana', b'Copacabana'), (b'Coper', b'Coper'), (b'Cordoba', b'Cordoba'), (b'Corinto', b'Corinto'), (b'Coromoro', b'Coromoro'), (b'Corozal', b'Corozal'), (b'Corrales', b'Corrales'), (b'Cota', b'Cota'), (b'Cotorra', b'Cotorra'), (b'Covarachia', b'Covarachia'), (b'Coyaima', b'Coyaima'), (b'Cravo Norte', b'Cravo Norte'), (b'Cuaspud (Carlosama)', b'Cuaspud (Carlosama)'), (b'Cubar', b'Cubar'), (b'Cubarral', b'Cubarral'), (b'Cucaita', b'Cucaita'), (b'Cucunuba', b'Cucunuba'), (b'C\xc3\xbacuta', b'C\xc3\xbacuta'), (b'Cucutilla', b'Cucutilla'), (b'Cuitiva', b'Cuitiva'), (b'Cumaral', b'Cumaral'), (b'Cumaribo', b'Cumaribo'), (b'Cumbal', b'Cumbal'), (b'Cumbitara', b'Cumbitara'), (b'Cunday', b'Cunday'), (b'Curillo', b'Curillo'), (b'Curiti', b'Curiti'), (b'Curumani', b'Curumani'), (b'Dabeiba', b'Dabeiba'), (b'Dagua', b'Dagua'), (b'Dibulla', b'Dibulla'), (b'Distraccion', b'Distraccion'), (b'Dolores', b'Dolores'), (b'Don Matias', b'Don Matias'), (b'Dos Quebradas', b'Dos Quebradas'), (b'Duitama', b'Duitama'), (b'Durania', b'Durania'), (b'Ebejico', b'Ebejico'), (b'El \xc3\x81guila', b'El \xc3\x81guila'), (b'El Bagre', b'El Bagre'), (b'El Banco', b'El Banco'), (b'El Cairo', b'El Cairo'), (b'El Calvario', b'El Calvario'), (b'El Carmen', b'El Carmen'), (b'El Carmen de Bolivar', b'El Carmen de Bolivar'), (b'El Castillo', b'El Castillo'), (b'El Cerrito', b'El Cerrito'), (b'El Charco', b'El Charco'), (b'El Cocuy', b'El Cocuy'), (b'El Colegio', b'El Colegio'), (b'El Copey', b'El Copey'), (b'El Doncello', b'El Doncello'), (b'El Dorado', b'El Dorado'), (b'El Dovio', b'El Dovio'), (b'El Espino', b'El Espino'), (b'El Guacamayo', b'El Guacamayo'), (b'El Guamo', b'El Guamo'), (b'El Litoral de San Juan', b'El Litoral de San Juan'), (b'El Molino', b'El Molino'), (b'El Paso', b'El Paso'), (b'El Paujil', b'El Paujil'), (b'El Pe\xc3\xb1on', b'El Pe\xc3\xb1on'), (b'El Pi\xc3\xb1on', b'El Pi\xc3\xb1on'), (b'El Playon', b'El Playon'), (b'El Reten', b'El Reten'), (b'El Retorno', b'El Retorno'), (b'El Rosal', b'El Rosal'), (b'El Rosario', b'El Rosario'), (b'El Tablon', b'El Tablon'), (b'El Tambo', b'El Tambo'), (b'El Tarra', b'El Tarra'), (b'El Zulia', b'El Zulia'), (b'Elias', b'Elias'), (b'Encino', b'Encino'), (b'Enciso', b'Enciso'), (b'Entrerrios', b'Entrerrios'), (b'Envigado', b'Envigado'), (b'Espinal', b'Espinal'), (b'Facatativa', b'Facatativa'), (b'Falan', b'Falan'), (b'Filadelfia', b'Filadelfia'), (b'Filandia', b'Filandia'), (b'Firavitoba', b'Firavitoba'), (b'Flandes', b'Flandes'), (b'Florencia', b'Florencia'), (b'Floresta', b'Floresta'), (b'Florian', b'Florian'), (b'Florida', b'Florida'), (b'Floridablanca', b'Floridablanca'), (b'Fomeque', b'Fomeque'), (b'Fonseca', b'Fonseca'), (b'Fortul', b'Fortul'), (b'Fosca', b'Fosca'), (b'Francisco Pizarro', b'Francisco Pizarro'), (b'Fredonia', b'Fredonia'), (b'Fresno', b'Fresno'), (b'Frontino', b'Frontino'), (b'Fuente de Oro', b'Fuente de Oro'), (b'Fundacion', b'Fundacion'), (b'Funes', b'Funes'), (b'Funza', b'Funza'), (b'F\xc3\xbaquene', b'F\xc3\xbaquene'), (b'Fusagasuga', b'Fusagasuga'), (b'Gachala', b'Gachala'), (b'Gachancipa', b'Gachancipa'), (b'Gachantiva', b'Gachantiva'), (b'Gacheta', b'Gacheta'), (b'Galan', b'Galan'), (b'Galapa', b'Galapa'), (b'Galeras (Nueva Granada)', b'Galeras (Nueva Granada)'), (b'Gama', b'Gama'), (b'Gamarra', b'Gamarra'), (b'Gambita', b'Gambita'), (b'Gameza', b'Gameza'), (b'Garagoa', b'Garagoa'), (b'Garzon', b'Garzon'), (b'Genova', b'Genova'), (b'Gigante', b'Gigante'), (b'Ginebra', b'Ginebra'), (b'Giraldo', b'Giraldo'), (b'Girardot', b'Girardot'), (b'Girardota', b'Girardota'), (b'Giron', b'Giron'), (b'Gomez Plata', b'Gomez Plata'), (b'Gonzalez', b'Gonzalez'), (b'Gramalote', b'Gramalote'), (b'Granada', b'Granada'), (b'Guaca', b'Guaca'), (b'Guacamayas', b'Guacamayas'), (b'Guacari', b'Guacari'), (b'Guacheta', b'Guacheta'), (b'Guachucal', b'Guachucal'), (b'Guadalupe', b'Guadalupe'), (b'Guaduas', b'Guaduas'), (b'Guaitarilla', b'Guaitarilla'), (b'Gualmatan', b'Gualmatan'), (b'Guamal', b'Guamal'), (b'Guamo', b'Guamo'), (b'Guapi', b'Guapi'), (b'Guapota', b'Guapota'), (b'Guaranda', b'Guaranda'), (b'Guarne', b'Guarne'), (b'Guasca', b'Guasca'), (b'Guatape', b'Guatape'), (b'Guataqui', b'Guataqui'), (b'Guatavita', b'Guatavita'), (b'Guateque', b'Guateque'), (b'Guatica', b'Guatica'), (b'Guavata', b'Guavata'), (b'Guayabal de Siquima', b'Guayabal de Siquima'), (b'Guayabetal', b'Guayabetal'), (b'Guayata', b'Guayata'), (b'Guepsa', b'Guepsa'), (b'Guican', b'Guican'), (b'Gutierrez', b'Gutierrez'), (b'Hacari', b'Hacari'), (b'Hatillo de Loba', b'Hatillo de Loba'), (b'Hato', b'Hato'), (b'Hato Corozal', b'Hato Corozal'), (b'Hatonuevo', b'Hatonuevo'), (b'Heliconia', b'Heliconia'), (b'Herran', b'Herran'), (b'Herveo', b'Herveo'), (b'Hispania', b'Hispania'), (b'Hobo', b'Hobo'), (b'Honda', b'Honda'), (b'Ibague', b'Ibague'), (b'Icononzo', b'Icononzo'), (b'Iles', b'Iles'), (b'Im\xc3\xbaes', b'Im\xc3\xbaes'), (b'Inza', b'Inza'), (b'Ipiales', b'Ipiales'), (b'Iquira', b'Iquira'), (b'Isnos', b'Isnos'), (b'Itag\xc3\xbci', b'Itag\xc3\xbci'), (b'Itsmina', b'Itsmina'), (b'Ituango', b'Ituango'), (b'Iza', b'Iza'), (b'Jambalo', b'Jambalo'), (b'Jamundi', b'Jamundi'), (b'Jardin', b'Jardin'), (b'Jenesano', b'Jenesano'), (b'Jerico', b'Jerico'), (b'Jerusalen', b'Jerusalen'), (b'Jes\xc3\xbas Maria', b'Jes\xc3\xbas Maria'), (b'Jordan', b'Jordan'), (b'Juan de Acosta', b'Juan de Acosta'), (b'Junin', b'Junin'), (b'Jurado', b'Jurado'), (b'La Apartada (Frontera)', b'La Apartada (Frontera)'), (b'La Argentina', b'La Argentina'), (b'La Belleza', b'La Belleza'), (b'La Calera', b'La Calera'), (b'La Capilla', b'La Capilla'), (b'La Ceja', b'La Ceja'), (b'La Celia', b'La Celia'), (b'La Cruz', b'La Cruz'), (b'La Cumbre', b'La Cumbre'), (b'La Dorada', b'La Dorada'), (b'La Esperanza', b'La Esperanza'), (b'La Estrella', b'La Estrella'), (b'La Florida', b'La Florida'), (b'La Gloria', b'La Gloria'), (b'La Jagua de Ibirico', b'La Jagua de Ibirico'), (b'La Llanada', b'La Llanada'), (b'La Macarena', b'La Macarena'), (b'La Merced', b'La Merced'), (b'La Mesa', b'La Mesa'), (b'La Monta\xc3\xb1ita', b'La Monta\xc3\xb1ita'), (b'La Palma', b'La Palma'), (b'La Paz', b'La Paz'), (b'La Paz (Robles)', b'La Paz (Robles)'), (b'La Pe\xc3\xb1a', b'La Pe\xc3\xb1a'), (b'La Pintada', b'La Pintada'), (b'La Plata', b'La Plata'), (b'La Playa', b'La Playa'), (b'La Primavera', b'La Primavera'), (b'La Salina', b'La Salina'), (b'La Sierra', b'La Sierra'), (b'La Tebaida', b'La Tebaida'), (b'La Tola', b'La Tola'), (b'La Ubita', b'La Ubita'), (b'La Union', b'La Union'), (b'La Uribe', b'La Uribe'), (b'La Vega', b'La Vega'), (b'La Victoria', b'La Victoria'), (b'La Virginia', b'La Virginia'), (b'Labateca', b'Labateca'), (b'Labranzagrande', b'Labranzagrande'), (b'Landazuri', b'Landazuri'), (b'Lebrija', b'Lebrija'), (b'Leiva', b'Leiva'), (b'Lejanias', b'Lejanias'), (b'Lenguazaque', b'Lenguazaque'), (b'Lerida', b'Lerida'), (b'Leticia', b'Leticia'), (b'Libano', b'Libano'), (b'Liborina', b'Liborina'), (b'Linares', b'Linares'), (b'Lloro', b'Lloro'), (b'Lopez (Micay)', b'Lopez (Micay)'), (b'Lorica', b'Lorica'), (b'Los Andes (Sotomayor)', b'Los Andes (Sotomayor)'), (b'Los Cordobas', b'Los Cordobas'), (b'Los Palmitos', b'Los Palmitos'), (b'Los Patios', b'Los Patios'), (b'Los Santos', b'Los Santos'), (b'Lourdes', b'Lourdes'), (b'Luruaco', b'Luruaco'), (b'Macanal', b'Macanal'), (b'Macaravita', b'Macaravita'), (b'Maceo', b'Maceo'), (b'Macheta', b'Macheta'), (b'Madrid', b'Madrid'), (b'Magangue', b'Magangue'), (b'Mag\xc3\xbci (Payan)', b'Mag\xc3\xbci (Payan)'), (b'Mahates', b'Mahates'), (b'Maicao', b'Maicao'), (b'Majagual', b'Majagual'), (b'Malaga', b'Malaga'), (b'Malambo', b'Malambo'), (b'Mallama (Piedrancha)', b'Mallama (Piedrancha)'), (b'Manati', b'Manati'), (b'Manaure', b'Manaure'), (b'Manaure Balcon Cesar', b'Manaure Balcon Cesar'), (b'Mani', b'Mani'), (b'Manizales', b'Manizales'), (b'Manta', b'Manta'), (b'Manzanares', b'Manzanares'), (b'Mapiripan', b'Mapiripan'), (b'Margarita', b'Margarita'), (b'Maria la Baja', b'Maria la Baja'), (b'Marinilla', b'Marinilla'), (b'Maripi', b'Maripi'), (b'Mariquita', b'Mariquita'), (b'Marmato', b'Marmato'), (b'Marquetalia', b'Marquetalia'), (b'Marsella', b'Marsella'), (b'Marulanda', b'Marulanda'), (b'Matanza', b'Matanza'), (b'Medellin', b'Medellin'), (b'Medina', b'Medina'), (b'Melgar', b'Melgar'), (b'Mercaderes', b'Mercaderes'), (b'Mesetas', b'Mesetas'), (b'Milan', b'Milan'), (b'Miraflores', b'Miraflores'), (b'Miranda', b'Miranda'), (b'Mistrato', b'Mistrato'), (b'Mit\xc3\xba', b'Mit\xc3\xba'), (b'Mocoa', b'Mocoa'), (b'Mogotes', b'Mogotes'), (b'Molagavita', b'Molagavita'), (b'Momil', b'Momil'), (b'Mompos', b'Mompos'), (b'Mongua', b'Mongua'), (b'Mongui', b'Mongui'), (b'Moniquira', b'Moniquira'), (b'Monitos', b'Monitos'), (b'Montebello', b'Montebello'), (b'Montecristo', b'Montecristo'), (b'Montelibano', b'Montelibano'), (b'Montenegro', b'Montenegro'), (b'Monteria', b'Monteria'), (b'Monterrey', b'Monterrey'), (b'Morales', b'Morales'), (b'Morelia', b'Morelia'), (b'Morroa', b'Morroa'), (b'Mosquera', b'Mosquera'), (b'Motavita', b'Motavita'), (b'Murillo', b'Murillo'), (b'Murindo', b'Murindo'), (b'Mutata', b'Mutata'), (b'Mutiscua', b'Mutiscua'), (b'Muzo', b'Muzo'), (b'Nari\xc3\xb1o', b'Nari\xc3\xb1o'), (b'Nataga', b'Nataga'), (b'Natagaima', b'Natagaima'), (b'Nechi', b'Nechi'), (b'Necocli', b'Necocli'), (b'Neira', b'Neira'), (b'Neiva', b'Neiva'), (b'Nemocon', b'Nemocon'), (b'Nilo', b'Nilo'), (b'Nimaima', b'Nimaima'), (b'Nobsa', b'Nobsa'), (b'Nocaima', b'Nocaima'), (b'Novita', b'Novita'), (b'Nuevo Colon', b'Nuevo Colon'), (b'Nunchia', b'Nunchia'), (b'Nuqui', b'Nuqui'), (b'Obando', b'Obando'), (b'Ocamonte', b'Ocamonte'), (b'Oca\xc3\xb1a', b'Oca\xc3\xb1a'), (b'Oiba', b'Oiba'), (b'Oicata', b'Oicata'), (b'Olaya', b'Olaya'), (b'Onzaga', b'Onzaga'), (b'Oporapa', b'Oporapa'), (b'Orito', b'Orito'), (b'Orocue', b'Orocue'), (b'Ortega', b'Ortega'), (b'Ospina', b'Ospina'), (b'Otanche', b'Otanche'), (b'Ovejas', b'Ovejas'), (b'Pachavita', b'Pachavita'), (b'Pacho', b'Pacho'), (b'Pacora', b'Pacora'), (b'Padilla', b'Padilla'), (b'Paez', b'Paez'), (b'Paez (Belalcazar)', b'Paez (Belalcazar)'), (b'Paicol', b'Paicol'), (b'Pailitas', b'Pailitas'), (b'Paime', b'Paime'), (b'Paipa', b'Paipa'), (b'Pajarito', b'Pajarito'), (b'Palermo', b'Palermo'), (b'Palestina', b'Palestina'), (b'Palmar', b'Palmar'), (b'Palmar de Varela', b'Palmar de Varela'), (b'Palmas del Socorro', b'Palmas del Socorro'), (b'Palmira', b'Palmira'), (b'Palmito', b'Palmito'), (b'Palocabildo', b'Palocabildo'), (b'Pamplona', b'Pamplona'), (b'Pamplonita', b'Pamplonita'), (b'Pandi', b'Pandi'), (b'Panqueba', b'Panqueba'), (b'Paramo', b'Paramo'), (b'Paratebueno', b'Paratebueno'), (b'Pasca', b'Pasca'), (b'Pasto', b'Pasto'), (b'Patia (El Bordo)', b'Patia (El Bordo)'), (b'Pauna', b'Pauna'), (b'Paya', b'Paya'), (b'Paz de Ariporo', b'Paz de Ariporo'), (b'Paz de Rio', b'Paz de Rio'), (b'Pedraza', b'Pedraza'), (b'Pelaya', b'Pelaya'), (b'Pensilvania', b'Pensilvania'), (b'Pe\xc3\xb1ol', b'Pe\xc3\xb1ol'), (b'Peque', b'Peque'), (b'Pereira', b'Pereira'), (b'Pesca', b'Pesca'), (b'Piamonte', b'Piamonte'), (b'Pie de Cuesta', b'Pie de Cuesta'), (b'Piedras', b'Piedras'), (b'Piendamo', b'Piendamo'), (b'Pijao', b'Pijao'), (b'Piji\xc3\xb1o del Carmen', b'Piji\xc3\xb1o del Carmen'), (b'Pinchote', b'Pinchote'), (b'Pinillos', b'Pinillos'), (b'Piojo', b'Piojo'), (b'Pisva', b'Pisva'), (b'Pital', b'Pital'), (b'Pitalito', b'Pitalito'), (b'Pivijay', b'Pivijay'), (b'Planadas', b'Planadas'), (b'Planeta Rica', b'Planeta Rica'), (b'Plato', b'Plato'), (b'Policarpa', b'Policarpa'), (b'Polonuevo', b'Polonuevo'), (b'Ponedera', b'Ponedera'), (b'Popayan', b'Popayan'), (b'Pore', b'Pore'), (b'Potosi', b'Potosi'), (b'Pradera', b'Pradera'), (b'Prado', b'Prado'), (b'Providencia', b'Providencia'), (b'Publoviejo', b'Publoviejo'), (b'Pueblo Bello', b'Pueblo Bello'), (b'Pueblo Nuevo', b'Pueblo Nuevo'), (b'Pueblo Rico', b'Pueblo Rico'), (b'Pueblorrico', b'Pueblorrico'), (b'Puente Nacional', b'Puente Nacional'), (b'Puerres', b'Puerres'), (b'Puerto Asis', b'Puerto Asis'), (b'Puerto Berrio', b'Puerto Berrio'), (b'Puerto Boyaca', b'Puerto Boyaca'), (b'Puerto Caicedo', b'Puerto Caicedo'), (b'Puerto Carre\xc3\xb1o', b'Puerto Carre\xc3\xb1o'), (b'Puerto Colombia', b'Puerto Colombia'), (b'Puerto Concordia', b'Puerto Concordia'), (b'Puerto Escondido', b'Puerto Escondido'), (b'Puerto Gaitan', b'Puerto Gaitan'), (b'Puerto Guzman', b'Puerto Guzman'), (b'Puerto Inirida', b'Puerto Inirida'), (b'Puerto Leguizamo', b'Puerto Leguizamo'), (b'Puerto Libertador', b'Puerto Libertador'), (b'Puerto Lleras', b'Puerto Lleras'), (b'Puerto Lopez', b'Puerto Lopez'), (b'Puerto Nare', b'Puerto Nare'), (b'Puerto Nari\xc3\xb1o', b'Puerto Nari\xc3\xb1o'), (b'Puerto Parra', b'Puerto Parra'), (b'Puerto Rico', b'Puerto Rico'), (b'Puerto Rondon', b'Puerto Rondon'), (b'Puerto Salgar', b'Puerto Salgar'), (b'Puerto Santander', b'Puerto Santander'), (b'Puerto Tejada', b'Puerto Tejada'), (b'Puerto Triunfo', b'Puerto Triunfo'), (b'Puerto Wilches', b'Puerto Wilches'), (b'Puli', b'Puli'), (b'Pupiales', b'Pupiales'), (b'Purace (Coconuco)', b'Purace (Coconuco)'), (b'Purificacion', b'Purificacion'), (b'Purisima', b'Purisima'), (b'Quebradanegra', b'Quebradanegra'), (b'Quetame', b'Quetame'), (b'Quibdo', b'Quibdo'), (b'Quimbaya', b'Quimbaya'), (b'Quinchia', b'Quinchia'), (b'Quipama', b'Quipama'), (b'Quipile', b'Quipile'), (b'Ricaurte', b'Ricaurte'), (b'Rio de Oro', b'Rio de Oro'), (b'Rio Viejo', b'Rio Viejo'), (b'Rioblanco', b'Rioblanco'), (b'Riofrio', b'Riofrio'), (b'Riohacha', b'Riohacha'), (b'Rionegro', b'Rionegro'), (b'Riosucio', b'Riosucio'), (b'Risaralda', b'Risaralda'), (b'Rivera', b'Rivera'), (b'Roberto Payan (San Jose)', b'Roberto Payan (San Jose)'), (b'Roldanillo', b'Roldanillo'), (b'Roncesvalles', b'Roncesvalles'), (b'Rondon', b'Rondon'), (b'Rosas', b'Rosas'), (b'Rovira', b'Rovira'), (b'Sabalarga', b'Sabalarga'), (b'Sabana de Torres', b'Sabana de Torres'), (b'Sabanagrande', b'Sabanagrande'), (b'Sabanalarga', b'Sabanalarga'), (b'Sabaneta', b'Sabaneta'), (b'Saboya', b'Saboya'), (b'Sacama', b'Sacama'), (b'Sachica', b'Sachica'), (b'Sahag\xc3\xban', b'Sahag\xc3\xban'), (b'Saladoblanco', b'Saladoblanco'), (b'Salamina', b'Salamina'), (b'Salazar', b'Salazar'), (b'Salda\xc3\xb1a', b'Salda\xc3\xb1a'), (b'Salento', b'Salento'), (b'Salgar', b'Salgar'), (b'Samaca', b'Samaca'), (b'Samana', b'Samana'), (b'Samaniego', b'Samaniego'), (b'Sampues', b'Sampues'), (b'San Agustin', b'San Agustin'), (b'San Alberto', b'San Alberto'), (b'San Andres', b'San Andres'), (b'San Andres Sotavento', b'San Andres Sotavento'), (b'San Antero', b'San Antero'), (b'San Antonio', b'San Antonio'), (b'San Antonio de Tequendama', b'San Antonio de Tequendama'), (b'San Benito', b'San Benito'), (b'San Benito Abad', b'San Benito Abad'), (b'San Bernardo', b'San Bernardo'), (b'San Bernardo del Viento', b'San Bernardo del Viento'), (b'San Calixto', b'San Calixto'), (b'San Carlos', b'San Carlos'), (b'San Carlos de Guaroa', b'San Carlos de Guaroa'), (b'San Cayetano', b'San Cayetano'), (b'San Cristobal', b'San Cristobal'), (b'San Diego', b'San Diego'), (b'San Eduardo', b'San Eduardo'), (b'San Estanislao', b'San Estanislao'), (b'San Fernando', b'San Fernando'), (b'San Francisco', b'San Francisco'), (b'San Gil', b'San Gil'), (b'San Jacinto', b'San Jacinto'), (b'San Jacinto del Cauca', b'San Jacinto del Cauca'), (b'San Jeronimo', b'San Jeronimo'), (b'San Joaquin', b'San Joaquin'), (b'San Jose', b'San Jose'), (b'San Jose de Miranda', b'San Jose de Miranda'), (b'San Jose de Monta\xc3\xb1a', b'San Jose de Monta\xc3\xb1a'), (b'San Jose de Pare', b'San Jose de Pare'), (b'San Jose del Fragua', b'San Jose del Fragua'), (b'San Jose del Guaviare', b'San Jose del Guaviare'), (b'San Jose del Palmar', b'San Jose del Palmar'), (b'San Juan de Arama', b'San Juan de Arama'), (b'San Juan de Betulia', b'San Juan de Betulia'), (b'San Juan de Rioseco', b'San Juan de Rioseco'), (b'San Juan de Uraba', b'San Juan de Uraba'), (b'San Juan del Cesar', b'San Juan del Cesar'), (b'San Juan Nepomuceno', b'San Juan Nepomuceno'), (b'San Juanito', b'San Juanito'), (b'San Lorenzo', b'San Lorenzo'), (b'San Luis', b'San Luis'), (b'San Luis de Gaceno', b'San Luis de Gaceno'), (b'San Luis de Palenque', b'San Luis de Palenque'), (b'San Marcos', b'San Marcos'), (b'San Martin', b'San Martin'), (b'San Martin de Loba', b'San Martin de Loba'), (b'San Mateo', b'San Mateo'), (b'San Miguel', b'San Miguel'), (b'San Miguel de Sema', b'San Miguel de Sema'), (b'San Onofre', b'San Onofre'), (b'San Pablo', b'San Pablo'), (b'San Pablo de Borbur', b'San Pablo de Borbur'), (b'San Pedro', b'San Pedro'), (b'San Pedro de Cartago', b'San Pedro de Cartago'), (b'San Pedro de Uraba', b'San Pedro de Uraba'), (b'San Pelayo', b'San Pelayo'), (b'San Rafael', b'San Rafael'), (b'San Roque', b'San Roque'), (b'San Sebastian', b'San Sebastian'), (b'San Sebastian de Buuenavista', b'San Sebastian de Buuenavista'), (b'San Vicente', b'San Vicente'), (b'San Vicente de Chucuri', b'San Vicente de Chucuri'), (b'San Vicente del Caguan', b'San Vicente del Caguan'), (b'San Zenon', b'San Zenon'), (b'Sandona', b'Sandona'), (b'Santa Ana', b'Santa Ana'), (b'Santa Barbara', b'Santa Barbara'), (b'Santa Barbara (Iscuande)', b'Santa Barbara (Iscuande)'), (b'Santa Catalina', b'Santa Catalina'), (b'Santa Cruz (Guachavez)', b'Santa Cruz (Guachavez)'), (b'Santa Helena del Opon', b'Santa Helena del Opon'), (b'Santa Isabel', b'Santa Isabel'), (b'Santa Lucia', b'Santa Lucia'), (b'Santa Maria', b'Santa Maria'), (b'Santa Marta', b'Santa Marta'), (b'Santa Rosa', b'Santa Rosa'), (b'Santa Rosa de Cabal', b'Santa Rosa de Cabal'), (b'Santa Rosa de Osos', b'Santa Rosa de Osos'), (b'Santa Rosa de Viterbo', b'Santa Rosa de Viterbo'), (b'Santa Rosa del Sur', b'Santa Rosa del Sur'), (b'Santa Rosalia', b'Santa Rosalia'), (b'Santa Sofia', b'Santa Sofia'), (b'Santafe de Bogota', b'Santafe de Bogota'), (b'Santana', b'Santana'), (b'Santander de Quilichao', b'Santander de Quilichao'), (b'Santiago', b'Santiago'), (b'Santo Domingo', b'Santo Domingo'), (b'Santo Tomas', b'Santo Tomas'), (b'Santuario', b'Santuario'), (b'Sapuyes', b'Sapuyes'), (b'Saravena', b'Saravena'), (b'Sardinata', b'Sardinata'), (b'Sasaima', b'Sasaima'), (b'Sativanorte', b'Sativanorte'), (b'Sativasur', b'Sativasur'), (b'Segovia', b'Segovia'), (b'Sesquile', b'Sesquile'), (b'Sevilla', b'Sevilla'), (b'Siachoque', b'Siachoque'), (b'Sibate', b'Sibate'), (b'Sibundoy', b'Sibundoy'), (b'Silos', b'Silos'), (b'Silvania', b'Silvania'), (b'Silvia', b'Silvia'), (b'Simacota', b'Simacota'), (b'Simijaca', b'Simijaca'), (b'Simiti', b'Simiti'), (b'Since', b'Since'), (b'Sincelejo', b'Sincelejo'), (b'Sipi', b'Sipi'), (b'Sitionuevo', b'Sitionuevo'), (b'Soacha', b'Soacha'), (b'Soata', b'Soata'), (b'Socha', b'Socha'), (b'Socorro', b'Socorro'), (b'Socota', b'Socota'), (b'Sogamoso', b'Sogamoso'), (b'Solano', b'Solano'), (b'Soledad', b'Soledad'), (b'Solita', b'Solita'), (b'Somondoco', b'Somondoco'), (b'Sonson', b'Sonson'), (b'Sopetran', b'Sopetran'), (b'Soplaviento', b'Soplaviento'), (b'Sopo', b'Sopo'), (b'Sora', b'Sora'), (b'Soraca', b'Soraca'), (b'Sotaquira', b'Sotaquira'), (b'Sotara (Paispamba)', b'Sotara (Paispamba)'), (b'Suaita', b'Suaita'), (b'Suan', b'Suan'), (b'Suarez', b'Suarez'), (b'Suaza', b'Suaza'), (b'Subachoque', b'Subachoque'), (b'Sucre', b'Sucre'), (b'Suesca', b'Suesca'), (b'Supata', b'Supata'), (b'Supia', b'Supia'), (b'Surata', b'Surata'), (b'Susa', b'Susa'), (b'Susacon', b'Susacon'), (b'Sutamarchan', b'Sutamarchan'), (b'Sutatausa', b'Sutatausa'), (b'Sutatenza', b'Sutatenza'), (b'Tabio', b'Tabio'), (b'Tado', b'Tado'), (b'Talaigua Nuevo', b'Talaigua Nuevo'), (b'Tamalameque', b'Tamalameque'), (b'Tamara', b'Tamara'), (b'Tame', b'Tame'), (b'Tamesis', b'Tamesis'), (b'Taminango', b'Taminango'), (b'Tangua', b'Tangua'), (b'Taraza', b'Taraza'), (b'Tarqui', b'Tarqui'), (b'Tarso', b'Tarso'), (b'Tasco', b'Tasco'), (b'Tatama', b'Tatama'), (b'Tauramena', b'Tauramena'), (b'Tausa', b'Tausa'), (b'Tello', b'Tello'), (b'Tena', b'Tena'), (b'Tenerife', b'Tenerife'), (b'Tenjo', b'Tenjo'), (b'Tenza', b'Tenza'), (b'Teorama', b'Teorama'), (b'Teruel', b'Teruel'), (b'Tesalia', b'Tesalia'), (b'Tibacuy', b'Tibacuy'), (b'Tibana', b'Tibana'), (b'Tibasosa', b'Tibasosa'), (b'Tibirita', b'Tibirita'), (b'Tib\xc3\xba', b'Tib\xc3\xba'), (b'Tierralta', b'Tierralta'), (b'Timana', b'Timana'), (b'Timbio', b'Timbio'), (b'Timbiqui', b'Timbiqui'), (b'Tinjaca', b'Tinjaca'), (b'Tipacoque', b'Tipacoque'), (b'Tiquisio (Puerto Rico)', b'Tiquisio (Puerto Rico)'), (b'Titiribi', b'Titiribi'), (b'Toca', b'Toca'), (b'Tocaima', b'Tocaima'), (b'Tocancipa', b'Tocancipa'), (b'Togui', b'Togui'), (b'Toledo', b'Toledo'), (b'Tol\xc3\xba', b'Tol\xc3\xba'), (b'Toluviejo', b'Toluviejo'), (b'Tona', b'Tona'), (b'Topaga', b'Topaga'), (b'Topaipi', b'Topaipi'), (b'Toribio', b'Toribio'), (b'Toro', b'Toro'), (b'Tota', b'Tota'), (b'Totoro', b'Totoro'), (b'Trinidad', b'Trinidad'), (b'Trujillo', b'Trujillo'), (b'Tubara', b'Tubara'), (b'Tulua', b'Tulua'), (b'Tumaco', b'Tumaco'), (b'Tunja', b'Tunja'), (b'Tunungua', b'Tunungua'), (b'T\xc3\xbaquerres', b'T\xc3\xbaquerres'), (b'Turbaco', b'Turbaco'), (b'Turbana', b'Turbana'), (b'Turbo', b'Turbo'), (b'Turmeque', b'Turmeque'), (b'Tuta', b'Tuta'), (b'Tutaza', b'Tutaza'), (b'Ubala', b'Ubala'), (b'Ubaque', b'Ubaque'), (b'Ubate', b'Ubate'), (b'Ulloa', b'Ulloa'), (b'\xc3\x9ambita', b'\xc3\x9ambita'), (b'Une', b'Une'), (b'Unguia', b'Unguia'), (b'Uramita', b'Uramita'), (b'Uribia', b'Uribia'), (b'Urrao', b'Urrao'), (b'Urumita', b'Urumita'), (b'Usiacuri', b'Usiacuri'), (b'\xc3\x9atica', b'\xc3\x9atica'), (b'Valdivia', b'Valdivia'), (b'Valencia', b'Valencia'), (b'Valle de San Jose', b'Valle de San Jose'), (b'Valle de San Juan', b'Valle de San Juan'), (b'Valledupar', b'Valledupar'), (b'Valparaiso', b'Valparaiso'), (b'Vegachi', b'Vegachi'), (b'Velez', b'Velez'), (b'Venadillo', b'Venadillo'), (b'Venecia', b'Venecia'), (b'Venecia (Ospina Perez)', b'Venecia (Ospina Perez)'), (b'Ventaquemada', b'Ventaquemada'), (b'Vergara', b'Vergara'), (b'Versalles', b'Versalles'), (b'Vetas', b'Vetas'), (b'Viani', b'Viani'), (b'Victoria', b'Victoria'), (b'Vigia del Fuerte', b'Vigia del Fuerte'), (b'Vijes', b'Vijes'), (b'Villa de Leyva', b'Villa de Leyva'), (b'Villa del Rosario', b'Villa del Rosario'), (b'Villa Gamuez (La Hormiga)', b'Villa Gamuez (La Hormiga)'), (b'Villa Garzon', b'Villa Garzon'), (b'Villacaro', b'Villacaro'), (b'Villagomez', b'Villagomez'), (b'Villahermosa', b'Villahermosa'), (b'Villamaria', b'Villamaria'), (b'Villanueva', b'Villanueva'), (b'Villapinzon', b'Villapinzon'), (b'Villarrica', b'Villarrica'), (b'Villavicencio', b'Villavicencio'), (b'Villavieja', b'Villavieja'), (b'Villeta', b'Villeta'), (b'Viota', b'Viota'), (b'Viracacha', b'Viracacha'), (b'Vistahermosa', b'Vistahermosa'), (b'Viterbo', b'Viterbo'), (b'Yacopi', b'Yacopi'), (b'Yacuanquer', b'Yacuanquer'), (b'Yaguara', b'Yaguara'), (b'Yali', b'Yali'), (b'Yarumal', b'Yarumal'), (b'Yolombo', b'Yolombo'), (b'Yondo (Casabe)', b'Yondo (Casabe)'), (b'Yopal', b'Yopal'), (b'Yotoco', b'Yotoco'), (b'Yumbo', b'Yumbo'), (b'Zambrano', b'Zambrano'), (b'Zapatoca', b'Zapatoca'), (b'Zaragoza', b'Zaragoza'), (b'Zarzal', b'Zarzal'), (b'Zetaquira', b'Zetaquira'), (b'Zipacon', b'Zipacon'), (b'Zipaquira', b'Zipaquira')]),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='telefono_celular',
            field=models.CharField(max_length=15, blank=True),
        ),
    ]