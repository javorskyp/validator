import collections
import re

Token = collections.namedtuple('Token', ['type', 'value', 'line', 'column']) 

token_specification = [ 
    ('SCIFIC',   r'-?[1-9](\d*)(?:\.\d+)?[Ee][-+]?\d+'),  ##   Scientific notation values         ##
    ('INT',      r'(?<![\.\w\-eE])-?(\d+)(?![\d\.Ee])'),  ##   Integer values                     ##
    ('DECIMAL',  r'-?\d*(\.\d+)'),                        ##   Decimal values                     ## 
    ('EQUAL',    r'='),                                   ##   Assignm operator                   ##
    ('ID',       r'[A-Za-z_0-9]+'),                       ##   Identifiers                        ##
    ('COMA',     r','),                                   ##   Coma                               ## 
    ('SKIP',     r'([ \t])'),                             ##   Skip over spaces and tabs          ##
    ('OBR',      r'\('),                                  ##   Open bracket round                 ##
    ('CBR',      r'\)'),                                  ##   Close bracket round                ## 
    ('ARRAY_OPEN',      r'\['),                           ##   Open ARRAY bracket                 ##
    ('ARRAY_CLOSE',      r'\]'),                          ##   Close ARRAY bracket                ## 
    ('JOIN',     r'\-\-'),                                ##   Circiut symbol of Joining between  ## 
    ('NEWLINE',  r'\n'),                                  ##   End of line                        ## 
]

class Scanner:
    keywords = {'begin', 'resistor', 'capacitor', 'voltagesource', 'voltageprobe', 'currentsource', 'currentprobe', 'inductor', 'diode', 'end', 'gnd', 'EOF'} 

    def __init__(self, input, fix):
        self.fix = fix  
        self.tokens = [] 
        self.current_token_number = 0  
        for token in self.tokenize(input): self.tokens.append(token)
        for token in self.tokenize(input): print(token)
        
    def tokenize(self, input_string):
        tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification) 
        get_token = re.compile(tok_regex).match
        line_number = 1
        current_position = line_start = 0 
        match = get_token(input_string)
        while match is not None: 
            type = match.lastgroup 
            if type == 'NEWLINE':
                yield (Token(type, '\n', line_number, match.start() - line_start)) 
                line_start = current_position 
                line_number += 1
            elif type != 'SKIP': 
                value = match.group(type)
                if type == 'ID' and value in self.keywords:
                    type = value.upper() 
                yield (Token(type, value, line_number, match.start()-line_start)) 
            current_position = match.end() 
            match = get_token(input_string, current_position) 
        if current_position != len(input_string):
            raise RuntimeError('Error: Unexpected character %r on line %d' % \
                                (input_string[current_position], line_number))
        yield (Token('EOF', '', line_number, current_position-line_start)) 

    def next_token(self): 
        self.current_token_number += 1 
        if self.current_token_number-1 < len(self.tokens): 
            return self.tokens[self.current_token_number-1]
        else:  raise RuntimeError('Error: No more tokens') 