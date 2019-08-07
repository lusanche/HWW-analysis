#variables = {}
    
#'fold' : # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow
 
variables['events']  = { 'name': '1',
                         'range' : (1,0,2),  
                         'xaxis' : 'events', 
                         'fold' : 3
                         }

variables['mll']  = { 'name': 'mll', 
                            'range' : ([12,30,50,70,90,110,150,200],), # For VBF SR
                            'xaxis' : 'mll [GeV]', 
                            'fold' : 3,
                            'doWeight' : 1,
                            'binX'     : 1,
                            'binY'     : 7
                            }

variables['DNNvar10'] = { 'name': 'DNNvar',            #   variable name
                        'range' : (10,0,1),    #   variable range
                        'xaxis' : 'DNNvar',  #   x axis name
                        'fold' : 3,
                       }

variables['DNNvar20'] = { 'name': 'DNNvar',            #   variable name
                        'range' : (20,0,1),    #   variable range
                        'xaxis' : 'DNNvar',  #   x axis name
                        'fold' : 3,
                       }

variables['DNNvar30'] = { 'name': 'DNNvar',            #   variable name
                        'range' : (30,0,1),    #   variable range
                        'xaxis' : 'DNNvar',  #   x axis name
                        'fold' : 3,
                       }

variables['DNNvar_optim']  = { 'name': 'DNNvar',   
                               'range' : ([0,0.00045,0.00055,0.00145,0.00155,0.00425,0.01695,0.13695,0.49815,1],),
                               'range' : (10000,0,1),
                               'xaxis' : 'DNNvar',  #   x axis name
                               'fold' : 3,
                              }

