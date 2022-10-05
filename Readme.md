# Buffer App

La logica relacionada al buffer la podemos encontrar en los sigueintes archivos
- app/buffer.py
- app/buffer_operations.py
- app/utils.py

Principalmente testee esas funcionalidades.

Use docker para levantar un restapi en fastapi y redis

Agregue linters para que cualquier persona que trabaje en este repo
cumpla los mismos estandares, solo debemos installar el pre-commit luego de haber instalado los requerimientos del sistema
de esta manera en cada commit se ejecutaran los linters

```bash
pre-commit install  
```
Si queremos testear lo referente al buffer
```bash
pip3 install -r requirements/base.txt
pytest
```
Con el siguiente comando tendremos el REST API en el puerto 8000
```bash
docker-compose up -d
```
