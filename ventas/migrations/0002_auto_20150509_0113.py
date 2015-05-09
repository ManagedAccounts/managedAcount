# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='tipo_comprobante',
            field=models.CharField(max_length=2, choices=[(b'00', b'Otros'), (b'01', b'Factura'), (b'02', b'Recibo por Honorarios'), (b'03', b'Boleta de Venta'), (b'04', b'Liquidaci\xc3\xb3n de Compra'), (b'05', b'Boleto de compa\xc3\xb1\xc3\xada de aviaci\xc3\xb3n comercial por el servicio de transporte a\xc3\xa9reo de pasajeros'), (b'06', b'Carta de porte a\xc3\xa9reo por el servicio de transporte de carga a\xc3\xa9rea'), (b'07', b'Nota de cr\xc3\xa9dito'), (b'08', b'Nota de d\xc3\xa9bito'), (b'09', b'Gu\xc3\xada de remisi\xc3\xb3n - Remitente'), (b'10', b'Recibo por Arrendamiento'), (b'11', b'P\xc3\xb3liza emitida por las Bolsas de Valores, Bolsas de Productos o Agentes de Intermediaci\xc3\xb3n por operaciones realizadas en las Bolsas de Valores o Productos o fuera de las mismas, autorizadas por CONASEV'), (b'12', b'Ticket o cinta emitido por m\xc3\xa1quina registradora'), (b'13', b'Documento emitido por bancos, instituciones financieras, crediticias y de seguros que se encuentren bajo el control de la Superintendencia de Banca y Seguros'), (b'14', b'Recibo por servicios p\xc3\xbablicos de suministro de energ\xc3\xada el\xc3\xa9ctrica, agua, tel\xc3\xa9fono, telex y telegr\xc3\xa1ficos y otros servicios complementarios que se incluyan en el recibo de servicio p\xc3\xbablico'), (b'15', b'Boleto emitido por las empresas de transporte p\xc3\xbablico urbano de pasajeros'), (b'16', b'Boleto de viaje emitido por las empresas de transporte p\xc3\xbablico interprovincial de pasajeros dentro del pa\xc3\xads'), (b'17', b'Documento emitido por la Iglesia Cat\xc3\xb3lica por el arrendamiento de bienes inmuebles'), (b'18', b'Documento emitido por las Administradoras Privadas de Fondo de Pensiones que se encuentran bajo la supervisi\xc3\xb3n de la Superintendencia de Administradoras Privadas de Fondos de Pensiones'), (b'19', b'Boleto o entrada por atracciones y espect\xc3\xa1culos p\xc3\xbablicos'), (b'20', b'Comprobante de Retenci\xc3\xb3n'), (b'21', b'Conocimiento de embarque por el servicio de transporte de carga mar\xc3\xadtima'), (b'22', b'Comprobante por Operaciones No Habituales'), (b'23', b'P\xc3\xb3lizas de Adjudicaci\xc3\xb3n emitidas con ocasi\xc3\xb3n del remate o adjudicaci\xc3\xb3n de bienes por venta forzada, por los martilleros o las entidades que rematen o subasten bienes por cuenta de terceros'), (b'24', b'Certificado de pago de regal\xc3\xadas emitidas por PERUPETRO S.A'), (b'25', b'Documento de Atribuci\xc3\xb3n (Ley del Impuesto General a las Ventas e Impuesto Selectivo al Consumo, Art. 19\xc2\xba, \xc3\xbaltimo p\xc3\xa1rrafo, R.S. N\xc2\xb0 022-98-SUNAT).'), (b'26', b'Recibo por el Pago de la Tarifa por Uso de Agua Superficial con fines agrarios y por el pago de la Cuota para la ejecuci\xc3\xb3n de una determinada obra o actividad acordada por la Asamblea General de la Comisi\xc3\xb3n de Regantes o Resoluci\xc3\xb3n expedida por el Jefe de la Unidad de Aguas y de Riego (Decreto Supremo N\xc2\xb0 003-90-AG, Arts. 28 y 48)'), (b'27', b'Seguro Complementario de Trabajo de Riesgo'), (b'28', b'Tarifa Unificada de Uso de Aeropuerto'), (b'29', b'Documentos emitidos por la COFOPRI en calidad de oferta de venta de terrenos, los correspondientes a las subastas p\xc3\xbablicas y a la retribuci\xc3\xb3n de los servicios que presta'), (b'30', b'Documentos emitidos por las empresas que desempe\xc3\xb1an el rol adquirente en los sistemas de pago mediante tarjetas de cr\xc3\xa9dito y d\xc3\xa9bito'), (b'31', b'Gu\xc3\xada de Remisi\xc3\xb3n - Transportista'), (b'32', b'Documentos emitidos por las empresas recaudadoras de la denominada Garant\xc3\xada de Red Principal a la que hace referencia el numeral 7.6 del art\xc3\xadculo 7\xc2\xb0 de la Ley N\xc2\xb0 27133 \xe2\x80\x93 Ley de Promoci\xc3\xb3n del Desarrollo de la Industria del Gas Natural'), (b'34', b'Documento del Operador'), (b'35', b'Documento del Part\xc3\xadcipe'), (b'36', b'Recibo de Distribuci\xc3\xb3n de Gas Natural'), (b'37', b'Documentos que emitan los concesionarios del servicio de revisiones t\xc3\xa9cnicas vehiculares, por la prestaci\xc3\xb3n de dicho servicio'), (b'40', b'Constancia de Dep\xc3\xb3sito - IVAP (Ley 28211)'), (b'50', b'Declaraci\xc3\xb3n \xc3\x9anica de Aduanas - Importaci\xc3\xb3n definitiva'), (b'52', b'Despacho Simplificado - Importaci\xc3\xb3n Simplificada'), (b'53', b'Declaraci\xc3\xb3n de Mensajer\xc3\xada o Courier'), (b'54', b'Liquidaci\xc3\xb3n de Cobranza'), (b'87', b'Nota de Cr\xc3\xa9dito Especial'), (b'88', b'Nota de D\xc3\xa9bito Especial'), (b'91', b'Comprobante de No Domiciliado'), (b'96', b'Exceso de cr\xc3\xa9dito fiscal por retiro de bienes'), (b'97', b'Nota de Cr\xc3\xa9dito - No Domiciliado'), (b'98', b'Nota de D\xc3\xa9bito - No Domiciliado'), (b'99', b'Otros -  Consolidado de Boletas de Venta')]),
        ),
    ]
