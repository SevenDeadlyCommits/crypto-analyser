from dataclasses import dataclass

@dataclass
class SimpleResult():
    min_value: float
    min_value_date: str
    max_value: float
    max_value_date: str

    def __str__(self):
        return 'Min value: ' + str(self.min_value) + '\nMin value acheived: ' + self.min_value_date + '\nMax value: ' + str(self.max_value) + '\nMax value acheived: ' + self.max_value_date