#!flask/bin/python
from fastapi import FastAPI
from starlette.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from repair_service import RepairService
from pydantic import BaseModel

app = FastAPI()

class Device(BaseModel):
    id: int
    name: str
    issue: str

service = RepairService()

@app.get("/repair_service/api/v1.0/devices_on_repair")
def get_devices():
    json_compatible_item_data = jsonable_encoder(service.get_devices())
    return JSONResponse(content=json_compatible_item_data)


@app.get('/repair_service/api/v1.0/devices_on_repair/<int:device_id>')
def get_device(device_id: int):
    device_on_repair = service.get_device_by_id(device_id)
    if len(device_on_repair) == 0:
        return {'error_code': "404"}
    json_compatible_item_data = jsonable_encoder(device_on_repair[0])
    return JSONResponse(content=json_compatible_item_data)

@app.post('/repair_service/api/v1.0/devices_on_repair')
def create_device(device: Device):
    new_device = service.add_device(device.name, device.issue)
    json_compatible_item_data = jsonable_encoder(new_device)
    return JSONResponse(content=json_compatible_item_data)

@app.put('/repair_service/api/v1.0/devices_on_repair/<int:device_id>')
def update_device(device: Device):
    device_update = service.update_device(device.id, device.name, device.issue)
    if len(device_update) == 0:
        return {'error_code': "404"}
    json_compatible_item_data = jsonable_encoder(device_update[0])
    return JSONResponse(content=json_compatible_item_data)

@app.delete('/repair_service/api/v1.0/devices_on_repair/<int:device_id>')
def delete_device(device_id: int):
    if service.delete_device(device_id):
        return {'result': True}
    return {'error_code': "404"}
