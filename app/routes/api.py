from flask import request
from app import app
from app.controllers.health_indicator import HealthIndicator
from app.libraries.slug_validate import SlugValidate
from app.controllers.privilege_types import PrivilegeTypes

@app.route('/api')
def helloapi():
    return "Hello World!"

## Health Check ##
@app.route('/health')
def health_indicator():
    return HealthIndicator().run()
##################

## Privilege Types ##
@app.route('/privilege-type')
def privilegetypelistapi():
    return PrivilegeTypes(request).get_list()

@app.route('/privilege-type/<value>')
def privilegetypedetailapi(value):
    if value.isnumeric():
        return PrivilegeTypes(request).get_detail('id', value)

    if SlugValidate().run(value):
        return PrivilegeTypes(request).get_detail('error', value)

    return PrivilegeTypes(request).get_detail('name', value)

@app.route('/privilege-type', methods=['POST'])
def privilegetypecreateapi():
    return PrivilegeTypes(request).create_data()

@app.route('/privilege-type/<id>', methods=['PUT'])
def privilegetypeupdateapi(id):
    return PrivilegeTypes(request).update_data(id)

@app.route('/privilege-type/<id>', methods=['DELETE'])
def privilegetypedeleteapi(id):
    return PrivilegeTypes(request).delete_data(id)
##################
