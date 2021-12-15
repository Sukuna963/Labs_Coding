EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

def bake_time_remaining(elapsed_bake_time):
    '''
    '''
    return EXPECTED_BAKE_TIME - elapsed_bake_time
   
def preparation_time_in_minutes(number_of_layers):
    ''' 
    :param number_of_layers: int the number of lasagna layers made
    :return: int amount of prep time (in minutes), based on constant PREPARATION_TIME
 
    This function takes an integer representing the number of layers added to the dish,
    calculating preparation time using a PREPARATION_TIME.
    '''
    
    return number_of_layers * PREPARATION_TIME

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    ''' 
    :param number_of_layers: int the number of layers added to the lasagna
    :param elapsed_bake_time: int the number of minutes the lasagna has been baking in the oven
    :return:  int total time elapsed (in in minutes) preparing and cooking
 
     This function takes two numbers representing the number of layers & the time already spent 
    baking and calculates the total elapsed minutes spent cooking the lasagna.
    '''
    
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time