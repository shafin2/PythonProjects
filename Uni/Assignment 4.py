def speed(meter,second):
    car_speed=meter/second
    return car_speed

def convert(speed_in_ms):
    speed_in_km=(speed_in_ms*3600)/1000
    return speed_in_km

if __name__ == '__main__':
    while(1):
        print("Enter the distance traveled by car (in meters) : ")
        try:
            meter = float(input())
            break
        except:
            print("Invalid input")
            continue
    while(True):
        print("Enter the time taken (in seconds) : ")
        try:
            second = float(input())
            break
        except:
            print("Invalid input")
            continue

speed_in_ms = speed(meter,second)
speed_in_km = convert(speed_in_ms)
speed_in_ms="{:.2f}".format(speed_in_ms)
speed_in_km="{:.2f}".format(speed_in_km)
print(f"The speed of the car is {speed_in_ms} m/s or {speed_in_km} km/h")