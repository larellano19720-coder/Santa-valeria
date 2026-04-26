from django.http import JsonResponse
from Aplicacion.models import Control
from django.utils import timezone

def obtener_comando(request):

    token = request.GET.get("token")

    if not token:
        return JsonResponse({"error": "Falta token"}, status=400)

    control = Control.objects.filter(Token=token).first()

    if not control:
        return JsonResponse({"error": "Token inválido"}, status=403)

    # Actualiza última conexión
    control.ultima_conexion = timezone.now()
    control.save(update_fields=["ultima_conexion"])

    return JsonResponse({
        "idtolva": control.IDDispositivo_id,  # 👈 importante
        "alias": control.Alias,
        "estatus": control.Estatus,
        "movil": control.Movil,
        "com_bau": control.ComBau,
        "ip_bd": control.IPBaseDatos,
        "accion": control.comando_pendiente or "ninguna"
    })