from scanner import *

class Parser: # Parser header #

    def __init__(self, scanner, fix):
        self.fix = fix 
        print('\n PARSER \n\n')
        self.next_token = scanner.next_token 
        self.token = self.next_token()
        
    def take_token(self, token_type):
        if self.token.type != token_type:
            self.error(f"Expected token: {token_type}, but found token: {self.token.type} value: '{self.token.value}'. Line: {self.token.line}, column: {self.token.column}")
        if token_type != 'END':
            if self.fix is True: print({self.token}) 
            self.token = self.next_token()
            
    def error(self,msg): raise RuntimeError('Parser error, %s' % msg)

                # Parser body #

    def start(self):      # Start symbol
        self.program()  # Start program
        
    def program(self): # program -> BEGIN NEWLINE module_definitions module_emptySpace module_connections END
        if  (self.token.type == 'BEGIN'): 
            print(' The program starts!')
            self.take_token('BEGIN')
            self.take_token('NEWLINE')
            print(' module_definitions start')
            self.module_definitions()
            print(' module_definitions completed!')
            self.module_emptySpace() 
            print(' module_connections start')
            self.module_connections()
            print(' module_connections completed!')
            self.take_token('END')
            print(' Program completed!') 
        else: self.error('Begin token needed!')
            
    def module_definitions(self):   # module_definitions -> define module_definitions      
        if (self.token.type == 'ID'):
            self.define()
            self.module_definitions()
       
    def define(self): # define -> ID EQUAL key_state NEWLINE
        if (self.token.type == 'ID'):
            print(' define start')
            self.take_token('ID') 
            self.take_token('EQUAL')
            self.key_state () 
            self.take_token('NEWLINE')
           
    def key_state(self):
        if   (self.token.type == 'RESISTOR'):  self.resistor()
        elif (self.token.type == 'CAPACITOR'): self.capacitor()
        elif (self.token.type == 'DIODE'): self.diode()
        elif (self.token.type == 'VOLTAGESOURCE'): self.voltagesource() 
        elif (self.token.type == 'CURRENTSOURCE'): self.currentsource()
        elif (self.token.type == 'VOLTAGEPROBE'): self.voltageprobe()
        elif (self.token.type == 'CURRENTPROBE'): self.currentprobe() 
        elif (self.token.type == 'INDUCTOR'): self.inductor() 
             
    def resistor(self): # resistor -> RESISTOR OBR number CBR
        if (self.token.type == 'RESISTOR'):
            self.take_token('RESISTOR') 
            self.take_token('OBR')
            self.number()
            self.take_token('CBR')
            print(' resistor key_state completed!')
        else: self.error('Resistor token needed!')
    
    def capacitor(self): # capacitor -> CAPACITOR OBR NUMBER CBR
        if (self.token.type == 'CAPACITOR'):
            self.take_token('CAPACITOR')
            self.take_token('OBR')
            self.number() 
            self.take_token('CBR')
            print(' capacitor key_state completed!') 
        else: self.error('Capacitor token needed!')

    def voltagesource(self):  # voltagesource -> VOLTAGESOURCE OBR any_number CBR
        if (self.token.type == 'VOLTAGESOURCE'): 
            self.take_token('VOLTAGESOURCE')
            self.take_token('OBR')
            self.any_number() 
            self.take_token('CBR')
            print(' voltagesource key_state completed!')
        else: self.error('Voltagesource token needed!') 
            
    def voltageprobe(self): # voltageprobe -> VOLTAGREPROBE OBR CBR 
        if (self.token.type == 'VOLTAGEPROBE'):
            self.take_token('VOLTAGEPROBE') 
            self.take_token('OBR')
            self.take_token('CBR') 
            print(' voltageprobe key_state completed!')
        else: self.error('Voltageprobe token needed!')
    
    def currentsource(self):  # currentsource -> CURRENTSOURCE OBR any_number CBR
        if (self.token.type == 'CURRENTSOURCE'): 
            self.take_token('CURRENTSOURCE')
            self.take_token('OBR')
            self.any_number() 
            self.take_token('CBR')
            print(' currentsource key_state completed!')
        else: self.error('Currentsource token needed!') 

    def currentprobe(self):   # currentprobe -> CURRENTPROBE OBR CBR
        if (self.token.type == 'CURRENTPROBE'):
            self.take_token('CURRENTPROBE') 
            self.take_token('OBR')
            self.take_token('CBR')
            print(' currentprobe key_state completed!')
        else: self.error('Currentprobe token needed!') 
    
    def inductor(self):   # inductor -> INDUCTOR OBR number CBR
        if (self.token.type == 'INDUCTOR'):
            self.take_token('INDUCTOR')
            self.take_token('OBR')
            self.number() 
            self.take_token('CBR')
            print(' inductor key_state completed!')
        else: self.error('Inductor token needed!') 
    
    def diode(self):  # diode -> DIODE OBR diode_arguments CBR 
        if (self.token.type == 'DIODE'): 
            print(' diode key_state  start')
            self.take_token('DIODE')
            self.take_token('OBR')
            self.diode_arguments() 
            self.take_token('CBR') 
            print(' diode key_state completed!')
        else: self.error('Diode token needed!') 
             
    def any_number(self):    # any_number -> number
        if (self.token.type in ['INT', 'DECIMAL', 'SCIFIC']):
            self.number()

    def number(self): # number ->  INT, DECIMAL, SCIFIC
        if (self.token.type == 'INT'):
            self.take_token('INT')
        elif self.token.type == 'DECIMAL':
            self.take_token('DECIMAL') 
        elif self.token.type == 'SCIFIC':
            self.take_token('SCIFIC')
        else: self.error('Expected value but found nothing on line..')
            
    def diode_arguments(self): # diode_arguments -> argument second_argument
        if (self.token.type == 'ID'):
            print(' diode_arguments start') 
            self.argument()
            self.next_argument()
            print(' diode_arguments completed!')
     
    def argument(self): # argument -> ID EQUAL number
        if (self.token.type == 'ID'): 
            self.take_token('ID')
            self.take_token('EQUAL')
            self.number()
            print(' argument completed!') 
        else: self.error('expected ID token')
            
    def next_argument(self): # next_argument -> COMA argument next_argument
        if (self.token.type == 'COMA'):
            self.take_token('COMA') 
            self.argument()
            self.next_argument()
        
    def module_emptySpace(self): # module_emptySpace -> NEWLINE block_empty
        if (self.token.type == 'NEWLINE'):
            print(' module_emptySpace start')
            self.take_token('NEWLINE') 
            self.block_empty()
            print(' module_emptySpace completed!')
        else: self.error('Newline token needed!')
             
    def block_empty(self): # block_empty -> NEWLINE block_empty
        if (self.token.type == 'NEWLINE'):
            self.take_token('NEWLINE') 
            self.block_empty() 
        else:              # block_empty -> epsilon
            pass        
            
    def module_connections(self): # module_connections -> single_connection module_connections 
        if (self.token.type in ['ID', 'GND']):
            self.single_connection() 
            self.module_connections() 
        
    def single_connection(self): # single_connection -> connection_value JOIN connection_value join_connector NEWLINE
        if (self.token.type in ['ID', 'GND']):
            print(' single_connection start')
            self.connection_value()  
            self.take_token('JOIN')
            self.connection_value()
            self.join_connector() 
            self.take_token('NEWLINE')
            print(' single_connection completed!') 
        else: self.error('Expected ID or GND tokens')
    
    def index_valueINT(self):
        if (self.token.type == 'ID'): # index_valueINT -> ID ARRAY_OPEN INT ARRAY_CLOSE
            self.take_token('ID') 
            self.take_token('ARRAY_OPEN') 
            self.take_token('INT')
            self.take_token('ARRAY_CLOSE') 
        else: self.error('ID token needed!')      
    
    def join_connector(self): # join_connector -> JOIN connection_value join_connector
        if (self.token.type == 'JOIN'): 
            self.take_token('JOIN') 
            self.connection_value()
            self.join_connector()
            
    def connection_value(self):
        print(' connection_value start')
        if (self.token.type == 'GND'): # connection_value -> GND 
            self.take_token('GND')
            print(' connection_value completed!')
        elif self.token.type == 'ID': # connection_value -> index_valueINT 
            self.index_valueINT() 
            print(' connection_value completed!')
        else: self.error('GND or ID tokens needed!') 