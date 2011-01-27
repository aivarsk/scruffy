Makes SVG shapes look hand-drawn and creates UML diagrams using yUML (http://yuml.me) syntax

Requires dot (http://www.graphviz.org/) and rsvg-convert (http://librsvg.sourceforge.net/), has been tested on Ubuntu.

./yuml2dot.py --png "[User|+Forename;+Surname;+HashedPassword;-Salt|+Login();+Logout()]" > samples/sample13.png

.. image:: https://github.com/aivarsk/scruffy/raw/master/samples/sample13.png

./yuml2dot.py --png --font-family Purisa --scruffy "[User|+Forename;+Surname;+HashedPassword;-Salt|+Login();+Logout()]" > samples/sample13-scruffy.png

.. image:: https://github.com/aivarsk/scruffy/raw/master/samples/sample13-scruffy.png

./yuml2dot.py --png "[note: You can stick notes on diagrams too!{bg:cornsilk}],[Customer]<>1-orders 0..*>[Order], [Order]++*-*>[LineItem], [Order]-1>[DeliveryMethod], [Order]*-*>[Product], [Category]<->[Product], [DeliveryMethod]^[National], [DeliveryMethod]^[International]" > samples/sample14.png

.. image:: https://github.com/aivarsk/scruffy/raw/master/samples/sample14.png

./yuml2dot.py --png --font-family Purisa --scruffy "[note: You can stick notes on diagrams too!{bg:cornsilk}],[Customer]<>1-orders 0..*>[Order], [Order]++*-*>[LineItem], [Order]-1>[DeliveryMethod], [Order]*-*>[Product], [Category]<->[Product], [DeliveryMethod]^[National], [DeliveryMethod]^[International]" > samples/sample14-scruffy.png

.. image:: https://github.com/aivarsk/scruffy/raw/master/samples/sample14-scruffy.png
