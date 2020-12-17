# SnipeIT API
Intended to be a Structured way to interface with Snipe-IT's API.\

# Usage
Open a context manager so the requests session can be reused etc
~~~python
import SnipeITAPI
import json
with SnipeITAPI.Sessions(server='XXXXXXXXXXXXXX',token='XXXXXXXXXXXXXX') as snipeit_session:

    x=snipeit_session.assets_get_byserial(serial='123456789').json()

    patch_data={'_snipeit_mycustomfield_9000':'MaintenanceComplete'}

    y=snipeit_session.asset_patch(
        asset_id=x['serial'],
        data=json.dumps(patch_data) # Its important to json.dumps() the dict; Snipe-IT wont accept it otherwise. Tempted to just incorporate this into the asset_patch method.
    )

~~~
_This API returns the whole requests object assuming the request is 'ok'_

Some basic exception handling is in place, but needs work.


 
