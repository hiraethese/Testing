Feature: Managing products

    Background:
        Given the user is logged in as an administrator

    Scenario Outline: Removing a product
        Given the user has navigated to the "Products" page
        And <product_name> is on the list
        When the user checks the box of <product_name> product
        And the user clicks the "Delete" button
        And the user agrees to the removal of <product_name>
        Then <product_name> is removed from the product list
        And the user receives a deletion notification

    Examples:
        | product_name      |
        | Apple Cinema 30"  |
        | Canon EOS 5D      |
        | HP LP3065         |

    Scenario Outline: Editing product price
        Given the user has navigated to the <product_name> page
        When the user changes the price to <product_price> in Data section
        And the user clicks the "Save" button
        Then the new price <product_price> is displayed in the description of <product_name>
        And the user receives a modification notification

    Examples:
        | product_name  | product_price |
        | HTC Touch HD  | 200.0000      |
        | iPod Classic  | 150.0000      |

    Scenario Outline: Editing quantity of product
        Given the user has navigated to the <product_name> page
        When the user changes the quantity to <product_quantity> in Data section
        And the user clicks the "Save" button
        Then the quantity <product_quantity> is displayed in the description of <product_name>
        And the user receives a modification notification

    Examples:
        | product_name  | product_quantity  |
        | HTC Touch HD  | 10000             |
        | iPod Touch    | 1                 |
        | iPhone        | 0                 |

    Scenario Outline: Adding a new product
        Given the user has navigated to the "Add New" page
        When the user enters <product_name> as the product name in General section
        And the user enters <meta_tag_title> as the meta tag title in General section
        And the user enters <product_model> as the model in Data section
        And the user enters a unique <keyword> as a keyword in SEO section
        And the user clicks the "Save" button
        Then <product_name> addition outcome should be <Outcome>
        And the user receives <Outcome> notification

    Examples:
        | product_name  | meta_tag_title    | product_model | keyword       | Outcome       |
        | NewProduct    | NewProduct        | NewProduct    | new-product   | Successful    |
        | NewProduct    | NewProduct        | NewProduct    | ""            | Unsuccessful  |
        | TooLongName...| NewProduct        | NewProduct    | new-product   | Unsuccessful  |
