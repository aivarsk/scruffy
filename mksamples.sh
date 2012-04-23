#!/bin/sh

mkdir -p tmp
suml --png "[User]" > tmp/sample01.png
suml --png "[Customer]->[Billing Address]" > tmp/sample02.png
suml --png "[Customer]1-0..*[Address]" > tmp/sample03.png
suml --png "[Order]-billing[Address], [Order]-shipping[Address]" > tmp/sample04.png
suml --png "[❝Customer❞{bg:orange}]❶- ☂>[Order{bg:green}]" > tmp/sample05.png
suml --png "[Company]<>-1>[Location], [Location]+->[Point]" > tmp/sample06.png
suml --png "[Company]++-1>[Location]" > tmp/sample07.png
suml --png "[Customer]<>1->*[Order], [Customer]-[note: Aggregate Root{bg:cornsilk}]" > tmp/sample08.png
suml --png "[Wages]^-[Salaried], [Wages]^-[Contractor]" > tmp/sample09.png
suml --png "[<<ITask>>]^-.-[NightlyBillingTask]" > tmp/sample10.png
suml --png "[日本語]->[Köttbullar]" > tmp/sample11.png
suml --png "[HttpContext]uses -.->[Response]" > tmp/sample11.png
suml --png "[<<IDisposable>>;Session]" > tmp/sample12.png
suml --png "[User|+Forename;+Surname;+HashedPassword;-Salt|+Login();+Logout()]" > tmp/sample13.png
suml --png "[note: You can stick notes on diagrams too!{bg:cornsilk}],[Customer]<>1-orders 0..*>[Order], [Order]++*-*>[LineItem], [Order]-1>[DeliveryMethod], [Order]*-*>[Product], [Category]<->[Product], [DeliveryMethod]^[National], [DeliveryMethod]^[International]" > tmp/sample14.png
suml --png "[Node A]->[Node B],[Node B]->[Node C],[Group [Node A][Node B]]" > tmp/sample15.png

suml --png --scruffy "[User]" > tmp/sample01-scruffy.png
suml --png --scruffy "[Customer]->[Billing Address]" > tmp/sample02-scruffy.png
suml --png --scruffy "[Customer]1-0..*[Address]" > tmp/sample03-scruffy.png
suml --png --scruffy "[Order]-billing[Address], [Order]-shipping[Address]" > tmp/sample04-scruffy.png
suml --png --scruffy "[❝Customer❞{bg:orange}]❶- ☂>[Order{bg:green}]" > tmp/sample05-scruffy.png
suml --png --scruffy "[Company]<>-1>[Location], [Location]+->[Point]" > tmp/sample06-scruffy.png
suml --png --scruffy "[Company]++-1>[Location]" > tmp/sample07-scruffy.png
suml --png --scruffy "[Customer]<>1->*[Order], [Customer]-[note: Aggregate Root{bg:cornsilk}]" > tmp/sample08-scruffy.png
suml --png --scruffy "[Wages]^-[Salaried], [Wages]^-[Contractor]" > tmp/sample09-scruffy.png
suml --png --scruffy "[<<ITask>>]^-.-[NightlyBillingTask]" > tmp/sample10-scruffy.png
suml --png --scruffy "[日本語]->[Köttbullar]" > tmp/sample11-scruffy.png
suml --png --scruffy "[HttpContext]uses -.->[Response]" > tmp/sample11-scruffy.png
suml --png --scruffy "[<<IDisposable>>;Session]" > tmp/sample12-scruffy.png
suml --png --scruffy "[User|+Forename;+Surname;+HashedPassword;-Salt|+Login();+Logout()]" > tmp/sample13-scruffy.png
suml --png --font-family Purisa --scruffy "[note: You can stick notes on diagrams too!{bg:cornsilk}],[Customer]<>1-orders 0..*>[Order], [Order]++*-*>[LineItem], [Order]-1>[DeliveryMethod], [Order]*-*>[Product], [Category]<->[Product], [DeliveryMethod]^[National], [DeliveryMethod]^[International]" > tmp/sample14-scruffy.png

suml --png --font-family Purisa --scruffy "[Node A]->[Node B],[Node B]->[Node C],[Group [Node A][Node B]]" > tmp/sample15-scruffy.png
suml --font-family Purisa --svg --scruffy "[Node A]->[Node B],[Node B]->[Node C],[Group [Node A][Node B]]" > tmp/sample15-scruffy.svg

suml --svg --scruffy --sequence "[Patron]order food>[Waiter],[Waiter]order food>[Cook],[Waiter]serve wine>[Patron],[Cook]pickup>[Waiter],[Waiter]serve food>[Patron],[Patron]pay>[Cashier]" > tmp/sequence1-scruffy.svg
suml --png --scruffy --sequence "[Patron]order food>[Waiter],[Waiter]order food>[Cook],[Waiter]serve wine>[Patron],[Cook]pickup>[Waiter],[Waiter]serve food>[Patron],[Patron]pay>[Cashier]" > tmp/sequence1-scruffy.png
