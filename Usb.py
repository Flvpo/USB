import pywinusb.hid as hid

# Enumerar todos los dispositivos HID (Human Interface Device) USB conectados
def enumerar_dispositivos_usb():
    dispositivos = hid.find_all_hid_devices()

    if dispositivos:
        for dispositivo in dispositivos:
            print(f"ID del Vendedor: 0x{dispositivo.vendor_id:04X}")
            print(f"ID del Producto: 0x{dispositivo.product_id:04X}")
            print(f"Nombre del Dispositivo: {dispositivo.product_name}")
            print("-----------------------------")
    else:
        print("No se encontraron dispositivos HID USB conectados.")

if __name__ == "__main__":
    enumerar_dispositivos_usb()
