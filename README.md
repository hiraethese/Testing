# ITS Projekt 1

- **Autor:** Illia Baturov (xbatur00)
- **Datum:** 2024-04-07

## Matice pokrytí artefaktů

Čísla testů jednoznačně identifikují scénář v souborech `.feature`.

| Page                    | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 |
|-------------------------|---|---|---|---|---|---|---|---|---|----|----|----|----|----|
| Search user page        | x | x | x | x | x |   |   | x |   |    |    |    |    |    |
| Main user page          | x | x |   |   |   | x |   | x |   |    |    |    |    |    |
| Any product user page   | x | x |   |   |   |   | x | x |   |    |    |    |    |    |
| Shopping cart user page | x | x |   |   |   | x | x | x | x | x  |    |    |    |    |
| "Products" admin page   |   |   |   |   |   |   |   |   |   |    | x  | x  | x  | x  |
| Any product admin page  |   |   |   |   |   |   |   |   |   |    |    | x  | x  |    |
| "Add New" admin page    |   |   |   |   |   |   |   |   |   |    |    |    |    | x  |


## Matice pokrytí aktivit

| Activities                                 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 |
|--------------------------------------------|---|---|---|---|---|---|---|---|---|----|----|----|----|----|
| Searching with empty criteria              | x |   |   |   |   |   |   |   |   |    |    |    |    |    |
| Searching for a product by name            |   | x | x |   |   |   |   |   |   |    |    |    |    |    |
| Searching for a product by category        |   |   | x |   | x |   |   |   |   |    |    |    |    |    |
| Searching in descriptions                  |   |   |   | x | x |   |   |   |   |    |    |    |    |    |
| Adding a product to the cart               |   |   |   |   |   | x | x |   |   | x  |    |    |    |    |
| Removing a product from the cart           |   |   |   |   |   |   |   | x | x | x  |    |    |    |    |
| Editing product quantity in the cart       |   |   |   |   |   | x | x |   |   | x  |    |    |    |    |
| Remove product from the store              |   |   |   |   |   |   |   |   |   |    | x  |    |    |    |
| Editing a product description in the store |   |   |   |   |   |   |   |   |   |    |    | x  | x  | x  |
| Add a new product to the store             |   |   |   |   |   |   |   |   |   |    |    |    |    | x  |


## Matice Feature-Test

| Feature file       | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 |
|--------------------|---|---|---|---|---|---|---|---|---|----|----|----|----|----|
| search.feature     | x | x | x | x | x |   |   |   |   |    |    |    |    |    |
| purchase.feature   |   |   |   |   |   | x | x | x | x | x  |    |    |    |    |
| management.feature |   |   |   |   |   |   |   |   |   |    | x  | x  | x  | x  |

