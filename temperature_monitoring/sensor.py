from exception import SensorReadError, SensorOutOfRangeError
from logger import TemperatureLogger
import random

class TemperatureSensor:
    min_temp = -50
    max_temp = 50
    
    def __init__(self, sensor_id, location):
        self.sensor_id = sensor_id
        self.location = location
        self.logger = TemperatureLogger()
        self.current_temp = None
    
    def baca_suhu(self):
        try:
            temp = self._simulator_sensor_read()
            
            #Validasi
            if temp < self.min_temp or temp > self.max_temp:
                raise SensorOutOfRangeError(f'Suhu {temp}°C berada di luar batas yang ditentukan.')
            
            self.current_temp = temp
            self.logger.log_info(f'[{self.sensor_id}] Suhu dibaca: {temp}°C di lokasi {self.location}.')
            return temp
        
        except SensorOutOfRangeError as e:
            self.logger.log_error(f'[{self.sensor_id}] {e.message}')
            raise
        except Exception as e:
            error_msg = f'[{self.sensor_id}] Terjadi kesalahan saat membaca sensor: {str(e)}'
            self.logger.log_error(error_msg)
            raise SensorReadError(error_msg)
    
    def _simulator_sensor_read(self):
        
        if random.random() < 0.1:
            raise Exception('Simulasi kesalahan sensor.')
        return round(random.uniform(-60, 60), 2)
    
    def get_status(self):
        if self.current_temp is None:
            return f'Sensor {self.sensor_id} di {self.location} belum membaca suhu.'
        
        status = 'OK'
        if self.current_temp < 0:
            status = 'Dingin'
        elif self.current_temp > 30:
            status = 'Panas'
        
        return f'Sensor {self.sensor_id} di {self.location}: Suhu saat ini {self.current_temp}°C - Status: {status}'