"""oven_temp_converter.py

    Modified from ex_temp_converter.py by Leif Roschier. Creates
    nomograph that converts to/from celsius from/to Fahrenheit in the
    range needed for oven baking temperatures.

    Modified by Kevin Zembower, kevin@zembower.org

    Version 0.2 created 19 Nov 2022

    Changed name of output file to reflect side of scale for
    Fahrenheit scale ("..._FR.pdf" is Fahrenheit on right side of
    scale).

    Commented out food names; not complete.


    Version 0.1 created Jan 2021

    -----------------------------------------------------------------
    Celsius-Fahrenheit converter
 
    Copyright (C) 2007-2008  Leif Roschier
 
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
 
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
 
    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""
from pynomo.nomographer import *
F_start=150.0
F_stop=550.0
C_start=70.0
C_stop=290.0
 
def celsius(fahrenheit):
    return (fahrenheit-32.0)/1.8

F_para={
    'tag':'A',
    'u_min':F_start,
    'u_max':F_stop,
    'function':lambda u:celsius(u),
    'title':r'$^\circ$ F',
    'tick_levels':4,
    'tick_text_levels':3,
    'align_func':celsius,
    'title_x_shift':0.5,
    'extra_params':[{'scale_type':'manual arrow',
                     'manual_axis_data':{255:r'very low',
                                         305:r'low',
                                         355:r'moderate',
                                         405:r'hot',
                                         455:r'very hot',
                                         505:r'extremely hot',
                                         545:r'broil',},
                     'arrow_length':0.5,
    }
    ]
}
 
C_para={
    'tag':'A',
    'u_min':C_start,
    'u_max':C_stop,
    'function':lambda u:u,
    'title':r'$^\circ$ C',
    'tick_levels':2,
    'tick_text_levels':1,
    'scale_type':'linear',
    'tick_side':'left',
    'title_x_shift':-0.5,
    'extra_params':[
        # {'scale_type':'manual arrow',
        #  'manual_axis_data':{90:r'Steak:extra-rare',
        #                      122:r'Steak:R',
        #                      133:r'Steak:MR',
        #                      143:r'Steak:M',
        #                      153:r'Steak:MW',
        #                      160:r'Steak:W',
        #                      165:r'Brisket; Ground Meat',
        #                      180:r'Pot Roast',
        #  },
        #  'arrow_length':0.8,
        # },
        {'scale_type':'manual arrow',
         'manual_axis_data':{112:r'$1/4$',
                             125:r'$1/2$',
                             142:r'1',
                             152:r'2',
                             165:r'3',
                             182:r'4',
                             192:r'5',
                             202:r'6',
                             222:r'7',
                             232:r'8',
                             242:r'9',},
         'arrow_length':0.4,
        },
    ],
}

C_block={
    'block_type':'type_8',
    'f_params':C_para
}
F_block={
    'block_type':'type_8',
    'f_params':F_para
}
 
main_params={
    'filename':'oven_temp_converter_RF.pdf',
    'paper_height':20.0,
    'paper_width':2.0,
    'block_params':[C_block,F_block],
    'transformations':[('scale paper',)],
    'title_x':2.5,
    'title_y':-1,
    'title_box_width':7,
    'title_str':r'\Large Oven Temperature Conversions',
    'extra_texts':[
        {'x':-1.5,
         'y':-1.5,
         'text':r'Small numbers in\
         Celsius scale represent\par\
         British gas oven marks.',
         'width':7.0,
        },
        {'x':-1.5,
         'y':-2.5,
         'text':r'Image available at:\par\
         https://github.com/kzembower/Cooking',
         'width':7.2,
        },
    ],
}
Nomographer(main_params)
