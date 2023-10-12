import requests
import json

jwt = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiJodHRwczovL3Jldm9sdXQuY29tIiwic3ViIjoia3FyVk14WG1ubkdDSnBXZmRnbEpiS05YcDExZmxuVDAtSUNzMGxDTFJ2NCIsImlzcyI6Im55bXRlY2gub2Rvb2FwcHMuY2giLCJleHAiOjIwMTIwODMyMDB9.puJiKFr-UmJp2PJd_FT5EcVTB4Kuyqwoh1crt9MSdTjteWbaQgBvADhn5gmnU08B6BfGuidENEnfg4zHQQk453yj1mTFIAQYWPYsmitaQB5DiXG6dzjjkeiakiuyyp-fMbU636ToUkWPKc1plr1VDMZt4yXICsDaz9RpbmUtDYiJBs7-EUAgpikUiG_nzqopa3qHPZnpIyNEo9piBKvYpd-BxqgMRLeRzx--Qu0zdQxbWEmDGxijk2IZC-QlPIFwCKpoOfSaze0wL5LPI0zwWshyYDkgz-zDUUvB5qPHHs0JETtOKnB74AtSW1Gam3DbUj-nHJ--nL6pUuqFo4K3-w"
access_token = "oa_prod_nd2-RrQ8PH4jz_QbafdPtLJtc1_CrqPkWhRWU63_THg"
access_token = "oa_prod_nEN9iQjVPox9_cF5C_1CHp7zxwPnzI071b_fGp7kTt4"
access_token = "oa_prod_vHBbK3aLtWoFMK43-LBP_It383jB9O3VN2wOXvtuRM4"
refresh_token = "oa_prod_h9NoOIbBOFUKyp-IVS9C953_1NUCx5F6DfktuCzEQXQ"
url = "https://b2b.revolut.com/api/1.0"


payload = {
}
headers = {
    'Accept': 'application/json',
    'Authorization': f'Bearer {access_token}'
}




# response = requests.request("GET", url + '/accounts', headers=headers, data=payload)
# print(response.text)
# accounts = json.loads(response.text)




headers = {'Content-Type': 'application/x-www-form-urlencoded'}
data = {
    'grant_type': 'refresh_token',
    'refresh_token': refresh_token,
    'client_assertion_type': 'urn:ietf:params:oauth:client-assertion-type:jwt-bearer',
    'client_assertion': jwt,
}
print(data)
res = requests.post(url + '/auth/token', headers=headers, data=data)
print(res.text)
