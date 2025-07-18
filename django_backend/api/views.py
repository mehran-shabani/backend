from rest_framework.views import APIView
from rest_framework.response import Response
from django.db import connections
from django.core.cache import cache

class HealthCheckView(APIView):
    def get(self, request):
        response = {
            'status': 'success',
            'database': 'healthy',
            'cache': 'healthy',
        }
        # Check DB connection
        try:
            connections['default'].cursor()
        except Exception:
            response['database'] = 'unhealthy'

        # Check cache connection (if configured)
        try:
            cache.set('health_check', 'ok', 1)
            if cache.get('health_check') != 'ok':
                raise Exception('cache failed')
        except Exception:
            response['cache'] = 'unhealthy'

        if response['database'] != 'healthy' or response['cache'] != 'healthy':
            response['status'] = 'failure'
            return Response(response, status=503)
        return Response(response)
