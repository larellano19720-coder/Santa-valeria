import sys
import os
import django
import time

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Ganadera.settings')
django.setup()

from Aplicacion.models import Registro

def monitorear():
    while True:
        registro = Registro.objects.using('servidor').filter(estatus=2).first()
        if registro:
            registro.estatus = 1
            registro.save(using='servidor')
            print(f"✔ Actualizado: {registro.descripcion}")
        else:
            print("Sin cambios")
        time.sleep(10)

if __name__ == "__main__":
    monitorear()
