from PIL import Image

def encode_image(img, secret_message):
    img = img.convert("RGB") 
    pixels = img.load()

    secret_message += "#####"
    binary_message = ''.join(format(ord(char), '08b') for char in secret_message)

    data_index = 0
    width, height = img.size
    
    for y in range(height):
        for x in range(width):
            pixel = list(pixels[x, y])

            for i in range(3): 
                if data_index < len(binary_message):
                    pixel[i] = pixel[i] & ~1 | int(binary_message[data_index])
                    data_index += 1

            pixels[x, y] = tuple(pixel)

            if data_index >= len(binary_message):
                return img
    
    return img

def decode_image(img):
    img = img.convert("RGB")
    pixels = img.load()

    binary_data = ""
    width, height = img.size

    for y in range(height):
        for x in range(width):
            pixel = pixels[x, y]

            for i in range(3):
                binary_data += str(pixel[i] & 1)

    all_bytes = [binary_data[i:i+8] for i in range(0, len(binary_data), 8)]

    decoded_message = ""

    for byte in all_bytes:
        decoded_message += chr(int(byte, 2))

        if decoded_message.endswith("#####"):
            return decoded_message[:-5]

    return "Tidak ada pesan tersembunyi yang ditemukan."
