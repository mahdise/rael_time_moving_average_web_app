"""
This request demo for start the process of pull data from api (stock data)
    request = {
    "user_name" : "mahdi",
    "symbol" : ["AMD","AAPL"],
    "periods" : ["4","10"],
    "result" :"start_info"
    }

    response = {
    results = True
    }
    """

"""
    This end point created to get result of crossover for desired user symbol.
    response ={
    "results": {
        "symbol": [
            "list of symbol"
        ],
        "time": [
            "01-12-2020 12:20:00"
        ]
    }
}
    request = {
    "user_name" : "mahdi",
    "result" :"crossover result"
    }
    """
