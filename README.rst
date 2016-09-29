Scruffy UML: Creates UML diagrams using yUML-like (http://yuml.me) syntax.


** I am not sure I will continue this project since I found http://plantuml.com/ and it does everything I need **

Requires dot (http://www.graphviz.org/), rsvg-convert (http://librsvg.sourceforge.net/) and pic2plot (http://www.gnu.org/software/plotutils/), has been developed and tested on Ubuntu.
For scruffy output Purisa font is used by default if it's available. More fallback fonts will be added in future.

Class diagrams
--------------

The same syntax as yUML (http://yuml.me/diagram/scruffy/class/draw):

================  =========================================================  
Class             [Customer]
Directional       [Customer]->[Order]
Bidirectional     [Customer]<->[Order]
Aggregation       [Customer]+-[Order] or [Customer]<>-[Order]
Composition       [Customer]++-[Order]
Inheritance       [Customer]^[Cool Customer], [Customer]^[Uncool Customer]
Dependencies      [Customer]uses-.->[PaymentStrategy]
Cardinality       [Customer]<1-1..2>[Address]
Labels            [Person]customer-billingAddress[Address]
Notes             [Person]-[Address],[Address]-[note: Value Object]
Full Class        [Customer|Forename;Surname;Email|Save()]
Splash of Colour  [Customer{bg:orange}]<>1->*[Order{bg:green}]
================  =========================================================  

Simple example:

suml --png "[User|+Forename;+Surname;+HashedPassword;-Salt|+Login();+Logout()]" > samples/sample13.png

.. image:: https://github.com/aivarsk/scruffy/raw/master/samples/sample13.png

suml --png --font-family Purisa --scruffy "[User|+Forename;+Surname;+HashedPassword;-Salt|+Login();+Logout()]" > samples/sample13-scruffy.png

.. image:: https://github.com/aivarsk/scruffy/raw/master/samples/sample13-scruffy.png

More complex example:

suml --png "[note: You can stick notes on diagrams too!{bg:cornsilk}],[Customer]<>1-orders 0..*>[Order], [Order]++*-*>[LineItem], [Order]-1>[DeliveryMethod], [Order]*-*>[Product], [Category]<->[Product], [DeliveryMethod]^[National], [DeliveryMethod]^[International]" > samples/sample14.png

.. image:: https://github.com/aivarsk/scruffy/raw/master/samples/sample14.png

suml --png --font-family Purisa --scruffy "[note: You can stick notes on diagrams too!{bg:cornsilk}],[Customer]<>1-orders 0..*>[Order], [Order]++*-*>[LineItem], [Order]-1>[DeliveryMethod], [Order]*-*>[Product], [Category]<->[Product], [DeliveryMethod]^[National], [DeliveryMethod]^[International]" > samples/sample14-scruffy.png

.. image:: https://github.com/aivarsk/scruffy/raw/master/samples/sample14-scruffy.png


Class diagram extensions
------------------------

There are some extensions to yUML syntax:

[ClassA|field1;field2] and following [ClassA] refer to the same class (box) so
you don't have to repeat all the class members in each relation.

You can group/put classes (boxes) inside another box using "embedded classes" like [Group [NodeA][NodeB]] This is not related to UML class diagrams, but might be useful to communicate you ideas.

suml --png --font-family Purisa --scruffy "[Node A]->[Node B],[Node B]->[Node C],[Group [Node A][Node B]]" > samples/sample15-scruffy.png

.. image:: https://github.com/aivarsk/scruffy/raw/master/samples/sample15-scruffy.png

Sequence diagrams
-----------------

Some initial support for sequence diagrams:

=============== ========================================================
Object          [Object]
Send message    [Object1]Message>[Object2] or [Object1]<Message[Object2]
=============== ========================================================

suml --png --scruffy --sequence "[Patron]order food>[Waiter],[Waiter]order food>[Cook],[Waiter]serve wine>[Patron],[Cook]pickup>[Waiter],[Waiter]serve food>[Patron],[Patron]pay>[Cashier]" > tmp/sequence1-scruffy.png

.. image:: https://github.com/aivarsk/scruffy/raw/master/samples/sequence1-scruffy.png
