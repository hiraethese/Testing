Feature: Purchasing products

    Background:
        Given the user is on the website

    Scenario Outline: Adding an item from the list to the shopping cart
        Given the user is on the main page
        When the user clicks on <product_name> button with a shopping cart icon
        Then <product_name> is added to the shopping cart
        And the user receives an addition notification

    Examples:
        | product_name  |
        | MacBook       |
        | iPhone        |

    Scenario Outline: Adding multiple items to the shopping cart
        Given the user has navigated to the page of <product_name>
        When the user enters <product_quantity> in the "Qty" input field
        And the user clicks on "Add to Cart" button
        Then <product_name> in the amount of <product_quantity> is added to the shopping cart
        And the user receives an addition notification

    Examples:
        | product_name  | product_quantity  |
        | MacBook       | 5                 |
        | iPhone        | 999999            |
        | MacBook       | -100              |

    Scenario Outline: Removing an item from the mini shopping cart
        Given the user clicked on the shopping cart button
        And the shopping cart is not empty
        When the user clicks on the cross button of <product_name>
        Then <product_name> is removed from the shopping list
        And the user receives a deletion notification

    Examples:
        | product_name  |
        | iPhone        |
        | MacBook       |

    Scenario Outline: Removing an item from the shopping cart
        Given the user has navigated to the shopping cart page
        And the shopping cart is not empty
        When the user clicks on the cross button of <product_name>
        Then <product_name> is removed from the shopping list
        And the user receives a deletion notification

    Examples:
        | product_name  |
        | MacBook       |
        | iPhone        |

    Scenario Outline: Editing the number of items in the shopping cart
        Given the user has navigated to the shopping cart page
        When the user enters <product_quantity> in the "Quantity" input field of <product_name>
        And the user clicks the "Update" button
        Then <product_name> in the amount of <product_quantity> is in the shopping cart
        And the user receives a modification notification

    Examples:
        | product_name  | product_quantity  |
        | MacBook       | 10                |
        | MacBook       | 1000000           |
