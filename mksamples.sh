#!/bin/sh

./yuml2dot.py --png "[User]" > samples/sample01.png
./yuml2dot.py --png "[Customer]->[Billing Address]" > samples/sample02.png
./yuml2dot.py --png "[Customer]1-0..*[Address]" > samples/sample03.png
./yuml2dot.py --png "[Order]-billing[Address], [Order]-shipping[Address]" > samples/sample04.png
./yuml2dot.py --png "[❝Customer❞{bg:orange}]❶- ☂>[Order{bg:green}]" > samples/sample05.png
./yuml2dot.py --png "[Company]<>-1>[Location], [Location]+->[Point]" > samples/sample06.png
./yuml2dot.py --png "[Company]++-1>[Location]" > samples/sample07.png
./yuml2dot.py --png "[Customer]<>1->*[Order], [Customer]-[note: Aggregate Root{bg:cornsilk}]" > samples/sample08.png
./yuml2dot.py --png "[Wages]^-[Salaried], [Wages]^-[Contractor]" > samples/sample09.png
./yuml2dot.py --png "[<<ITask>>]^-.-[NightlyBillingTask]" > samples/sample10.png
./yuml2dot.py --png "[日本語]->[Köttbullar]" > samples/sample11.png
./yuml2dot.py --png "[HttpContext]uses -.->[Response]" > samples/sample11.png
./yuml2dot.py --png "[<<IDisposable>>;Session]" > samples/sample12.png
./yuml2dot.py --png "[User|+Forename;+Surname;+HashedPassword;-Salt|+Login();+Logout()]" > samples/sample13.png
./yuml2dot.py --png "[note: You can stick notes on diagrams too!{bg:cornsilk}],[Customer]<>1-orders 0..*>[Order], [Order]++*-*>[LineItem], [Order]-1>[DeliveryMethod], [Order]*-*>[Product], [Category]<->[Product], [DeliveryMethod]^[National], [DeliveryMethod]^[International]" > samples/sample14.png
./yuml2dot.py --png "[Node A]->[Node B],[Node B]->[Node C],[Group [Node A][Node B]]" > samples/sample15.png

./yuml2dot.py --png --font-family Purisa --scruffy "[User]" > samples/sample01-scruffy.png
./yuml2dot.py --png --font-family Purisa --scruffy "[Customer]->[Billing Address]" > samples/sample02-scruffy.png
./yuml2dot.py --png --font-family Purisa --scruffy "[Customer]1-0..*[Address]" > samples/sample03-scruffy.png
./yuml2dot.py --png --font-family Purisa --scruffy "[Order]-billing[Address], [Order]-shipping[Address]" > samples/sample04-scruffy.png
./yuml2dot.py --png --font-family Purisa --scruffy "[❝Customer❞{bg:orange}]❶- ☂>[Order{bg:green}]" > samples/sample05-scruffy.png
./yuml2dot.py --png --font-family Purisa --scruffy "[Company]<>-1>[Location], [Location]+->[Point]" > samples/sample06-scruffy.png
./yuml2dot.py --png --font-family Purisa --scruffy "[Company]++-1>[Location]" > samples/sample07-scruffy.png
./yuml2dot.py --png --font-family Purisa --scruffy "[Customer]<>1->*[Order], [Customer]-[note: Aggregate Root{bg:cornsilk}]" > samples/sample08-scruffy.png
./yuml2dot.py --png --font-family Purisa --scruffy "[Wages]^-[Salaried], [Wages]^-[Contractor]" > samples/sample09-scruffy.png
./yuml2dot.py --png --font-family Purisa --scruffy "[<<ITask>>]^-.-[NightlyBillingTask]" > samples/sample10-scruffy.png
./yuml2dot.py --png --font-family Purisa --scruffy "[日本語]->[Köttbullar]" > samples/sample11-scruffy.png
./yuml2dot.py --png --font-family Purisa --scruffy "[HttpContext]uses -.->[Response]" > samples/sample11-scruffy.png
./yuml2dot.py --png --font-family Purisa --scruffy "[<<IDisposable>>;Session]" > samples/sample12-scruffy.png
./yuml2dot.py --png --font-family Purisa --scruffy "[User|+Forename;+Surname;+HashedPassword;-Salt|+Login();+Logout()]" > samples/sample13-scruffy.png
./yuml2dot.py --png --font-family Purisa --scruffy "[note: You can stick notes on diagrams too!{bg:cornsilk}],[Customer]<>1-orders 0..*>[Order], [Order]++*-*>[LineItem], [Order]-1>[DeliveryMethod], [Order]*-*>[Product], [Category]<->[Product], [DeliveryMethod]^[National], [DeliveryMethod]^[International]" > samples/sample14-scruffy.png

./yuml2dot.py --png --font-family Purisa --scruffy "[Node A]->[Node B],[Node B]->[Node C],[Group [Node A][Node B]]" > samples/sample15-scruffy.png

