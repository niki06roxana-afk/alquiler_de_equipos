from django.db import models
from django.contrib.auth.models import User

# ==========================
# CATEGORÍAS
# ==========================
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


# ==========================
# EQUIPOS TECNOLÓGICOS
# ==========================
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.SET_NULL,
        null=True
    )

    precio = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )

    stock = models.IntegerField(default=1)

    activo = models.BooleanField(default=True)

    disponible = models.BooleanField(default=True)

    ESTADOS = [
        ('Disponible', 'Disponible'),
        ('Alquilado', 'Alquilado'),
        ('Mantenimiento', 'Mantenimiento'),
    ]

    estado = models.CharField(
        max_length=20,
        choices=ESTADOS,
        default='Disponible'
    )

    def __str__(self):
        return self.nombre


# ==========================
# SOLICITUD DE ALQUILER
# ==========================
class Pedido(models.Model):

    usuario = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    productos = models.ManyToManyField(
        Producto,
        through='DetallePedido'
    )

    fecha = models.DateTimeField(auto_now_add=True)

    fecha_alquiler = models.DateField()

    fecha_devolucion = models.DateField()

    ESTADO_PEDIDO = [
        ('Pendiente', 'Pendiente'),
        ('Aprobado', 'Aprobado'),
        ('Devuelto', 'Devuelto'),
    ]

    estado = models.CharField(
        max_length=20,
        choices=ESTADO_PEDIDO,
        default='Pendiente'
    )

    def __str__(self):
        return f"Solicitud {self.id} - {self.usuario.username}"


# ==========================
# DETALLE DEL ALQUILER
# ==========================
class DetallePedido(models.Model):

    pedido = models.ForeignKey(
        Pedido,
        on_delete=models.CASCADE
    )

    producto = models.ForeignKey(
        Producto,
        on_delete=models.CASCADE
    )

    cantidad = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.producto.nombre} x {self.cantidad}"