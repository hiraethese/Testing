# ITS Projekt 1

- **Autor:** Illia Baturov (xbatur00)
- **Datum:** 2024-04-07

## Matice pokrytí artefaktů

Čísla testů jednoznačně identifikují scénář v souborech `.feature`.

| Page | 1 | 2 | 3 | ... |
|----------|---|---|---|-----|
| Page XYZ1 | x | x |   |     |
| Page XYZ2 | x |   | x |     |
| Page ... |   |   | x |  x   |


## Matice pokrytí aktivit

| Activities | 1 | 2 | 3 | ... |
|----------|---|---|---|-----|
| Setting quantity of A to N | x |  | x | |
| Putting XYZ to cart | x |  | x | |
| Frenzy clicking ... | | | | x |
| Checking out | x |  |  |  x  |
| Cancelling ABCD |   | x | x |    |
| Registering ... | x | x | x |    |
| Removing ... | | | | x |


## Matice Feature-Test

| Feature file       | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |10 |11 |12 |13 |14 |
|--------------------|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| search.feature     | x | x | x | x | x |   |   |   |   |   |   |   |   |   |
| purchase.feature   |   |   |   |   |   | x | x | x | x | x |   |   |   |   |
| management.feature |   |   |   |   |   |   |   |   |   |   | x | x | x | x |

