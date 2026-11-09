# Data Sources and Collection

## 1. Overview

The Clean Air Graph project relies on several data sources to investigate air-quality patterns across the neighbourhoods of Riga. The selected sources provide complementary information, including air-quality measurements, monitoring station information and geographical boundaries.

Using multiple sources makes it possible to connect environmental observations with their geographical context and prepare the information for storage in a graph database.

## 2. Identified Data Sources

### 2.1 European Environment Agency (EEA)

The European Environment Agency is one of the planned sources of air-quality observations. Its data will be examined to identify measurements relevant to the project's focus on PM2.5 pollution in Riga.

Source: https://www.eea.europa.eu/en/datahub/datahubitem-view/778ef9f5-6293-4846-badd-56a29c70880d

### 2.2 Riga Municipal Air Quality Monitoring

The Riga municipal monitoring service provides information about local air-quality monitoring activities. This source will be reviewed to identify relevant monitoring stations and determine whether suitable PM2.5 measurements are available.

Source: https://mvd.riga.lv/par-mums/darbibas-jomas/vides-parvalde/gaisa-kvalitate/gaisa-monitorings-riga/

### 2.3 GEO RĪGA Neighbourhood Boundaries

Geographical boundary data from GEO RĪGA will be used to represent the neighbourhoods of Riga. These boundaries provide the spatial foundation for connecting monitoring locations and observations with individual neighbourhoods.

Source: https://data.gov.lv/dati/eng/dataset/rigas_apkaimes

## 3. Planned Data Preparation

Before the data is incorporated into the graph database, the selected datasets will be examined and prepared. The preparation process is expected to include:

- Reviewing the available data fields and formats.
- Identifying relevant PM2.5 measurements.
- Checking the availability of station identifiers and geographical information.
- Standardizing timestamps and measurement units where necessary.
- Identifying missing values and duplicate observations.
- Examining the geographical boundaries required for neighbourhood analysis.

## 4. Integration with the Graph Database

After preparation, the collected information will be used as input for the Neo4j database.

Air-quality monitoring locations will be represented through Sensor nodes, while geographical areas will be represented through District nodes. Individual measurements will be represented as Observation nodes.

This structure is intended to preserve the connection between monitoring stations, their geographical locations and the measurements recorded over time.

## 5. Data Availability Considerations

An important consideration is whether the selected sources provide sufficient PM2.5 measurements for the intended analysis. The availability of monitoring stations does not necessarily mean that every station provides PM2.5 observations.

Therefore, the actual coverage, measurement frequency and availability of historical observations must be examined before deciding which analytical comparisons can be performed.

## 6. Next Steps

The next stage is to inspect the selected datasets, document their available fields and assess their suitability for the planned spatiotemporal analysis.