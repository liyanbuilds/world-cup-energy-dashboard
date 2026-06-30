# Hidden Energy Behind World Cup 2026

How much energy does the world's biggest sporting event actually consume?

This project estimates the hidden energy footprint of FIFA World Cup 2026 using public data and simple energy modeling. The goal is to turn abstract energy numbers into something people can understand, compare, and share.

## Why this project

Most people see goals, stadiums, travel, and fans.

I want to explore the infrastructure behind the tournament:

- Stadium operations
- Lighting and cooling
- Broadcasting
- Fan travel
- Digital streaming
- Local grid carbon intensity

## MVP

The first version will focus on a simple energy counter:

- Games played
- Estimated cumulative electricity use
- Human-friendly equivalents
- Top energy matches
- Host city comparison

## Possible future features

- Team travel footprint
- Streaming and data center energy estimate
- Match-day weather impact
- Carbon intensity by host city
- Interactive energy map

## Data sources

Planned public data sources include:

- FIFA match schedule
- Stadium capacity and host city data
- Weather data
- Grid emission factors
- Public stadium sustainability reports

## Estimation Methodology V0

Goal:
Estimate electricity consumption of a World Cup match.

Inputs:
- Stadium capacity
- Attendance
- Stadium type

Assumption:

Low Case:
30 MWh / match

Base Case:
60 MWh / match

High Case:
100 MWh / match

## How to Run Locally

```bash
source .venv/bin/activate
python -m streamlit run dashboard/app.py

## Build Log

### Day 1
- Created repository
- Defined project vision

### Day 2
- Collected first stadium dataset
- Drafted estimation methodology

### Day 3
- Set up the local development environment with VS Code
- Created a Python virtual environment (`.venv`)
- Installed Streamlit and project dependencies
- Built the first Streamlit dashboard prototype
- Ran the dashboard locally
- Committed and pushed the first dashboard code to GitHubgit 


### Day 4

- Added the first energy estimation model
- Created Low / Base / High energy scenarios
- Added a games played slider
- Calculated total estimated stadium energy
- Converted MWh into equivalent annual household electricity use

