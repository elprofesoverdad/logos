flowchart TB

%% NIVEL 1: Núcleo del Nexus
MMA["Mundo Mejor Asesores UK (estructura tecnológica, mediadora y formadora)"]

%% NIVEL 2: Actores estratégicos
INFLU["Influencers / Hosts (gestionan cadenas de promoción y formación)"]
FORM["Formadores / Mentores (capacitan dentro del sistema elearning)"]
EMP["Empresas / Fábricas (proveen productos y servicios)"]
COW["Coworkings (centros de logística, formación y gestión local)"]
EVENTOS["Ferias, Expos, Congresos (activación masiva y visibilidad)"]

%% NIVEL 3: Agentes Clusterizadores
IGLESIA["Instituciones: Iglesia, Cámaras, ONG (activan y sostienen clústeres)"]

%% NIVEL 4: Clústeres
CL1["Clúster Comercial / Industrial"]
CL2["Clúster Turístico / Cultural"]
CL3["Clúster Institucional / Eclesial"]

%% CONEXIONES FUNCIONALES
MMA -->|Media contratos, automatiza procesos, entrega plataforma| EMP
MMA -->|Diseña sistema formativo eLearning, integra contenidos| FORM
MMA -->|Suministra CRM, ecommerce, seguimiento automatizado| INFLU
MMA -->|Coordina reservas, logística de espacios, soporte físico| COW
MMA -->|Implementa herramientas digitales para inscripción, datos, acceso| EVENTOS

INFLU -->|Promocionan productos y servicios con enlaces afiliados| EMP
INFLU -->|Canalizan estudiantes hacia mentores, consolidan comunidad| FORM
FORM -->|Forman nuevos promotores, generan contenido educativo| INFLU
FORM -->|Ofrecen programas formativos a empresas y clusters| EMP

EMP -->|Entregan productos y servicios, pagan comisiones escalables| CL1
EMP -->|Participan en ferias para networking y activación comercial| EVENTOS
INFLU -->|Generan tráfico turístico-digital, visibilidad en redes| CL2
COW -->|Facilitan oficinas, salas de formación y operación territorial| CL3

IGLESIA -->|Activa un clúster institucional, vincula fieles y recursos| CL3
EVENTOS -->|Generan prospectos calificados y posicionamiento zonal| CL1
EVENTOS -->|Facilitan encuentros culturales y turísticos estratégicos| CL2

%% RELACIONES ENTRE CLÚSTERES
CL1 -->|Comparte productos, logística y flujo económico| CL2
CL2 -->|Difunde formación, promueve cultura local| CL3
CL3 -->|Activa valores éticos, compromiso comunitario| CL1

%% FLUJOS DE MADURACIÓN DE RELACIONES (Hooks logrados)
INFLU -->|Relación madura: promoción con propósito, con trazabilidad y comisión justa| EMP
FORM -->|Relación madura: formación ética, rentable y escalable| INFLU
EMP -->|Relación madura: ventas automatizadas con retorno social| CL1
IGLESIA -->|Relación madura: participación institucional sostenible| CL3
