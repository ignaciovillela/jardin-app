import os
import sys
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jardin_app.settings')
django.setup()

from clientes.models import Solicitud

def eliminar_solicitud(solicitud_id):
    try:
        solicitud = Solicitud.objects.get(id=solicitud_id)
        solicitud.delete()
        print(f"Solicitud #{solicitud_id} eliminada correctamente.")
    except Solicitud.DoesNotExist:
        print(f"Solicitud con ID {solicitud_id} no existe.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python eliminar_solicitud.py <ID>")
    else:
        eliminar_solicitud(int(sys.argv[1]))
