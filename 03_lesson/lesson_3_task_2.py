from smartphone import Smartphone

catalog = [
    Smartphone('Samsung', '1', '+79859999999'),
    Smartphone('Samsung', '2', '+79858888888'),
    Smartphone('Samsung', '3', '+79853333333')
]

for Smartphone in catalog:
    print(f"{Smartphone.name} - {Smartphone.model} - {Smartphone.number}")
