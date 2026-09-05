from sensor import TemperatureSensor
from exception import SensorReadError, SensorOutOfRangeError
import time

def main():
    print("=" * 60)
    print("SISTEM MONITORING SUHU")
    print("=" * 60)
    
    # Create sensors
    sensor1 = TemperatureSensor("SENSOR-001", "Ruang Server")
    sensor2 = TemperatureSensor("SENSOR-002", "Outdoor")
    
    sensors = [sensor1, sensor2]
    
    # Reading loop
    print("\n Memulai pembacaan sensor...\n")
    
    for i in range(10):  # 10 kali pembacaan
        print(f"\n--- Pembacaan #{i+1} ---")
        
        for sensor in sensors:
            try:
                # Baca suhu
                temp = sensor.baca_suhu()
                print(f" {sensor.location}: {temp}°C {sensor.get_status()}")
            
            except SensorOutOfRangeError as e:
                print(f" {sensor.location}: {e.message}")
            
            except SensorReadError as e:
                print(f" {sensor.location}: {e.message}")
            
            except Exception as e:
                print(f" {sensor.location}: Unexpected error - {e}")
        
        # Wait sebelum reading berikutnya
        time.sleep(1)
    
    # Summary
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    
    for sensor in sensors:
        print(f"{sensor.location}: {sensor.get_status()}")
    
    print("\n Check logs/temperature_errors.log untuk error details")
    print("\n Monitoring selesai!")

if __name__ == "__main__":
    main()