#Q6
class Cell_Phone:
    
    def __init__(self,manufacturer,model_number,retail_price):
       self.__manufacturer = manufacturer
       self.__model_number = model_number
       self.__retail_price = retail_price

    def set_manufacturer(self,manufacturer):
        self.__manufacturer = manufacturer
    def set_model (self,model_number):
        self.__model_number = model_number
    def set_reatil_price(self,retail_price):
        self.__retail_price = retail_price  
        
    def get_manufacturer(self):   
        return self.__manufacturer
    def get_retail_price(self):
        return self.__retail_price
    def get_model_number(self):
        return self.__model_number  