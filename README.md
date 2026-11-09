# Clean Air Graph
### A Spatiotemporal Graph Pipeline for Air Quality Analysis in Riga

## 1. Project Overview

Air quality is an important environmental factor that can vary across geographical areas and over time. Understanding these variations requires more than examining individual monitoring measurements; it also involves considering the geographical relationships between locations and the temporal patterns of recorded observations.

The **Clean Air Graph** project explores how graph database technology can be applied to analyse air-quality patterns across the neighbourhoods of Riga. The project focuses on PM2.5 measurements and uses a spatiotemporal graph model to connect monitoring stations, observations and geographical districts.

The main objective is to develop a reproducible data pipeline that transforms air-quality and geographical datasets into a graph representation using Neo4j.

## 2. Project Objectives

The project aims to:

- Collect and examine relevant air-quality data for Riga.
- Prepare and standardize environmental observations for analysis.
- Represent Riga neighbourhoods and their geographical relationships.
- Develop a graph data model using Neo4j.
- Identify pollution episodes based on PM2.5 measurements.
- Investigate temporal and geographical patterns through graph queries.
- Evaluate the correctness and performance of the developed solution.

## 3. Research Focus

The central research question is:

**How can a spatiotemporal graph database support the identification and analysis of air-pollution episodes across geographically connected neighbourhoods?**

An additional investigation considers whether precomputed pollution episodes can improve the efficiency of repeated temporal and neighbourhood-based graph queries compared with querying raw hourly observations.

## 4. Data Sources

The project plans to use the following sources:

| Source | Purpose |
|---|---|
| European Environment Agency (EEA) | Air-quality measurements |
| Riga Municipal Air Quality Monitoring | Local monitoring information |
| GEO RĪGA | Riga neighbourhood geographical boundaries |

The availability and completeness of PM2.5 measurements will be examined before conducting the planned analysis.

## 5. Technology Stack

The planned technologies include:

- **Python** – data collection, processing and pipeline implementation.
- **Neo4j** – graph database storage and querying.
- **Cypher** – graph query language.
- **Pandas** – data inspection and transformation.
- **GeoPandas / Shapely** – geographical data processing.
- **Streamlit** – interactive data presentation (planned).

## 6. Graph Data Model

The proposed graph model includes four main node types:

- `Sensor` – represents an air-quality monitoring station.
- `District` – represents a Riga neighbourhood.
- `Observation` – stores an individual air-quality measurement.
- `Episode` – represents a continuous period of elevated pollution according to the project's defined rules.

The model will use relationships such as:

- `LOCATED_IN`
- `OBSERVED`
- `IN_DISTRICT`
- `NEIGHBOUR_OF`

This structure is intended to connect environmental measurements with their spatial and temporal context.

## 7. Project Structure

```text
clean-air-graph/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── src/
├── notebooks/
├── cypher/
├── dashboard/
├── docs/
├── tests/
│
├── README.md
├── requirements.txt
└── .gitignore
```

## 8. Project Documentation

Additional project documentation is maintained in the `docs/` directory.

- `data_sources.md` – overview of selected data sources and collection plans.
- `data_quality_testing.md` – data quality assessment and testing strategy.
- `testing_plan.md` – planned system testing activities (if maintained separately).

## 9. Expected Outcome

The expected outcome is a reproducible graph-based pipeline that stores air-quality observations and geographical relationships in Neo4j. The implementation will support the identification of pollution episodes and enable temporal and neighbourhood-based analysis through graph queries.

The final evaluation will consider data quality, correctness of the graph model, analytical query results and query performance.

---

*Project status: Under development.*