# -*- coding: utf-8 -*-
"""
Modified on Tuesday 15 Sept

@author: Chris Esterhuizen
"""

"""
==================
IMPORT LIBRARIES
==================
"""
import matplotlib
import serial
import numpy as np
from matplotlib import pyplot as plt
from mlxtend.evaluate import permutation_test
import pandas as pd
from scipy import stats
import statsmodels.api as sm
from statsmodels.formula.api import ols
'''
=====================
Functions
=====================
'''


def read_data_reference(filename='control.txt'):
    file_data = []
    count = 0
    with open(filename) as f:
        while True:
            count += 1

            # Get next line form file
            line = f.readline()
            file_data.append(line.strip("\n"))
            # If line is empty
            # end of file is reached

            if not line:
                break
            #print("Line{}: {}".format(count, line.strip()))
        del file_data[-1]
    return file_data


def read_data_contamination(filename='contamination.txt'):
    file_data = []
    count = 0
    with open(filename) as contamination:
        while True:
            count += 1

            # Get next line form file
            line = contamination.readline()
            file_data.append(line.strip("\n"))
            # If line is empty
            # end of file is reached

            if not line:
                break
            #print("Line{}: {}".format(count, line.strip()))
        del file_data[-1]
    return file_data


def read_data_sensor(filename):
    file_data = []
    count = 0
    with open(filename) as sensor:
        while True:
            count += 1

            # Get next line form file
            line = sensor.readline()
            file_data.append(line.strip("\n"))
            # If line is empty
            # end of file is reached

            if not line:
                break
            #print("Line{}: {}".format(count, line.strip()))
        del file_data[-1]
    return file_data

def average(lst):
    return sum(lst) / len(lst)


def convert_To_Int(lst):
    for i in range(0, len(lst)):
        lst[i] = int(lst[i])
    return lst


def read_serial_reference():
    ser = serial.Serial('COM4', baudrate=115200, timeout=0.1)
    serial_counter = 0

    '''Sensor Value .txt writer'''
    filepath_control = 'control.txt'
    file_control = open(filepath_control, 'w', newline='\n')

    while serial_counter <= 20:
        data = ser.readline().decode('ascii')
        file_control.writelines(data)
        serial_counter = serial_counter + 1

    file_control.close()
    print('Reference data serial reading is done')


def read_serial_sensor1():
    ser = serial.Serial('COM4', baudrate=115200, timeout=0.1)
    serial_counter = 0

    '''Sensor Value .txt writer'''
    filepath_control = 'sensor1.txt'
    file_control = open(filepath_control, 'w', newline='\n')

    while serial_counter <= 20:
        data = ser.readline().decode('ascii')
        file_control.writelines(data)
        serial_counter = serial_counter + 1

    file_control.close()
    print('sensor 1 data serial reading is done')


def read_serial_sensor2():
    ser = serial.Serial('COM4', baudrate=115200, timeout=0.1)
    serial_counter = 0

    '''Sensor Value .txt writer'''
    filepath_control = 'sensor2.txt'
    file_control = open(filepath_control, 'w', newline='\n')

    while serial_counter <= 20:
        data = ser.readline().decode('ascii')
        file_control.writelines(data)
        serial_counter = serial_counter + 1

    file_control.close()
    print('sensor 2 data serial reading is done')


def read_serial_sensor3():
    ser = serial.Serial('COM4', baudrate=115200, timeout=0.1)
    serial_counter = 0

    '''Sensor Value .txt writer'''
    filepath_control = 'sensor3.txt'
    file_control = open(filepath_control, 'w', newline='\n')

    while serial_counter <= 20:
        data = ser.readline().decode('ascii')
        file_control.writelines(data)
        serial_counter = serial_counter + 1

    file_control.close()
    print('sensor 3 data serial reading is done')


def read_serial_sensor4():
    ser = serial.Serial('COM4', baudrate=115200, timeout=0.1)
    serial_counter = 0

    '''Sensor Value .txt writer'''
    filepath_control = 'sensor4.txt'
    file_control = open(filepath_control, 'w', newline='\n')

    while serial_counter <= 20:
        data = ser.readline().decode('ascii')
        file_control.writelines(data)
        serial_counter = serial_counter + 1

    file_control.close()
    print('sensor 4 data serial reading is done')


def read_serial_sensor5():
    ser = serial.Serial('COM4', baudrate=115200, timeout=0.1)
    serial_counter = 0

    '''Sensor Value .txt writer'''
    filepath_control = 'sensor5.txt'
    file_control = open(filepath_control, 'w', newline='\n')

    while serial_counter <= 20:
        data = ser.readline().decode('ascii')
        file_control.writelines(data)
        serial_counter = serial_counter + 1

    file_control.close()
    print('sensor 5 data serial reading is done')


def read_serial_sensor6():
    ser = serial.Serial('COM4', baudrate=115200, timeout=0.1)
    serial_counter = 0

    '''Sensor Value .txt writer'''
    filepath_control = 'sensor6.txt'
    file_control = open(filepath_control, 'w', newline='\n')

    while serial_counter <= 20:
        data = ser.readline().decode('ascii')
        file_control.writelines(data)
        serial_counter = serial_counter + 1

    file_control.close()
    print('sensor 6 data serial reading is done')


def read_serial_sensor7():
    ser = serial.Serial('COM4', baudrate=115200, timeout=0.1)
    serial_counter = 0

    '''Sensor Value .txt writer'''
    filepath_control = 'sensor7.txt'
    file_control = open(filepath_control, 'w', newline='\n')

    while serial_counter <= 20:
        data = ser.readline().decode('ascii')
        file_control.writelines(data)
        serial_counter = serial_counter + 1

    file_control.close()
    print('sensor 7 data serial reading is done')


def read_serial_sensor8():
    ser = serial.Serial('COM4', baudrate=115200, timeout=0.1)
    serial_counter = 0

    '''Sensor Value .txt writer'''
    filepath_control = 'sensor8.txt'
    file_control = open(filepath_control, 'w', newline='\n')

    while serial_counter <= 20:
        data = ser.readline().decode('ascii')
        file_control.writelines(data)
        serial_counter = serial_counter + 1

    file_control.close()
    print('sensor 8 data serial reading is done')


def read_serial_contamination():
    ser = serial.Serial('COM4', baudrate=115200, timeout=0.1)
    serial_counter = 0

    '''Sensor Value .txt writer'''
    filepath_contamination = 'contamination.txt'
    file_contamination = open(filepath_contamination, 'w', newline='\n')

    while serial_counter <= 20:
        data = ser.readline().decode('ascii')
        file_contamination.writelines(data)
        serial_counter = serial_counter + 1

    file_contamination.close()
    print('Contamination data serial reading is done')


'''
=====================
Main Function
=====================
'''


def main():
    start_stop_flag = 0
    start_stop_flag_ANOVA = 0


    while start_stop_flag == 0:
        user_start_stop_input = input("Enter 1 for Start => ")
        if user_start_stop_input == "1":
            start_stop_flag = 1
        elif user_start_stop_input == "2":
            start_stop_flag = 0
        else:
            print("User input error: Please enter a 1 or a 2")
            start_stop_flag = 0

    '''
    =====================
    Permutation Test
    =====================
    '''

    while start_stop_flag == 1:
        user_input = input("Enter 1 for Clear Reference distribution or Enter 2 for Contamination Readings => ")

        if user_input == '1':
            print('You pressed 1 \n Now wait... \n')
            read_serial_reference()
            read_serial_data_reference = read_data_reference()
            data_final_reference = convert_To_Int(read_serial_data_reference)
            print(data_final_reference)
            avg_reference = np.mean(data_final_reference)
            print("The average of the reference data is: ", avg_reference)

            read_file_control = pd.read_csv(r'control.txt')
            read_file_control.columns = ['Control 1']
            read_file_control.to_csv('control.csv', index=None)

        elif user_input == '2':
            print('You pressed 2 \n Now wait... \n')
            read_serial_contamination()
            read_serial_data_contamination = read_data_contamination()
            data_final_contamination = convert_To_Int(read_serial_data_contamination)
            print(data_final_contamination)
            avg_contamination = np.mean(data_final_contamination)
            print("The average of the contamination data is: ", avg_contamination)
            start_stop_flag = 0

            read_file_contamination = pd.read_csv(r'contamination.txt')
            read_file_contamination.columns = ['Contamination 2']
            read_file_contamination.to_csv('contamination.csv', index=None)

            con = pd.concat([read_file_control, read_file_contamination], axis=1)
            con.to_csv('combined_csv.csv')

            df = pd.read_csv('combined_csv.csv')
            print(df)
        else:
            print('User Input Error: Please enter a 1 or a 2')

    p_value = permutation_test(data_final_contamination, data_final_reference, method='approximate', num_rounds=10000, seed=0)
    if(p_value < 0.05):
        print("Reject the Null Hypothesis: The difference has statistical significance: ", p_value)
    else:
        print("Accept the Null Hypothesis: The difference has NO statistical significance: ", p_value)

    '''
    =====================
    ANOVA Test
    =====================
    '''
    while start_stop_flag_ANOVA == 0:
        user_start_stop_input = input("Enter 1 for Start of ANOVA test => ")
        if user_start_stop_input == "1":
            start_stop_flag_ANOVA = 1
        elif user_start_stop_input == "2":
            start_stop_flag_ANOVA = 0
        else:
            print("User input error: Please enter a 1 or a 2")
            start_stop_flag_ANOVA = 0

    while start_stop_flag_ANOVA == 1:
        user_input_ANOVA = input("Enter sensor number for reading (1-8) =>")

        if user_input_ANOVA == '1':
            print('You pressed SENSOR 1 \n Now wait... \n')
            read_serial_sensor1()
            read_serial_data_sensor1 = read_data_sensor('sensor1.txt')
            data_final_sensor1 = convert_To_Int(read_serial_data_sensor1)
            print(data_final_sensor1)
            avg_sensor1 = np.mean(data_final_sensor1)
            print("The average of the sensor 1 data is: ", avg_sensor1)

            read_file1 = pd.read_csv(r'sensor1.txt')
            read_file1.columns = ['Sensor 1']
            read_file1.to_csv('sensor1.csv', index=None)

        elif user_input_ANOVA == '2':
            print('You pressed SENSOR 2 \n Now wait... \n')
            read_serial_sensor2()
            read_serial_data_sensor2 = read_data_sensor('sensor2.txt')
            data_final_sensor2 = convert_To_Int(read_serial_data_sensor2)
            print(data_final_sensor2)
            avg_sensor2 = np.mean(data_final_sensor2)
            print("The average of the sensor 2 data is: ", avg_sensor2)

            read_file2 = pd.read_csv(r'sensor2.txt')
            read_file2.columns = ['Sensor 2']
            read_file2.to_csv('sensor2.csv', index=None)

        elif user_input_ANOVA == '3':
            print('You pressed SENSOR 3 \n Now wait... \n')
            read_serial_sensor3()
            read_serial_data_sensor3 = read_data_sensor('sensor3.txt')
            data_final_sensor3 = convert_To_Int(read_serial_data_sensor3)
            print(data_final_sensor3)
            avg_sensor3 = np.mean(data_final_sensor3)
            print("The average of the sensor 3 data is: ", avg_sensor3)

            read_file3 = pd.read_csv(r'sensor3.txt')
            read_file3.columns = ['Sensor 3']
            read_file3.to_csv('sensor3.csv', index=None)

        elif user_input_ANOVA == '4':
            print('You pressed SENSOR 4 \n Now wait... \n')
            read_serial_sensor4()
            read_serial_data_sensor4 = read_data_sensor('sensor4.txt')
            data_final_sensor4 = convert_To_Int(read_serial_data_sensor4)
            print(data_final_sensor4)
            avg_sensor4 = np.mean(data_final_sensor4)
            print("The average of the sensor 4 data is: ", avg_sensor4)

            read_file4 = pd.read_csv(r'sensor4.txt')
            read_file4.columns = ['Sensor 4']
            read_file4.to_csv('sensor4.csv', index=None)

        elif user_input_ANOVA == '5':
            print('You pressed SENSOR 5 \n Now wait... \n')
            read_serial_sensor5()
            read_serial_data_sensor5 = read_data_sensor('sensor5.txt')
            data_final_sensor5 = convert_To_Int(read_serial_data_sensor5)
            print(data_final_sensor5)
            avg_sensor5 = np.mean(data_final_sensor5)
            print("The average of the sensor 5 data is: ", avg_sensor5)

            read_file5 = pd.read_csv(r'sensor5.txt')
            read_file5.columns = ['Sensor 5']
            read_file5.to_csv('sensor5.csv', index=None)

        elif user_input_ANOVA == '6':
            print('You pressed SENSOR 6 \n Now wait... \n')
            read_serial_sensor6()
            read_serial_data_sensor6 = read_data_sensor('sensor6.txt')
            data_final_sensor6 = convert_To_Int(read_serial_data_sensor6)
            print(data_final_sensor6)
            avg_sensor6 = np.mean(data_final_sensor6)
            print("The average of the sensor 6 data is: ", avg_sensor6)

            read_file6 = pd.read_csv(r'sensor6.txt')
            read_file6.columns = ['Sensor 6']
            read_file6.to_csv('sensor6.csv', index=None)

        elif user_input_ANOVA == '7':
            print('You pressed SENSOR 7 \n Now wait... \n')
            read_serial_sensor7()
            read_serial_data_sensor7 = read_data_sensor('sensor7.txt')
            data_final_sensor7 = convert_To_Int(read_serial_data_sensor7)
            print(data_final_sensor7)
            avg_sensor7 = np.mean(data_final_sensor7)
            print("The average of the sensor 7 data is: ", avg_sensor7)

            read_file7 = pd.read_csv(r'sensor7.txt')
            read_file7.columns = ['Sensor 7']
            read_file7.to_csv('sensor7.csv', index=None)

        elif user_input_ANOVA == '8':
            print('You pressed SENSOR 8 \n Now wait... \n')
            read_serial_sensor8()
            read_serial_data_sensor8 = read_data_sensor('sensor8.txt')
            data_final_sensor8 = convert_To_Int(read_serial_data_sensor8)
            print(data_final_sensor8)
            avg_sensor8 = np.mean(data_final_sensor8)
            print("The average of the sensor 8 data is: ", avg_sensor8)

            read_file8 = pd.read_csv(r'sensor8.txt')
            read_file8.columns = ['Sensor 8']
            read_file8.to_csv('sensor8.csv', index=None)

            start_stop_flag_ANOVA = 0

            frames = [read_file1, read_file2, read_file3, read_file4, read_file5, read_file6, read_file7, read_file8]

            concatenated_csv = pd.concat(frames, axis=1)
            concatenated_csv.to_csv('combined_csv_sensors.csv')

            df = pd.read_csv('combined_csv_sensors.csv')
            print(df)

    df_new = pd.melt(df.reset_index(), id_vars=None, value_vars=['Sensor 1', 'Sensor 2', 'Sensor 3', 'Sensor 4', 'Sensor 5', 'Sensor 6', 'Sensor 7', 'Sensor 8'])
    df_new.columns = ["SensorNumber", "Value"]
    df_new.head()
    print(df_new)

    model = ols("Value ~ C(SensorNumber)", data=df_new).fit()
    one_way_anova = sm.stats.anova_lm(model, typ=1)
    print(one_way_anova)

if __name__ == "__main__":
    main()






