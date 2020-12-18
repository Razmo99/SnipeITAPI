import requests
import logging
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from .Exceptions import SnipeITErrorHandler

logger = logging.getLogger(__name__)
logger.debug('Importing Module : '+__name__)

class Sessions(object):
    """Class to manage SnipeIT API Sessions"""

    def __init__(self,server,token):
        self.server=server
        self.token=token
        self.session=requests.Session()
        self.headers={
            'Authorization': 'Bearer {0}'.format(token),
            "Accept": "application/json",
            "Content-Type": "application/json"}
        self.session.headers.update(self.headers)
        self.session.mount(
            'https://',
            HTTPAdapter(
                max_retries=Retry(
                    total=10,
                    backoff_factor=0.5)))

    def __enter__(self):
        return self
    
    def __exit__(self,exec_types,exec_val,exc_tb):
        self.session.close()

    def maintenances_get(self,params={}):
        """Get list of Maintenances
            
            Arguments:
                params {dictionary} --
            Returns:
                requests object
        """
        
        uri = '/api/v1/maintenances'
        url = self.server + uri
        results = self.session.get(
            url,
            params=params,
            timeout=5
            )
        if results.ok and not results.json().get('status') == 'error':
            return results
        else:
            SnipeITErrorHandler(results)

    def maintenances_post(self,data):
        """Get list of Maintenances
            
            Arguments:
                params {dictionary} --
                {
                    'asset_id':'',#int
                    'supplier_id':'',#int
                    'asset_maintenance_type':'',#Has to Match drop down list in Snipe-IT
                    'start_date':'',#Date YYYY-MM-DD
                    'completion_date':'',#Date YYYY-MM-DD
                    'title':''#String
                }
            Returns:
                requests object
        """
        
        uri = '/api/v1/maintenances'
        url = self.server + uri
        results = self.session.post(
            url,
            data=data,
            timeout=5
            )
        if results.ok and not results.json().get('status') == 'error':
            return results
        else:
            SnipeITErrorHandler(results)

    def assets_get_byserial(self,serial,params={}):
        """Get asset by serial
            
            Arguments:
                serial {string} --
                params {dictionary} --
            Returns:
                requests object
        """
        
        uri = '/api/v1/hardware/byserial/{0}'.format(serial)
        url = self.server + uri
        results = self.session.get(
            url,
            params=params,
            timeout=5
            )
        if results.ok and not results.json().get('status') == 'error':
            return results
        else:
            SnipeITErrorHandler(results)
    
    def asset_patch(self,asset_id,data):
        """Patch an Asset
            
            Arguments:
                id {int} --
                data {dictionary} --
            Returns:
                requests object
        """
        
        uri = '/api/v1/hardware/{0}'.format(asset_id)
        url = self.server + uri
        results = self.session.patch(
            url,
            data=data,
            timeout=5,
            )
        if results.ok and not results.json().get('status') == 'error':
            return results
        else:
            SnipeITErrorHandler(results)
    
    def custom_fieldsets_get(self,params={}):
        """Get list of Custom Fieldsets
            
            Arguments:
                params {dictionary} --
            Returns:
                requests object
        """
        
        uri = '/api/v1/fields'
        url = self.server + uri
        results = self.session.get(
            url,
            params=params,
            timeout=5
            )
        if results.ok and not results.json().get('status') == 'error':
            return results
        else:
            SnipeITErrorHandler(results)
    
    def custom_fieldsets_post(self,data):
        """post an Asset
            
            Arguments:
                data {dictionary} --
            Returns:
                requests object
        """
        
        uri = '/api/v1/fieldsets'
        url = self.server + uri
        results = self.session.post(
            url,
            data=data,
            timeout=5
            )
        if results.ok and not results.json().get('status') == 'error':
            return results
        else:
            SnipeITErrorHandler(results)