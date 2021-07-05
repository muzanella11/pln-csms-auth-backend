from flask import request
from app import app
from app.controllers.health_indicator import HealthIndicator
from app.libraries.slug_validate import SlugValidate
from app.controllers.privilege_types import PrivilegeTypes
from app.controllers.user_roles import UserRoles

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

## User Role ##
@app.route('/user-role')
def userrolelistapi():
    return UserRoles(request).get_list()

@app.route('/user-role/<value>')
def userroledetailapi(value):
    if value.isnumeric():
        return UserRoles(request).get_detail('id', value)

    if SlugValidate().run(value):
        return UserRoles(request).get_detail('error', value)

    return UserRoles(request).get_detail('name', value)

@app.route('/user-role', methods=['POST'])
def userrolecreateapi():
    return UserRoles(request).create_data()

@app.route('/user-role/<id>', methods=['PUT'])
def userroleupdateapi(id):
    return UserRoles(request).update_data(id)

@app.route('/user-role/<id>', methods=['DELETE'])
def userroledeleteapi(id):
    return UserRoles(request).delete_data(id)
##################
