from typing import Callable, Dict, List, Optional

from aws_lambda_powertools.event_handler import CORSConfig
from aws_lambda_powertools.event_handler.api_gateway import (
    ApiGatewayResolver,
    ProxyEventType,
)
from aws_lambda_powertools.utilities.data_classes import VPCLatticeEvent


class VPCLatticeResolver(ApiGatewayResolver):
    """AWS Lambda Function URL resolver

    Notes:
    -----
    Invokes your Lambda function and passes the content of the request to the Lambda function, in JSON format

    Documentation:
    - https://docs.aws.amazon.com/vpc-lattice/latest/ug/lambda-functions.html


    Examples
    --------
    Simple example integrating with Tracer

    ```python
    from aws_lambda_powertools import Tracer
    from aws_lambda_powertools.event_handler import VPCLatticeResolver

    tracer = Tracer()
    app = VPCLatticeResolver()

    @app.get("/get-call")
    def simple_get():
        return {"message": "Foo"}

    @app.post("/post-call")
    def simple_post():
        post_data: dict = app.current_event.json_body
        return {"message": post_data}

    @tracer.capture_lambda_handler
    def lambda_handler(event, context):
        return app.resolve(event, context)
    """

    current_event: VPCLatticeEvent

    def __init__(
        self,
        cors: Optional[CORSConfig] = None,
        debug: Optional[bool] = None,
        serializer: Optional[Callable[[Dict], str]] = None,
        strip_prefixes: Optional[List[str]] = None,
    ):
        super().__init__(ProxyEventType.VPCLatticeEvent, cors, debug, serializer, strip_prefixes)
