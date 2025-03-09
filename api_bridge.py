## Solace Nexus API Bridge

This is the central API bridge for interacting with Solace-Intelligence and Solace-Interface.

import flask
import requests

class SolaceAPIBridge:

    def __init__(self, indt_url, intf_url):

        self.intell_url = indt_url
        self.interf_url = intf_url


    def send_request(self, payload):
        """Send a data request from Solace-Intelligence to Solace-Interface"""
        response = requests.get(self.interf_url, params=payload)
        return response.json()

    def receive_data(self, response):

        """Returns the response data in a structured manner"""
        return {\"status\": \"success\", "data\": response}
