from pyfortimanager.core.fortimanager import FortiManager


class System(FortiManager):
    """API class for the FortiManager system.
    """

    def __init__(self, **kwargs):
        super(System, self).__init__(**kwargs)
    
    def ha(self):
        """Obtain FortiManager HA information and status of the system.

        Returns:
            dict: JSON data.
        """
   
        params = {
            "url": "/sys/ha/status"
        }

        return self.post(method="get", params=params)

    def reboot(self, message: str=None):
        """Reboots the FortiManager.

        Args:
            message (str, optional): Optional message to be stored in the event log.

        Returns:
            dict: JSON data.
        """
   
        params = {
            "url": "/sys/reboot",
            "data": {
                "message": message
            }
        }

        return self.post(method="exec", params=params)

    def status(self):
        """Retrieves the FortiManager system status.

        Returns:
            dict: JSON data.
        """
   
        params = {
            "url": "/sys/status"
        }

        return self.post(method="get", params=params)

    def tasks(self, task:int=None, filter: list=None, loadsub: int=0):
        """Retrieves all FortiManager tasks or a single task.

        Args:
            task (int): ID of a specific task.
            filter (list): Filter the result according to a set of criteria. example: List [ "{attribute}", "==", "{value}" ]
            loadsub (int): Enable or disable the return of any sub-objects.

        Returns:
            dict: JSON data.
        """
   
        params = {
            "url": "/task/task",
            "filter": filter,
            "loadsub": loadsub
        }

        # Retrieve a single task
        if task:
            params['url'] = f"/task/task/{task}/line"

        return self.post(method="get", params=params)
    
    def proxy(self, targets: list, action: str="get", payload: object=None, resource: str=None, timeout: int=None):
        """Send and receive a JSON request to/from managed FortiGates. The response will be an array of data, one for each queried device.

        Args:
            targets (list): A list of FortiGates with their ADOM to target. Ex. ["/adom/<name_of_adom>/device/<name_of_fortigate>"]
            action (str): Specify HTTP action for the request: get, post, put, delete. Default is get.
            resource (str): URL on the remote device to be accessed. Ex. /api/v2/<rest_of_the_endpoint>
            payload (object, optional): An object containing the payload needed for the resource URL. Ex. { "vdom": "root", "admin": "enable" }
            timeout (int, optional): How long to wait for the FortiGate to respond. Defaults to the proxy_timeout set when the API was instantiated.

        Returns:
            dict: JSON data.
        """

        params = {
            "url": "/sys/proxy/json",
            "data":
                {
                    "target": targets,
                    "action": action,
                    "timeout": timeout or self.api.proxy_timeout,
                    "resource": resource
                }
        }

        # Optional fields
        if payload:
            params['data']['payload'] = payload

        return self.post(method="exec", params=params)