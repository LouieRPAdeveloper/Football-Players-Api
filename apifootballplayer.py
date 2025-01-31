from flask import Flask, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)
players = [
  {
    "name": "Arturo Vidal",
    "age": 35,
    "position": "Midfielder",
    "club": "Inter Milan",
    "nationality": "Chile",
    "image": "https://dalealbo.cl/__export/1629936947276/sites/dalealbo/img/2021/08/25/arturo-vidal_crop1629936946130.jpg_1159711837.jpg",
    "atribute":{
      "ATT":50,
      "TEC":53,
      "TAC":54,
      "DEF":51,
      "CRE":54,
    },
    "value_player":"1.5M €",
  },
  {
    "name": "Alexis Sanchez",
    "age": 34,
    "position": "Forward",
    "club": "Olympique Marseille",
    "nationality": "Chile",
    "image": "https://www.encancha.cl/resizer/T4tx1hi-sPU_hAi8tSoJCiZ8kFw=/800x0/filters:format(jpg):quality(70)/cloudfront-us-east-1.images.arcpublishing.com/palco/EIFDKQYCDVAJRK7YCYNP42GEYE.jpg",
    "atribute":{
      "ATT":77,
      "TEC":87,
      "TAC":48,
      "DEF":25,
      "CRE":65,
    },
    "value_player":"4.3M €",
  },
  {
    "name": "Claudio Bravo",
    "age": 39,
    "position": "Goalkeeper",
    "club": "Real Betis Balompie",
    "nationality": "Chile",
    "image": "https://bolavip.com/__export/1571504998784/sites/bolavip/img/2019/10/19/claudio-bravo-capitan_274494_1_5d7259c5275f5_crop1571504998331.jpg_1159711837.jpg",
    "atribute":{
      "ATT":77,
      "TEC":48,
      "TAC":87,
      "DEF":73,
      "CRE":72,
    },
    "value_player":"900K €",
  },
  {
    "name": "Ben Brereton Diaz",
    "age": 23,
    "position": "Forward",
    "club": "Villarreal CF",
    "nationality": "Chile",
    "image": "https://publimicro.cl/wp-content/uploads/2021/11/Club-de-Ben-Brereton-pone-precios-a-sus-servicios-y-se-torna-uno-de-los-ma%CC%81s-caros-en-la-historia-del-fu%CC%81tbol-chileno.jpeg",
  "atribute":{
      "ATT":64,
      "TEC":51,
      "TAC":38,
      "DEF":33,
      "CRE":49,
    },
    "value_player":"15.4M €",
  },
  {
    "name": "Brayan Cortez",
    "age": 27,
    "position": "Goalkeeper",
    "club": "Colo Colo",
    "nationality": "Chile",
    "image": "https://redgol.cl/__export/1682688472247/sites/redgol/img/2023/04/28/brayan_cortes_colo_colo_x2x_crop1682688313367.jpg_1159711837.jpg",
    "atribute":{
      "ATT":66,
      "TEC":59,
      "TAC":62,
      "DEF":62,
      "CRE":64,
    },
    "value_player":"2.4M €",
  },
  {
    "name": "Neymar",
    "age": 31,
    "position": "Forward",
    "club": "Paris Saint Germain",
    "nationality": "Brazil",
    "image": "https://bolavip.com/__export/1658948543647/sites/bolavip/img/2022/07/27/neymar_jrx_paris_saint_germain.jpeg_1159711837.jpeg",
    "atribute":{
      "ATT":88,
      "TEC":73,
      "TAC":53,
      "DEF":23,
      "CRE":91,
    },
    "value_player":"64M €",
  },
  {
    "name": "Vinicius Junior",
    "age": 21,
    "position": "Forward",
    "club": "Real Madrid CF",
    "nationality": "Brazil",
    "image": "https://bolavip.com/__export/1653231197348/sites/bolavip/img/2022/05/22/vinicius_junior_of_real_madrid.jpg_1159711837.jpg",
    "atribute":{
      "ATT":82,
      "TEC":68,
      "TAC":58,
      "DEF":26,
      "CRE":77,
    },
    "value_player":"156M €",
  },
  
  {
    "name": "Allison Becker",
    "age": 26,
    "position": "Goalkeeper",
    "club": "Liverpool FC",
    "nationality": "Brazil",
    "image": "https://bolavip.com/__export/1669320010638/sites/bolavip/img/2022/11/24/alissson_becker_brasil_arquero_qatar_2022_primer_plano.jpg_1159711837.jpg",
    "atribute":{
      "ATT":83,
      "TEC":74,
      "TAC":90,
      "DEF":87,
      "CRE":75,
    },
    "value_player":"38M €",
  },
   {
    "name": "Thiago SIlva",
    "age": 36,
    "position": "Defense",
    "club": "Chelsea FC",
    "nationality": "Brazil",
    "image": "https://redgol.cl/__export/1647973067518/sites/redgol/img/2022/03/22/thiago_silva_chile_brasil_crop1647973065027.jpeg_1159711837.jpeg",
    "atribute":{
      "ATT":39,
      "TEC":54,
      "TAC":87,
      "DEF":91,
      "CRE":51,
    },
    "value_player":"1.9M €",
  },
  {
    "name": "Ederson Moraes",
    "age": 29,
    "position": "Goalkeeper",
    "club": "Manchester City FC",
    "nationality": "Brazil",
    "image": "https://bolavip.com/__export/1596637272862/sites/bolavip/img/2020/08/05/gettyimages-1259219251_crop1596637272344.jpg_1159711837.jpg",
    "atribute":{
      "ATT":71,
      "TEC":69,
      "TAC":73,
      "DEF":87,
      "CRE":67,
    },
    "value_player":"37M €",
  },
  {
    "name": "Lionel Messi",
    "age": 36,
    "position": "Forward",
    "club": "Inter Miami FC",
    "nationality": "Argentina",
    "image": "https://bolavip.com/__export/1621253019130/sites/bolavip/img/2021/05/17/gettyimages_x68x_crop1621250888022.jpg_1159711837.jpg",
    "atribute":{
      "ATT":95,
      "TEC":94,
      "TAC":73,
      "DEF":28,
      "CRE":91,
    },
    "value_player":"38M €",
  },
  {
    "name": "Angel Di Maria",
    "age": 37,
    "position": "Forward",
    "club": "Benfica",
    "nationality": "Argentina",
    "image": "https://bolavip.com/__export/1654620855859/sites/bolavip/img/2022/06/07/angel_di_maria_seleccion_argentina_festejo_clasico.jpg_1159711837.jpg",
    "atribute":{
      "ATT":79,
      "TEC":77,
      "TAC":52,
      "DEF":27,
      "CRE":79,
    },
    "value_player":"8.5M €",
  },

  {
    "name": "Julian Alvarez",
    "age": 23,
    "position": "Forward",
    "club": "Manchester City",
    "nationality": "Argentina",
    "image": "https://bolavip.com/__export/1657290331989/sites/bolavip/img/2022/07/08/julian_alvarez_nuevo_jugador_manchester_city.jpg_1159711837.jpg",
    "atribute":{
      "ATT":79,
      "TEC":68,
      "TAC":62,
      "DEF":41,
      "CRE":61,
    },
    "value_player":"58M €",
  },
  {
    "name": "Lautaro Martinez",
    "age": 27,
    "position": "Forward",
    "club": "Inter Milan",
    "nationality": "Argentina",
    "image": "https://bolavip.com/__export/1638983269972/sites/bolavip/img/2021/12/08/inter_de_milan_lautaro_martinez_motivo_por_el_que_no_lo_ficha_bayern_crop1638983133643.jpg_1159711837.jpg",
    "atribute":{
      "ATT":80,
      "TEC":58,
      "TAC":65,
      "DEF":34,
      "CRE":62,
    },
    "value_player":"80M €",
  },
  {
    "name": "Emiliano Martinez",
    "age": 27,
    "position": "Goalkeeper",
    "club": "Aston Villa",
    "nationality": "Argentina",
    "image": "https://s3.amazonaws.com/charitycdn/cache/resizedcrop-ad66248a11d38e6d822a5f165882a230-800x800.jpg",
    "atribute":{
      "ATT":80,
      "TEC":67,
      "TAC":79,
      "DEF":81,
      "CRE":76,
    },
    "value_player":"27M €",
  },
  
  {
    "name": "Harry Kane",
    "age": 30,
    "position": "Forward",
    "club": "Tottenham",
    "nationality": "England",
    "image": "https://bolavip.com/__export/1658597111910/sites/bolavip/img/2022/07/23/harry_kane_tottenham_bayern_interes.jpg_1159711837.jpg",
    "atribute":{
      "ATT":91,
      "TEC":73,
      "TAC":74,
      "DEF":27,
      "CRE":70,
    },
    "value_player":"98M €",
  },
  
  {
    "name": "Marcus Rashford",
    "age": 25,
    "position": "Forward",
    "club": "Manchester United",
    "nationality": "England",
    "image": "https://bolavip.com/__export/1679516615162/sites/bolavip/img/2023/03/22/rashford_crop1679516613955.jpg_1159711837.jpg",
    "atribute":{
      "ATT":71,
      "TEC":61,
      "TAC":49,
      "DEF":29,
      "CRE":58,
    },
    "value_player":"76M €",
  },
  {
    "name": "Jaime Vardy",
    "age": 35,
    "position": "Forward",
    "club": "Leicester City",
    "nationality": "England",
    "image": "https://bolavip.com/__export/1623852516308/sites/bolavip/img/2021/06/16/estados_unidos_jamie_vardy_rochester_rhinos.jpg_1159711837.jpg",
    "atribute":{
      "ATT":69,
      "TEC":50,
      "TAC":45,
      "DEF":23,
      "CRE":53,
    },
    "value_player":"2.4M €",
  },
  
  {
    "name": "Jordan Pickford",
    "age": 28,
    "position": "Goalkeeper",
    "club": "Everton",
    "nationality": "England",
    "image": "https://bolavip.com/__export/1644931616176/sites/bolavip/img/2022/02/15/jordan_pickford.jpg_1159711837.jpg",
    "atribute":{
      "ATT":80,
      "TEC":56,
      "TAC":60,
      "DEF":78,
      "CRE":63,
    },
    "value_player":"24M €",
  },
  
  {
    "name": "Luke Shaw",
    "age": 28,
    "position": "Defense",
    "club": "Manchester United",
    "nationality": "England",
    "image": "https://caracol.com.co/resizer/OZ1sxfp_bDJB82rdJevptvg3pKk=/800x800/filters:format(jpg):quality(70)/cloudfront-us-east-1.images.arcpublishing.com/prisaradioco/W2R736IRLVPHXIFNFNNE6362IM.jpg",
    "atribute":{
      "ATT":49,
      "TEC":58,
      "TAC":54,
      "DEF":67,
      "CRE":65,
    },
    "value_player":"39M €",
  },
  
  {
    "name": "David De Gea",
    "age": 31,
    "position": "Goalkeeper",
    "club": "Manchester United",
    "nationality": "Spain",
    "image": "https://cms.somosfanaticos.com/__export/1661199092777/sites/fanaticos/img/2022/08/22/de_gea_head_crop1661199092049.jpg_1159711837.jpg",
    "atribute":{
      "ATT":79,
      "TEC":55,
      "TAC":58,
      "DEF":74,
      "CRE":60,
    },
    "value_player":"18M €",
  },
  
  {
    "name": "Alvaro Morata",
    "age": 29,
    "position": "Forward",
    "club": "Atletico Madrid",
    "nationality": "Spain",
    "image": "https://bolavip.com/__export/1654212056606/sites/bolavip/img/2022/06/02/alvaro-morata-espaxa-020622-getty_crop1654212037785.jpg_1159711837.jpg",
    "atribute":{
      "ATT":72,
      "TEC":56,
      "TAC":42,
      "DEF":32,
      "CRE":55,
    },
    "value_player":"21M €",
  },
  
  {
    "name": "Gerard Moreno",
    "age": 27,
    "position": "Forward",
    "club": "Villarreal CF",
    "nationality": "Spain",
    "image": "https://soyreferee.com/sites/referee/img/2021/05/12/gerard-moreno-1.jpeg",
    "atribute":{
      "ATT":78,
      "TEC":69,
      "TAC":66,
      "DEF":32,
      "CRE":72,
    },
    "value_player":"19.4M €",
  },
  
  {
    "name": "Dani Carvajal",
    "age": 32,
    "position": "Defense",
    "club": "Real Madrid",
    "nationality": "Spain",
    "image": "https://bolavip.com/__export/1636522514457/sites/bolavip/img/2021/11/10/dani-carvajal-real-madrid-101121-getty_crop1636522488888.jpg_1159711837.jpg",
    "atribute":{
      "ATT":40,
      "TEC":47,
      "TAC":53,
      "DEF":65,
      "CRE":58,
    },
    "value_player":"11.6M €",
  },
  
  {
    "name": "Sergio Ramos",
    "age": 37,
    "position": "Defense",
    "club": "Paris Saint Germain",
    "nationality": "Spain",
    "image": "https://bolavip.com/__export/1623960585799/sites/bolavip/img/2021/06/17/sergio_ramos_madrid.jpg_1159711837.jpg",
    "atribute":{
      "ATT":40,
      "TEC":56,
      "TAC":74,
      "DEF":68,
      "CRE":50,
    },
    "value_player":"38M €",
  },
  
  {
    "name": "Manuel Neuer",
    "age": 35,
    "position": "Goalkeeper",
    "club": "Bayern Munich",
    "nationality": "Germany",
    "image": "https://img.fcbayern.com/image/upload/t_cms-1x1-seo-thumbnail/v1641729906/cms/public/images/fcbayern-com/homepage/saison-21-22/Profis/Neuer/210918_Neuer_GET.jpg",
    "atribute":{
      "ATT":85,
      "TEC":73,
      "TAC":76,
      "DEF":97,
      "CRE":68,
    },
    "value_player":"7.2M €",
  },
  
  {
    "name": "Joshua Kimmich",
    "age": 26,
    "position": "Midfielder",
    "club": "Bayern Munich",
    "nationality": "Germany",
    "image": "https://img.fcbayern.com/image/upload/t_cms-1x1-seo-thumbnail/v1604107897/cms/public/images/fcbayern-com/homepage/saison-20-21/profis/kimmich/200918_kimmich_get.jpg",
    "atribute":{
      "ATT":72,
      "TEC":77,
      "TAC":82,
      "DEF":65,
      "CRE":92,
    },
    "value_player":"82M €",
  },
  
  {
    "name": "Leon Goretzka",
    "age": 27,
    "position": "Midfielder",
    "club": "Bayern Munich",
    "nationality": "Germany",
    "image": "https://img.fcbayern.com/image/upload/t_cms-1x1-seo-thumbnail/v1601352725/cms/public/images/fcbayern-com/homepage/saison-19-20/profis/goretzka/200125_goretzka_get.png",
    "atribute":{
      "ATT":60,
      "TEC":56,
      "TAC":54,
      "DEF":53,
      "CRE":67,
    },
    "value_player":"41M €",
  },
  
  {
    "name": "Mats Hummels",
    "age": 34,
    "position": "Defense",
    "club": "Borussia Dortmund",
    "nationality": "Germany",
    "image": "https://img.fcbayern.com/image/upload/t_cms-1x1-seo-thumbnail/v1601347106/cms/public/images/fcbayern-com/homepage/saison-18-19/profis/hummels/181002_hummels_get.jpg",
    "atribute":{
      "ATT":40,
      "TEC":57,
      "TAC":75,
      "DEF":79,
      "CRE":54,
    },
    "value_player":"5.5M €",
  },
  {
    "name": "Leroy Sane",
    "age": 22,
    "position": "Forward",
    "club": "Bayern Munich",
    "nationality": "Germany",
    "image": "https://img.fcbayern.com/image/upload/t_cms-1x1-seo-thumbnail/v1604025264/cms/public/images/fcbayern-com/homepage/saison-20-21/profis/sane/sane169fakten.jpg",
    "atribute":{
      "ATT":74,
      "TEC":78,
      "TAC":42,
      "DEF":32,
      "CRE":76,
    },
    "value_player":"71M €",
  },
  
  {
    "name": "Christian Pulisic",
    "age": 22,
    "position": "Forward",
    "club": "AC Milan",
    "nationality": "United States of America",
    "image": "https://bolavip.com/__export/1642794817853/sites/bolavip/img/2022/01/21/usmnt_christian_pulisic_mundial.jpg_1159711837.jpg",
    "atribute":{
      "ATT":67,
      "TEC":52,
      "TAC":42,
      "DEF":29,
      "CRE":63,
    },
    "value_player":"38M €",
  },
  {
    "name": "Timothy Weah",
    "age": 23,
    "position": "Forward",
    "club": "Juventus",
    "nationality": "United States of America",
    "image": "https://redgol.cl/__export/1669063027882/sites/redgol/img/2022/11/21/timothy_weah_x2x_crop1669063025989.jpg_1159711837.jpg",
    "atribute":{
      "ATT":55,
      "TEC":57,
      "TAC":44,
      "DEF":44,
      "CRE":55,
    },
    "value_player":"12.7M €",
  },
  {
    "name": "Matt Turner",
    "age": 24,
    "position": "Goalkeeper",
    "club": "Arsenal",
    "nationality": "United States of America",
    "image": "https://bolavip.com/__export/1670025266364/sites/bolavip/img/2022/12/02/turner_es_el_arquero_de_usa.jpg_1159711837.jpg",
    "atribute":{
      "ATT":75,
      "TEC":54,
      "TAC":64,
      "DEF":62,
      "CRE":69,
    },
    "value_player":"8.4M €",
  },
  
  {
    "name": "Ricardo Pepi",
    "age": 23,
    "position": "Forward",
    "club": "Groningen",
    "nationality": "United States of America",
    "image": "https://bolavip.com/__export/1641154810935/sites/bolavip/img/2022/01/02/pepi.jpg_1159711837.jpg",
    "atribute":{
      "ATT":69,
      "TEC":56,
      "TAC":52,
      "DEF":30,
      "CRE":49,
    },
    "value_player":"9.4M €",
  },
  
  {
    "name": "Brenden Aaronson",
    "age": 25,
    "position": "Midfielder",
    "club": "Leeds United",
    "nationality": "United States of America",
    "image": "https://bolavip.com/__export/1661281816747/sites/bolavip/img/2022/08/23/premier_aaronson_leeds.jpg_1159711837.jpg",
    "atribute":{
      "ATT":59,
      "TEC":48,
      "TAC":22,
      "DEF":20,
      "CRE":66,
    },
    "value_player":"26M €",
  },
  
  
  {
    "name": "Hector Herrera",
    "age": 34,
    "position": "Midfielder",
    "club": "Atletico Madrid",
    "nationality": "Mexico",
    "image": "https://bolavip.com/__export/1625701121908/sites/bolavip/img/2021/07/07/hector-herrera-mx-imago_x2x_crop1625699241999.jpg_1287788575.jpg",
    "atribute":{
      "ATT":58,
      "TEC":68,
      "TAC":58,
      "DEF":51,
      "CRE":65,
    },
    "value_player":"2.7M €",
  },
  
  {
    "name": "Guillermo Ochoa",
    "age": 38,
    "position": "Goalkeeper",
    "club": "Salernitana",
    "nationality": "Mexico",
    "image": "https://bolavip.com/__export/1657714981913/sites/bolavip/img/2022/07/13/guillermo_ochoa_crop1657714574749.jpg_1159711837.jpg",
    "atribute":{
      "ATT":70,
      "TEC":47,
      "TAC":57,
      "DEF":72,
      "CRE":57,
    },
    "value_player":"1.4M €",
  },
  
  {
    "name": "Santiago Gimenez",
    "age": 22,
    "position": "Forward",
    "club": "Feyenoord",
    "nationality": "Mexico",
    "image": "https://bolavip.com/__export/1660423864067/sites/bolavip/img/2022/08/13/santi_gimenez_debut_feyenoord_oficial_crop1660423832628.jpg_1159711837.jpg",
    "atribute":{
      "ATT":67,
      "TEC":47,
      "TAC":53,
      "DEF":31,
      "CRE":43,
    },
    "value_player":"26M €",
  },
  
  {
    "name": "Javier Hernandez",
    "age": 35,
    "position": "Forward",
    "club": "Los Angeles Galaxy",
    "nationality": "Mexico",
    "image": "https://bolavip.com/__export/1629738563586/sites/bolavip/img/2021/08/23/chicharito-hernandez-juego-de-estrellas-mls-vs-liga-mx-2021_crop1629738560945.jpg_1159711837.jpg",
    "atribute":{
      "ATT":67,
      "TEC":57,
      "TAC":51,
      "DEF":30,
      "CRE":47,
    },
    "value_player":"2.1M €",
  },
  
  {
    "name": "Raul Jimenez",
    "age": 30,
    "position": "Forward",
    "club": "Fulham",
    "nationality": "Mexico",
    "image": "https://bolavip.com/__export/1669133079364/sites/bolavip/img/2022/11/22/rauljimenez1_crop1669132989006.png_1159711837.png",
    "atribute":{
      "ATT":68,
      "TEC":43,
      "TAC":45,
      "DEF":25,
      "CRE":60,
    },
    "value_player":"6.3M €",
  },
  
  
  {
    "name": "Diego Godin",
    "age": 36,
    "position": "Defense",
    "club": "Velez",
    "nationality": "Uruguay",
    "image": "https://bolavip.com/__export/1639801282055/sites/bolavip/img/2021/12/18/diego-godin-171221-getty_crop1639801257700.jpg_1159711837.jpg",
    "atribute":{
      "ATT":23,
      "TEC":24,
      "TAC":50,
      "DEF":87,
      "CRE":25,
    },
    "value_player":"8M €",
  },
  
  {
    "name": "Jose Maria Gimenez",
    "age": 28,
    "position": "Defense",
    "club": "Atletico Madrid",
    "nationality": "Uruguay",
    "image": "https://bolavip.com/__export/1645044565856/sites/bolavip/img/2022/02/16/jose_maria_gimenez_atletico_de_madrid_levante_laliga_2022_crop1645043782447.jpg_1159711837.jpg",
    "atribute":{
      "ATT":39,
      "TEC":50,
      "TAC":79,
      "DEF":80,
      "CRE":49,
    },
    "value_player":"34M €",
  },
  
  {
    "name": "Luis Suarez",
    "age": 35,
    "position": "Forward",
    "club": "Gremio",
    "nationality": "Uruguay",
    "image": "https://bolavip.com/__export/1671859929091/sites/bolavip/img/2022/12/24/jam_media-luis-suarez-cruz-azul.jpg_263484570.jpg",
    "atribute":{
      "ATT":73,
      "TEC":54,
      "TAC":57,
      "DEF":31,
      "CRE":57,
    },
    "value_player":"3.6M €",
  },
  
  {
    "name": "Edinson Cavani",
    "age": 36,
    "position": "Forward",
    "club": "Valencia CF",
    "nationality": "Uruguay",
    "image": "https://bolavip.com/__export/1629845858786/sites/bolavip/img/2021/08/24/edinson-cavani-uruguay-240821-getty_crop1629845736511.jpg_1159711837.jpg",
    "atribute":{
      "ATT":72,
      "TEC":52,
      "TAC":38,
      "DEF":25,
      "CRE":49,
    },
    "value_player":"3.1M €",
  },
  
  {
    "name": "Giorgian De Arrascaeta",
    "age": 27,
    "position": "Forward",
    "club": "Flamengo",
    "nationality": "Uruguay",
    "image": "https://bolavip.com/__export/1659635751626/sites/bolavip/img/2022/08/04/agif22041300264471.jpg_1159711837.jpg",
    "atribute":{
      "ATT":70,
      "TEC":68,
      "TAC":50,
      "DEF":37,
      "CRE":74,
    },
    "value_player":"19.4M €",
  },
  
  {
    "name": "Keylor Navas",
    "age": 34,
    "position": "Goalkeeper",
    "club": "Paris Saint Germain",
    "nationality": "Costa Rica",
    "image": "https://bolavip.com/__export/1642273544038/sites/bolavip/img/2022/01/15/keylor_navas_psg_interes_newcastle_crop1642273474542.jpg_1159711837.jpg",
    "atribute":{
      "ATT":75,
      "TEC":50,
      "TAC":66,
      "DEF":72,
      "CRE":67,
    },
    "value_player":"4.3M €",
  },
  
  {
    "name": "Bryan Ruiz",
    "age": 36,
    "position": "Forward",
    "club": "Alajuense",
    "nationality": "Costa Rica",
    "image": "https://www.sensaciondeportiva.com/wp-content/uploads/2022/09/Bryan-Ruiz1.jpg",
    "atribute":{
      "ATT":63,
      "TEC":54,
      "TAC":60,
      "DEF":17,
      "CRE":35,
    },
    "value_player":"200K €",
  },
  
  {
    "name": "Roan Wilson",
    "age": 26,
    "position": "Midfielder", 
    "club": "Gil VIcente",
    "nationality": "Costa Rica",
    "image": "https://bolavip.com/__export/1668021271536/sites/bolavip/img/2022/11/09/costarica1_crop1668021151316.png_1159711837.png",
    "atribute":{
      "ATT":23,
      "TEC":54,
      "TAC":50,
      "DEF":57,
      "CRE":55,
    },
    "value_player":"315K €",
  },
  
  {
    "name": "Celso Borges",
    "age": 36,
    "position": "Midfielder", 
    "club": "Alajuense",
    "nationality": "Costa Rica",
    "image": "https://futbolcentroamerica.com/__export/1631652610494/sites/futbolcentroamerica/img/2021/09/14/crc-celso-borges-cnlf_crop1631652562908.jpg_1159711837.jpg",
    "atribute":{
      "ATT":23,
      "TEC":54,
      "TAC":50,
      "DEF":57,
      "CRE":55,
    },
    "value_player":"160K €",
  },
  
  {
    "name": "Pablo Arboine",
    "age": 25,
    "position": "Defense", 
    "club": "Deportivo Saprissa",
    "nationality": "Costa Rica",
    "image": "https://futbolcentroamerica.com/__export/1667340383938/sites/futbolcentroamerica/img/2022/11/01/313427735_10159695857338884_1155600465155142429_n_crop1667338411996.jpg_1159711837.jpg",
    "atribute":{
      "ATT":23,
      "TEC":24,
      "TAC":20,
      "DEF":57,
      "CRE":25,
    },
    "value_player":"275K €",
  },
  
  {
    "name": "Alphonse Davies",
    "age": 24,
    "position": "Defense", 
    "club": "Bayern Munich",
    "nationality": "Canada",
    "image": "https://img.fcbayern.com/image/upload/t_cms-1x1-seo-thumbnail/v1667723002/cms/public/images/fcbayern-com/homepage/Saison-22-23/Profis/Davies/221101-davies-ima.jpg",
    "atribute":{
      "ATT":56,
      "TEC":74,
      "TAC":49,
      "DEF":56,
      "CRE":69,
    },
    "value_player":"68M €",
  },
  {
    "name": "Jonathan David",
    "age": 25,
    "position": "Forward", 
    "club": "Losc Lille",
    "nationality": "Canada",
    "image": "https://bolavip.com/__export/1667084003026/sites/bolavip/img/2022/10/29/jonathan_david_of_lille.jpg_1159711837.jpg",
    "atribute":{
      "ATT":74,
      "TEC":59,
      "TAC":54,
      "DEF":27,
      "CRE":56,
    },
    "value_player":"58M €",
  },
  
  {
    "name": "Cyle Larin",
    "age": 26,
    "position": "Forward", 
    "club": "Real Valladolid",
    "nationality": "Canada",
    "image": "https://i12.haber7.net//haber/haber7/photos/2022/04/BvTeB_1643218754_1998.jpg",
    "atribute":{
      "ATT":69,
      "TEC":48,
      "TAC":34,
      "DEF":23,
      "CRE":51,
    },
    "value_player":"8.2M €",
  },
  
  {
    "name": "Tajon Buchanan",
    "age": 24,
    "position": "Forward", 
    "club": "Brujas",
    "nationality": "Canada",
    "image": "https://bolavip.com/__export/1616301101381/sites/bolavip/img/2021/03/21/tajon_buchanan_of_canada_celebrates_after_scoring_against_el_salvador.jpg_1159711837.jpg",
    "atribute":{
      "ATT":54,
      "TEC":40,
      "TAC":36,
      "DEF":37,
      "CRE":51,
    },
    "value_player":"10.8M €",
  },
  
  {
    "name": "Alistair Johnston",
    "age": 24,
    "position": "Defense", 
    "club": "Celtic FC",
    "nationality": "Canada",
    "image": "https://cdn.canpl.ca/app/uploads/cpl/2021/08/31102544/51323536520_228f89e12d_o-e1630419992796-730x366.jpg",
    "atribute":{
      "ATT":45,
      "TEC":51,
      "TAC":50,
      "DEF":59,
      "CRE":50,
    },
    "value_player":"6.7M €",
  },
  
  {
    "name": "Cristiano Ronaldo",
    "age": 37,
    "position": "Forward",
    "club": "Manchester United",
    "nationality": "Portugal",
    "image": "https://bolavip.com/__export/1630523621284/sites/bolavip/img/2021/09/01/cristiano_ronaldo_rxcord_portugal_histxrico_crop1630522496005.jpg_1159711837.jpg",
    "atribute":{
      "ATT":76,
      "TEC":61,
      "TAC":53,
      "DEF":35,
      "CRE":55,
    },
    "value_player":"16M €",
  },
  {
    "name": "Bernardo Silva",
    "age": 27,
    "position": "Forward",
    "club": "Manchester City",
    "nationality": "Portugal",
    "image": "https://redgol.cl/__export/1669991641086/sites/redgol/img/2022/12/02/por-que-no-juega-bernardo-silva_crop1669991640104.jpg_1159711837.jpg",
    "atribute":{
      "ATT":66,
      "TEC":67,
      "TAC":57,
      "DEF":43,
      "CRE":69,
    },
    "value_player":"77M €",
  },
  {
    "name": "Rui Patricio",
    "age": 34,
    "position": "Goalkeeper",
    "club": "AS Roma",
    "nationality": "Portugal",
    "image": "https://bolavip.com/__export/1626228115345/sites/bolavip/img/2021/07/13/rui_patricio_wolverhampton_130721_getty_crop1626228052194.jpg_1159711837.jpg",
    "atribute":{
      "ATT":73,
      "TEC":58,
      "TAC":61,
      "DEF":75,
      "CRE":60,
    },
    "value_player":"5.3M €",
  },
  {
    "name": "Bruno Fernandes",
    "age": 29,
    "position": "Forward",
    "club": "Manchester United",
    "nationality": "Portugal",
    "image": "https://www.wradio.com.co/resizer/XRw3ZFb_TmsAe7yNRRTOO636NDs=/800x800/filters:format(jpg):quality(70)/cloudfront-us-east-1.images.arcpublishing.com/prisaradioco/HTVBTZXRNFE6HG7YXXBBLD64RM.jpg",
    "atribute":{
      "ATT":79,
      "TEC":78,
      "TAC":58,
      "DEF":44,
      "CRE":94,
    },
    "value_player":"69M €",
  },
  {
    "name": "Ruben Dias",
    "age": 28,
    "position": "Defense",
    "club": "Manchester City",
    "nationality": "Portugal",
    "image": "https://bolavip.com/__export/1647990797182/sites/bolavip/img/2022/03/22/ruben_dias.jpg_1159711837.jpg",
    "atribute":{
      "ATT":38,
      "TEC":52,
      "TAC":78,
      "DEF":81,
      "CRE":47,
    },
    "value_player":"87M €",
  },
  
  {
    "name": "Kylian Mbappé",
    "age": 23,
    "position": "Forward",
    "club": "Paris Saint-Germain",
    "nationality": "France",
    "image": "https://redgol.cl/__export/1665502487372/sites/redgol/img/2022/10/11/mbappe_psg_crop1665502486332.jpg_1159711837.jpg",
    "atribute":{
      "ATT":95,
      "TEC":83,
      "TAC":69,
      "DEF":29,
      "CRE":75,
    },
    "value_player":"191M €",
  },
  {
    "name": "Antoine Griezmann",
    "age": 30,
    "position": "Forward",
    "club": "Atletico Madrid",
    "nationality": "France",
    "image": "https://bolavip.com/__export/1682262517219/sites/bolavip/img/2023/04/23/gettyimages-1450775705.jpg_1879782745.jpg",
    "atribute":{
      "ATT":84,
      "TEC":78,
      "TAC":66,
      "DEF":42,
      "CRE":85,
    },
    "value_player":"24M €",
  },
  {
    "name": "Karim Benzema",
    "age": 35,
    "position": "Forward",
    "club": "Real Madrid CF",
    "nationality": "France",
    "image": "https://bolavip.com/__export/1671108490324/sites/bolavip/img/2022/12/15/puede_jugar_benzema_crop1671108489443.jpg_1159711837.jpg",
    "atribute":{
      "ATT":94,
      "TEC":79,
      "TAC":72,
      "DEF":32,
      "CRE":73,
    },
    "value_player":"26M €",
  },
  {
    "name": "Oliver Giroud",
    "age": 36,
    "position": "Forward",
    "club": "AC Milan",
    "nationality": "France",
    "image": "https://bolavip.com/__export/1669146333291/sites/bolavip/img/2022/11/22/gettyimages-1443625488_crop1669146332461.jpg_1159711837.jpg",
    "atribute":{
      "ATT":77,
      "TEC":56,
      "TAC":55,
      "DEF":34,
      "CRE":52,
    },
    "value_player":"4.1M €",
  },
  
  {
    "name": "Hugo Lloris",
    "age": 37,
    "position": "Goalkeeper",
    "club": "Tottenham",
    "nationality": "France",
    "image": "https://bolavip.com/__export/1642180593488/sites/bolavip/img/2022/01/14/hugo_lloris_francia_arquero_titular_crop1642178243460.jpg_1159711837.jpg",
    "atribute":{
      "ATT":79,
      "TEC":59,
      "TAC":63,
      "DEF":79,
      "CRE":62,
    },
    "value_player":"6.9M €",
  },
]

#debe haber 32 y hay 14 completos
@app.route("/chile-soccer-players")
def get_chile_players():
  return jsonify([player for player in players if player["nationality"] == "Chile"])

@app.route("/brazil-soccer-players")
def get_brazil_players():
  return jsonify([player for player in players if player["nationality"] == "Brazil"])
  
@app.route("/argentina-soccer-players")
def get_argentina_players():
  return jsonify([player for player in players if player["nationality"] == "Argentina"])
  
@app.route("/england-soccer-players")
def get_england_players():
  return jsonify([player for player in players if player["nationality"] == "England"])
  
@app.route("/spain-soccer-players")
def get_spain_players():
  return jsonify([player for player in players if player["nationality"] == "Spain"])  
  
@app.route("/germany-soccer-players")
def get_germany_players():
  return jsonify([player for player in players if player["nationality"] == "Germany"])  

@app.route("/american-soccer-players")
def get_american_players():
  return jsonify([player for player in players if player["nationality"] == "United States of America"])  

@app.route("/mexico-soccer-players")
def get_mexico_players():
  return jsonify([player for player in players if player["nationality"] == "Mexico"])  

@app.route("/uruguay-soccer-players")
def get_uruguay_players():
  return jsonify([player for player in players if player["nationality"] == "Uruguay"])

@app.route("/costarica-soccer-players")
def get_costarica_players():
  return jsonify([player for player in players if player["nationality"] == "Costa Rica"])

@app.route("/canada-soccer-players")
def get_canada_players():
  return jsonify([player for player in players if player["nationality"] == "Canada"])

@app.route("/portugal-soccer-players")
def get_portugal_players():
  return jsonify([player for player in players if player["nationality"] == "Portugal"])

@app.route("/france-soccer-players")
def get_france_players():
  return jsonify([player for player in players if player["nationality"] == "France"])

@cross_origin 
@app.route("/players")
def get_players():
  return jsonify([player for player in players])
  

if __name__ == "__main__":
  app.run(debug=True, port=8000)
