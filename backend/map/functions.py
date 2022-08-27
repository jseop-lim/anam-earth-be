from django.contrib.gis.db.models.functions import Distance


class DistanceSphere(Distance):

    def as_mysql(self, compiler, connection, **extra_context):
        function = None
        if self.geo_field.geodetic(connection):
            function = connection.ops.spatial_function_name("Distance_Sphere")
        return super().as_sql(
            compiler, connection, function=function, **extra_context
        )
