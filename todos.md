- Menu: Your web application should support all of the available menu items for Pinnochio’s Pizza & Subs
decide how to construct your models to best represent the information. DOONEEE

- Adding Items: Using Django Admin, site administrators (restaurant owners) should be able to add, update, and remove items on the menu. Add all of the items from the Pinnochio’s menu into your database using either the Admin UI or by running Python commands in Django’s shell. DOONEEEE

-Registration, Login, Logout: Site users (customers) should be able to register for your web application with a username, password, first name, last name, and email address. Customers should then be able to log in and log out of your website.
=> eb2a e3ml alerts on login, register, logout

DOONEEE

.. Complete the Menu, Adding Items, and Registration/Login/Logout steps.. DOONEEEE :DDDDDD


- Shopping Cart: Once logged in, users should see a representation of the restaurant’s menu, where they can add items (along with toppings or extras, if appropriate) to their virtual “shopping cart.” DONEE
=> submit form, aw b ajax msh hane5tlf, ajax a7sn badal ma t reload, e3ml zay alert keda en el item added to cart
**MMkn tadd l list gowa el session, search 3n sessions django el awel**
on receiving a post request for adding to a cart, make sure that user is logged in first, else redirect
**LAAA, save b localStorage w clear once item is confirmed aw keda y3ni**

DOONEEEEE

-  The contents of the shopping should be saved even if a user closes the window, or logs out and logs back in again. DONNNE

- Placing an Order: Once there is at least one item in a user’s shopping cart, they should be able to place an order, whereby the user is asked to confirm the items in the shopping cart, and the total (no need to worry about tax!) before placing an order. DONNEEE



...Complete the Shopping Cart and Placing an Order steps.... DONNEE



- Viewing Orders: Site administrators should have access to a page where they can view any orders that have already been placed.    DONNEEE
**Make an account and grant it admin permissions b if statements aw search 3n admin users in django, aw add is_admin fel user table a7sn :DD**  IT IS request.is_superuser :D


- Personal Touch: Add at least one additional feature of your choosing to the web application. Possibilities include: allowing site administrators to mark orders as complete and allowing users to see the status of their pending or completed orders, integrating with the Stripe API to allow users to actually use a credit card to make a purchase during checkout, or supporting sending users a confirmation email once their purchase is complete. If you need to use any credentials (like passwords or API credentials) for your personal touch, be sure not to store any credentials in your source code, better to use environment variables!  DONNEEEE

- In README.md, include a short writeup describing your project, what’s contained in each file you created or modified, and (optionally) any other additional information the staff should know about your project. Also, include a description of your personal touch and what you chose to add to the project. DOONEEE

- If you’ve added any Python packages that need to be installed in order to run your web application, be sure to add them to requirements.txt!
