from rest_framework.views import APIView
from rest_framework.response import Response


class StartPullData(APIView):
    """
    This end point created to start the process of pull data from stock api and calculate the crossover with sma.
    """

    def post(self, request):
        import pprint
        pprint.pprint(request.data, depth=3)

        user_name = request.data.get("user_name") or None
        symbol = request.data.get("symbol") or None
        periods = request.data.get("periods") or None
        requested_result = request.data.get("result") or None

        start_process_output = False

        if symbol and periods:
            start_process_output = True
            pass

        if requested_result is not None:
            response_data = dict(
                results=start_process_output
            )

        else:
            response_data = dict(
                results="Missing request info to start pull data"
            )

        return Response(response_data)


class Result(APIView):
    """
    This end point created to get result of crossover for desired user symbol.
    """

    def post(self, request):
        import pprint
        pprint.pprint(request.data, depth=3)

        user_name = request.data.get("user_name") or None

        requested_result = request.data.get("result") or None

        get_crossover = dict()

        if user_name:
            get_crossover = {
                "symbol": ["list of symbol"],
                "time": ["01-12-2020 12:20:00"],
            }

        if requested_result is not None:
            response_data = dict(
                results=get_crossover
            )

        else:
            response_data = dict(
                results="Missing request info to get crossover"
            )

        return Response(response_data)

