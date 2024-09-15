import requests
from sentinelhub import SHConfig


config = SHConfig()
config.sh_client_id = "sh-3bdd95e9-29a6-44a5-bacf-9dde97c88645"
config.sh_client_secret = "6QGRYqEKdIiBlTsUHccN1sDtZCWgtF2S"
config.sh_token_url = "https://identity.dataspace.copernicus.eu/auth/realms/CDSE/protocol/openid-connect/token"
config.sh_base_url = "https://sh.dataspace.copernicus.eu"
config.save("cdse")


url = "https://sh.dataspace.copernicus.eu/api/v1/process"
headers = {
  "Content-Type": "application/json",
  "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJYVUh3VWZKaHVDVWo0X3k4ZF8xM0hxWXBYMFdwdDd2anhob2FPLUxzREZFIn0.eyJleHAiOjE3MjY0MDAyNTgsImlhdCI6MTcyNjM5OTY1OCwiYXV0aF90aW1lIjoxNzI2Mzg5NTk3LCJqdGkiOiIzODg3MDY1MC1mZGJmLTQxZWUtOWE3Yi05OGNjMTgyYzA5MjYiLCJpc3MiOiJodHRwczovL2lkZW50aXR5LmRhdGFzcGFjZS5jb3Blcm5pY3VzLmV1L2F1dGgvcmVhbG1zL0NEU0UiLCJzdWIiOiI5YThiMTZiNS05NmQ4LTQ3M2UtOTc2OC1iZDI1YTc5YjQ3M2UiLCJ0eXAiOiJCZWFyZXIiLCJhenAiOiJzaC0yZDA3NzkxNy1lZTZlLTQyOGUtODZiZC1lZjNmOWVlNGUyZTEiLCJub25jZSI6IjYwOTMwMjBiLTFkYjctNDliYy04ZWJkLTMyMTY2ZjUwYjlhMSIsInNlc3Npb25fc3RhdGUiOiI3ZTJiZjFmNS00NzA2LTRlNjQtYjAyNi02MDk2MTFhN2FlNGQiLCJhbGxvd2VkLW9yaWdpbnMiOlsiaHR0cHM6Ly9zaGFwcHMuZGF0YXNwYWNlLmNvcGVybmljdXMuZXUiXSwic2NvcGUiOiJvcGVuaWQgZW1haWwgcHJvZmlsZSB1c2VyLWNvbnRleHQiLCJzaWQiOiI3ZTJiZjFmNS00NzA2LTRlNjQtYjAyNi02MDk2MTFhN2FlNGQiLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwib3JnYW5pemF0aW9ucyI6WyJkZWZhdWx0LTlhOGIxNmI1LTk2ZDgtNDczZS05NzY4LWJkMjVhNzliNDczZSJdLCJuYW1lIjoiRG9yaXMgS29sZSIsInVzZXJfY29udGV4dF9pZCI6IjM3YTA5NDIyLTgwMjEtNGE4Ni04ZGY0LTc2Y2UyODE0ZDRjZCIsImNvbnRleHRfcm9sZXMiOnt9LCJjb250ZXh0X2dyb3VwcyI6WyIvYWNjZXNzX2dyb3Vwcy91c2VyX3R5cG9sb2d5L2NvcGVybmljdXNfZ2VuZXJhbC8iLCIvYWNjZXNzX2dyb3Vwcy91c2VyX3R5cG9sb2d5L3B1YmxpY19jY20vIiwiL29yZ2FuaXphdGlvbnMvZGVmYXVsdC05YThiMTZiNS05NmQ4LTQ3M2UtOTc2OC1iZDI1YTc5YjQ3M2UvcmVndWxhcl91c2VyLyJdLCJwcmVmZXJyZWRfdXNlcm5hbWUiOiJrb2xlZG9yaXMxOEBnbWFpbC5jb20iLCJnaXZlbl9uYW1lIjoiRG9yaXMiLCJ1c2VyX2NvbnRleHQiOiJkZWZhdWx0LTlhOGIxNmI1LTk2ZDgtNDczZS05NzY4LWJkMjVhNzliNDczZSIsImZhbWlseV9uYW1lIjoiS29sZSIsImVtYWlsIjoia29sZWRvcmlzMThAZ21haWwuY29tIn0.ACaQ04Z8DPRyhwZOW1L8dTSduRs2hK8udEASMgUDcZdaUCB3tel11EbgFHpR39Si09xVGeE2u3XcJRxBrgaxuj7-Le_a5LM4cV_CAz9jDbLL2wC1TJLPHEWaRCHyFO84BR5Ykld1GHPYC5VeGIJxeUZBktGcfP7Ddvi3v-m0S-S-3wNBaI29EvWKuWhNW4Ixbvji_KOymVHdEERvVTxI7YL6H9BHA4Z8IWCClWPOyoReZ67c02gqohlCIvLBmcB5Lu4P-fakEnG2icFx1DQbF8CM_CCJmBG0Vr8l91GJRZJUMKIkW53A9UHMC3sENNOcQIXOaB1itS-_XLF3OXsQPw",
  "Accept": "application/tar"
}
data = {
  "input": {
    "bounds": {
      "bbox": [
        19.765718,
        41.302313,
        19.870466,
        41.358644
      ]
    },
    "data": [
      {
        "dataFilter": {
          "timeRange": {
            "from": "2024-08-14T00:00:00Z",
            "to": "2024-09-14T23:59:59Z"
          }
        },
        "type": "sentinel-2-l2a"
      }
    ]
  },
  "output": {
    "width": 512,
    "height": 366.517,
    "responses": [
      {
        "identifier": "default",
        "format": {
          "type": "image/jpeg"
        }
      },
      {
        "identifier": "dataMask",
        "format": {
          "type": "image/tiff"
        }
      }
    ]
  },
  "evalscript": "//VERSION=3\nfunction setup() {\n  return {\n    input: [\"B03\", \"B04\", \"B08\", \"dataMask\"],\n    output: [\n      { id: \"default\", bands: 4 },\n      { id: \"index\", bands: 1, sampleType: \"FLOAT32\" },\n      { id: \"eobrowserStats\", bands: 2, sampleType: \"FLOAT32\" },\n      { id: \"dataMask\", bands: 1 },\n    ],\n  };\n}\n\nfunction evaluatePixel(samples) {\n  let val = index(samples.B08, samples.B04);\n  let imgVals = null;\n  // The library for tiffs works well only if there is only one channel returned.\n  // So we encode the \"no data\" as NaN here and ignore NaNs on frontend.\n  const indexVal = samples.dataMask === 1 ? val : NaN;\n\n  if (val < -0.5) imgVals = [0.05, 0.05, 0.05, samples.dataMask];\n  else if (val < -0.2) imgVals = [0.75, 0.75, 0.75, samples.dataMask];\n  else if (val < -0.1) imgVals = [0.86, 0.86, 0.86, samples.dataMask];\n  else if (val < 0) imgVals = [0.92, 0.92, 0.92, samples.dataMask];\n  else if (val < 0.025) imgVals = [1, 0.98, 0.8, samples.dataMask];\n  else if (val < 0.05) imgVals = [0.93, 0.91, 0.71, samples.dataMask];\n  else if (val < 0.075) imgVals = [0.87, 0.85, 0.61, samples.dataMask];\n  else if (val < 0.1) imgVals = [0.8, 0.78, 0.51, samples.dataMask];\n  else if (val < 0.125) imgVals = [0.74, 0.72, 0.42, samples.dataMask];\n  else if (val < 0.15) imgVals = [0.69, 0.76, 0.38, samples.dataMask];\n  else if (val < 0.175) imgVals = [0.64, 0.8, 0.35, samples.dataMask];\n  else if (val < 0.2) imgVals = [0.57, 0.75, 0.32, samples.dataMask];\n  else if (val < 0.25) imgVals = [0.5, 0.7, 0.28, samples.dataMask];\n  else if (val < 0.3) imgVals = [0.44, 0.64, 0.25, samples.dataMask];\n  else if (val < 0.35) imgVals = [0.38, 0.59, 0.21, samples.dataMask];\n  else if (val < 0.4) imgVals = [0.31, 0.54, 0.18, samples.dataMask];\n  else if (val < 0.45) imgVals = [0.25, 0.49, 0.14, samples.dataMask];\n  else if (val < 0.5) imgVals = [0.19, 0.43, 0.11, samples.dataMask];\n  else if (val < 0.55) imgVals = [0.13, 0.38, 0.07, samples.dataMask];\n  else if (val < 0.6) imgVals = [0.06, 0.33, 0.04, samples.dataMask];\n  else imgVals = [0, 0.27, 0, samples.dataMask];\n\n  return {\n    default: imgVals,\n    index: [indexVal],\n    eobrowserStats: [val, isCloud(samples) ? 1 : 0],\n    dataMask: [samples.dataMask],\n  };\n}\n\nfunction isCloud(samples) {\n  const NGDR = index(samples.B03, samples.B04);\n  const bRatio = (samples.B03 - 0.175) / (0.39 - 0.175);\n  return bRatio > 1 || (bRatio > 0 && NGDR > 0);\n}\n"
}


response = requests.post(url, headers=headers, json=data)



# Check if the request was successful
if response.status_code == 200:
    # Save the image as JPEG
    with open("default.jpg", "wb") as f:
        f.write(response.content)
    print("Image saved as default.jpg")
else:
    print(f"Failed to retrieve image. Status code: {response.status_code}")