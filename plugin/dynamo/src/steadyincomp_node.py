# assign inputs
_turbulenceProp_, fvSchemes_, fvSolution_, residualControl_, _relaxationFactors_ = IN
recipe = None

try:
    from butterfly.recipe import SteadyIncompressible
except ImportError as e:
    msg = '\nFailed to import butterfly. Did you install butterfly on your machine?' + \
            '\nYou can download the installer file from github: ' + \
            'https://github.com/mostaphaRoudsari/Butterfly/tree/master/plugin/dynamo/samplefiles' + \
            '\nOpen an issue on github if you think this is a bug:' + \
            ' https://github.com/mostaphaRoudsari/Butterfly/issues'
        
    raise ImportError('{}\n{}'.format(msg, e))

recipe = SteadyIncompressible(_turbulenceProp_, fvSchemes_, fvSolution_,
                              residualControl_, _relaxationFactors_)

l = len(recipe.quantities)
q = ''.join(q + ' ..... ' if (c + 1) % 4 != 0 and c + 1 != l else q + '\n'
            for c, q in enumerate(recipe.quantities))


# assign outputs to OUT
OUT = (recipe,)