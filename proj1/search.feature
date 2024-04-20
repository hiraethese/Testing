Feature: Searching products

    Background:
        Given the user is on the website

    Scenario: Searching with empty search bar
        Given the user is on any page on the website
        When the user clicks the search button
        Then the user navigates to the search page
        And the search results are empty

    Scenario Outline: Searching for a product by name
        Given the user is on any page on the website
        When the user enters <product_keyword> into the search bar
        And the user clicks the search button
        Then the user navigates to the search page
        And products similar to <product_keyword> are displayed in the results

    Examples:
        | product_keyword   |
        | iPhone            |
        | iMac              |
        | MacBook           |
        | Apple             |
        | Samsung           |
        | APPLE             |
        | HELLO             |

    Scenario Outline: Applying search criteria to search results
        Given the user has navigated to the search page
        When the user enters <product_keyword> into keywords
        And the user clicks on "All Categories"
        And the user selects the <product_category> from the menu that appears
        And the user submits the search
        Then products similar to <product_keyword> are displayed in the results
        And products in the results from the <product_category> category

    Examples:
        | product_keyword   | product_category  |
        | Samsung           | Monitors          |
        | Samsung           | Tablets           |
        | Samsung           | test 11           |

    Scenario Outline: Searching in product descriptions
        Given the user has navigated to the search page
        When the user enters <product_keyword> into keywords
        And the user checks the box "Search in product descriptions"
        And the user submits the search
        Then products are displayed in the results
        And the product descriptions contain the keyword <product_keyword>

    Examples:
        | product_keyword   |
        | Apple             |
        | Windows           |
        | phone             |
        | tablet            |

    Scenario Outline: Searching in product descriptions and subcategories
        Given the user has navigated to the search page
        When the user enters <product_keyword> into keywords
        And the user checks the box "Search in product descriptions"
        And the user clicks on "All Categories"
        And the user selects the <product_category> from the menu that appears
        And the user checks the box "Search in subcategories"
        And the user submits the search
        Then similar products are displayed in the results
        And the product descriptions contain the keyword <product_keyword>
        And the product category is a subcategory of the <product_category> category

    Examples:
        | product_keyword   | product_category  |
        | Apple             | Components        |
        | Samsung           | Components        |
        | tablet            | Tablets           |
