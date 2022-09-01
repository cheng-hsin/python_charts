def temperature_converter(degree, from_scale, to_scale):
    """
    >>> temperature_converter(0, 'Celsius', 'Fahrenheit')
    32.0
    >>> temperature_converter(0, 'Celsius', 'Kelvin')
    273.15
    >>> temperature_converter(32, 'Fahrenheit', 'Celsius')
    0.0
    >>> temperature_converter(32, 'Fahrenheit', 'Kelvin')
    273.15
    >>> temperature_converter(273.15, 'Kelvin', 'Celsius')
    0.0
    >>> temperature_converter(273.15, 'Kelvin', 'Fahrenheit')
    32.0
    """
    ### BEGIN SOLUTION
    #Fahrenheit = Celsius*9/5+32 = (Kelvin-273.15)*9/5+32
    #Kelvin = Celsius+273.15 = (Fahrenheit-32)*5/9+273.15
    #Celsius = Kelvin-273.15 = (Fahrenheit-32)*5/9
    
    if from_scale == 'Celsius' and to_scale == 'Fahrenheit':
        return print(degree*9/5+32)
    if from_scale == 'Celsius' and to_scale == 'Kelvin':
        return degree+273.15
    if from_scale == 'Fahrenheit' and to_scale == 'Celsius':
        return degree*9/5+32
    if from_scale == 'Fahrenheit' and to_scale == 'Kelvin':
        return (degree-32)*5/9+273.15
    if from_scale == 'Kelvin' and to_scale == 'Celsius':
        return degree-273.15
    if from_scale == 'Kelvin' and to_scale == 'Fahrenheit':
        return (degree-273.15)*9/5+32

temperature_converter(0, 'Celsius', 'Fahrenheit')
