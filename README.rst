====================
sesam-base64-decoder
====================

Decodes base64 encoded strings and stores it on the entity during transform.

The encoded bytes are decoded to a string using UTF-8 by default, can be overriden with the ENCODING environment variable.

::

  $ SOURCE_PROPERTY=name TARGET_PROPERTY=name_decoded python3 service/transform-service.py
   * Running on http://0.0.0.0:5001/ (Press CTRL+C to quit)
   * Restarting with stat
   * Debugger is active!
   * Debugger pin code: 260-787-156

The service listens on port 5001.

JSON entities can be posted to 'http://localhost:5001/transform'. The result is streamed back to the client.


Examples:

::

   $ curl -s -XPOST 'http://localhost:5001/transform' -H "Content-type: application/json" -d '[{ "_id": "jane", "name": "PT09PT09" }]' | jq -S .
   [
     {
       "_id": "jane",
       "message": "Hello world!",
       "name": "PT09PT09"
       "name_decoded": "--"
     }
   ]

Note the example uses `curl <https://curl.haxx.se/>`_ to send the request and `jq <https://stedolan.github.io/jq/>`_ prettify the response.
