#!flask/bin/python
from fastapi import FastAPI
from starlette.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from repair_service import RepairService
from pydantic import BaseModel
from device import Device

app = FastAPI()

class DeviceModel(BaseModel):
    id: int
    name: str
    issue: str

service = RepairService()

@app.get("/repair_service/api/v1.0/devices_on_repair")
def get_devices():
    json_compatible_item_data = jsonable_encoder(service.devices_on_repair)
    return JSONResponse(content=json_compatible_item_data)


@app.get('/repair_service/api/v1.0/devices_on_repair/<int:device_id>')
def get_device(device_id: int):
    device_on_repair = list(filter(lambda d: d.id == device_id, service.devices_on_repair))
    if len(device_on_repair) == 0:
        return {'error_code': "404"}
    json_compatible_item_data = jsonable_encoder(device_on_repair[0])
    return JSONResponse(content=json_compatible_item_data)

@app.post('/repair_service/api/v1.0/devices_on_repair')
def create_device(device: DeviceModel):
    new_device_id = service.devices_on_repair[-1].id + 1
    new_device = Device(new_device_id, device.name, device.issue)
    service.devices_on_repair.append(new_device)
    json_compatible_item_data = jsonable_encoder(new_device)
    return JSONResponse(content=json_compatible_item_data)

@app.put('/repair_service/api/v1.0/devices_on_repair/<int:device_id>')
def update_device(device: DeviceModel):
    device_update = list(filter(lambda d: d.id == device.id, service.devices_on_repair))
    if len(device_update) == 0:
        return {'error_code': "404"}
    device_update[0].name = device.name
    device_update[0].issue = device.issue
    json_compatible_item_data = jsonable_encoder(device_update[0])
    return JSONResponse(content=json_compatible_item_data)

@app.delete('/repair_service/api/v1.0/devices_on_repair/<int:device_id>')
def delete_device(device_id: int):
    device_for_delete = list(filter(lambda d: d.id == device_id, service.devices_on_repair))
    if len(device_for_delete) == 0:
        return {'error_code': "404"}
    service.devices_on_repair.remove(device_for_delete[0])
    return {'result': True}