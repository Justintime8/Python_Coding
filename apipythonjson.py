import urllib.request, urllib.parse, urllib.error
import json
{
  "status": "OK",
    "results": [
    {
        "geometry" : {
          "location_type" : "APPROXIMATE",
            "locatoin" : {
                "lat" : 42.2808256,
                "lng" : -83.7430378
            }
        },
        "address_components" : [
          {
              "long_name" : "Ann Arbor",
                "types" : [
                    "locality",
                    "political"
                ],
                "short_name" : "Ann Arbor"
          }
        ],
        "formatted_address": "Ann Arbor, MI, USA",
        "types": [
            "locality",
            "political"
        ]
    }
    ]
}

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'
