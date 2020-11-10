# ejemplo basico de uso de la API de OS.
# reemplazar por un token valido y por el dominio de OS que se eta usando
# como token se puede usar el que entrega OS para el acceso desde consola o sino se puede crear uno desde linea de comando con:
# oc create sa robot
# dar acceso al proyecto al token con:
# oc policy add-role-to-user view system:serviceaccount:{mi_proyecto}:robot
# buscar en la consola el token "robot", copiar el token y pegarlo en la variable "tToken"

import requests
if 1 == 1:
    tToken = "eyJhbGciOiJSUzI1NiIsImtpZCI6IiJ9.eyJpc3MiOiJrdWJlcm5ldGVzL3NlcnZpY2VhY2NvdW50Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9uYW1lc3BhY2UiOiJzZXIiLCJrdWJlcm5ldGVzLmlvL3NlcnZpY2VhY2NvdW50L3NlY3JldC5uYW1lIjoicm9ib3QtdG9rZW4tanBtOWMiLCJrdWJlcm5ldGVzLmlvL3NlcnZpY2VhY2NvdW50L3NlcnZpY2UtYWNjb3VudC5uYW1lIjoicm9ib3QiLCJrdWJlcm5ldGVzLmlvL3NlcnZpY2VhY2NvdW50L3NlcnZpY2UtYWNjb3VudC51aWQiOiJhZTNjYjQ1Zi0yMzA1LTExZWItODQyNy0wMjQyYWMxMTAwMDkiLCJzdWIiOiJzeXN0ZW06c2VydmljZWFjY291bnQ6c2VyOnJvYm90In0.vYXpUnBZkZyatYMGWrwXdmRKCsdt4pTQKwTT6d30z2rxIO4OZdmXMT_iFGFKnZGDtQj4XGtwT0KAEaxXUfFLiw55mDRs6XElpH7oQx3at4BqCgKSEQg0UedZwKoBeKhQ8_8yqlJH6jwH0Y4GOZSCkeSZOPb598CjiSxsyKHNc91nDuIRV7Kma2dnspUJjOYBhywpRxVIkmRFGNb6kwUKz7_mUz34keAM2VEG99YGQJL6D7PnYCmJ-ONIuGYgwJ1QyFTDHZxEP-9CcNPpEr2Tca4DhGjZtdxp01R7uQV3cFa7j3jHY1Qxgv7EdLikTSgpTizQDBRCulMRPdTK2V1W8w"
    token = "Bearer " + tToken
    cabe = {'Authorization': token, 'Accept': 'application/json'}
    base = "https://2886795273-8443-kitek03.environments.katacoda.com/"
    endpoint = "apis/user.openshift.io/v1/users/~"
    endpoint = "/api/v1/namespaces/ser/pods"

    r = requests.get(base + endpoint, headers = cabe, verify=False).json()
    print (r)
