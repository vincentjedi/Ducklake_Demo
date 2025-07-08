# Ducklake_Demo
Rollback Safety Using Ducklake from DuckDb

An e-commerce system where inventory and orders must stay consistent. What happens when something goes wrong mid-transaction?
Traditional formats can’t roll back across tables. If the order inserts but the inventory update fails, you’re stuck with inconsistent data. DuckLake’s true ACID transactions mean all-or-nothing across any number of tables.
