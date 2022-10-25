
from connection import *

def get_matching_records(features_list):
    rows = idadb.ida_query('''SELECT * FROM properties 
                                        WHERE BEDS>={0} AND BATHS>={1} AND SQFEET>={2} AND CATS_ALLOWED >={3} 
                                        AND DOGS_ALLOWED >={4} AND SMOKING_ALLOWED>={5} AND WHEELCHAIR_ACCESS >={6}
                                         AND ELECTRIC_VEHICLE_CHARGE >= {7}
                                        AND COMES_FURNISHED>={8} ;  
                            '''
                            .format(features_list['beds'],features_list['baths'],features_list['sqfeet'],
                            features_list['cats'],features_list['dogs'],features_list['Smoking Allowed'],features_list['Wheel-Chair Access'],
                            features_list['Electric-vehicle charging'],features_list['Furnished Apartment'],
                            features_list['Laundry'],features_list['Garage parking']))
    return rows

def get_range_of_values(column):
    max_value = idadb.ida_query('SELECT MAX({}) FROM properties'.format(column))
    min_value = idadb.ida_query('SELECT MIN({}) FROM properties'.format(column))
    return max_value,min_value



def get_all_records():
    rows = idadb.ida_query('''SELECT * FROM properties;''')
    return rows

