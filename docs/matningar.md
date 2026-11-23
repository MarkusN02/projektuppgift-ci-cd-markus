# Mätningar av pipelinen

Syfte: kunna visa före och efter varje optimering.

| Datum | Körning | Ändring | Test and Lint totalt | Install dependencies | Run Ruff | Run tests |
|---|---|---|---|---|---|---|
| 2026-11-17 | PR #2, körning #4 | Baslinje efter steg 2 (ingen cache) | 14 s | 7 s | 0 s | 1 s |

## Före optimering: hela kedjan

CI Pipeline på main, ubuntu-latest, ingen cache. Tider från körningens
Summary-sida i GitHub Actions.

| Körning | Test and Lint | Build Docker Image | Simulated Deployment | Hela kedjan |
|---|---|---|---|---|
| #24 | 15 s | 14 s | 15 s | 51 s |
| #26 | 22 s | 23 s | 19 s | 1 min 12 s |
| #28 | 14 s | 27 s | 16 s | 1 min 6 s |
| Medel | 17 s | 21 s | 17 s | 1 min 3 s |

### Observationer

- Tiden är jämnt fördelad mellan jobben, ingen tydlig flaskhals.
- Körtiderna varierar mellan körningar (Build 14-27 s), så vi jämför medelvärden.
- Runt 8 s går åt till uppstart av runner mellan jobben.
- Imagen byggs två gånger (Build och Simulated Deployment).