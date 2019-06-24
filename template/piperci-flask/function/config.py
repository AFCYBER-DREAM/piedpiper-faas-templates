# Config = {
#    "gman": {"url": "http://172.17.0.1:8089"},
#    "storage": {
#        "url": "172.17.0.1:9000",
#        "access_key": "",
#        "secret_key": "",
#    },
#    "name": "noop",
#    "executor_url": "http://172.17.0.1:8080/async-function/piperci-noop-executor",
# }
"""
Configuration parameters for your FaaS function.
Required parameters:
  * gman_url: The URL that GMan is located at.
  * name: The name of your FaaS function. Usually this will be
  <something>_controller and <something>_executor
  * executor_url: If your function is a controller and has another
  function that it needs to call you need to define
  that here.
"""
Config = {}
