from device import Device


class RepairService:

    devices_on_repair = [
        Device(1, "MacBook Pro", "Unexpectedly shutting down"),
        Device(2, "Macbook Pro", "An odd stage light effect at the bottom of the display when the lid is fully opened"),
        Device(3, "iPad Pro", "No sound"),
        Device(4, "iPhone XR", "White screen"),
        Device(5, "MacBook Air", "TouchID does not work"),
        Device(6, "iPhone 11 Pro Max Plus S", "Dust on camera")
    ]

    def get_devices(self):
        return self.devices_on_repair

    def get_device_by_id(self, id):
        return list(filter(lambda d: d.id == id, self.devices_on_repair))

    def add_device(self, name, issue):
        new_device_id = self.devices_on_repair[-1].id + 1
        new_device = Device(new_device_id, name, issue)
        self.devices_on_repair.append(new_device)
        return new_device

    def update_device(self, id, name, issue):
        device_update = self.get_device_by_id(id)
        if len(device_update) == 0:
            return device_update
        device_update[0].name = name
        device_update[0].issue = issue
        return device_update

    def delete_device(self, id):
        device_for_delete = list(filter(lambda d: d.id == id, self.devices_on_repair))
        if len(device_for_delete) != 0:
            return False
        self.devices_on_repair.remove(device_for_delete[0])
        return True
